from scheduler import Process, fcfs, sjf, priority_scheduling, round_robin, calculate_metrics
from visualization import draw_gantt


def main():
    print("CPU Scheduler Simulator")

    n = int(input("Enter number of processes: "))

    processes = []

    for i in range(n):
        pid = f"P{i+1}"
        at = int(input(f"Enter Arrival Time of {pid}: "))
        bt = int(input(f"Enter Burst Time of {pid}: "))
        pr = int(input(f"Enter Priority of {pid}: "))

        processes.append(Process(pid, at, bt, pr))

    print("\nChoose Scheduling Algorithm:")
    print("1. FCFS")
    print("2. SJF")
    print("3. Round Robin")
    print("4. Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        schedule = fcfs(processes)

    elif choice == 2:
        schedule = sjf(processes)

    elif choice == 3:
        quantum = int(input("Enter Time Quantum: "))
        # create copy so original burst is not destroyed
        import copy
        schedule = round_robin(copy.deepcopy(processes), quantum)

    elif choice == 4:
        schedule = priority_scheduling(processes)

    else:
        print("Invalid choice. Running FCFS.")
        schedule = fcfs(processes)

    print("\nExecution Order (Gantt Chart):")
    for pid, start, end in schedule:
        print(f"{pid}: {start} -> {end}")

    draw_gantt(schedule)

    calculate_metrics(processes, schedule)


if __name__ == "__main__":
    main()