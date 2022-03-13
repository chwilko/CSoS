function CDF(t, X, MC)
    len = length(t);
    X = sort(X);
    X = X * ones(1, length(t));
    return (sum(X .< t' .* ones(MC,1), dims = 1) ./ (MC * ones(1,len)))';
end

function PDF(t, X, MC)
    X = sort(X);
    n = length(t);
    return ((MC * ones(n, 1))
        - (sum((X * ones(1, n) .< t' .* ones(MC, 1))
        + [X * ones(1, n - 1) .> (t[2:n])' .* ones(MC, 1) zeros(MC, 1)],
        dims = 1)')) ./ MC
end

function characterist_r_i(t, X, MC)
    len = length(t);
    X = X * ones(1, length(t));
    t = t' .* ones(MC, 1);
    Re = (sum(cos.(X .* t), dims = 1) ./ (MC * ones(1, len)))';
    Im = (sum(sin.(X .* t), dims = 1) ./ (MC * ones(1, len)))';
    return [Re Im];
end

function d_exp(N, M, lambda)
    return -1 / lambda * log.(rand(N,M));
end