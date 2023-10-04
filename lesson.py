import os
import sys
import re
from threading import Timer

class Dastur:
    def __init__(self):
        self.name = None
        self.surname = None
        self.__email = None
        self.__password = None
        self.choose_keys = [1, 2, 3]
        self.regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

    def main_window(self):
        self.clear()
        print("""Assalomu alaykum tizimga xush kelibsiz
              Login [1]
              Register [2]
              Log out [3]""")
        
        tanlov = int(input("Bo'limni tanlang: "))
        while not tanlov in self.choose_keys:
            self.clear()
            print("""Assalomu alaykum tizimga xush kelibsiz
              Login [1]
              Register [2]
              Log out [3]""")
        
            tanlov = int(input("Bo'limni tanlang: "))
        if tanlov == 1:
            self.login()
        if tanlov == 2:
            self.register()
        if tanlov == 3:
            self.exit()

    def register(self):
        self.clear()

        print("""       Register        """)
        self.name = input("Ismingizni kiriting: ").strip()
        self.surname = input("Familiyangizni kiriting: ").strip()
        self.__email = input("Emailingizni kiriting: ").strip()
        self.__password = input("Parolingizni kiriting: ").strip()

        while not len(self.name) > 2:
            self.clear()
            self.name = input("Ismingizni qaytadan kiriting: ").strip()

        while not len(self.surname) > 2:
            self.clear()
            self.surname = input("Familiyangizni qaytadan kiriting: ").strip()

        while not (len(self.__email) >= 8 and len(self.__password) >= 8):
            self.clear()
            self.__email = input("Emailingizni qaytadan kiriting: ").strip()
            self.__password = input("Parolingizni qaytadan kiriting: ").strip()

        while not self.check_email(self.__email):
            self.clear()
            self.__email = input("mavjud email kiritdingiz qaytadan kiriting: ").strip()

        with open("users.txt", "a") as fayl:
            fayl.write(f"{self.name}#{self.surname}#{self.__email}#{self.__password}\n")
        print("Registration successful")
        self.main_window()



    def login(self):
        self.__email = input("Emailingizni kiriting: ").strip()
        self.__password = input("Parolingizni kiriting: ").strip()

        while not (len(self.__email) >= 8 and len(self.__password) >= 8):
            self.clear()
            print("Belgilar soni kam!!")
            self.__email = input("Emailingizni qaytadan kiriting: ").strip()
            self.__password = input("Parolingizni qaytadan kiriting: ").strip()

        while not self.check_enter(self.__email, self.__password):
            self.clear()
            self.__email = input("email kiritdingiz qaytadan kiriting: ").strip()

        print("Login successful")
        self.login_window()
    # ----
    def check_email(self, email):
        self.clear()
        if not re.search(self.regex, email):
            return False
        with open("users.txt", "r") as fayl:
            users = fayl.read().split('\n')
            users.pop()
            for user in users:
                if user.split("#")[2] == email:
                    return False
                
            return True
        

    # ------
    def check_enter(self, email, password):
        with open("users.txt", "r") as fayl:
            users = fayl.read().split('\n')
            users.pop()
            for user in users:
                if user.split("#")[2] == email and user.split("#")[3] == password:
                    return True
            return False
        

    def login_window(self):
        self.clear()
        print("""Tizimga xush kelibsiz. Quydagilarni bajarish mumkin!
              Change login [1]
              Change password [2]
              Log out [3]""")





    @staticmethod
    def clear():
        os.system("clear")


    @staticmethod
    def exit():
        sys.exit()

app = Dastur()
app.main_window()