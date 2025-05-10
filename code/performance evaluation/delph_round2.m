%% Supplementary Note S9 - Delphi Method Analysis (Round 2)
%
% Author: Songkai Liu @ Shanghai Jiao Tong University
% Date: 2025-04-07
%
% This script implements the full analysis pipeline for the second round of Delphi expert evaluations, 
% incorporating structured decision rules to refine evaluation outcomes based on Round 1 results.
%
% Features:
% - Applies quantitative thresholds derived from Round 1 to assess internal robustness of expert scores.
% - Computes Kendall’s coefficient of concordance (W) for inter-rater agreement and assesses significance via Chi-square test.
% - Implements decision rules based on global statistical thresholds for Mean, Coefficient of Variation (CV), and Full-Score Rate (FSR).
% - Classifies each evaluation item into four categories: 'Keep', 'Consider', 'Recommend Drop', or 'Strongly Drop'.
% - Identifies top 5 items with highest variability (CV) and lowest full-score rates to highlight evaluation inconsistencies.
% - Exports comprehensive evaluation results and statistical summaries to Excel and CSV formats for traceable reporting.
% - Generates Kendall’s W bar charts to visualize expert agreement across all design challenges.
%
% Outputs:
% - 'Delphi_Threshold_Summary.xlsx' (Updated Threshold Summary with Decision Criteria)
% - 'Delphi_Indicator_Judgment.xlsx' (Final Evaluation Results per Challenge)
% - 'Boxplot_*.csv' (CSV files for Origin boxplot visualization)

%% 
% 1. Load expert scoring data from 6 Excel files, each representing one design challenge
files = {'Emergency Aerial Response.xlsx', 'Lunar Cryogenic Tech.xlsx', 'Soft Materials Tool.xlsx', ...
         'Lunar Power Transfer.xlsx', 'Lunar Soil Sampling.xlsx', 'Carbon Capture Pilot.xlsx'};

% Store all challenge data
all_data = struct();

for i = 1:length(files)
    filename = files{i};

    % Load each evaluation dimension as a separate sheet
    novelty = readtable(filename, 'Sheet', 'Novelty', 'VariableNamingRule', 'preserve');
    originality = readtable(filename, 'Sheet', 'Originality', 'VariableNamingRule', 'preserve');
    rationality = readtable(filename, 'Sheet', 'Rationality', 'VariableNamingRule', 'preserve');
    technical_maturity = readtable(filename, 'Sheet', 'Technical Maturity', 'VariableNamingRule', 'preserve');
    modularity = readtable(filename, 'Sheet', 'Modularity', 'VariableNamingRule', 'preserve');
    efficiency = readtable(filename, 'Sheet', 'Efficiency', 'VariableNamingRule', 'preserve');

    % Store all six dimensions
    all_data(i).Novelty = novelty;
    all_data(i).Originality = originality;
    all_data(i).Rationality = rationality;
    all_data(i).TechnicalMaturity = technical_maturity;
    all_data(i).Modularity = modularity;
    all_data(i).Efficiency = efficiency;
end

% Save raw data for backup
save('expert_scores_data.mat', 'all_data');

% 2. Kendall W analysis and indicator judgment (per challenge)
kendall_w_results = struct();
indicator_judgments = struct();

% Pre-collect thresholds per challenge
threshold_summary = struct();

