function CDF(t, X, MC)
    len = length(t);
    # if length(size(X)) == 2
    #     X = sort(X, dims=1);
    # else
    #     X = sort(X);
    # end
    X = X * ones(1, length(t));
    return (sum(X .< t' .* ones(MC,1), dims = 1) ./ (MC * ones(1,len)))';
end

function CDF2(X)
    MC = length(X);
    if length(size(X)) == 2
        X = sort(X, dims=1);
    else
        X = sort(X);
    end
    X = X * ones(1, length(t));
    return (sum(X .< t' .* ones(MC,1), dims = 1) ./ (MC * ones(1,len)))';
end



function PDF(t, X, MC)
    t = t .- (t[2] - t[1]) / 2;
    p = CDF(t[1:end-1], X, MC);
    q = CDF(t[2:end], X, MC);
    return .- p .+ q;
end

# function PDF(t, X, MC)
#     if length(size(X)) == 2
#         X = sort(X, dims=1);
#     else
#         X = sort(X);
#     end
#     n = length(t);
#     dt = t[2] - t[1];
#     t1 = t[1]:dt:(t[end] + 2*dt);
#     return ((MC * ones(n, 1))
#         - (sum((X * ones(1,n) .< t[1:n]' .* ones(MC,1)),
#         dims = 1)'
#         + sum(X * ones(1,n) .> (t1[2:(n+1)])' .* ones(MC,1),
#         dims = 1)')) ./ MC
# end

function characterist_r_i(t, X, MC)
    len = length(t);
    X = X * ones(1,length(t));
    t = t' .* ones(MC,1);
    Re = (sum(cos.(X .* t), dims = 1) ./ (MC * ones(1,len)))';
    Im = (sum(sin.(X .* t), dims = 1) ./ (MC * ones(1,len)))';
    return [Re Im];
end

function d_exp(N, M, lambda)
    return -1 / lambda * log.(rand(N,M));
end