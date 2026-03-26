class Account:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
    
    def get_username(self):
        print(f"Username is : {self.__username}")

    def get_password(self):
        print(f"Password is : {self.__password}")
    
    def set_password(self,password):
        if len(password) >= 6 :
            self.__password = password
        else:
            print("password must be have 6 characters")

    def set_username(self,username):
        if username:
            self.__username = username
        else:
            print("username cant be empty")
    
    def show_masked_password(self):
        print("*" * len(self.__password))


u1 = Account("Abhishek","542158")

u1.get_password()
u1.get_username()
u1.set_password("swgsdsfg")
u1.get_password()