
def fcfs(sort_wt):
        process_num = []
        waiting_time = []
        burst_time = []

        for i in sort_wt:
                process_num.append(i[0])
                waiting_time.append(i[1])
                burst_time.append(i[2])
                
        print(process_num)

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
        
        sort_wt = sorter(processes, 1)

except FileNotFoundError:
        print(f"{filename} not found")


fcfs(sort_wt)