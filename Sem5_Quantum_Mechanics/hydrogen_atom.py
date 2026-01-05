import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Syllabus Constants ---
# e = 3.795 (eV A)^1/2 -> e^2 = 14.399
# hbar*c = 1973 (eV A)
# m = 0.511x10^6 eV/c^2
e_sq = 3.795**2      
hbar_c = 1973.0
m_e = 0.511e6         

# Pre-calculate factor 2m/hbar^2
factor = 2 * m_e / (hbar_c**2)

def potential(r):
    """Coulomb Potential V(r) = -e^2 / r"""
    return -e_sq / r

def schrodinger(r, y, E):
    """
    System: u'' = A(r)u 
    Converted to: u' = v, v' = A(r)u
    """
    u, v = y
    A = factor * (potential(r) - E)
    return [v, A * u]

def shoot(E):
    """
    Integrates wavefunction from r~0 to r=10.
    Returns the value of u(r) at the boundary.
    """
    # Boundary conditions at r=0: u=0, u'=1 (arbitrary slope)
    sol = solve_ivp(schrodinger, [1e-5, 10.0], [0.0, 1.0], args=(E,), max_step=0.05)
    return sol.y[0][-1]

def find_ground_state():
    print("Scanning for Ground State Energy (Target: ~ -13.6 eV)...")
    energies = np.linspace(-15, -10, 50)
    boundary_values = [shoot(E) for E in energies]

    # Find root (where boundary value crosses zero)
    ground_E = None
    for i in range(len(boundary_values)-1):
        if np.sign(boundary_values[i]) != np.sign(boundary_values[i+1]):
            ground_E = (energies[i] + energies[i+1]) / 2
            break

    print(f"Calculated Energy: {ground_E:.3f} eV")
    
    # Plot Wavefunction
    if ground_E:
        sol = solve_ivp(schrodinger, [1e-5, 10.0], [0.0, 1.0], args=(ground_E,), max_step=0.05)
        
        # Normalize max value to 1 for visualization
        u = sol.y[0] / np.max(np.abs(sol.y[0]))
        
        plt.plot(sol.t, u, label=f'Wavefunction (E={ground_E:.2f} eV)')
        plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
        plt.title('Hydrogen Ground State (s-wave)')
        plt.xlabel('Radius r (Å)')
        plt.ylabel('u(r)')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    find_ground_state()
