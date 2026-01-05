import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre, jv

def plot_special_functions():
    x = np.linspace(-1, 1, 200)
    x_bessel = np.linspace(0, 20, 200)
    
    plt.figure(figsize=(12, 5))

    # --- 1. Legendre Polynomials Pn(x) ---
    plt.subplot(1, 2, 1)
    for n in range(1, 5):
        Pn = legendre(n)
        plt.plot(x, Pn(x), label=f'$P_{n}(x)$')
    plt.title("Legendre Polynomials")
    plt.xlabel("x")
    plt.legend()
    plt.grid()

    # --- 2. Bessel Functions Jv(x) ---
    plt.subplot(1, 2, 2)
    for v in [0, 1, 2]:
        plt.plot(x_bessel, jv(v, x_bessel), label=f'$J_{v}(x)$')
    plt.title("Bessel Functions of First Kind")
    plt.xlabel("x")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_special_functions()
