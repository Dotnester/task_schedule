graph = { "T1":["T2","T3","T4","T5","T6"],
        "T2":["T7"],
        "T3":["T8"],
        "T4":["T8"],
        "T5":["T8"],
        "T6":["T8"],
        "T7":["T9"],
        "T8":["T9"],
        "T9":[]}

values = []

for vals in graph.values():
    for val in vals:
        values.append(val)

inKeyes = list(set(graph.keys())-set(values))

taskSchedule = {1:inKeyes}

counter = 1

while taskSchedule[counter] != []:
    keyes = []
    for val in taskSchedule[counter]:
        for elem in graph[val]:
            keyes.append(elem)
    counter+=1
    taskSchedule[counter] = list(set(keyes))

print(taskSchedule)

taskQueue = []

for vals in taskSchedule.values():
    for val in vals:
        taskQueue.append(val)

print(taskQueue)
