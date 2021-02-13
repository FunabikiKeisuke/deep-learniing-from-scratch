import argparse
import numpy as np
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=str, help="保存するグラフのファイルパス")
    return parser.parse_args()


def save_graph():
    args = parse_args()
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)

    plt.plot(x, y)
    plt.savefig(args.p)


if __name__ == '__main__':
    save_graph()
