class Item:
	pay_rate = 0.8 # The pay rate after 20% discount
	all = []
	def __init__(self, name: str, price: float, quantity=0):
		# Run validations to the received arguments
		assert price >= 0, f"Price {price} is not greater or equal to zero!"
		assert quantity >= 0, f"Quatity {quantity} is not greater or equal to zero!"

		# Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

		# Actions to execute
		Item.all.append(self)

	def calculate_total_price(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate

	def __repr__(self):
		return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

# Printing single Values
for instance in Item.all:
	print(instance.name)


class Math:

	@staticmethod
	def add5(x):
		return x + 5

	@staticmethod
	def add10(x):
		return x + 10

	@staticmethod
	def pr():
		print("run")

print(Math.add10(5))

class Person:
	# Class Attributes
	number_of_people = 0

	def __init__(self, name):
		self.name = name
		#Person.number_of_people += 1
		Person.add_person()

	@classmethod
	def number_of_people_(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1

p1 = Person("tim")
#print(Person.number_of_people)
p2 = Person("jill")
#print(Person.number_of_people)
print(Person.number_of_people_())

class Student:
	
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade # 0 - 100

	def get_grade(self):
		return self.grade

class Course:
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True 
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())

