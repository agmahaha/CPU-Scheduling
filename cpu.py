
def fcfs(processes):
    processes.sort(key=lambda x: x[1]) # Sort by arrival time
    current_time = 0
    waiting_times = []

    for pid, arrival_time, burst_time in processes:
        if arrival_time <= current_time:
            start_time = current_time
            end_time = start_time + burst_time
            waiting_time = start_time - arrival_time
            waiting_times.append((pid, start_time, end_time, waiting_time))
            current_time = end_time
        else:
            current_time = arrival_time
    return waiting_times

def sjf(processes):
    # Sort processes by arrival time and then by burst time
    processes.sort(key=lambda x: (x[1], x[2]))
    current_time = 0
    waiting_times = []

    while processes:
        shortest_process = None
        for process in processes:
            pid, arrival_time, burst_time = process

            if arrival_time <= current_time:
                if shortest_process is None or burst_time < shortest_process[2]:
                    shortest_process = process

        if shortest_process is None:
            current_time += 1
            continue

        # Execute the shortest process
        pid, arrival_time, burst_time = shortest_process
        start_time = current_time
        end_time = start_time + burst_time
        waiting_time = start_time - arrival_time
        waiting_times.append((pid, start_time, end_time, waiting_time))
        current_time = end_time

        # Remove the executed process from the list
        processes.remove(shortest_process)
    return waiting_times

def srtf(processes):
    # Sort processes by arrival time and then by burst time
    current_time = 0
    waiting_times = []
    hold_wt = []
    start_time = 0
    end_time = 0
    store_id = None


    while processes:
        available_process = []
        for process in processes:
            arrival_time = process[1]

            if arrival_time <= current_time:
                available_process.append(process)

        if available_process == []:
            current_time += 1
            
            continue

        
        available_process.sort(key=lambda x: (x[2], x[1]))
        available = available_process[0]
        updated_process = list(available)
        print(updated_process)
        updated_process[2] -= 1

        if store_id is not None and available[0] != store_id and start_time == end_time:
            start_time = end_time
            pid, arrival_time, burst_time = previous
            end_time = current_time
            waiting_time = 0
            waiting_times.append((pid, start_time , end_time, waiting_time))

        store_id = available[0]
        current_time += 1
        
        if updated_process[2] == 0:
            start_time = end_time
            processes.remove(available)
            pid, arrival_time, burst_time = available
            end_time = current_time
            waiting_time = end_time - arrival_time
            waiting_times.append((pid, start_time , end_time, waiting_time))
        else:
            previous = available
            processes.remove(available)
            processes.append(updated_process)

        

                
    return waiting_times


filename = input("Enter Filename: ")

try:
    with open(filename, 'r') as file:
        contents = file.readlines()

        # Parse the first line to get the scheduling algorithm, number of processes, and time quantum
        algorithm, num_processes, time_quantum = map(int, contents[0].split())

        # Parse the rest of the lines to get the processes
        processes = [list(map(int, line.split())) for line in contents[1:]]

        # Choose the scheduling algorithm based on the input

        if algorithm == 0:
            waiting_times = fcfs(processes)
        elif algorithm == 1:
            waiting_times = sjf(processes)
        elif algorithm == 2:
            waiting_times = srtf(processes)
        # Add other scheduling algorithms here if needed

        # Print the waiting times for each process
        for pid, start_time, end_time, waiting_time in waiting_times:
            print(f"P[{pid}] start time: {start_time} end time: {end_time} | Waiting time: {waiting_time}")

        # Calculate and print the average waiting time
        average_waiting_time = sum(wt for _, _, _, wt in waiting_times) / num_processes
        print(f"Average Waiting Time: {average_waiting_time:.2f}")

except FileNotFoundError:
    print(f"{filename} not found")