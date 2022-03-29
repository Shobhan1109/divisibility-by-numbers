def divisibleby5(x):
    if (x%5==0):
        return True
    else:
        return False

def divisibleby7(x):
    if (x%7==0):
        return True
    else:
        return False

def divisibleby9(x):
    if (x%9==0):
        return True
    else:
        return False

def divisibleby11(x):
    if (x%11==0):
        return True
    else:
        return False

if __name__=="__main__":
    x=int(input("Enter the number:"))
    r1=divisibleby5(x)
    r2=divisibleby7(x)
    r3=divisibleby9(x)
    r4=divisibleby11(x)

    print("By 5:",r1,"\nBy 7:",r2,"\nBy 9:",r3,"\nBy 11:", r4)