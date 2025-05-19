def by_arrival(proc):
    return proc[1]['arrivingtime']

def by_arrival_burst(proc):
    return (proc[1]['arrivingtime'], proc[1]['burstTime'])

def by_priority(proc):
    return proc[1]['priority']

# FCFS Scheduling Algorithm
def fcfs(processList):
    plist = list(processList.items())
    plist.sort(key=by_arrival)
    ans = {}
    currentTime = 0
    for p in plist:
        if currentTime < p[1]['arrivingtime']:
            currentTime = p[1]['arrivingtime']
        currentTime += p[1]['burstTime']
        turnaroundtime = currentTime - p[1]['arrivingtime']
        waiting = turnaroundtime - p[1]['burstTime']
        ans[p[0]] = {'turnaroundtime': turnaroundtime, 'waitingTime': waiting, 'completionTime': currentTime}
    return ans


# SJF Scheduling Algorithm
def sjf(processList):
    plist = list(processList.items())
    plist.sort(key=by_arrival_burst)
    ans = {}
    currentTime = 0
    for p in plist:
        if currentTime < p[1]['arrivingtime']:
            currentTime = p[1]['arrivingtime']
        currentTime += p[1]['burstTime']
        turnaroundtime = currentTime - p[1]['arrivingtime']
        waiting = turnaroundtime - p[1]['burstTime']
        ans[p[0]] = {'turnaroundtime': turnaroundtime, 'waitingTime': waiting, 'completionTime': currentTime}
    return ans


# Priority Scheduling (Non-preemptive)
def priority_scheduling(processes):
    n = len(processes)
    done = {pid: False for pid in processes}
    ans, time = {}, 0

    while len(ans) < n:
        ready = []
        for pid in processes:
            if not done[pid] and processes[pid]['arrivingtime'] <= time:
                ready.append((pid, processes[pid]))

        if ready:
            # Sort by priority using function
            ready.sort(key=by_priority)
            pid, p = ready[0]
            time = max(time, p['arrivingtime']) + p['burstTime']
            tat = time - p['arrivingtime']
            wt = tat - p['burstTime']
            ans[pid] = {'completionTime': time, 'waitingTime': wt, 'turnaroundtime': tat}
            done[pid] = True
        else:
            time += 1
    return ans

# Function to print the results in the desired format
def print_results(processes, ans, algorithm_name):
    print(f"\n{algorithm_name} Scheduling:")
    print("Process | Completion Time | Waiting Time | Turnaround Time")
    print("------------------------------------------------------------")
    for i in processes:
        completion_time = ans[i]['completionTime']
        waiting_time = ans[i]['waitingTime']
        turnaround_time = ans[i]['turnaroundtime']
        print(f"   {i+1}   |      {completion_time}      |      {waiting_time}      |      {turnaround_time}")
    print()


# Example process data for FCFS, SJF, and Priority Scheduling
process1 = {
    0: {'arrivingtime': 0, 'burstTime': 2},
    1: {'arrivingtime': 3, 'burstTime': 4},
    2: {'arrivingtime': 5, 'burstTime': 3},
    3: {'arrivingtime': 5, 'burstTime': 1},
    4: {'arrivingtime': 4, 'burstTime': 3}
}

process2 = {
    0: {'arrivingtime': 0, 'burstTime': 100},
    1: {'arrivingtime': 10, 'burstTime': 10},
    2: {'arrivingtime': 10, 'burstTime': 5}
}

process3 = {
    0: {'arrivingtime': 0, 'burstTime': 11, 'priority': 2},
    1: {'arrivingtime': 5, 'burstTime': 28, 'priority': 0},
    2: {'arrivingtime': 12, 'burstTime': 2, 'priority': 3},
    3: {'arrivingtime': 2, 'burstTime': 10, 'priority': 1},
    4: {'arrivingtime': 9, 'burstTime': 16, 'priority': 4}
}

# FCFS Scheduling
print("FCFS Scheduling Results:")
fcfs_ans = fcfs(process3)
print_results(range(len(process3)), fcfs_ans, "FCFS")

# SJF Scheduling
print("SJF Scheduling Results:")
sjf_ans = sjf(process3)
print_results(range(len(process3)), sjf_ans, "SJF")

# Priority Scheduling
print("Priority Scheduling Results:")
priority_ans = priority_scheduling(process3)
print_results(range(len(process3)), priority_ans, "Priority")
