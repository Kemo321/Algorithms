import matplotlib.pyplot as plt
import os


def plot_result(x_axis: list, y_axis: list, algorithm: str) -> None:
    plt.plot(x_axis, y_axis)
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title(f"Performance of {algorithm} Sort")
    plt.grid(True)

    # save result in plots directory
    directory = "plots"
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, f"{algorithm}_sort_plot.png"))
    plt.close()
