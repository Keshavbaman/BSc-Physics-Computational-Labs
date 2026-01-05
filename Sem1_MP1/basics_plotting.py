import numpy as np
import matplotlib.pyplot as plt

def plot_functions():
    """
    Syllabus Topic: Introduction to Python plotting.
    Plots sin(x), cos(x), and exp(-0.1x^2).
    """
    x = np.linspace(-4*np.pi, 4*np.pi, 200)
    
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_gauss = np.exp(-0.1 * x**2)

    plt.figure(figsize=(10, 6))
    
    plt.plot(x, y_sin, label='sin(x)', color='blue', alpha=0.6)
    plt.plot(x, y_cos, label='cos(x)', color='red', alpha=0.6, linestyle='--')
    plt.plot(x, y_gauss, label='Gaussian exp(-0.1x^2)', color='black', linewidth=2)
    
    plt.title("Basic Mathematical Functions")
    plt.xlabel("x values")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_functions()
