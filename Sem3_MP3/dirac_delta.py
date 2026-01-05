import numpy as np
from scipy.integrate import quad

def gaussian_integrand(x, sigma):
    """
    Syllabus Problem: Evaluate integral involving Gaussian.
    Integral of (1/sqrt(2pi*sigma^2)) * exp(-(x-2)^2/2sigma^2) * (x+3)
    As sigma -> 0, this behaves like Dirac Delta centered at 2.
    Result should pick out (x+3) at x=2, which is 2+3 = 5.
    """
    prefactor = 1.0 / (np.sqrt(2 * np.pi) * sigma)
    exponent = -((x - 2)**2) / (2 * sigma**2)
    return prefactor * np.exp(exponent) * (x + 3)

def check_limit():
    sigmas = [1.0, 0.1, 0.01]
    print("Checking Dirac Delta Property:")
    print(f"{'Sigma':<10} {'Integral Result':<20} {'Expected':<10}")
    print("-" * 45)

    for sigma in sigmas:
        # Integrate from -infinity to +infinity
        result, error = quad(gaussian_integrand, -np.inf, np.inf, args=(sigma))
        print(f"{sigma:<10} {result:<20.6f} {5.0:<10}")

if __name__ == "__main__":
    check_limit()
