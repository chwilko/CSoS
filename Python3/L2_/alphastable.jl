include("MBP.jl")

function alphastable_(N, M, alpha, beta)

    U = pi * (rand(N,M) .- (1 / 2));
    W = d_exp(N, M, 1);
    if alpha == 1
        X = 2 / pi * (
            (pi / 2 .+ beta * U) .* tan.(U) -
            beta * log.(W .* cos.(U) ./ (1 .+ beta * U)));
    else
        B = (atan(beta * tan(pi * alpha / 2))) / alpha;
        S = (1 + beta ^ 2 * (tan(pi * alpha / 2))^2) ^ (1 / (2 * alpha));
        X = S * 
            (sin.(alpha * (U .+ B))) ./ ((cos.(U)) .^ (1 / alpha)) .* 
            ((cos.(U - alpha * (U .+ B))) ./ W) .^ ((1 - alpha) / alpha);
    end
    return X;
end

function alphastable(N, M, alpha, beta, gamma, delta, k)
    
    if k == 0
        if alpha == 1
            X = gamma * alphastable_(N, M, alpha, beta) .+ delta;
        else
            X = gamma * (alphastable_(N, M, alpha, beta) .-
                beta .* tan.(pi * alpha / 2)) .+ delta;
        end
    else

        if alpha == 1
            X = gamma * alphastable_(N, M, alpha, beta) .+
                (delta + beta * 2 / pi *gamma * log(gamma));
        else
            X = gamma * alphastable_(N, M, alpha, beta) .+ delta;
        end
    end
    return X;
end

