using Plots #mega długo się ładuje 
using Distributions
using StatsPlots #to jeszcze dłużej się ładuje 

include("MBP.jl")
pyplot()

lambda = 1;
MC = 1 * 10 ^ 4;
n_ = [2 6 12 100];

# n = n_[3];

k = length(n_);
global X;
X = zeros(MC, k);
CDE_X = zeros(MC, 1);
my_phi = zeros(MC, 2);

my_dist = Normal(0,1);
print("lol\n")
for i in range(1, length = k)
    n = n_[i]
    A = (sum(-log.(rand(MC, n)), dims = 2) - n * ones(MC, 1)) / sqrt(n)
    X[:, i] = A
    # X[:,i] = 
    # size((sum(-log.(rand(MC, n)), dims = 2) - n * ones(MC, 1)) / sqrt(n))
    # CDE_X = [CDE_X, CDE(t, X, MC)];

    # my_phi = [my_phi, characterist_r_i(t, X, MC)];
end
print("lol\n")

histogram(X, alpha = 0.5, legend = false, normalize = true, reuse = false)

plot!(my_dist, lw = 3, linecolor = colorant"magenta")

plot(t, CDE_X, lw = 3, reuse = false)

plot!(my_dist, func = cdf, linecolor = colorant"magenta")

p3 = plot(t, my_phi[:,1], lw = 3, reuse = false)
plot!(p3, t, exp.(-t.*t/2), linecolor = colorant"magenta")
p4 = plot(t, my_phi[:,2], lw = 3)
plot!(p4, t, zeros(len, 1), linecolor = colorant"magenta")

plot(p3, p4, layout = (2, 1))

# display(p1)

# plot(p1, p2, layout = (2, 1))

# print("\n");

# print("PRESS ENTER"); readline()
