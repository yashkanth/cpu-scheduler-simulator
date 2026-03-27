class Process:
    def __init__(self, pid, arrival, burst, priority=0):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority


# ------------------ FCFS -----------------
def fcfs(processes):
    processes = sorted(processes, key=lambda x: x.arrival)

    time = 0
    schedule = []

    for p in processes:
        if time < p.arrival:
            time = p.arrival

        start = time
        time += p.burst
        end = time

        schedule.append((p.pid, start, end))

    return schedule


# ---------------- SJF (Non-Preemptive) ----------------
def sjf(processes):
    processes = processes[:]
    time = 0
    schedule = []

    while processes:
        ready = [p for p in processes if p.arrival <= time]

        if not ready:
            time += 1
            continue

        p = min(ready, key=lambda x: x.burst)
        processes.remove(p)

        start = time
        time += p.burst
        end = time

        schedule.append((p.pid, start, end))

    return schedule


# ---------------- Priority Scheduling ----------------
def priority_scheduling(processes):
    processes = processes[:]
    time = 0
    schedule = []

    while processes:
        ready = [p for p in processes if p.arrival <= time]

        if not ready:
            time += 1
            continue

        p = min(ready, key=lambda x: x.priority)
        processes.remove(p)

        start = time
        time += p.burst
        end = time

        schedule.append((p.pid, start, end))

    return schedule


# ---------------- Round Robin ----------------
def round_robin(processes, quantum):
    queue = processes[:]
    time = 0
    schedule = []

    while queue:
        p = queue.pop(0)

        if time < p.arrival:
            time = p.arrival

        exec_time = min(p.burst, quantum)

        start = time
        time += exec_time
        end = time

        schedule.append((p.pid, start, end))
        p.burst -= exec_time

        if p.burst > 0:
            queue.append(p)

    return schedule


# ---------------- Metrics ----------------
def calculate_metrics(processes, schedule):
    completion = {}

    for pid, start, end in schedule:
        completion[pid] = end

    total_wt = 0
    total_tat = 0

    print("\nProcess Details:")

    for p in processes:
        ct = completion[p.pid]
        tat = ct - p.arrival
        wt = tat - p.burst

        total_wt += wt
        total_tat += tat

        print(f"{p.pid} -> WT: {wt}, TAT: {tat}")

    n = len(processes)
    print(f"\nAverage Waiting Time: {total_wt/n:.2f}")
    print(f"Average Turnaround Time: {total_tat/n:.2f}")
