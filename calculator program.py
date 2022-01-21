import random


print("Welcome")
print("Select option.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square_root")
print("6.Random_integer")
again='y'
while again=='y':
    # Input from the user
    option = input("Enter option(1/2/3/4/5/6): ")

    # check the options
    if option in ("1","2","3","4","5","6"):
        # num1 = int(input("Enter first number: "))
        # num2 = int(input("Enter second number: "))

        if option == "1":
            #Addition 
            a=[int(i) for i in input().split()]
            print(sum(a))

        elif option == '2':
            #Subtraction
            a=[int(i) for i in input().split()]
            print()
    

        elif option == '3':
            #Multiply
            a=[int(i) for i in input().split()]
            print()

            

        elif option == "4":
            #Divide
            a=int(input())
            b=int(input())
            print(a/ b)

        elif option == "5":
            #Square root
            a=int(input())
            print(a**0.5)

        elif option == "6":
            #Random integer
            a=int(input())
            b=int(input())
            print(random.randint(a,b))

        print('Do you want to continue!(y/n) : ')
        again=input()


    else:
        print('Please enter thecorrect option.')



# a = [int(i) for i in input().split()]
# print(a)
# r1=[]
# c=0
# for i in a:
#     c+=i
# print(c)

# sum = 0
# num = int(input())
# for i in range(num):
#     sum+=a
# print("Result : ")
# #multiple
# for i in a_list:
#     num = num * i
# print(num)


    
    

# #divide
# def div(a,b):
#     return(a/b)
# print("Ans:",div(25,3))

# #square root
# for i in a:r1.append(i**(1/2)) 
# print(r1)

# #multiply
# #random
# import random
# randomlist=random.sample(range(30,60),10)
# print(randomlist)

# next_option = input(" next option? (yes/no): ")
# if (next_option == "no"):
#     pass
    
# else:
#     print("Input")
