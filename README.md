# ODE-Solver

A beginner computational physics project implementing numerical ordinary differential equation (ODE) solvers in Python and applying them to physical systems such as free fall and pendulum motion.

## Methods Implemented

* Euler Method
* RK4 (Runge-Kutta 4th Order)
* RK5 (Runge-Kutta 5th Order)

## Topics Covered

### Numerical Analysis

* Error analysis
* Relative and absolute error
* Convergence analysis
* Order of accuracy
* Log-scale error visualization

### Physical Systems

* Free fall motion
* Free fall with linear drag
* Free fall with quadratic drag
* Simple pendulum dynamics
* Energy conservation
* Phase-space analysis

## Repository Structure

```text
ODE-Solver/
│
├── notebooks/
│   ├── 01_Euler-Method.ipynb
│   ├── 02_RK-Method.ipynb
│   ├── 03_Free fall.ipynb
│   └── 04_Pendulum.ipynb
│
├── src/
│   ├── euler.py
│   └── rkmethods.py
│
└── README.md
```

## Motivation

This project was started as an effort to better understand numerical methods used in computational physics. The motivation also came from a PhD interview question regarding solving ODEs/PDEs numerically, which encouraged me to implement these methods practically rather than only studying the theory.

## Tools Used

* Python
* NumPy
* Matplotlib
* Jupyter Notebook

## Learning Goals

* Understanding numerical ODE solving
* Comparing solver accuracy and stability
* Connecting numerical methods with physical systems
* Improving scientific programming skills



## Notes

This project was developed as a learning project. AI tools were used for assistance in debugging, formatting, visualization improvements, and explanation refinement while learning the numerical methods and implementing the solvers.
