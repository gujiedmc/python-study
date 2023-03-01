class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def log(self):
        print("name=", self.name, ", age=", self.age)


s1 = Student("dyc", 10)
s1.log()
