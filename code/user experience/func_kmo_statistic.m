%% KMO (Kaiser-Meyer-Olkin) Sampling Adequacy Test
%
% Author: Songkai Liu @ Shanghai Jiao Tong University
% Date: 2025-04-15
%
% Purpose:
% - Compute the KMO statistic to assess sampling adequacy for factor analysis.
%
% Inputs:
% - X: Data matrix (samples × variables)
%
% Outputs:
% - kmoOverall: Overall KMO value
% - kmoDetail: KMO values for individual variables

function [kmoOverall, kmoDetail] = func_kmo_statistic(X)
    R = corr(X);
    invR = pinv(R);
    S2 = diag(1 ./ sqrt(diag(invR)));
    partialCorr = -S2 * invR * S2;
    partialCorr(logical(eye(size(partialCorr)))) = 0;
    kmoDetail = sum(R.^2, 2) ./ (sum(R.^2, 2) + sum(partialCorr.^2, 2));
    kmoOverall = sum(R(:).^2) / (sum(R(:).^2) + sum(partialCorr(:).^2));
end
