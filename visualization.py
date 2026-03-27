import matplotlib.pyplot as plt

def draw_gantt(schedule):
    for pid, start, end in schedule:
        plt.barh(pid, end - start, left=start)

    plt.xlabel("Time")
    plt.ylabel("Processes")
    plt.title("Gantt Chart")
    plt.grid(True)

    plt.show()
