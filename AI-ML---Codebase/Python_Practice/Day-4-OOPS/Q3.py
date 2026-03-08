class Student():
    def __init__(self,name,roll_no,marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks


    def get_name(self):
            return self.__name
        
    def get_roll_no(self):
            return self.__roll_no
        
    def get_marks(self):
            return self.__marks
        
    def set_marks(self,marks):
            if marks >=0 :
                self.__marks = marks
            else:
                print("Marks cannot be negative")

    def set_roll_no(self,roll_no):
            if 1<= roll_no <=100:
                self.__roll_no = roll_no
            else:
                print("Roll no. is invalid")

    def set_name(self,name):
            if name != "":
                self.__name = name 
            else:
                print("enter name")

s1 = Student("abhishek",9,95)
print(s1.get_name(""))