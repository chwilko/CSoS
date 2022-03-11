include("MBP.jl")

function alphastable_(N, M, alpha, beta)
    On = ones(N,M);
    U = pi * (rand(N,M) - (1 / 2 * On));
    W = d_exp(N, M, 1);
    if alpha == 1
        X = 2 / pi * (
            (On * pi / 2 + beta * U) .* tan.(U) -
            beta * log.(W .* cos.(U) ./ (On + beta * U)));
    else
        B = (atan(beta * tan(pi * alpha / 2))) / alpha;
        S = (1 + beta ^ 2 * (tan(pi * alpha / 2))^2) ^ (1 / (2 * alpha));
        X = S * 
            (sin.(alpha * (U + On * B))) ./ ((cos.(U)) .^ (1 / alpha)) .* 
            ((cos.(U - alpha * (U + On * B))) ./ W) .^ ((1 - alpha) / alpha);
    end
    return X;
end

function alphastable(N, M, alpha, beta, gamma, delta, k)
    if k == 0
        On = ones(N,M);
        if alpha == 1
            X = gamma * alphastable_(N, M, alpha, beta) + On * delta;
        else
            X = gamma * (alphastable_(N, M, alpha, beta) - On * beta * tan.(pi * alpha / 2)) + On * delta;
        end
    else
        On = ones(N,M);
        if alpha == 1
            X = gamma * alphastable_(N, M, alpha, beta) + On * (delta + beta * 2 / pi *gamma * log(gamma));
        else
            X = gamma * alphastable_(N, M, alpha, beta) + On * delta;
        end
    end
    return X;
end

