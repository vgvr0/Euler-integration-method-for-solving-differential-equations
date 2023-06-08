def euler_integration(f, x0, y0, h, n):
    """
    Función para realizar la integración numérica utilizando el método de Euler.

    Parámetros:
    - f: La función que describe la ecuación diferencial dy/dx = f(x, y).
    - x0: El valor inicial de x.
    - y0: El valor inicial de y.
    - h: El tamaño del paso.
    - n: El número de iteraciones.

    Retorna:
    - Dos listas: una con los valores de x y otra con los valores de y.
    """
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        x = x_values[-1]
        y = y_values[-1]
        y_new = y + h * f(x, y)
        x_new = x + h

        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values


def equation(x, y):
    """
    La función que describe la ecuación diferencial dy/dx = x^2.
    """
    return x ** 2


# Parámetros de integración
x0 = 0  # Valor inicial de x
y0 = 0  # Valor inicial de y
h = 0.1  # Tamaño del paso
n = 10  # Número de iteraciones

# Realizar la integración
x_values, y_values = euler_integration(equation, x0, y0, h, n)

# Imprimir los resultados
for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")
