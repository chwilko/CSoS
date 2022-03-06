include("MBP.jl")

lambda = 1;
MC = 1 * 10 ^ 4;
n_ = [2 6 12 100];

# n = n_[3];

my_dist = Normal(0,1);
for n in n_
    println(n)
    X = (sum(-log.(rand(MC, n)), dims = 2) - n * ones(MC, 1)) / sqrt(n);

    X = X;

    histogram(X, legend = false, normalize = true, reuse = false)

    plot!(my_dist, lw = 3, linecolor = colorant"magenta")
    # display(p1)

    CDE_X = CDE(t,X, MC);

    plot(t, CDE_X, lw = 3, reuse = false)

    plot!(my_dist, func = cdf, linecolor = colorant"magenta")

    my_phi = characterist_r_i(t, X, MC);

    p3 = plot(t, my_phi[:,1], lw = 3, reuse = false)
    plot!(p3, t, exp.(-t.*t/2), linecolor = colorant"magenta")
    p4 = plot(t, my_phi[:,2], lw = 3)
    plot!(p4, t, zeros(len, 1), linecolor = colorant"magenta")

    plot(p3, p4, layout = (2, 1))
end


# plot(p1, p2, layout = (2, 1))

# print("\n");

# print("PRESS ENTER"); readline()
