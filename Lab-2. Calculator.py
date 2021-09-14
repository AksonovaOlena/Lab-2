print("Привіт! Шалений калькулятор допоможе тобі порахувати твої цукерки в заначці! Погнали!")
while True:
    a=float(input("Напишіть перше число:"))
    what=input("Що робимо?(+,-,*,/):")
    b=float(input("Напишіть друге число:"))
    if what == "+":
        c=a+b
        print("Результат:"+str(c))
    elif what == "-":
        c=a-b
        print("Результат:"+str(c))
    elif what == "*":
        c=a*b
        print("Результат:"+str(c))
    elif what == "/":
        c=a/b
        print("Результат:"+str(c))
    else:
        print("Хибна операція :3")   
input()



    
    
