include("MBP.jl")

function alphastable(N, alpha, beta, gamma, delta, k)
    U = pi * (rand(N,1) - 1/2);
    On = ones(N,1);
    W = d_exp(N, 1, 1);
    if alpha == 1
        X = 2 / pi * (
            (On * pi / 2 + beta * U) * tan.(U) -
            beta * log.(W .* cos.(U) ./ (On + beta * U)));
    else
        B = (atan(beta * tan(pi * alpha / 2)))/alpha;
        S = (1 + beta ^ 2 * (tam(pi * alpha/2))^2)^(1/(2 * alpha));
        X = S * 
            (sin(alpha * (U + Ob * B)))/(cos.(U) .^ (1/alpha)) .* 
            ((cos.(U - alpha * (U + On * B)))/ W) .^ ((1 - alpha) / alpha)
    end
    return X;
end
