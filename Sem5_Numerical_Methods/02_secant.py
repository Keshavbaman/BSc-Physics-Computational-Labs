import numpy as np

def secant_method(func, x0, x1, tol=1e-8, max_iter=20):
    """
    Implements Secant Method based on Q3 & Q4.
    Formula: x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    """
    print(f"{'Iter':<5} {'x0':<12} {'x1':<12} {'x2 (new)':<12} {'f(x2)':<12}")
    
    for k in range(1, max_iter + 1):
        f0, f1 = func(x0), func(x1)
        
        if f1 - f0 == 0:
            print("Division by zero error.")
            return None
            
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        
        print(f"{k:<5} {x0:<12.6f} {x1:<12.6f} {x2:<12.6f} {func(x2):<12.1e}")
        
        if abs(func(x2)) < tol:
            print(f"Converged to root: {x2:.8f}")
            return x2
        
        x0, x1 = x1, x2

    return x2

# --- Q3: Solve x^3 + x - 1 = 0 ---
print("\n--- Question 3: f(x) = x^3 + x - 1 ---")
f3 = lambda x: x**3 + x - 1
secant_method(f3, 0, 1, max_iter=10)

# --- Q4: Solve x^3 - 2 = 0 ---
print("\n--- Question 4: f(x) = x^3 - 2 ---")
f4 = lambda x: x**3 - 2
secant_method(f4, 0, 2, tol=1e-8)
