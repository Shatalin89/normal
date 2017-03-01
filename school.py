

class School:
    def __init__(self, name, address ,group = None):
        self.name = name
        self.address = address
        if group:
            self.group = group
        else:
            self.group = []

    def get_group(self):
        l = []
        for i in self.group:
            l.append(str(i))
        return l

    def __str__(self):
        return self.name
