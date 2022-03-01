using Plots #mega długo się ładuje 

function CDE(t, X, MC)
    X = sort(X, dims=1);
    X = X * ones(1,length(t));
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

MC = 10000;
k = 12;
len = 1000;

t = range(-3.5, 3.5, length=len);
X = sum(rand(MC, k), dims=2) - 12 * 1/2* ones(MC,1);
X = X;

histogram(X, legend = false, normalize = true)

CDE_X = CDE(t,X, MC);

plot(t[2:length(t)], CDE_X)

# print("\n");


# print("PRESS ENTER"); readline()
