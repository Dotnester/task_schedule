graph = { "T1":["T2","T3","T4","T5","T6"],
        "T2":["T7"],
        "T3":["T8"],
        "T4":["T8"],
        "T5":["T8"],
        "T6":["T8"],
        "T7":["T9"],
        "T8":["T9"],
        "T9":[]}

outKeyes = []

for elem in graph:
    if graph[elem] == []:
        outKeyes.append(elem)

taskSchedule = {1:outKeyes}

counter = 1

while taskSchedule[counter] != []:
    keyes = []
    for val in taskSchedule[counter]:
        for k, v in graph.items():
            if val in v:
                keyes.append(k)

    counter+=1
    taskSchedule[counter] = list(set(keyes))

print(taskSchedule)

taskQueue = []

for vals in taskSchedule.values():
    for val in vals:
        taskQueue.insert(0, val)

print(taskQueue)
