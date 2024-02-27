
def fcfs(sort_at, si):
        process_num = []
        arrival_time = []
        burst_time = []

        for i in sort_at:
                process_num.append(i[0])
                arrival_time.append(i[1])
                burst_time.append(i[2])
                
        j = 0
        start_time = arrival_time[0]
        end_time = burst_time[0]
        waiting_time = 0
        sum = 0

        while j < si[1]:
                print(f"P[{process_num[j]}] start time: {start_time} end time: {end_time} | Waiting time: {waiting_time}")
                s_t = end_time 
                start_time = s_t
                sum += waiting_time
                k = j+1

                if  k != si[1]:
                    end_time += burst_time[k]
                    waiting_time = start_time - arrival_time[k]

                j += 1
        average = sum / si[1]
        print(f"Average Waiting Time: {average: .2f}")

def sjf(sort_at, si):
        process_num = []
        arrival_time = []
        burst_time = []
        sorted = []

        sort_bt = sorter(sort_at[1:si[1]], 2)
        sorted.append(sort_at[0])

        for i in sort_bt:
                sorted.append(i)

        for i in sorted:
                process_num.append(i[0])
                arrival_time.append(i[1])
                burst_time.append(i[2])
                
        start_time = arrival_time[0]
        end_time = burst_time[0]
        waiting_time = 0
        sum = 0
        j = 0
        print(sorted)
        while j < si[1]:
                print(f"P[{process_num[j]}] start time: {start_time} end time: {end_time} | Waiting time: {waiting_time}")
                s_t = end_time 
                start_time = s_t
                sum += waiting_time
                k = j+1

                if  k != si[1]:
                    end_time += burst_time[k]
                    waiting_time = start_time - arrival_time[k]

                j += 1
        average = sum / si[1]
        print(f"Average Waiting Time: {average: .2f}")


def sorter(processes, n):
        return sorted(processes, key=lambda x: x[n])

filename = input("Enter Filename: ")

try:
        file = open(filename, 'r')
        contents = file.readlines()

        standard_input= []
        processes =[]
        process_num = []
        waiting_time = []
        burst_time = []

        values = list(map(int, contents[0].split()))

        for i in values:
                standard_input.append(i)

        i = 1
        while i < len(contents):
                values = list(map(int, contents[i].split()))
                processes.append(values)
                i+=1
        
        sort_at = sorter(processes, 1)

except FileNotFoundError:
        print(f"{filename} not found")


sjf(sort_at, standard_input)