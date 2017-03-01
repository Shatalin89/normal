from people import People


class Learner(People):
    def __init__(self, lastname, middlename, name, gender, age, parents, subject = None):
        People.__init__(self, lastname, middlename, name, gender, age)
        self.parents = parents
        if subject:
            self.subject = subject
        else:
            self.subject = []


    def __str__(self):
        return '{} {}.{}.'.format(self.lastname, self.name[0], self.middlename[0])

    def get_parents(self):
        return '{} и {}'.format(self.parents.father, self.parents.mother)

    def get_subject(self):
        l =[]
        for i in self.subject:
            l.append(str(i))
        return l

    def get_teacher(self):
        return self.subject.teacher