for i = 1:length(all_data)
    case_data = all_data(i);
    case_name = erase(files{i}, '.xlsx');  % remove extension for clean naming

    all_scores = [];
    label_names = {};  % store "GPT - Dimension" labels

    fields = fieldnames(case_data);  % 6 dimensions
    for j = 1:length(fields)
        dim_data = case_data.(fields{j});
        scores_only = dim_data{:, 2:end};  % remove first column (expert names)
        all_scores = [all_scores, scores_only];  % concatenate horizontally

        gpt_names = dim_data.Properties.VariableNames(2:end);
        for g = 1:length(gpt_names)
            label = [gpt_names{g}, '-', fields{j}];
            label_names{end+1} = label;
        end
    end

    % ========== Kendall W ==========
    rank_matrix = zeros(size(all_scores));
    for r = 1:size(all_scores, 1)
        rank_matrix(r, :) = tiedrank(all_scores(r, :));
    end

    m = size(rank_matrix, 1);  % number of experts
    n = size(rank_matrix, 2);  % number of evaluation items (24)

    Rj = sum(rank_matrix, 1);
    S = sum((Rj - m * (n + 1) / 2).^2);
    W = 12 * S / (m^2 * (n^3 - n));

    chi_sq = m * (n - 1) * W;
    df = n - 1;
    p_val = 1 - chi2cdf(chi_sq, df);
    alpha = 0.05;
    judgment = "Not Significant";
    if p_val < alpha
        judgment = "Significant";
    end

    kendall_w_results(i).CaseName = case_name;
    kendall_w_results(i).W = W;
    kendall_w_results(i).ChiSq = chi_sq;
    kendall_w_results(i).p = p_val;
    kendall_w_results(i).judgment = judgment;

    % ========== Indicator Concentration Analysis ==========
    mean_vals = mean(all_scores, 1);
    std_vals = std(all_scores, 0, 1);
    cv_vals = std_vals ./ mean_vals;
    full_score_counts = sum(all_scores == 5, 1);
    full_score_rate = full_score_counts / m;

    % Thresholds
    mean_val_avg = mean(mean_vals);
    mean_val_std = std(mean_vals);
    mean_threshold = mean_val_avg - mean_val_std;

    cv_avg = mean(cv_vals);
    cv_std = std(cv_vals);
    cv_threshold = cv_avg + cv_std;

    fsr_avg = mean(full_score_rate) * 100;  % to percentage
    fsr_std = std(full_score_rate) * 100;
    fsr_threshold = fsr_avg - fsr_std;

    % Save to threshold summary
    T = table(...
        ["Mean"; "CV"; "Full Score Rate (%)"], ...
        [mean_val_avg; cv_avg; fsr_avg], ...
        [mean_val_std; cv_std; fsr_std], ...
        ["Mean - StdDev"; "CV + StdDev"; "Mean - StdDev"], ...
        [mean_threshold; cv_threshold; fsr_threshold], ...
        ["< threshold: Issue"; "> threshold: Issue"; "< threshold: Issue"], ...
        'VariableNames', {'Item', 'Average', 'StdDev', 'ThresholdFormula', 'ThresholdValue', 'JudgmentCriteria'});
    threshold_summary(i).CaseName = case_name;
    threshold_summary(i).Table = T;

    % ========== Store item-level details ==========
    judgment_results = struct();

    for k = 1:n
        mean_judge = "Pass";
        cv_judge = "Pass";
        fsr_judge = "Pass";

        if mean_vals(k) < mean_threshold
            mean_judge = "Fail";
        end
        if cv_vals(k) > cv_threshold
            cv_judge = "High Variance";
        end
        if full_score_rate(k)*100 < fsr_threshold
            fsr_judge = "Low 5-Score Rate";
        end

        total_issues = sum([mean_judge=="Fail", cv_judge=="High Variance", fsr_judge=="Low 5-Score Rate"]);
        if total_issues == 0
            final_judgment = "Keep";
        elseif total_issues == 1
            final_judgment = "Consider";
        elseif total_issues == 2
            final_judgment = "Recommend Drop";
        else
            final_judgment = "Strongly Drop";
        end

        % Save results
        judgment_results(k).ItemName = label_names{k};
        judgment_results(k).mean = mean_vals(k);
        judgment_results(k).std = std_vals(k);
        judgment_results(k).cv = cv_vals(k);
        judgment_results(k).full_score_rate = full_score_rate(k);
        judgment_results(k).mean_judge = mean_judge;
        judgment_results(k).cv_judge = cv_judge;
        judgment_results(k).fsr_judge = fsr_judge;
        judgment_results(k).final_judgment = final_judgment;
    end

    indicator_judgments(i).CaseName = case_name;
    indicator_judgments(i).Details = judgment_results;

    % ========== Export CSV for Origin Boxplot ==========
    csv_data = array2table(all_scores, 'VariableNames', matlab.lang.makeValidName(label_names));
    csv_filename = ['Boxplot_', strrep(case_name, ' ', '_'), '.csv'];
    writetable(csv_data, csv_filename);
