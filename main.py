def is_palindrome(string):
    string = string.lower().replace(' ', '')
    rev_string = ''.join(reversed(string))
    return string == rev_string

my_str = 'А роза упала на лапу Азора'
print("Задача 1")
print('True\n' if is_palindrome(my_str) else 'False\n')

def roma_conv(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    if number >=1 and number <=2000:
        while number:
            div = number // num[i]
            number %= num[i]
    
            while div:
                print(sym[i], end = "")
                div -= 1
            i -= 1
    else:
        print("Input error: number range is [1,...2000]" )

if __name__ == "__main__":
    number = 2765
    print("Задача 2")
    print("Roman number is", end =" ")
    roma_conv(number)


def balance(Str):
    stack= []
    if Str != "":
        for i in Str:
            if i in open:
                stack.append(i)
            elif i in close:
                pos = close.index(i)
                if ((len(stack) > 0) and (open[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return "Non valid"
        if len(stack) == 0:
            return "Valid"
    else:
        print("Задача 3"+"\nInput error" )


if __name__ == "__main__":
    open = ["[","{","("]
    close = ["]","}",")"]
    Str="{[()())]{}}"
    print("\nЗадача 3")
    print("\n"+balance(Str)+"\n")
    balance(Str)

 
x1 = 11011
x2 = 100
x1 = str(x1)
x2 = str(x2)
for char in x1 and x2:
    if char!="0" and char!="1":
       print("Задача 4"+"\nInput error" )
       break
    else:    
        Multiply= int(x1, 2) * int(x2, 2)
        binMul = bin(Multiply)[2:]
        print("Задача 4"+"\nResult = " + binMul)
        break

    
        



