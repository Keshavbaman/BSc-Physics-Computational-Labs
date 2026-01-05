import numpy as np

# --- Regula Falsi Method (Question 5) ---
def regula_falsi(func, a, b, tol=1e-6, max_iter=20):
    print(f"\nRunning Regula Falsi for root in [{a}, {b}]")
    if func(a) * func(b) >= 0:
        print("Invalid interval.")
        return None
        
    for k in range(1, max_iter + 1):
        fa, fb = func(a), func(b)
        # Formula: c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        c = (a * fb - b * fa) / (fb - fa)
        fc = func(c)
        
        print(f"Iter {k}: c = {c:.6f}, f(c) = {fc:.1e}")
        
        if abs(fc) < tol:
            print(f"Converged: {c:.6f}")
            return c
            
        if fa * fc < 0:
            b = c
        else:
            a = c
            
# --- Newton Raphson Method (Question 6) ---
def newton_raphson(func, deriv, x0, tol=1e-8, max_iter=20):
    print(f"\nRunning Newton Raphson starting at x0 = {x0}")
    x = x0
    for k in range(1, max_iter + 1):
        fx = func(x)
        dfx = deriv(x)
        
        if dfx == 0: return None
        
        x_new = x - fx / dfx
        print(f"Iter {k}: x = {x_new:.8f}")
        
        if abs(x_new - x) < tol:
            print(f"Converged: {x_new:.8f}")
            return x_new
        x = x_new

# Q5: f(x) = x^3 - x - 1
f5 = lambda x: x**3 - x - 1
regula_falsi(f5, 1, 2, tol=1e-6)

# Q6: f(x) = x^3 - 4x + 2
f6 = lambda x: x**3 - 4*x + 2
df6 = lambda x: 3*x**2 - 4
newton_raphson(f6, df6, 0.5, tol=1e-8)
