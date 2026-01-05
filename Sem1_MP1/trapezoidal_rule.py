import numpy as np

def trapezoidal_integral(func, a, b, n):
    """
    Integrates f(x) from a to b using the Trapezoidal Rule.
    Formula: h/2 * [f(a) + 2*sum(f(x_i)) + f(b)]
    """
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    
    # Sum of first and last elements
    s = y[0] + y[-1]
    
    # Sum of middle elements multiplied by 2
    s += 2 * np.sum(y[1:-1])
    
    return (h/2) * s

if __name__ == "__main__":
    print("\n--- Numerical Integration (Trapezoidal) ---")
    
    # Example: Integral of x^2 from 0 to 1 (Exact = 1/3 = 0.3333...)
    f = lambda x: x**2
    a, b = 0, 1
    n = 10
    
    result = trapezoidal_integral(f, a, b, n)
    exact = 1/3
    
    print(f"Integral of x^2 from {a} to {b} with {n} steps:")
    print(f"Numerical: {result:.6f}")
    print(f"Exact:     {exact:.6f}")
    print(f"Error:     {abs(result - exact):.6f}")
