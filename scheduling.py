def print_table(processes, wt, tat):
    print("\nPID\tBT\tPriority\tWT\tTAT")
    for i in range(len(processes)):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t\t{wt[i]}\t{tat[i]}")
    avg_wt = sum(wt) / len(processes)
    avg_tat = sum(tat) / len(processes)
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def fcfs(processes):
    print("\n--- FCFS Scheduling ---")
    time = 0
    wt = []
    tat = []
    for p in processes:
        wt.append(time)
        tat.append(time + p[1])
        time += p[1]
    print_table(processes, wt, tat)


def sjf(processes):
    print("\n--- SJF Scheduling ---")
    sorted_proc = sorted(processes, key=lambda x: x[1])  # sort by BT     ☝️☝️☝️ sorted()  
    time = 0
    wt = []
    tat = []
    for p in sorted_proc:
        wt.append(time)
        tat.append(time + p[1])
        time += p[1]
    print_table(sorted_proc, wt, tat)


def priority_scheduling(processes):
    print("\n--- Priority Scheduling ---")
    sorted_proc = sorted(processes, key=lambda x: x[2])  # sort by Priority (lower is higher)
    time = 0
    wt = []
    tat = []
    for p in sorted_proc:
        wt.append(time)
        tat.append(time + p[1])
        time += p[1]
    print_table(sorted_proc, wt, tat)


def round_robin(processes, quantum):
    print("\n--- Round Robin Scheduling ---")
    n = len(processes)
    rem_bt = [p[1] for p in processes]
    wt = [0] * n
    tat = [0] * n
    t = 0
    queue = list(range(n))

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - processes[i][1]
                    rem_bt[i] = 0
        if done:
            break

    for i in range(n):
        tat[i] = wt[i] + processes[i][1]
    print_table(processes, wt, tat)


# Main
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    print(f"\nEnter details for Process P{i+1}:")
    bt = int(input("Burst Time: "))
    pr = int(input("Priority (lower = higher): "))
    processes.append([i + 1, bt, pr])  # PID, BT, Priority

fcfs(processes.copy())
sjf(processes.copy())
priority_scheduling(processes.copy())

quantum = int(input("\nEnter Time Quantum for Round Robin: "))
round_robin(processes.copy(), quantum)
