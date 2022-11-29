import re
import traceback


def register(email, password):
    flag = False
    filename = email.split("@")[0]
    try:
        with open(f"{filename}.txt", "w") as f:
            f.write(f"{email} {password}")
            f.close()
            flag = True
    except Exception:
        traceback.print_exc()
        flag = False
    return flag


def login(email, password):
    flag = False
    filename = email.split("@")[0]
    try:
        with open(f"{filename}.txt", "r") as f:
            credentials = f.read().split(" ")
            f.close()
        if (credentials[0] == email) and (credentials[1] == password):
            flag = True
        else:
            print("Invalid Credentials")
    except Exception:
        traceback.print_exc()
        flag = False
    return flag

def validate_email(email):
    regex = r'\b[A-Za-z]+[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
    # 2regex = r'/^[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$/'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def validate_password(password):
    flag = False
    if (len(password) > 5) and (len(password) < 16):
        a = True
    else:
        print(f"Your password length is {len(password)}. Length should be in between 5-16")
        a = False

    if any(chr.isdigit() for chr in password):
        b = True
    else:
        print("Password must contain atleast one digit")
        b = False

    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(special_chars.search(password) == None):
        print("Password should have atleast one special character")
        c = False
    else:
        c = True
    if any(chr.isupper() for chr in password):
        d = True
    else:
        print("Password must contain atleast one capital letter")
        d = False
    if any(chr.islower() for chr in password):
        e = True
    else:
        print("Password must contain atleast one small letter")
        e = False
    if a==True and b==True and c==True and d==True and e==True:
        flag = True
    else:
        flag = False
    return flag

def forget(email):
    flag = False
    filename = email.split("@")[0]
    try:
      with open(f"{filename}.txt", "r") as f:
            credentials = f.read().split(" ")
            f.close()
      if (credentials[0] == email):
            email= credentials[0]
            password=credentials[1]
            print(f"{password} is your password")
            flag = True
      else:
            print("You are not registered")
    except Exception:
        flag = False
    return flag
	
def check(email):
    flag = False
    filename = email.split("@")[0]
    try:
      with open(f"{filename}.txt", "r") as f:
            credentials = f.read().split(" ")
            f.close()
      if (credentials[0] == email):
            email= credentials[0]
            password=credentials[1]
            
            flag = True
      else:
            pass
    except Exception:
        flag = False
    return flag

print("1. Register\n2. Login")
print("Please choose your option:")
option = int(input())

if not (option in [1, 2]):
    print("Invalid Option")


if option == 1:
    email = input("Email: ")
    while not validate_email(email):
      print("Email is invalid. Please enter again.")
      email = input("Email: ")

    password = input("Passowrd: ")
    while not validate_password(password):
      print("Please enter password again")
      password = input("Password: ")

    result = register(email, password)
    if result:
        print(f"{email} successfully registered.")
    else:
        print("Error while registration")

    
elif option == 2:
    email = input("Email: ")
    while not validate_email(email):
      print("Email is invalid. Please enter again.")
      email = input("Email: ")
    result = check(email)
    if result:
      password = input("Passowrd: ")
      

      result = login(email, password)
      if result:
        print(f"{email} successfully logged in.")
      else:
        print("Entered password is incorrect")
        print("3. forget password\n4. enter new password")
        print("Please choose your option:")
        option = int(input())

        if not (option in [3, 4]):
            print("Invalid Option")
        
    else:
      result = forget(email)
      if result:
         pass
      else:
        print("you are not registered. please do Registration")
        email = input("Email: ")
        while not validate_email(email):
          print("Email is invalid. Please enter again.")
          email = input("Email: ")

        password = input("Passowrd: ")
        while not validate_password(password):
          print("Please enter password again")
          password = input("Password: ")
        result = register(email, password)
        if result:
          print(f"{email} successfully registered.")
        else:
          print("Error while registration")

    if option == 3:
      email = input("Email: ")
      while not validate_email(email):
        print("Email is invalid. Please enter again.")
        email = input("Email: ")

      result = forget(email)
      if result:
           pass
      else:
          print("you are not registered. please do Registration")
          email = input("Email: ")
          while not validate_email(email):
            print("Email is invalid. Please enter again.")
            email = input("Email: ")

          password = input("Passowrd: ")
          while not validate_password(password):
            print("Please enter password again")
            password = input("Password: ")
          result = register(email, password)
          if result:
            print(f"{email} successfully registered.")
          else:
            print("Error while registration")
    elif option == 4:
       password = input("Passowrd: ")
       while not validate_password(password):
         print("Please enter password again")
         password = input("Password: ")

       result = register(email, password)
       if result:
          print(f"{email} successfully changed password.")
       else:
          print("Error while entering new password")
    