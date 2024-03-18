from file import File
from algorithms import quick_sort, merge_sort, insertion_sort, bubble_sort, selection_sort
from plot import plot_result
import time
import os


def main():
    file = File(filename='pan-tadeusz-unix.txt')
    text_to_sort = file.load_text()
    probes = [2000, 4000, 6000, 8000, 10000]
    algorithms = [quick_sort, merge_sort, insertion_sort, bubble_sort, selection_sort]

    for algorithm in algorithms:
        directory = "results"
        if not os.path.exists(directory):
            os.makedirs(directory)
        file.set_filename(os.path.join(directory, f'{algorithm.__name__}_result.txt'))
        times = []
        for probe in probes:
            start = time.time()
            sorted_list = algorithm(text_to_sort[:probe])
            times.append(time.time() - start)
        if probe == 10000:
            file.write_text(sorted_list)
        plot_result(x_axis=probes, y_axis=times, algorithm=algorithm.__name__)


if __name__ == "__main__":
    main()
