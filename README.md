[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/10tEkNmo)
## Introduction to Programming
## Winter Semester 2025/26 -- Assignment 5
## All concepts required for these tasks have been covered in the lectures and examples.



##task1

Write a function `column_range_plot(A, filename="column_ranges.pdf")` that;

- receives a 2D NumPy array `A`,
- computes the range (maximum minus minimum) of each column,
- create a bar plot showing the ranges of all columns,
- saves the plot as a PDF file,
- and returns a 1D NumPy array containiing the column ranges.

---

##task2

Write a function `detect_turning_points(signal, filename="turning_points.pdf")` that:

- receives a 1D NumPy array representing a signal
- identifies all indices where the direction of the signal changes  
  (i.e., where the discrete difference changes sign),
- plots the signal and mark these turning points,
- saves the figure as a PDF file,
- and returns a NumPy array containing the indices of the detected points

---

##task3

Write a function `approx_real_root(coeffs, interval)` that:

- receives a list `coeffs` of four numbers representing a cubic polynomial,starting with the coefficient of the free term and finishing with the coefficient of x^3
- receives a tuple `interval = (a, b)` with `a < b`,
- assumes that **the polynomial has exactly one real root inside this interval**,
- computes and returns a floating-point approximation of that root,
- and ensures that the approximation is accurate to at least **1×10⁻⁹** in absolute error
---

## Notes on saving figures and gitHub

When saving a figure, call `plt.savefig(filename)` *before* `plt.show()`,  
otherwise the saved file may be blank

If your function generate a PDF,remember to include it in your gitHub repository  
using for example: `git add filename.pdf`.
