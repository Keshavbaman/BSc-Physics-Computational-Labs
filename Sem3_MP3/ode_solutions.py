import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def solve_odes():
    # --- Problem 1: dy/dx = e^-x, y(0) = 0 ---
    # Analytic solution: y = 1 - e^-x
    def f1(x, y):
        return np.exp(-x)
    
    x_eval = np.linspace(0, 5, 100)
    sol1 = solve_ivp(f1, [0, 5], [0], t_eval=x_eval)
    
    # --- Problem 2: d2y/dt2 + 2dy/dt = -y ---
    # Rearranged: y'' = -y - 2y'
    # State vector: z = [y, y'] -> z' = [y', -y - 2y']
    def f2(t, z):
        y, v = z
        return [v, -y - 2*v]
    
    sol2 = solve_ivp(f2, [0, 10], [1, 0], t_eval=np.linspace(0, 10, 100))

    # --- Plotting ---
    plt.figure(figsize=(12, 5))
    
    # Plot 1
    plt.subplot(1, 2, 1)
    plt.plot(sol1.t, sol1.y[0], label='Numerical')
    plt.plot(x_eval, 1 - np.exp(-x_eval), 'r--', label='Exact (1 - $e^{-x}$)')
    plt.title("Solution to $dy/dx = e^{-x}$")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()

    # Plot 2
    plt.subplot(1, 2, 2)
    plt.plot(sol2.t, sol2.y[0], color='orange', label='y(t)')
    plt.title("Critically Damped: $y'' + 2y' + y = 0$")
    plt.xlabel('t')
    plt.legend()
    plt.grid()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    solve_odes()
