%% Figure 4h - Score Distribution Visualization
% 
% Author: Songkai Liu @ Shanghai Jiao Tong University
% Date: 2025-04-12
%
% This script visualizes the probability distribution of customer requirement 
% satisfaction scores among awarded design solutions in the GoAERO challenge.
%
% Features:
% - Kernel Density Estimation (KDE) for score distribution visualization.
% - Highlights the iDesignGPT solution score and its position.
% - Vertical plot with annotated solution scores.
% - Exports publication-quality SVG output.
%
% Output:
% - 'fig4h_score_distribution.svg'

 
% Data Import
data = [112, 127, 116, 121, 158, 153, 159, 140, 122, 135, 147, 134, ...
        151, 161, 129, 145, 107, 131, 108, 110, 139, 125];

% Define score range for visualization (X-axis of vertical plot)
x_range = linspace(100, 185, 500); % X-axis range for vertical plot

% Perform Kernel Density Estimation (KDE)
pd = fitdist(data', 'Kernel', 'Kernel', 'normal', 'BandWidth', 5); % Use normal kernel for KDE fitting
y_density = pdf(pd, x_range); % Compute probability density values

% Generate solution labels (A, B, C, ...)
labels = arrayfun(@(x) sprintf('Sol. %c', char(x + 64)), 1:length(data), 'UniformOutput', false); % A, B, C...

% Create vertical plot figure
figure;
hold on;

% Set figure size (Width: 40mm, Height: 70mm)
set(gcf, 'Units', 'centimeters', 'Position', [5, 5, 4, 7]); % Figure width 40mm, height 70mm

% 绘制概率密度曲线
fill([y_density, 0], [x_range, 100], [1, 0.8, 0.6], 'EdgeColor', 'none'); % Fill yellow shaded area (Awarded Design Distribution)
plot(y_density, x_range, 'Color', [1, 0.6, 0], 'LineWidth', 2); % Yellow curve line (Awarded Design)

% Add red dashed line to indicate iDesignGPT solution score
new_solution = 145; % iDesignGPT solution score
line([0, pdf(pd, new_solution)], [new_solution, new_solution], 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1.5); % Red dashed line
scatter(pdf(pd, new_solution), new_solution, 70, 'r', 'filled'); % Mark iDesignGPT solution score point
text(pdf(pd, new_solution) + 0.001, new_solution, 'iDesignGPT', 'FontSize', 6, 'FontName', 'Arial', ...
     'HorizontalAlignment', 'left', 'Color', 'r'); % Add label for iDesignGPT

% Annotate awarded solution scores
for i = 1:length(data)
    scatter(pdf(pd, data(i)), data(i), 30, 'b', 'filled'); % Mark awarded solution score point
    % Automatically adjust label positions (left/right) for clarity
    if mod(i, 2) == 0  % Even index: label positioned to the right
        text(pdf(pd, data(i)) + 0.001, data(i), labels{i}, 'FontSize', 6, 'FontName', 'Arial', ...
             'HorizontalAlignment', 'left', 'Color', 'b'); 
    else  % Odd index: label positioned to the left
        text(pdf(pd, data(i)) - 0.001, data(i), labels{i}, 'FontSize', 6, 'FontName', 'Arial', ...
             'HorizontalAlignment', 'right', 'Color', 'b'); 
    end
end

% Configure plot range and visual style
ylim([100, 185]); % Y-axis range (Total Score from lowest to highest)
xlim([0, max(y_density) + 0.002]); % X-axis range (Probability Density)
xlabel('Probability Density', 'FontSize', 6, 'FontName', 'Arial');
ylabel('Total Score', 'FontSize', 6, 'FontName', 'Arial');
title('Score Distribution Over Actual Designs', 'FontSize', 6, 'FontName', 'Arial');
grid on;

% Add legend to the plot
legend({'Awarded Design', 'iDesignGPT'}, 'Location', 'southwest', 'FontSize', 6, 'FontName', 'Arial');

% Add bounding box to the plot
set(gca, 'Box', 'on'); % Add border to the plot

hold off;

% Export the figure as SVG format
saveas(gcf, 'fig4h_score_distribution.svg');