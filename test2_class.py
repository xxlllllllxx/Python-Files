class Person:
    def __init__(self, name):
        self.name = name
        self.new_student_input()

    def new_student_input(self):
        try:
            self.age = int(input("Enter Student " + self.name + "'s age: "))
            self.address = input("Enter Student " + self.name + "'s address: ")
        except:
            print("Error")

    def __str__(self):
        return f"{self.name}({self.age})"

