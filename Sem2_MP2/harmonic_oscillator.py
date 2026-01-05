import numpy as np
import matplotlib.pyplot as plt

def rk4_step(f, t, y, h):
    """Runge-Kutta 4th Order Integration Step"""
    k1 = f(t, y)
    k2 = f(t + 0.5*h, y + 0.5*h*k1)
    k3 = f(t + 0.5*h, y + 0.5*h*k2)
    k4 = f(t + h, y + h*k3)
    return y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

def oscillator_derivs(t, state):
    """
    System: d^2x/dt^2 + 2*gamma*dx/dt + w0^2*x = 0
    State vector: [x, v] -> Returns [v, acceleration]
    """
    x, v = state
    gamma = 0.2  # Damping factor
    w0 = 1.0     # Natural frequency
    
    dxdt = v
    dvdt = -2 * gamma * v - w0**2 * x
    return np.array([dxdt, dvdt])

def simulate_oscillator():
    t_values = np.linspace(0, 20, 100)
    dt = t_values[1] - t_values[0]
    
    # Initial Conditions: x=1.0, v=0.0
    state = np.array([1.0, 0.0])
    x_history = []

    for t in t_values:
        x_history.append(state[0])
        state = rk4_step(oscillator_derivs, t, state, dt)

    plt.plot(t_values, x_history, color='purple', label='Damped Position (x)')
    plt.title("Damped Harmonic Oscillator (RK4 Method)")
    plt.xlabel("Time")
    plt.ylabel("Displacement")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    simulate_oscillator()
