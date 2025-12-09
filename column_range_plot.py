import numpy as np
import matplotlib.pyplot as plt
def column_range_plot(A, filename="column_ranges.pdf"):
    A = np.asarray(A)
    column_ranges = np.max(A, axis=0) - np.min(A, axis=0)
    plt.figure()
    plt.bar(np.arange(len(column_ranges)), column_ranges)
    plt.xlabel("Column Index")
    plt.ylabel("Range (max - min)")
    plt.title("Range of Each Column")
    plt.savefig(filename)
    plt.close()
    return column_ranges
A = np.array([[1, 4, 7],
              [2, 6, 3],
              [5, 8, 9]])
result = column_range_plot(A)
print(result)
