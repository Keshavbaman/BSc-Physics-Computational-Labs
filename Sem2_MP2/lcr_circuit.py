import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def solve_lcr_circuit():
    """
    Solves for Charge q(t) and Current I(t) in a Series LCR Circuit.
    Differential Eq: L*q'' + R*q' + q/C = V(t)
    State vector y = [q, I] -> y' = [I, (V - R*I - q/C)/L]
    """
    print("\n--- LCR Circuit Simulation ---")
    
    # Circuit Components
    L = 1.0      # Inductance (Henry)
    R = 0.5      # Resistance (Ohm) - Try 0.0 for LC, or 5.0 for Overdamped
    C = 1.0      # Capacitance (Farad)
    
    def voltage_source(t):
        return 0.0 # Source-free (Discharging)
        # return np.sin(t) # AC Source
    
    def circuit_eq(t, y):
        q, I = y
        dqdt = I
        dIdt = (voltage_source(t) - R*I - q/C) / L
        return [dqdt, dIdt]
    
    # Initial Conditions: Capacitor charged to 1.0V, No current
    # q(0) = C * V = 1.0 * 1.0 = 1.0, I(0) = 0
    y0 = [1.0, 0.0]
    t_span = [0, 20]
    
    sol = solve_ivp(circuit_eq, t_span, y0, t_eval=np.linspace(0, 20, 200))
    
    # Plotting
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(sol.t, sol.y[0], 'b-', label='Charge q(t)')
    plt.title('Charge vs Time')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(sol.t, sol.y[1], 'r-', label='Current I(t)')
    plt.title('Current vs Time')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.legend()
    
    plt.suptitle(f"Series LCR Circuit (R={R} Ohms)")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    solve_lcr_circuit()
