# ODE-Solver
## Euler Method Implementation

This repository implements a basic numerical solver for ordinary differential equations (ODEs) using the Forward Euler method.

## Objective
To study numerical solutions of ODEs and analyze the accuracy and convergence behavior of the Euler method.

## Method
The Euler method is implemented for solving equations of the form:

    dy/dt = f(t, y)

with numerical update:

    y_{n+1} = y_n + h f(t_n, y_n)

## Validation
The implementation is tested using the exponential decay equation:

    dy/dt = -y

which has the analytical solution:

    y(t) = e^{-t}

## Results
- The numerical solution closely matches the analytical solution for small step sizes.
- Error analysis shows dependence on step size h.
- Convergence study confirms first-order accuracy (Error ∝ h).
