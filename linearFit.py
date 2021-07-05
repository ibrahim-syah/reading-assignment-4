from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt

"""
Find the linear fit with least square method
and plot the result

Argument(s):
_data: two-dimensional numpy array
_isPlot: optional boolean to plot the graphs

Return:
a and b of the line as a tuple
also prints out the function of the line
in a slope-intercept form
where a is the slope and b is the intercept
"""
def lsfLinear(_data: np.array, _isPlot: bool = False) -> Tuple[int, int]:
    x = _data[0]
    y = _data[1]
    m = np.size(x) # number of observations

    Sx = sum(x)
    Sy = sum(y)
    Sxx = sum(x * x)
    Sxy = sum(x * y)

    d = (Sx * Sx) - (m * Sxx)

    # solve the two unknowns for the line
    a = (Sx * Sy - m * Sxy) / d
    b = (Sx * Sxy - Sxx * Sy) / d

    xAxis = np.linspace(min(x), max(x))
    yAxis = a * xAxis + b # this is our optimal line

    print("The linear fit for the given data is:")
    print(f"f(x) = {a} * x + {b}")

    if _isPlot:
        plt.plot(x, y, "go", label="Original Data")
        plt.plot(xAxis, yAxis, "b", label="Linear Fit")
        plt.legend()
        plt.show()

    return (a, b)

if __name__ == "__main__":
    """
    Example case:
    Randomly generated data of Adults weight and height
    (assuming that those two are normally distributed)

    According to https://www.cdc.gov/nchs/data/ad/ad347.pdf
    adults of age 20 - 74 has the average weight of 86.8 Kg with standard deviation of 0.5
    and the average height of 176.2 cm with standard deviation of 0.2

    We can randomly generate this sample with specified
    constraint easily with numpy
    """
    rng = np.random.default_rng()

    sampleSize = 10000 # just an example
    weight = 86.8 + 0.5 * np.random.standard_normal(sampleSize)
    height = 176.2 + 0.2 * np.random.standard_normal(sampleSize)

    data = [height, weight]
    lsfLinear(data, True)