class task:
    def __init__(self, id, duration):
        if not isinstance(id, str):
            raise Exception("in task_init: variable id is not str")

        if not isinstance(duration, int):
            raise Exception("in task_init: variable duration is not int")

        self.id = id
        self.inputs = []
        self.duration = duration
    
    def addInput(self, input):
        self.inputs.append(input)

    def addOutput(self, output):
        self.output = output
        

class dataUnit:
    def __init__(self, id, size):
        if not isinstance(id, str):
            raise Exception("in dataUnit_init: variable id is not str")

        if not isinstance(size, int):
            raise Exception("in dataUnit_init: variable size is not int")

        self.id = id
        self.outputs = []
        self.size = size

    def addInput(self, input):
        self.input = input

    def addOutput(self, output):
        self.outputs.append(output)

print("done1")