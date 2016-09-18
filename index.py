import rinobot_plugin as bot
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['savefig.dpi'] = 2 * matplotlib.rcParams['savefig.dpi']

def main():
    filepath = bot.filepath()
    data = bot.loadfile(filepath)
    x = data[:, 0]
    y = data[:, 1:]
    plt.plot(x, y)

    xmin = bot.get_arg('xmin', type=float)
    xmax = bot.get_arg('xmax', type=float)
    ymin = bot.get_arg('ymin', type=float)
    ymax = bot.get_arg('ymax', type=float)

    plt.xlim([xmin, xmax])
    plt.ylim([ymin, ymax])

    outname = bot.no_extension() + '-line-plot.png'
    outpath = bot.output_filepath(outname)

    plt.savefig(outpath)

if __name__ == "__main__":
    main()
