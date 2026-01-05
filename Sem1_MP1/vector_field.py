import numpy as np
import matplotlib.pyplot as plt

def plot_vector_field():
    """
    Visualizes a 2D Vector Field V = (vx, vy).
    Example: A rotational field V = (-y, x)
    """
    print("\n--- Vector Field Visualization ---")
    
    # Create a grid of points
    x, y = np.meshgrid(np.linspace(-5, 5, 20),
                       np.linspace(-5, 5, 20))
    
    # Define Vector Components (e.g., fluid rotation)
    vx = -y
    vy = x
    
    plt.figure(figsize=(8, 8))
    
    # Quiver plot draws arrows at every (x,y)
    plt.quiver(x, y, vx, vy, color='teal')
    
    plt.title("Vector Field: $\mathbf{V} = -y\mathbf{i} + x\mathbf{j}$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_vector_field()
