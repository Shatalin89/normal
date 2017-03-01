class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def get_teacher(self):
        return self.teacher

    def __str__(self):
        return self.name