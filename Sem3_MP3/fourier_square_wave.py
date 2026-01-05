import numpy as np
import matplotlib.pyplot as plt

def square_wave_fourier(n_terms=10):
    """
    Syllabus Topic: Summing Fourier Series for a Square Wave.
    The series is: 4/pi * (sin(x) + sin(3x)/3 + sin(5x)/5 + ...)
    """
    x = np.linspace(-np.pi, np.pi, 500)
    y_approx = np.zeros_like(x)

    # Define the actual square wave for comparison
    y_exact = np.sign(np.sin(x))

    # Sum the Fourier Series
    print(f"Summing first {n_terms} terms...")
    for n in range(1, n_terms + 1):
        # Only odd terms (1, 3, 5...) have non-zero coefficients
        k = 2*n - 1
        y_approx += (4 / np.pi) * (np.sin(k * x) / k)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_exact, 'k--', alpha=0.3, label='Exact Square Wave')
    plt.plot(x, y_approx, 'r', label=f'Fourier Sum ({n_terms} terms)')
    
    plt.title(f"Fourier Series Reconstruction (n={n_terms})")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    square_wave_fourier(n_terms=15)