end

% ========== 2.5 Export Threshold Summary as Separate Excel File ==========
threshold_filename = 'Delphi_Threshold_Summary.xlsx';
for i = 1:length(threshold_summary)
    writetable(threshold_summary(i).Table, threshold_filename, 'Sheet', threshold_summary(i).CaseName);
end
disp("✅ Threshold table exported: Delphi_Threshold_Summary.xlsx");

% 3. Export Excel with 6 Sheets (one per challenge)
excel_filename = 'Delphi_Indicator_Judgment.xlsx';
for i = 1:length(indicator_judgments)
    case_name = indicator_judgments(i).CaseName;
    details = indicator_judgments(i).Details;

    sheet_table = table();
    for j = 1:length(details)
        row = {
            details(j).ItemName, ...
            details(j).mean, ...
            details(j).std, ...
            details(j).cv, ...
            details(j).full_score_rate, ...
            details(j).mean_judge, ...
            details(j).cv_judge, ...
            details(j).fsr_judge, ...
            details(j).final_judgment
        };
        sheet_table = [sheet_table; row];
    end

    sheet_table.Properties.VariableNames = {'Item', 'Mean', 'StdDev', 'CV', 'FullScoreRate', ...
        'MeanEval', 'CVEval', 'FullScoreEval', 'FinalDecision'};

    writetable(sheet_table, excel_filename, 'Sheet', case_name);
end
disp("✅ Delphi indicator judgment exported: Delphi_Indicator_Judgment.xlsx");

% 4. Print Top 5 most inconsistent indicators (by CV & low full score rate)
cv_list = [];
fsr_list = [];
label_list = {};

for i = 1:length(indicator_judgments)
    details = indicator_judgments(i).Details;
    for j = 1:length(details)
        cv_list(end+1) = details(j).cv;
        fsr_list(end+1) = details(j).full_score_rate;
        label_list{end+1} = [indicator_judgments(i).CaseName, ' - ', details(j).ItemName];
    end
end

% Top 5 highest CV
[~, idx_cv] = maxk(cv_list, 5);
disp('📌 Top 5 highest variability (CV):');
for i = 1:5
    fprintf('%s, CV = %.3f\n', label_list{idx_cv(i)}, cv_list(idx_cv(i)));
end

% Top 5 lowest full score rate
[~, idx_fsr] = mink(fsr_list, 5);
disp('📌 Top 5 lowest full-score rate:');
for i = 1:5
    fprintf('%s, FullScoreRate = %.2f%%\n', label_list{idx_fsr(i)}, fsr_list(idx_fsr(i))*100);
end

% 5. Bar chart of Kendall W for all challenges
case_names = strings(length(kendall_w_results), 1);
w_vals = zeros(length(kendall_w_results), 1);

for i = 1:length(kendall_w_results)
    case_names(i) = kendall_w_results(i).CaseName;
    w_vals(i) = kendall_w_results(i).W;
end

figure('Name', 'Kendall W by Design Challenge');
bar(w_vals);
title('Kendall W - Expert Agreement per Challenge');
ylabel('Kendall W');
xticks(1:length(w_vals));
xticklabels(case_names);
xtickangle(45);
grid on;

for i = 1:length(w_vals)
    text(i, w_vals(i)+0.01, kendall_w_results(i).judgment, 'HorizontalAlignment', 'center');
end
