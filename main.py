# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

from learner import Learner
from people import People
from parents import Parents
from teacher import Teacher
from subject import Subject
from school import School
from group import Group

mother1 = People('Иванова', 'Анна', 'Витальевна', 'ж', 30)
father1 = People('Иванов', 'Иван', 'Васильевич', 'м', 33)
parents1 = Parents(father1, mother1)

teacher1 = Teacher('Мери', 'Афанасьевна', 'Попинс', 'ж', 45, 20)
subject1 = Subject('География', teacher1)

teacher2 = Teacher('Крузенштерн', 'Иван', 'Федорович', 'м', 37, 15)
subject2 = Subject('Математика', teacher2)

learner1 = Learner('Иванов', 'Александр', 'Иванович,' 'м', 12, [subject1, subject2], parents1)
learner2 = Learner('Иванова', 'Александра','Ивановна', 'ж', 13, [subject1], parents1)
learner3 = Learner('Сирота', 'Петр','Валерьевич','м', 14, [subject2], None)

group1 = Group('8 Б', [learner1, learner2])
school1 = School('Школа №1', 'Советская, 25', [group1])

group2 = Group('9 В', [learner3])
school1.group.append(group2)


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
print(school1.get_group())
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
print(group1.get_learner())
print(group2.get_learner())

# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
print(learner1.get_subject())

# 4. Узнать ФИО родителей указанного ученика
print(learner1.get_parents())
# 5. Получить список всех Учителей, преподающих в указанном классе
print(group1.get_teacher())



