import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from matplotlib.pyplot import figure

def histogram(data, min_value=None, max_value=None, num_bins=100, normalize=False):
    """ Calculates a histogram of the input array.
        Arguments:
        data -- input data
        min_value, max_value -- minimum and maximum value of the histogram 
                              (if not specified, taken as the minimum and maximum value of the input dats)
        num_bins -- final number of bins in the histogram
        normalize -- True if the final values of the histogram shall be normalized to get probability density
        Returns:
        Position of the centres of bins, histogram
    """

    if min_value is None:
        min_value = min(data)
    if max_value is None:
        max_value = max(data)

    bin_width = (max_value - min_value) / num_bins

    histogram = np.zeros(num_bins)

    for d in data:
        if min_value <= d < max_value:
            index = int((d - min_value) / bin_width)
            histogram[index] += 1

                                                                # Starting positions of bins
    bin_x_values = np.linspace(min_value, max_value, num_bins, endpoint=False)                                                                   
    bin_x_values += 0.5 * bin_width                             # Middle positions of bins

    if normalize:                                               # Integral of the histogram normalize to 1
        histogram /= bin_width * len(data)

    return bin_x_values, histogram


def plot_histogram(data, title="", distribution_function=None, **kwargs):
    """ Plots data and compares them with theoretic distributionFunction, if specified """
    x, h = histogram(data, **kwargs)

    plt.tight_layout()
    plt.plot(x, h, label="Histogram")
    plt.title(title)
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\rho$")
    plt.ylim(0)

    if distribution_function is not None:
        plt.plot(x, distribution_function(x), label="Hustota pravděpodobnosti")
        plt.legend()

    plt.plot()

generator = np.random.default_rng()

def generator_hm():
    """ Hit-and-miss method in a rectangle [-6,6]x[0, 1/sqrt(2 pi) ~ 0.4] """
    while True:
        x = 12 * generator.random() - 6
        y = 0.4 * generator.random()
        if y < gaussian_distribution(x):
            return x

def generator_clt():
    """ Central Limit Theorem - sum of 6 uniformly distributed values """
    gaussian_number = sum(generator.random(12)) - 6
    return gaussian_number

def gaussian_generator_clt(num_values=10000):
    """ Histogram of the sum of 12 uniform distributions, giving quite precisely the Gaussian distribution """
    data = [generator_clt() for _ in range(num_values)]

    plot_histogram(data, "Gaussovské rozdělení (Suma 12) CLT",gaussian_distribution, normalize=True) 

def gaussian_distribution(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

def gaussian_generator_hm(num_values=10000):
    """ Histogram of numbers from the Gaussian distribution generated using the hit-and-miss method """
    data = [generator_hm() for _ in range(num_values)]

    plot_histogram(data, "Gaussovské rozdělení (Hit-And-Miss)",gaussian_distribution, normalize=True) 

def main():
    figure(figsize=(11, 9), dpi=80)
    plt.subplot(1,2,1)
    gaussian_generator_hm()
    plt.subplot(1,2,2)
    gaussian_generator_clt()
    plt.show()
if __name__ == "__main__":
    main()