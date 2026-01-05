# BSc Physics Computational Portfolio

## Overview
This repository contains a comprehensive collection of computational physics simulations and numerical methods developed during my BSc Physics Honors at **Miranda House, University of Delhi**.

The projects demonstrate the application of Python to solve complex physical problems, ranging from fundamental calculus to advanced Quantum Mechanics and Statistical Analysis.

## Repository Structure

### 1. Mathematical Physics I (Semester 1)
**Focus:** Foundations of Computational Physics.
* **Calculus:** `taylor_series.py`, `vector_field.py` (Visualizing approximations and fields).
* **Root Finding:** `newton_raphson.py` (Solving f(x)=0).
* **Integration:** `simpsons_rule.py`, `trapezoidal_rule.py` (Numerical area calculation).
* **ODEs:** `euler_method.py` (First-order differential equations).
* **Basics:** `basics_plotting.py`.

### 2. Mathematical Physics II (Semester 2)
**Focus:** Linear Algebra, Curve Fitting, and Simulations.
* **Fitting:** `curve_fitting.py` (Least Square Fit for Ohm's Law).
* **Linear Algebra:** `gauss_elimination.py`, `coupled_springs.py` (Eigenvalues of coupled masses).
* **Mechanics:** `harmonic_oscillator.py` (RK4 simulation of Damped Motion).
* **Electronics:** `lcr_circuit.py` (Transient response of LCR circuits).
* **PDEs:** `pde_heat.py` (Finite Difference solution to the Heat Equation).

### 3. Mathematical Physics III (Semester 3)
**Focus:** Fourier Analysis and Special Functions.
* **Fourier Analysis:** `fourier_square_wave.py` (Series Summation), `fft_transform.py` (Fast Fourier Transform).
* **Special Functions:** `special_functions.py` (Legendre Polynomials & Bessel Functions).
* **Complex Analysis:** `complex_integration.py` (Contour integration verification).
* **Distribution Limit:** `dirac_delta.py` (Gaussian limit approaching Delta function).
* **Differential Eqs:** `ode_solutions.py` (Critically damped systems).

### 4. Numerical Methods (Semester 5)
**Focus:** Complete implementation of 15 standard numerical algorithms.
* **Root Finding:** Bisection, Secant, Regula Falsi, and Newton-Raphson methods.
    * *Code:* `01_bisection.py`, `02_secant.py`, `03_roots_advanced.py`.
* **Linear Algebra:** LU Decomposition, Gauss-Jacobi, and Gauss-Seidel solvers.
    * *Code:* `04_linear_algebra.py`.
* **Interpolation:** Lagrange and Newton's Divided Difference methods.
    * *Code:* `05_interpolation.py`.
* **Integration:** Trapezoidal and Simpson's 1/3 Rule.
    * *Code:* `06_integration.py`.
* **Differential Equations:** Euler's Method and Runge-Kutta (RK4) 4th Order.
    * *Code:* `07_ode_solvers.py`.

### 5. Quantum Mechanics (Semester 5)
**Focus:** Numerical solutions to the Schrödinger Equation using the Shooting Method.
* **Hydrogen Atom:** `hydrogen_atom.py` (Solving for Ground State Energy approx -13.6 eV).
* **Nuclear Physics:** `anharmonic_oscillator.py` (Eigenvalues for Anharmonic potentials).
* **Solid State:** `screened_coulomb.py` (Yukawa/Screened Coulomb potential).
* **Molecular Physics:** `morse_potential.py` (Vibrational states of the H2 molecule).

## Technology Stack
* **Language:** Python 3.x
* **Core Libraries:** numpy, scipy, matplotlib
* **Key Algorithms:** Shooting Method, Runge-Kutta (RK4), Finite Difference Method (FDM), Fast Fourier Transform (FFT).

---
*Created by Keshav Sharma | Physics Hons. | Miranda House*
