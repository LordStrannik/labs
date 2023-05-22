groupmates = [
	{
		"name": "Игорь",
		"surname": "Тулегенов",
		"exams": ["ОС", "МиСПИСТ", "ОС"],
		"marks": [5, 4, 5]
	}, {
		"name": "Аркадий",
		"surname": "Гусев",
		"exams": ["АИС", "МиСПИСТ", "ОС"],
		"marks": [4, 4, 4]
	}, {
		"name": "Арина",
		"surname": "Турлаева",
		"exams": ["АИС", "МиСПИСТ", "ОС"],
		"marks": [4, 3, 3]
	}, {
		"name": "Злата",
		"surname": "Филоненко",
		"exams": ["АИС", "МиСПИСТ", "ОС"],
		"marks": [4, 5, 5]
	}, {
		"name": "Павел",
		"surname": "Копоть",
		"exams": ["АИС", "МиСПИСТ", "ОС"],
		"marks": [5, 4, 4]
	}
]

def print_students(mean_ball):
	print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
	for student in groupmates:
		marks = student['marks']
		mean = sum(marks) / len(marks)
		if mean > mean_ball:
			print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

if __name__ == '__main__':
	#print_students(groupmates)
	ball = input('Введите средний балл для фильтрации:')
	print_students(float(ball))