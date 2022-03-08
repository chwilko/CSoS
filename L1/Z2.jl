using Plots #mega długo się ładuje 
using Distributions

include("MBP.jl")
pyplot()

lambda = 1;
len = 1000;
MC = 1 * 10 ^ 4;
t = range(-3.5, 3.5, length=len);
n_ = [2 6 12 100];

k = length(n_);
global X;
X = zeros(MC, k);
global CDE_X;
CDE_X = zeros(len, k);
global Re_simulation;
Re_simulation = zeros(len, k);
global Im_simulation;
Im_simulation = zeros(len, k);

my_dist = Normal(0,1);
print("lol\n")
for i in range(1, length = k)
    n = n_[i]
    A = (sum(-log.(rand(MC, n)), dims = 2) - n * ones(MC, 1)) / sqrt(n)
    X[:, i] = A
    A = CDE(t, X[:, i], MC)';
    CDE_X[:, i] = A;
    Re_simulation[:, i] = characterist_r_i(t, X[:, i], MC)[:, 1];
    Im_simulation[:, i] = characterist_r_i(t, X[:, i], MC)[:, 2];
end

histogram(X, alpha = 0.5, legend = false, normalize = true, reuse = false)

plot!(t -> pdf(my_dist, t), -3.5, 3.5, lw = 3, linecolor = colorant"magenta")

plot(t, CDE_X, lw = 3, reuse = false)

plot!(t -> cdf(my_dist, t), -3.5, 3.5, linecolor = colorant"magenta")

p3 = plot(t, Re_simulation, lw = 3, reuse = false)
plot!(p3, t, exp.(-t.*t/2), linecolor = colorant"magenta")
p4 = plot(t, Im_simulation, lw = 3)
plot!(p4, t, zeros(len, 1), linecolor = colorant"magenta")

plot(p3, p4, layout = (2, 1))

print("\n");

print("PRESS ENTER"); readline()
