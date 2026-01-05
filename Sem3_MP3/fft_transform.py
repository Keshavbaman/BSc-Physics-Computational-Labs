import numpy as np
import matplotlib.pyplot as plt

def compute_fft():
    """
    Syllabus Topic: FFT of Gaussian e^(-x^2).
    """
    N = 1024              # Number of sample points
    x = np.linspace(-10, 10, N)
    dx = x[1] - x[0]

    # Function f(x) = exp(-x^2)
    y = np.exp(-x**2)

    # Compute FFT
    # fftshift moves the zero-frequency component to the center of the spectrum
    y_fft = np.fft.fftshift(np.fft.fft(y))
    freq = np.fft.fftshift(np.fft.fftfreq(N, d=dx))

    # Plotting
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(x, y, color='blue')
    plt.title('Original Function $e^{-x^2}$')
    plt.xlabel('x')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(freq, np.abs(y_fft), color='orange')
    plt.title('FFT Magnitude')
    plt.xlabel('Frequency')
    plt.xlim(-2, 2)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compute_fft()
