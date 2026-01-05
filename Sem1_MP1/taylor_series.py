import numpy as np
import matplotlib.pyplot as plt
import math

def plot_taylor_series():
    """
    Visualizes the Taylor Series expansion of exp(x) around x=0.
    Series: 1 + x + x^2/2! + x^3/3! + ...
    """
    print("\n--- Taylor Series Visualization (exp(x)) ---")
    
    x = np.linspace(-3, 3, 200)
    y_exact = np.exp(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_exact, 'k', linewidth=2, label='Exact exp(x)')
    plt.ylim(-1, 20)
    
    # Calculate partial sums
    y_approx = np.zeros_like(x)
    
    colors = ['r--', 'g--', 'b--', 'm--']
    orders = [1, 2, 3, 4] # Number of terms
    
    for i, n in enumerate(orders):
        # Add the n-th term: x^n / n!
        term = (x**n) / math.factorial(n)
        
        # Note: Taylor series starts at n=0 (term 1). 
        # Here we accumulate. 
        if n == 1: 
             y_approx = 1 + x # First two terms for n=1 order
        else:
             y_approx += term
             
        plt.plot(x, y_approx, colors[i], label=f'Order {n}')
    
    plt.title("Taylor Series Convergence for $e^x$")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_taylor_series()
