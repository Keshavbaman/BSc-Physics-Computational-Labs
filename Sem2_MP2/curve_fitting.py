import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def ohms_law_fit():
    """
    Syllabus Topic: Curve fitting (Least Square Fit).
    Calculating Resistance from V-I data.
    """
    # Experimental Data (Synthetic)
    current_I = np.array([0.1, 0.2, 0.3, 0.4, 0.5])  # Amperes
    voltage_V = np.array([0.5, 1.1, 1.4, 2.1, 2.4])  # Volts

    # Perform Linear Regression (V = IR)
    slope, intercept, r_value, p_value, std_err = linregress(current_I, voltage_V)
    
    print(f"Calculated Resistance (R): {slope:.4f} Ohms")
    print(f"Standard Error: {std_err:.4f}")
    print(f"Goodness of fit (R^2): {r_value**2:.4f}")

    # Plotting
    plt.scatter(current_I, voltage_V, label='Experimental Data', color='red')
    plt.plot(current_I, slope*current_I + intercept, label=f'Best Fit (R={slope:.2f}$\Omega$)', color='blue')
    
    plt.xlabel('Current (A)')
    plt.ylabel('Voltage (V)')
    plt.title("Ohm's Law: Least Square Fit")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ohms_law_fit()
