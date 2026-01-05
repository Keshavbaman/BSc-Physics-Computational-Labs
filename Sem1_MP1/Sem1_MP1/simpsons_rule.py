import numpy as np

def simpson_integral(func, a, b, n):
    """Integrates f(x) from a to b using Simpson's 1/3 Rule."""
    if n % 2 != 0: raise ValueError("n must be even")
    x = np.linspace(a, b, n+1)
    y = func(x)
    h = (b - a) / n
    return (h/3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])

print(f"Integral of sin(x) (0 to pi): {simpson_integral(np.sin, 0, np.pi, 100):.6f}")
