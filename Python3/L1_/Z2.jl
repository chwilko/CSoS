using Plots #mega długo się ładuje 
using Distributions
using LaTeXStrings

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
global CDF_X;
CDF_X = zeros(len, k);
global Re_simulation;
Re_simulation = zeros(len, k);
global Im_simulation;
Im_simulation = zeros(len, k);

my_dist = Normal(0,1);
for i in range(1, length = k)
    n = n_[i]
    A = (sum(-log.(rand(MC, n)), dims = 2) - n * ones(MC, 1)) / sqrt(n)
    X[:, i] = A
    A = CDF(t, X[:, i], MC)';
    CDF_X[:, i] = A;
    Re_simulation[:, i] = characterist_r_i(t, X[:, i], MC)[:, 1];
    Im_simulation[:, i] = characterist_r_i(t, X[:, i], MC)[:, 2];
end

histogram(X, alpha = 0.5, normalize = true, reuse = false, 
            labels = ["n = " * string(i)  for i in n_])

plot!(xlabel = L"x",
    ylabel = L"f(x)", title  = "PDF and histogram comparison",
    labels = "theoretical",
    t -> pdf(my_dist, t), t[1], t[end], lw = 3, linecolor = colorant"magenta")

plot(t, CDF_X, lw = 3, reuse = false,
    labels = ["n = " * string(i)  for i in n_])

plot!(xlabel = L"x",
    ylabel = L"\Phi(x)", title  = "CDF and eCDF comparison",
    labels = "theoretical",
    t -> cdf(my_dist, t), t[1], t[end], linecolor = colorant"magenta")

p3 = plot(t, Re_simulation, lw = 3, reuse = false,
    labels = ["n = " * string(i)  for i in n_])
plot!(xlabel = L"x",
    ylabel = L"Re(\varphi(x))", title  = "Real part",
    labels = "theoretical",
    p3, t, exp.(-t.*t/2), linecolor = colorant"magenta")
p4 = plot(t, Im_simulation, lw = 3,
    labels = ["n = " * string(i)  for i in n_])
plot!(xlabel = L"x",
    ylabel = L"Im(\varphi(x))", title  = "Imaginary part",
    labels = "theoretical",
    p4, t, zeros(len, 1), linecolor = colorant"magenta")

plot(p3, p4, layout = (2, 1))

print("\n");

print("PRESS ENTER"); readline()
