using Plots #mega długo się ładuje 
using Distributions
using StatsPlots
using LaTeXStrings

include("MBP.jl")
pyplot()

MC = 10000;
k = 12;
len = 1000;
my_dist = Normal(0,1);

t = range(-3.5, 3.5, length=len);
X = sum(rand(MC, k), dims = 2) - 12 * 1/2* ones(MC,1);
# X = X;

histogram(X, legend = false, normalize = true, reuse = false)

display(plot!(xlabel = L"x",
    ylabel = L"f(x)", title  = "PDF and histogram comparison",
    my_dist, lw = 3, linecolor = colorant"magenta"))

CDF_X = CDF(t, vec(X), MC);

plot(t, CDF_X, lw = 3, reuse = false)

display(plot!(xlabel = L"x",
    ylabel = L"\Phi(x)", title  = "CDF and eCDF comparison",
    my_dist, func = cdf, linecolor = colorant"magenta"))

my_phi = characterist_r_i(t, X, MC);

p3 = plot(t, my_phi[:,1], lw = 3, reuse = false)
plot!(xlabel = L"x",
    ylabel = L"Re(\varphi(x))", title  = "Real part",
    p3, t, exp.(-t.*t/2), linecolor = colorant"magenta")
p4 = plot(t, my_phi[:,2], lw = 3)
plot!(xlabel = L"x",
    ylabel = L"Im(\varphi(x))", title  = "Imaginary part",
    p4, t, zeros(len, 1), linecolor = colorant"magenta")

display(plot(p3, p4, layout = (2, 1)))
# plot(p1, p2, layout = (2, 1))

# print("\n");

# print("PRESS ENTER"); readline()
