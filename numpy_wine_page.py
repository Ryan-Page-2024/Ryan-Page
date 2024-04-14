
import numpy as np
import matplotlib.pyplot as plt

def read_from_file():
    wines = np.genfromtxt("numpy_wine.csv", delimiter=";")
    wines = np.array(wines[1:])
    return wines

def get_combined_acidity(data):
    acid = data[:, 0] + data[:, 1] + data[:, 2]
    return acid

def get_high_quality_wines(data, high_quality_baseline = 8):
    high_quality_wines = []
    for row in data:
        if row[-1] >= high_quality_baseline:
            high_quality_wines.append(row)
    high_quality_wines = np.array(high_quality_wines)
    return high_quality_wines

def get_max_deviation(data):
    index = 0
    big = 0
    max_std = np.array(0)
    for col in range(12):
        column = data[:, col]
        deviation = np.ndarray.std(column)
        if big < deviation:
            max_std = column
            big = np.ndarray.std(max_std)
            index = col
    return(index, max_std)

def get_min_deviation(data):
    index = 0
    small = 100
    min_std = np.array(0)
    for col in range(12):
        column = data[:, col]
        deviation = np.ndarray.std(column)
        if small > deviation:
            min_std = column
            small = np.ndarray.std(min_std)
            index = col
    return(index, min_std)

def make_plots(data):
    d = []
    for col in range(12):
        column = data[:, col]
        stddev = np.ndarray.std(column)
        d.append(stddev)

    max_ind, max_std = get_max_deviation(data)
    min_ind, min_std = get_min_deviation(data)

    fig = plt.figure(figsize=(10, 10))
    fig.add_subplot(221)
    plt.scatter(range(len(max_std)), max_std, s=5)
    plt.title('total sulfur dioxide - Max')

    fig.add_subplot(222)
    plt.scatter(range(len(min_std)), min_std, s=5)

    plt.title('density - Min')

    fig.suptitle('Data with Min/Max Standard Deviation', fontsize=16)

    plt.plot()
    plt.savefig('numpy_wine_min_max_std.png')
    plt.show()


def main():
    colname=["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"]
    data = read_from_file()
    acid = get_combined_acidity(data)
    print("Minimum combined acidity is: %s." % round(np.amin(acid), 2))
    print("Maximum combined acidity is: %s." % round(np.amax(acid), 2))
    print()
    high_quality_wines = get_high_quality_wines(data, high_quality_baseline=8)
    print("Number of wines with quality >= 8 is: %s." % high_quality_wines.shape[0])
    print(f'Number of wines with quality >= 8 is: {high_quality_wines.shape[0]}.')
    print('Number of wines with quality >= 8 is: {0}.'.format(high_quality_wines.shape[0]))
    print()
    max_ind, max_std = get_max_deviation(data)
    min_ind, min_std = get_min_deviation(data)
    print("The column with largest standard deviation is:", colname[max_ind])
    print("The standard deviation for this column is: {0:.2f}".format(np.ndarray.std(max_std)))
    print()
    print("The column for smallest standard deviation is:", colname[min_ind])
    print("The standard deviation is: {0:.2f}".format(np.ndarray.std(min_std)))
    make_plots(data)

main()