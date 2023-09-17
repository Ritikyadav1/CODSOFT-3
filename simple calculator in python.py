a=int(input("Enter the 1 number : "))
b=int(input("Enter the 2 number : "))

print("1 add ")
print('2 subtract')
print('3 multiply')
print('4 divide ') 

choice = input("Enter what operation you want to perform : ")
if choice == '1':
    print(f'The sum of {a} and {b} = {a+b}')
elif choice == '2' :
    print(f'The subtract of {a} and {b} = {a-b}')
elif choice == '3' :
     print(f'The multiplication  of {a} and {b} = {a*b}')
elif choice == '4' :
     print(f'The division of {a} and {b} = {a/b}')
else:
    print("Invalid choice ")
