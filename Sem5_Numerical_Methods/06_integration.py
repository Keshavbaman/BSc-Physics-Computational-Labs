import numpy as np

# --- Question 12: Trapezoidal Rule ---
def trapezoidal(func, a, b, n):
    h = (b - a) / n
    s = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        s += func(a + i * h)
    return s * h

# --- Question 13: Simpson's 1/3 Rule ---
def simpsons(func, a, b, n):
    if n % 2 != 0: raise ValueError("n must be even")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    
    # Formula: h/3 * (y0 + 4*odd + 2*even + yn)
    integral = (h/3) * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])
    return integral

if __name__ == "__main__":
    # Q12: Integral of x^2 + 1 from 0 to 2 (n=4)
    print("\n--- Question 12: Trapezoidal Rule ---")
    f1 = lambda x: x**2 + 1
    res1 = trapezoidal(f1, 0, 2, 4)
    print(f"Integral (x^2+1): {res1:.4f} (Exact: 4.6667)")

    # Q13: Integral of x^3 + sin(x) from 0 to 4 (n=8)
    print("\n--- Question 13: Simpson's Rule ---")
    f2 = lambda x: x**3 + np.sin(x)
    res2 = simpsons(f2, 0, 4, 8)
    print(f"Integral (x^3+sin(x)): {res2:.4f}")
