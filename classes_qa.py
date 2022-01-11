class Student:
    def __init__(self, name, age, studentclass):
        self.name = name
        self.age = age
        if studentclass is None:
            self.studentclass = ("Student")
        else:
            self.studentclass = studentclass

    def studentdetails(self, test1, test2, test3):
        total = test1 + test2 + test3
        result = total/3
        return result