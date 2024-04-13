# Euler Integration

This project implements the Euler method for numerical integration of ordinary differential equations (ODEs). The Euler method is a simple and widely used numerical technique for solving initial value problems.

## Features
- Performs numerical integration using the Euler method.
- Supports custom differential equations defined as Python functions.
- Allows customization of initial conditions, step size, and number of iterations.
- Provides the computed x and y values as output.

## Getting Started
To use the Euler integration code in your project, follow these steps:
1. Clone the repository or download the source code files.
2. Make sure you have Python installed on your system.
3. Import the euler_integration function from the source code file.
4. Define your differential equation as a Python function that takes x and y as parameters and returns the value of dy/dx.
5. Set the initial conditions (x0 and y0), step size (h), and number of iterations (n) according to your problem.
6. Call the euler_integration function with your differential equation function and the specified parameters.
7. The function will return two lists: one containing the computed x values and another containing the corresponding y values.

## Example
Here's an example of how to use the Euler integration code:
```python
from euler_integration import euler_integration

def equation(x, y):
    return x ** 2

x0 = 0  # Initial value of x
y0 = 0  # Initial value of y
h = 0.1  # Step size
n = 10  # Number of iterations

x_values, y_values = euler_integration(equation, x0, y0, h, n)

for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")
```
In this example, we define a differential equation dy/dx = x^2 and set the initial conditions, step size, and number of iterations. The euler_integration function is called with these parameters, and the computed x and y values are printed.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License.

## Acknowledgments
The Euler method is a fundamental numerical integration technique, and this implementation is based on the mathematical principles described in various numerical analysis textbooks and resources.
## References
- Atkinson, Kendall E. "An Introduction to Numerical Analysis." John Wiley & Sons, 2008.
- Burden, Richard L., and J. Douglas Faires. "Numerical Analysis." Brooks/Cole, Cengage Learning, 2011.
