class Student:
    def __init__(self,sid,sname,marks):
        self.__sid=sid
        self.__sname=sname
        self.__marks=marks
    def set_marks(self,marks):
        if 0<=self.__marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks! marks should be between 0 and 100")
            
    def get_marks(self):
        return self.__marks
        
    def calculate_grade(self):
        if 90<=self.__marks<=100:
                return "A"
        elif 75<=self.__marks<=89:
                return "B"
        elif 60<=self.__marks<=74:
                return "C"
        elif 40<=self.__marks<=59:
                return "D"
        else:
                return "F"
    def display_details(self):
        print("Student Details")
        print("---------------")
        print(f"ID: {self.__sid}\n Name: {self.__sname}\n Marks: {self.__marks}\n Grade: {self.calculate_grade()}")
s1=Student("5609","chinni",85)
s1.display_details()
s1.set_marks(71)
s1.display_details()
