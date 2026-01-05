import numpy as np
import matplotlib.pyplot as plt

def solve_heat_equation():
    """
    Solves the 1D Heat Equation u_t = alpha * u_xx using Finite Difference Method.
    Boundary Conditions: u(0,t) = 0, u(L,t) = 0
    Initial Condition: u(x,0) = sin(pi*x/L) (Heat pulse in center)
    """
    print("\n--- Solving 1D Heat Equation (Finite Difference) ---")
    
    # Parameters
    L = 1.0         # Length of rod
    T = 0.5         # Total time
    Nx = 50         # Number of space points
    Nt = 1000       # Number of time steps
    alpha = 0.1     # Thermal diffusivity
    
    dx = L / Nx
    dt = T / Nt
    
    # Stability condition: alpha * dt / dx^2 <= 0.5
    gamma = alpha * dt / dx**2
    if gamma > 0.5:
        print(f"Warning: Unstable solution! Gamma = {gamma:.2f} (> 0.5)")
        
    # Initialize grid
    u = np.zeros(Nx + 1)
    x = np.linspace(0, L, Nx + 1)
    
    # Initial Condition: Sinusoidal heat distribution
    u = np.sin(np.pi * x / L)
    
    # Plotting setup
    plt.figure(figsize=(8, 5))
    plt.plot(x, u, label='t = 0.00 (Initial)')
    
    # Time Stepping Loop
    u_new = np.zeros_like(u)
    
    # We will plot the solution at specific time intervals
    plot_times = [0.1, 0.2, 0.3, 0.4, 0.5]
    current_time = 0
    
    for n in range(Nt):
        # Finite Difference Formula: u_new[i] = u[i] + gamma * (u[i+1] - 2u[i] + u[i-1])
        for i in range(1, Nx):
            u_new[i] = u[i] + gamma * (u[i+1] - 2*u[i] + u[i-1])
        
        # Update u
        u = u_new.copy()
        current_time += dt
        
        # Check if we should plot this frame
        for pt in plot_times:
            if abs(current_time - pt) < dt/2:
                plt.plot(x, u, label=f't = {current_time:.2f}')
                
    plt.title(f"1D Heat Equation Evolution (alpha={alpha})")
    plt.xlabel("Position x")
    plt.ylabel("Temperature u")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    solve_heat_equation()
