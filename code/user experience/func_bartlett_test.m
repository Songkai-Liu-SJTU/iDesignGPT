%% Bartlett’s Test for Sphericity
%
% Author: Songkai Liu @ Shanghai Jiao Tong University
% Date: 2025-04-15
%
% Purpose:
% - Perform Bartlett’s test to evaluate whether the correlation matrix 
%   is an identity matrix, supporting factorability of the dataset.
%
% Inputs:
% - X: Data matrix (samples × variables)
%
% Outputs:
% - chiSquare: Chi-square test statistic
% - pValue: P-value of the test

function [chiSquare, pValue] = func_bartlett_test(X)
    [n, p] = size(X);
    R = corr(X);
    detR = det(R);
    chiSquare = -(n - 1 - (2 * p + 5) / 6) * log(detR);
    df = p * (p - 1) / 2;
    pValue = 1 - chi2cdf(chiSquare, df);
end
