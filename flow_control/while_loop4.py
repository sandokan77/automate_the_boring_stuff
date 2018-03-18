while True:
    print('Please type your name.')
    name = input("name>>")
    
    if name != 'marcsi':
        print('name is ',name)
        continue
    
    print('Hello marcsi! What is the password?')
    
    password = input("pwd>>")
    
    if password == 'fokhagymas':
        break

print("access granted")
print('Thank you '+name+'!')