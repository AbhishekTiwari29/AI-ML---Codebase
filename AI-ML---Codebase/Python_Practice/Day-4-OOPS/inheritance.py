class employee:
    start_time = "9 AM"
    end_time = "5 PM"

class teacher(employee):
    def __init__(self,subject):
        self.subject = subject

class staff(teacher):
    def __init__(self,subject,department):
        super().__init__(subject)
        self.department = department

t1 = teacher("Data Science")
print(t1.subject,t1.end_time,t1.start_time)
s1 = staff("maths","Computer Science")
print(s1.department,s1.start_time,s1.end_time,s1.subject)
