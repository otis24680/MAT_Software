import scipy
import sympy
import matplotlib.pyplot as plt
import numpy as np



from ipywidgets import interact

def f(x):                                       # definice funkce f(x) = x^2 - 3
    return x ** 3 + 1

x0 = 1                                          # bod x0
x1 = 3                                          # koncové x

x = np.linspace(x0, x1, 100)                    # generování hodnot x pro vykreslení grafu
y_f = f(x)                                      # hodnoty funkce f(x) pro dané x

y0 = np.min(y_f)                                # krajní body grafu
if y0 > 0:
    y0 = 0
y1 = np.max(y_f)
h = 1                                           # krok h

def plot_graph(h):
    k = (f(x0+h) - f(x0)) / h                   # výpočet směrnice sečny
    q = f(x0) - k*x0                            # výpočet konstanty

    plt.plot(x, y_f, label='f(x) = x^2 - 3')    # vykreslení grafu funkce f(x) 
    plt.plot([x0, x1], [f(x0), k*x1+q], 'r--')  # sečna
    plt.plot(x0, f(x0), 'ro')                   # červený bod v bodě x0
    plt.plot(x0 + h, f(x0 + h), 'ro')           # červený bod v bodě x0 + h
    plt.plot([x0, x0+h], [f(x0), f(x0)], "m:")  # delta x a delta y
    plt.plot([x0+h, x0+h], [f(x0), f(x0+h)], "m:")

    plt.text(x0, f(x0), r'$x_0$', fontsize=12, verticalalignment='bottom')              # popiska x0
    plt.text(x0 + h, f(x0+h), r'$x_0 + h$', fontsize=12, verticalalignment='bottom')    # popiska x0 + h

    plt.axis([x0, x1, y0, y1])                  # nastavení rozsahů (xmin, xmax, ymin, ymax)
    plt.axhline(y = 0, color='k')               # vykreslení osy x
    plt.xlabel('x')                             # popisky os
    plt.ylabel('y')

    plt.grid(True)
    plt.show()

# Vytvoření slideru a jeho propojení s funkcí pro vykreslení grafu
interact(plot_graph, h=(0.001, 1.9, 0.1))
plt.show();


# def f(x):                               # definice funkce f(x) = x^2 - 3
#     return x ** 2 - 3
# def derivace(x):                        # definice derivace funkce f(x) pomocí limity
#     h = 0.1                             # malý krok pro výpočet limity (např. 0.001)
#     return (f(x + h) - f(x)) / h
# def df(x):                              # definice derivace funkce f'(x) = 2x
#     return 2 * x


# x = np.linspace(-5, 5, 100)             # generování hodnot x pro vykreslení grafu
# y_f = f(x)                              # hodnoty funkce f(x) pro dané x
# y_df = df(x)                            # hodnoty derivace f(x) pro dané x
# y_derivace = [derivace(xi) for xi in x] # hodnoty derivace f(x) pro dané x pomocí definice derivace jako limity

# plt.plot(x, y_f, label='f(x) = x^2 - 3')    # vykreslení grafu funkce f(x) 
# plt.plot(x, y_derivace, label="f'(x) pomocí limity")
# plt.plot(x, y_df, "r--", label="f'(x) = 2x")   # vykreslení grafu derivace f'(x)
# plt.axis([-2, 2, -4, 2])                # nastavení rozsahů (xmin, xmax, ymin, ymax)
# plt.axhline(y = 0, color='k')           # vykreslení osy x

# plt.xlabel('x')                         # popisky os
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)                          # mřížka
# plt.show()