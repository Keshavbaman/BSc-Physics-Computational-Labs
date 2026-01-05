import numpy as np
from scipy.interpolate import lagrange

# --- Question 10: Lagrange Interpolation ---
def lagrange_demo():
    print("\n--- Question 10: Lagrange Interpolation ---")
    # Data: f(0)=1, f(2)=5, f(3)=10
    x = np.array([0, 2, 3])
    y = np.array([1, 5, 10])
    
    poly = lagrange(x, y)
    print("Lagrange Polynomial Coefficients:\n", poly)
    print("Polynomial object:", poly)
    # Verification: check 1 + x^2
    print("Verify at x=2 (should be 5):", poly(2))

# --- Question 11: Newton's Divided Difference ---
def newton_interpolation():
    print("\n--- Question 11: Newton Interpolation ---")
    # Data: f(1)=2, f(2)=5, f(3)=7
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([2, 5, 7], dtype=float)
    n = len(x)
    
    # Create Divided Difference Table
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
            
    print("Divided Difference Table:\n", coef)
    print("Coefficients are the first row:", coef[0, :])
    print(f"Polynomial: {coef[0,0]} + {coef[0,1]}(x-1) + {coef[0,2]}(x-1)(x-2)")

if __name__ == "__main__":
    lagrange_demo()
    newton_interpolation()
