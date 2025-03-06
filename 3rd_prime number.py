num=int (input("enter a number:"))
if(num>2):
    for i in range(3,num):
        if(num%i==0):
            print(f"{num} is not prime number")
            break
        else:
            print(f"{num} is prime number")
            break
else:
    print(f"{num} is prime number")