class task:
    def __init__(self, id, duration):
        if not isinstance(id, str):
            raise Exception("in task_init: variable id is not str")

        if not isinstance(duration, int):
            raise Exception("in task_init: variable duration is not int")

        self.id = id
        self.inputs = []
        self.output = None
        self.duration = duration
    
    def addInput(self, input):
        self.inputs.append(input)

    def addOutput(self, output):
        if self.output is None:
            self.output = output
        

class dataUnit:
    def __init__(self, id, size):
        if not isinstance(id, str):
            raise Exception("in dataUnit_init: variable id is not str")

        if not isinstance(size, int):
            raise Exception("in dataUnit_init: variable size is not int")

        self.id = id
        self.outputs = []
        self.input = None
        self.size = size

    def addInput(self, input):
        if self.input is None:
            self.input = input

    def addOutput(self, output):
        self.outputs.append(output)

class taskGraph:
    def __init__(self):
        self.tasks = []
        self.dataUnits = []

    def addTasks(self, tasks):
        if not isinstance(tasks, task):
            self.tasks += tasks
        else:
            self.tasks.append(tasks)

    def addDataUnits(self, dataUnits):
        if not isinstance(dataUnits, dataUnit):
            self.tasks += dataUnits
        else:
            self.tasks.append(dataUnits)

class worker:
    def __init__(self, noCores):
        self.cores = noCores
        self.cIdle = noCores
        self.cRunning = 0

class cluster:
    def __init__(self):
        self.workers = []

    def addWorkers(self, workers):
        if not isinstance(workers, worker):
            self.workers += workers
        else:
            self.workers.append(workers)

class scheduler:
    def __init__(self, tGraph, clust):
        self.tGraph = tGraph
        self.clust = clust

    def schedule(self):
        return 0
