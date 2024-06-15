# решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Иван', 'Борис', 'Степан', 'Геннадий', 'Антон'}
students = list(sorted(students))
print(students)

Антон = sum(grades[0])/len(grades[0])
grades[0] = float(Антон)

Борис = sum(grades[1])/len(grades[1])
grades[1] = float(Борис)

Геннадий = sum(grades[2])/len(grades[2])
grades[2] = float(Геннадий)

Иван = sum(grades[3])/len(grades[3])
grades[3] = float(Иван)

Степан = sum(grades[4])/len(grades[4])
grades[4] = float(Степан)

print(sorted(grades))
new_ = zip(students, grades)
new_dict = dict(new_)
print(new_dict)

