import numpy as np

def newton_raphson(func, deriv, x0, tol=1e-6, max_iter=100):
    """Finds root of f(x)=0 using Newton-Raphson method."""
    x = x0
    for i in range(max_iter):
        fx = func(x)
        if abs(fx) < tol:
            print(f"Root found at x = {x:.6f}")
            return x
        dfx = deriv(x)
        if dfx == 0: return None
        x = x - fx / dfx
    return x

# Example: x^2 - 10 = 0
f = lambda x: x**2 - 10
df = lambda x: 2*x
newton_raphson(f, df, 3.0)
