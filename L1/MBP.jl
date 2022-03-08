

function CDE(t, X, MC)
    # X = sort(X, dims=1); to do
    X = sort(X);
    X = X * ones(1, length(t));
    return (sum(X .< t' .* ones(MC,1), dims = 1) ./ (MC * ones(1,len)))';
end

# function PDE(t, X, MC)
#     X = sort(X, dims=1);
#     n = length(t);
#     X = X * ones(1,n);
#     c = (sum(X .< t' .* ones(MC,1), dims = 1))'
#     return [ c[2:n] - c[1:n-1]];
#     # return (sum(X .< t' .* ones(MC,1), dims = 1))';
# end

function characterist_r_i(t, X, MC)
    X = X * ones(1,length(t));
    t = t' .* ones(MC,1);
    Re = (sum(cos.(X .* t), dims = 1) ./ (MC * ones(1,len)))';
    Im = (sum(sin.(X .* t), dims = 1) ./ (MC * ones(1,len)))';
    return [Re Im];
end