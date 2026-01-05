import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Nuclear Constants (MeV, fm) ---
m = 940.0             # Mass (MeV/c^2)
hbar_c = 197.3        # MeV fm
k = 100.0             # Spring constant
b = 10.0              # Anharmonicity

factor = 2 * m / (hbar_c**2)

def potential(r):
    return 0.5 * k * r**2 + (1.0/3.0) * b * r**3

def schrodinger(r, y, E):
    u, v = y
    A = factor * (potential(r) - E)
    return [v, A * u]

def solve_oscillator():
    # Search for energy in range 90-110 MeV
    energies = np.linspace(80, 120, 50)
    
    # Shooting Method Loop
    ground_E = None
    prev_val = None
    
    for E in energies:
        sol = solve_ivp(schrodinger, [1e-5, 5.0], [0.0, 1.0], args=(E,), max_step=0.05)
        val = sol.y[0][-1]
        
        if prev_val is not None and np.sign(val) != np.sign(prev_val):
            ground_E = E - (energies[1]-energies[0])/2 # Approx midpoint
            break
        prev_val = val

    print(f"Anharmonic Ground State Energy: {ground_E:.3f} MeV")

    # Plot
    if ground_E:
        sol = solve_ivp(schrodinger, [1e-5, 5.0], [0.0, 1.0], args=(ground_E,), max_step=0.05)
        plt.plot(sol.t, sol.y[0], color='purple', label=f'u(r) E={ground_E:.1f} MeV')
        plt.title(f'Anharmonic Oscillator (b={b})')
        plt.xlabel('r (fm)')
        plt.ylabel('u(r)')
        plt.grid()
        plt.legend()
        plt.show()

if __name__ == "__main__":
    solve_oscillator()
