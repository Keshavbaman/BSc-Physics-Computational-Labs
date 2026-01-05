import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def solve_screened_coulomb():
    print("\n--- Screened Coulomb Potential Simulation ---")
    
    # Constants
    e_sq = 14.4      # e^2 (eV A)
    hbar_c = 1973.0  # eV A
    m_e = 0.511e6    # eV/c^2
    factor = 2 * m_e / (hbar_c**2)
    
    # Screening length 'a' (Syllabus asks for 3, 5, 7 A)
    a_values = [3.0, 5.0, 7.0]
    
    def potential(r, a):
        # V(r) = -(e^2/r) * exp(-r/a)
        return -(e_sq / r) * np.exp(-r / a)

    def schrodinger(r, y, E, a):
        u, v = y
        # Limit V(r) at very small r to avoid singularity
        V = potential(r, a) if r > 1e-5 else potential(1e-5, a)
        return [v, factor * (V - E) * u]

    def shoot(E, a):
        sol = solve_ivp(schrodinger, [1e-5, 10.0], [0.0, 1.0], args=(E, a), max_step=0.05)
        return sol.y[0][-1]

    plt.figure(figsize=(10, 6))

    # Loop through different screening lengths
    for a in a_values:
        # Scan for ground state energy
        energies = np.linspace(-15, -1, 50)
        boundary_vals = [shoot(E, a) for E in energies]
        
        ground_E = None
        for i in range(len(boundary_vals)-1):
            if np.sign(boundary_vals[i]) != np.sign(boundary_vals[i+1]):
                ground_E = (energies[i] + energies[i+1]) / 2
                break
        
        if ground_E:
            print(f"Screening length a={a} Å -> Energy = {ground_E:.3f} eV")
            
            # Plot Wavefunction
            sol = solve_ivp(schrodinger, [1e-5, 10.0], [0.0, 1.0], args=(ground_E, a), max_step=0.05)
            # Normalize
            u = sol.y[0] / np.max(np.abs(sol.y[0]))
            plt.plot(sol.t, u, label=f'a={a} Å (E={ground_E:.2f} eV)')

    plt.title("Wavefunctions for Screened Coulomb Potential")
    plt.xlabel("Radius r (Å)")
    plt.ylabel("Normalized u(r)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    solve_screened_coulomb()
