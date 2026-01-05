import numpy as np
from scipy.linalg import lu

# --- Question 7: LU Decomposition ---
def lu_decomposition_demo():
    print("\n--- Question 7: LU Decomposition ---")
    A = np.array([[2, 1, 4], 
                  [3, 4, -1], 
                  [1, 2, 3]], dtype=float)
    
    # Using scipy for robust decomposition
    P, L, U = lu(A)
    
    print("Matrix A:\n", A)
    print("Lower Matrix L:\n", L)
    print("Upper Matrix U:\n", U)
    print("Verification (L @ U):\n", L @ U)

# --- Question 8: Gauss Jacobi Method ---
def gauss_jacobi(A, b, x0, max_iter=12):
    print("\n--- Question 8: Gauss Jacobi Method ---")
    n = len(b)
    x = x0.copy()
    print(f"Iter 0: {x}")
    
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_new[i] = (b[i] - s) / A[i][i]
        
        x = x_new
        print(f"Iter {k+1}: {x}")
    return x

# --- Question 9: Gauss Seidel Method ---
def gauss_seidel(A, b, x0, max_iter=10):
    print("\n--- Question 9: Gauss Seidel Method ---")
    n = len(b)
    x = x0.copy()
    print(f"Iter 0: {x}")
    
    for k in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - s) / A[i][i] # Updates x in-place immediately
        
        print(f"Iter {k+1}: {x}")
    return x

# --- Run Solvers ---
if __name__ == "__main__":
    # Run LU
    lu_decomposition_demo()
    
    # System for Q8 & Q9:
    # 2x - y = 7
    # -x + 2y - z = 1
    # -y + 2z = 1
    A_sys = np.array([[2, -1, 0], 
                      [-1, 2, -1], 
                      [0, -1, 2]], dtype=float)
    b_sys = np.array([7, 1, 1], dtype=float)
    x_init = np.zeros(3)

    gauss_jacobi(A_sys, b_sys, x_init)
    gauss_seidel(A_sys, b_sys, x_init)
