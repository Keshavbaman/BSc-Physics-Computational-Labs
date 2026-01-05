import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

def solve_coupled_masses():
    """
    Solves for Normal Modes of 3 coupled masses connected by springs.
    System: k-m-k-m-k-m-k (Fixed ends)
    Equations of motion lead to Matrix M*x'' = -K*x
    Eigenvalue problem: (K - w^2 M)v = 0
    """
    print("\n--- Coupled Spring-Mass System (3 Masses) ---")
    
    k = 1.0  # Spring constant
    m = 1.0  # Mass
    
    # Stiffness Matrix K for 3 masses
    K = np.array([[ 2*k, -k,    0 ],
                  [ -k,   2*k, -k ],
                  [  0,  -k,   2*k ]])
    
    # Find Eigenvalues (w^2) and Eigenvectors (Modes)
    # eigh is used for symmetric matrices (Hermitian)
    eigvals, eigvecs = eigh(K)
    
    frequencies = np.sqrt(eigvals / m)
    
    print("Eigenvalues (w^2):", eigvals)
    print("Frequencies (w):  ", frequencies)
    print("Eigenvectors (Columns):\n", eigvecs)

    # Visualization of Modes
    modes = ['Mode 1', 'Mode 2', 'Mode 3']
    x_positions = [1, 2, 3] # Mass positions
    
    plt.figure(figsize=(10, 4))
    for i in range(3):
        # Plot displacement pattern for each mode
        plt.plot(x_positions, eigvecs[:, i], 'o-', label=f'{modes[i]} (w={frequencies[i]:.2f})')
    
    plt.title("Normal Modes of Coupled Oscillators")
    plt.xlabel("Mass Number")
    plt.ylabel("Relative Displacement")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    solve_coupled_masses()
