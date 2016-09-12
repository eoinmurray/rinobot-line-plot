import sys
import os
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['savefig.dpi'] = 2 * matplotlib.rcParams['savefig.dpi']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('--xmin', type=float)
    parser.add_argument('--xmax', type=float)
    parser.add_argument('--ymin', type=float)
    parser.add_argument('--ymax', type=float)

    args = parser.parse_args()
    filepath = args.filepath

    filename_without_ext = os.path.splitext(filepath)[0]
    data = np.loadtxt(filepath)
    x = data[:, 0]
    y = data[:, 1:]
    plt.plot(x, y)

    plt.xlim([args.xmin, args.xmax])
    plt.ylim([args.ymin, args.ymax])

    plt.savefig(filename_without_ext + '-line-plot.png')
