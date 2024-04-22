from typing import Union


grade : Union[int, float] = 85

print(grade)

# # chain 1 run only one Block 

# if False:
#     print("Hello World")
# elif False:
#     print("elif logic 1")
# elif True:
#     print("elif logic 2")
# elif True:
#     print("elif logic 3 ")
# else:
#     print("final else block") 


user_name : str = input("Enter User id : \t")
user_password : str = input("Enter Your Password : \t")

if user_name == "Admin" and user_password == "Admin":
    print("Sent OPT on your registered number")
    opt : str = input("Please  Enter the OTP Received :\t ")
    if  opt == "123456":
            print("Welcome PIAIC")
else:
      print("Invalid User or Password")