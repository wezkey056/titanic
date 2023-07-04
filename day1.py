
x = 0

while x==0:
    myage = input('What is your age? Press "q" to quit: ')
    if(myage == "q"):
        exit()
    elif(int(myage) <= 0): 
        print('You are not born yet.')
    elif(int(myage) <=3 ):
        print('You are a baby.')
    elif(int(myage) <=5 ):
        print('You are a toddler.')
    elif(int(myage) <=12):
        print('You are a preeteen.')
    elif(int(myage) <=17):
        print('You are a teenager.')
    elif(int(myage) <30):
        print('You are pretty young.')
    elif(int(myage) <=64):
        print('You are middle aged.')
    elif(int(myage) <=99):
        print('You are a senior.')
    elif(int(myage) > 99):
        print('You are a centanarian.')


