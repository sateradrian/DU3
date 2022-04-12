import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import DU3novy

def generator_F(size=1):
    F = DU3novy.generator.random(size=size)
    return np.tan(np.pi / 2 * (2*F - 1))


def cauchy(num_values=100000):
    data = generator_F(num_values)

    def distribution_function(x):
        return 1 / (np.pi * (1 + x**2))

    DU3novy.plot_histogram(data, "Cauchyho rozdělení", distribution_function, normalize=True, min_value=-10, max_value=10, num_bins=500)

def main():
    
    figure(figsize=(11, 9), dpi=80)
    cauchy()
    plt.show()
if __name__ == "__main__":
    main()