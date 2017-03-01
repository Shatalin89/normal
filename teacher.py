from people import People

class Teacher(People):

    def __init__(self, name, middlename, lastname, gender, age, experience):
        super().__init__(lastname, middlename, name, gender, age)
        self.experience = experience

    def __str__(self):
        return 'Учитель: {} {}.{}.'.format(self.teacher.lastname, self.teacher.name[0], self.teacher.middlename[0])


