#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    wanderer = [40, 38, 35, 35, 35, 32, 30]
    activity = ["Oregon", "Idaho", "Utah", "Wyoming", "Nebraska", "Kansas", "Missouri"]

    fig, ax = plt.subplots()
    ax.plot(activity, wanderer, label="Wanderer")
    ax.legend()
    fig.suptitle('Latitude at each stop')

    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/graphing/WandererMap.png")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/WandererMap.png")

if __name__ == "__main__":
    main()
