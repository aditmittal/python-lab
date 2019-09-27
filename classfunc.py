class university:
    def __init__(self):
        self.sid = None
        self.sage = None
        self.smarks = None
    def setter(self, ID, age, marks):
        self.sid = ID
        self.sage = age
        self.smarks = marks
    def getter(self):
        ID = int(input("enter the student id: \n"))
        age = int(input("enter student age: \n"))
        marks = int(input("enter marks obtained: \n"))
        self.setter(ID,age,marks)
    def valmark(self):
        if self.smarks >= 0 & self.smarks <= 100:
            return True
        else:
            return False
    def valage(self):
        if self.sage>20:
            return True
        else:
            return False
    def checkqual(self):
        if self.valage() & self.valmark():
            if self.smarks >= 65:
                return True
        else:
            return False
    def disp(self):
        print("STUDENT ID: ",self.sid)
        print("STUDENT AGE: ",self.sage)
        print("STUDENT MARKS: ",self.smarks)
U = university()
U.getter()
x = U.checkqual()
if x:
    U.disp()
    print("badhaii ho!!")
else:
    print("afsosss")
