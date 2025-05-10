%% Questionnaire Reliability and Factor Analysis
%
% Author: Songkai Liu @ Shanghai Jiao Tong University
% Date: 2025-04-07
%
% This script performs reliability testing and factor analysis for user experience assessments 
% using three instruments: Creativity Support Index (CSI), NASA Task Load Index (NASA-TLX), 
% and Workflow-Specific Metrics (WSM).
%
% Features:
% - Computes Cronbach's Alpha for reliability analysis.
% - Calculates KMO statistic and Bartlett’s test for sampling adequacy and sphericity (Table 2).
% - Conducts Principal Component Analysis (PCA) and Factor Analysis to extract latent factors(Table 2).
% - Generates Scree plots and calculates cumulative explained variance (Supplementary Figure S18).
% - Exports factor loadings (Supplementary Tables S24–S26) and all intermediate results to Excel.
%
% Outputs:
% - 'Questionnaire_Analysis_Results.xlsx' (Reliability, factor loadings, and scree plot data)

clc; clear; close all;

filename = 'questionnaire_data.xlsx';
output_xlsx = 'Questionnaire_Analysis_Results.xlsx';
[~, sheet_names] = xlsfinfo(filename);

for i = 1:length(sheet_names)
    fprintf('========== Current Analysis: %s ==========', sheet_names{i});
    T = readtable(filename, 'Sheet', sheet_names{i});
    scale_data = T{:,3:end};
    headers = T.Properties.VariableNames(3:end);  % Retrieve item names

    % === Reliability Analysis ===
    k = size(scale_data, 2);
    alpha = (k / (k - 1)) * (1 - sum(var(scale_data, 0, 1)) / var(sum(scale_data, 2), 0, 1));

    % === KMO and Bartlett's Test ===
    [kmo_stat, ~] = kmo(scale_data);  % KMO sampling adequacy
    [chi_square, p_value] = bartlettTest(scale_data);  % Bartlett’s sphericity test

    % === Factor Structure Analysis ===
    [~, ~, latent, ~, explained] = pca(scale_data);
    eig_vals = latent(latent > 1);
    numFactors = max(1, min(length(eig_vals), size(scale_data, 2) - 1));  % Determine number of factors

    % Record Scree plot data
    scree_data = table((1:length(latent))', latent, explained, ...
        'VariableNames', {'Component', 'Eigenvalue', 'ExplainedVariance'});

    % Save factor loadings
    if strcmp(sheet_names{i}, 'CSI')  % Use PCA for CSI
        [coeff, ~, ~, ~, ~] = pca(scale_data);
        loadings = coeff(:, 1:min(2, size(coeff, 2)));
        method = 'PCA';
    else  % Use factor analysis for others
        try
            [loadings, ~, ~, ~] = factoran(scale_data, numFactors);
            method = 'FactorAnalysis';
        catch
            [coeff, ~, ~, ~, ~] = pca(scale_data);
            loadings = coeff(:, 1:min(2, size(coeff, 2)));
            method = 'PCA (fallback)';
        end
    end

    % Create factor loadings table
    factor_names = strcat('Factor', string(1:size(loadings, 2)));
    loading_tbl = array2table(loadings, 'VariableNames', factor_names);
    loading_tbl.Question = headers(:);
    loading_tbl = movevars(loading_tbl, 'Question', 'Before', 1);

    % Export all results to Excel
    % 1. Reliability, KMO, and Bartlett summary
    summary_tbl = table(alpha, kmo_stat, chi_square, p_value, ...
        'VariableNames', {'CronbachAlpha', 'KMO', 'BartlettChi2', 'BartlettP'});
    writetable(summary_tbl, output_xlsx, 'Sheet', sheet_names{i}, 'Range', 'A1');
    
    % 2. Factor loadings
    writetable(loading_tbl, output_xlsx, 'Sheet', sheet_names{i}, 'Range', 'A5');

    % 3. Scree plot data
    writetable(scree_data, output_xlsx, 'Sheet', sheet_names{i}, 'Range', 'A20');

    % Console report
    fprintf('→ Method used: %s', method);
    disp(loading_tbl);
end
