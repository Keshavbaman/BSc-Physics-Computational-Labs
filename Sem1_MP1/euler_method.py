import numpy as np
import matplotlib.pyplot as plt

def euler_method(dydx, x0, y0, x_end, step):
    """
    Solves dy/dx = f(x, y) using Euler's Method.
    """
    x_values = np.arange(x0, x_end + step, step)
    y_values = []
    
    y = y0
    for x in x_values:
        y_values.append(y)
        y = y + step * dydx(x, y)
        
    return x_values, np.array(y_values)

# Example: dy/dx = -y (Radioactive Decay)
def decay(x, y):
    return -y

x, y = euler_method(decay, 0, 100, 5, 0.1)

plt.plot(x, y, 'o-', label='Numerical (Euler)')
plt.plot(x, 100*np.exp(-x), 'r--', label='Exact')
plt.title("Euler's Method: Radioactive Decay")
plt.legend()
plt.show()
