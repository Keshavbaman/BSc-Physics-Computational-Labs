import numpy as np
from scipy.integrate import quad

def complex_integral():
    """
    Evaluate integral of 1/(x^2 + 2) from 0 to infinity.
    Analytic result: [1/sqrt(2) * arctan(x/sqrt(2))] from 0 to inf
    = 1/sqrt(2) * (pi/2 - 0) = pi / (2*sqrt(2))
    """
    def integrand(x):
        return 1 / (x**2 + 2)

    # Numerical Integration
    result, error = quad(integrand, 0, np.inf)
    
    # Exact Calculation
    exact = np.pi / (2 * np.sqrt(2))
    
    print(f"Integral of 1/(x^2 + 2) from 0 to infinity:")
    print("-" * 40)
    print(f"Numerical Result: {result:.8f}")
    print(f"Exact Result:     {exact:.8f}")
    print(f"Difference:       {abs(result - exact):.1e}")

if __name__ == "__main__":
    complex_integral()
