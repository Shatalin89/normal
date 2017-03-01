

class Group:
    def __init__(self, class_room, learner = None):
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}
        if learner:
            self.learner = learner
        else:
            self.learner = []

    def get_learner(self):
        l=[]
        for i in self.learner:
            l.append(str(i))
        return l

    def get_teacher(self):
        l = []
        for i in self.learner:
            l.append(i.subject.get_teacher())
        return l


    def __str__(self):
        return '{}{}'.format(self._class_room['class_num'], self._class_room['class_char'])

