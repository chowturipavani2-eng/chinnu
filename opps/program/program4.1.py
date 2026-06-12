class Student:
  def __init__(self, name, roll):
      self.name = name
      self.roll = roll

  def details(self):
      print(f"Name: {self.name} Roll: {self.roll}")

students = []

n = int(input("How many students? "))

for i in range(n):
  print(f"\nEnter Details of Student {i+1}")

  name = input("Enter Name: ")
  roll = int(input("Enter Roll Number: "))

  student = Student(name, roll)
  students.append(student)

print("\nStudent Details")
for student in students:
  student.details()
