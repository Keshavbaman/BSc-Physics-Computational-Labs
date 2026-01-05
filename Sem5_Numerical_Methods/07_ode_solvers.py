import numpy as np
import matplotlib.pyplot as plt

# --- Question 14: Euler's Method ---
def euler_method(func, x0, y0, x_end, h):
    print("\n--- Question 14: Euler's Method ---")
    steps = int((x_end - x0) / h)
    x, y = x0, y0
    print(f"Iter 0: x={x:.1f}, y={y:.5f}")
    
    for i in range(steps):
        y += h * func(x, y)
        x += h
        print(f"Iter {i+1}: x={x:.1f}, y={y:.5f}")
    return y

# --- Question 15: Runge-Kutta (RK4) ---
def rk4_method(func, x0, y0, x_end, h):
    print("\n--- Question 15: RK4 Method ---")
    steps = int((x_end - x0) / h)
    x, y = x0, y0
    print(f"Iter 0: x={x:.1f}, y={y:.5f}")
    
    for i in range(steps):
        k1 = h * func(x, y)
        k2 = h * func(x + h/2, y + k1/2)
        k3 = h * func(x + h/2, y + k2/2)
        k4 = h * func(x + h, y + k3)
        
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        print(f"Iter {i+1}: x={x:.1f}, y={y:.5f}")
    return y

if __name__ == "__main__":
    # Q14: dy/dx = x + y, y(0)=1, step 0.1
    f_euler = lambda x, y: x + y
    euler_method(f_euler, 0, 1, 1, 0.1)

    # Q15: dy/dx = x^2 - y, y(1)=2, step 0.1
    f_rk4 = lambda x, y: x**2 - y
    rk4_method(f_rk4, 1, 2, 2, 0.1)
