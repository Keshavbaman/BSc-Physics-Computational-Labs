import numpy as np

def solve_linear_system():
    """
    Syllabus Topic: Solution of Linear system of equations.
    Example: 
    2x + y - z = 8
    -3x - y + 2z = -11
    -2x + y + 2z = -3
    """
    # Coefficient Matrix A
    A = np.array([
        [ 2,  1, -1],
        [-3, -1,  2],
        [-2,  1,  2]
    ], dtype=float)

    # Constant Vector B
    B = np.array([8, -11, -3], dtype=float)

    print("Solving System Ax = B:")
    print("Matrix A:\n", A)
    print("Vector B:", B)

    # Using NumPy's optimized solver (Gaussian Elimination under the hood)
    solution = np.linalg.solve(A, B)

    print("-" * 20)
    print(f"Solution: x={solution[0]:.2f}, y={solution[1]:.2f}, z={solution[2]:.2f}")

if __name__ == "__main__":
    solve_linear_system()
