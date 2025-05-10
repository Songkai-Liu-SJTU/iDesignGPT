%% Probability Density Plot for Customer Requirement Satisfaction Scores
% 
% Author: Songkai Liu @ Shanghai Jiao Tong University
% Date: 2025-04-12
%
% This script visualizes the probability distribution of customer requirement 
% satisfaction scores among awarded design solutions in the GoAERO challenge.
% 
% Features:
% - Kernel Density Estimation (KDE) of the score distribution.
% - Highlights the iDesignGPT solution score and its position within the distribution.
% - Generates a vertical plot with annotated solution scores.
% - Exports the figure as an SVG file for publication quality visualization.
% 
% Corresponds to Figure 4h in the manuscript.
% 
% 数据导入
data = [112, 127, 116, 121, 158, 153, 159, 140, 122, 135, 147, 134, ...
        151, 161, 129, 145, 107, 131, 108, 110, 139, 125];

% 满分和最低分范围
x_range = linspace(100, 185, 500); % 分数范围（竖版图的x轴）

% 核密度估计 (Kernel Density Estimation, KDE)
pd = fitdist(data', 'Kernel', 'Kernel', 'normal', 'BandWidth', 5); % 使用正态核拟合
y_density = pdf(pd, x_range); % 计算概率密度

% 标注方案名称
labels = arrayfun(@(x) sprintf('Sol. %c', char(x + 64)), 1:length(data), 'UniformOutput', false); % A, B, C...

% 创建竖版图
figure;
hold on;

% 设置图大小（宽40mm，高70mm）
set(gcf, 'Units', 'centimeters', 'Position', [5, 5, 4, 7]); % 图像宽度40mm，高度70mm

% 绘制概率密度曲线
fill([y_density, 0], [x_range, 100], [1, 0.8, 0.6], 'EdgeColor', 'none'); % 填充黄色区域
plot(y_density, x_range, 'Color', [1, 0.6, 0], 'LineWidth', 2); % 黄色粗线（Awarded Design）

% 添加红色虚线标记 iDesignGPT
new_solution = 145; % 新方案分数
line([0, pdf(pd, new_solution)], [new_solution, new_solution], 'Color', 'r', 'LineStyle', '--', 'LineWidth', 1.5); % 红色虚线
scatter(pdf(pd, new_solution), new_solution, 70, 'r', 'filled'); % 标记新方案得分点
text(pdf(pd, new_solution) + 0.001, new_solution, 'iDesignGPT', 'FontSize', 6, 'FontName', 'Arial', ...
     'HorizontalAlignment', 'left', 'Color', 'r'); % 添加新方案名称

% 标注方案得分
for i = 1:length(data)
    scatter(pdf(pd, data(i)), data(i), 30, 'b', 'filled'); % 标记方案得分点
    % 自动调整标注文字位置：左右分布
    if mod(i, 2) == 0  % 偶数项标注在右侧
        text(pdf(pd, data(i)) + 0.001, data(i), labels{i}, 'FontSize', 6, 'FontName', 'Arial', ...
             'HorizontalAlignment', 'left', 'Color', 'b'); 
    else  % 奇数项标注在左侧
        text(pdf(pd, data(i)) - 0.001, data(i), labels{i}, 'FontSize', 6, 'FontName', 'Arial', ...
             'HorizontalAlignment', 'right', 'Color', 'b'); 
    end
end

% 设置竖版图的范围和样式
ylim([100, 185]); % y轴范围（满分到最低分）
xlim([0, max(y_density) + 0.002]); % x轴范围
xlabel('Probability Density', 'FontSize', 6, 'FontName', 'Arial');
ylabel('Total Score', 'FontSize', 6, 'FontName', 'Arial');
title('Score Distribution Over Actual Designs', 'FontSize', 6, 'FontName', 'Arial');
grid on;

% 添加图例
legend({'Awarded Design', 'iDesignGPT'}, 'Location', 'southwest', 'FontSize', 6, 'FontName', 'Arial');

% 添加图框
set(gca, 'Box', 'on'); % 给图表加边框

hold off;

% 导出为 SVG 图像
saveas(gcf, 'Score_Distribution.svg');