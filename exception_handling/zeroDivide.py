def spam(number):
    return 42 / number

def spam2(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        print("Error: Invalid argument.")

#print (spam(0)) #drives application to exception
print (spam2(0)) #gracefully handles exception