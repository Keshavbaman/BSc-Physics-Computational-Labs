import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def solve_morse_potential():
    print("\n--- Morse Potential (H2 Molecule) ---")
    
    # Constants from Syllabus
    m = 940.0e6        # Reduced mass (eV/c^2) approx for H2
    D = 0.755501       # Well depth (eV)
    alpha = 1.44       # Width parameter
    r0 = 0.131349      # Equilibrium distance (Angstroms) NOT used in reduced var form often, 
                       # but syllabus defines r' = (r - r0)/r. 
                       # NOTE: Syllabus formula V(r) = D(e^-2ar' - e^-ar') is unusual.
                       # Standard Morse is V(r) = D(1 - exp(-a(r-r0)))^2.
                       # We will implement the Syllabus version exactly.
    
    hbar_c = 1973.0
    factor = 2 * m / (hbar_c**2)

    def potential(r):
        # r' = (r - r0) / r
        if r < 1e-2: return 0 # avoid singularity or weirdness at 0
        r_prime = (r - r0) / r
        term = np.exp(-alpha * r_prime)
        # V = D * (e^(-2*alpha*r') - e^(-alpha*r'))
        return D * (term**2 - term)

    def schrodinger(r, y, E):
        u, v = y
        return [v, factor * (potential(r) - E) * u]

    def shoot(E):
        # Integration range 0.1 to 5.0 Angstroms
        sol = solve_ivp(schrodinger, [0.1, 5.0], [0.0, 1.0], args=(E,), max_step=0.02)
        return sol.y[0][-1]

    # Search for Lowest Vibrational Energy
    # Morse states are usually negative (bound), close to the bottom of the well.
    # The well depth is ~ -0.25 eV (min of V).
    energies = np.linspace(-0.25, 0.0, 50) 
    
    ground_E = None
    prev_val = shoot(energies[0])

    for E in energies[1:]:
        val = shoot(E)
        if np.sign(val) != np.sign(prev_val):
            ground_E = E
            break
        prev_val = val

    if ground_E:
        print(f"Lowest Vibrational Energy: {ground_E:.4f} eV")
        
        # Plot V(r) and Wavefunction
        r_plot = np.linspace(0.1, 3.0, 200)
        v_plot = [potential(r) for r in r_plot]
        
        sol = solve_ivp(schrodinger, [0.1, 3.0], [0.0, 1.0], args=(ground_E,), max_step=0.02)
        u_norm = sol.y[0] / np.max(np.abs(sol.y[0])) * 0.1 # Scale for plotting
        
        plt.figure(figsize=(8, 6))
        plt.plot(r_plot, v_plot, 'k--', label='Morse Potential V(r)')
        plt.plot(sol.t, u_norm + ground_E, 'r', label='Wavefunction u(r)')
        plt.axhline(ground_E, color='blue', alpha=0.5, label=f'Energy = {ground_E:.3f} eV')
        
        plt.ylim(-0.3, 0.2)
        plt.title("Hydrogen Molecule Vibrational State")
        plt.xlabel("Internuclear Distance (Å)")
        plt.ylabel("Energy (eV)")
        plt.legend()
        plt.grid()
        plt.show()
    else:
        print("Could not find bound state in scanned range.")

if __name__ == "__main__":
    solve_morse_potential()
