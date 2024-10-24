# wpp which will keep adding  a stream of numbers inputted by the users 
# the adding stops as soon a user presses q key on the keyboard.
sum=0
while True:
    userinput=input("enter the price:\n")
    if(userinput!='q'):
        sum=sum+int(userinput)
    else:
        print("Thanks for using our calculator")
        print(f"your total bill is::{sum}, Thanks for visiting our Hotal")
        break

