from traceback import print_tb

balance=500
PIN=1234
code=334
choice=1,2,3,4,5,6,7,8
chances = 3
print('WELCOME TO safaricom .....dial 334 for mpesa services')
x=int(input("enter code;"))
if x==code:
    print("1 send money")
    print("2withdraw cash")
    print("3 buy airtime")
    print("4 loans and savings")
    print("5 financial services ")
    print("6 lipa na mpesa")
    print("7 my account")
    print("pochi la biashara")
    print("mpesa ratiba")
    print(".............................")
    print("enter your choice")

x=int(input('choice:.... '))
if x==1:
    print("enter phone:" )
while chances>=0:
    if choice==
    x=int(input('Enter PIN Number: '))
    if x==PIN:
        print('****Login Sucessful****')
        x = int(input('Press 1 to continue: '))
        if x == 1:
            print('1. Check Balance')
            print('2. Withdraw Amount')
            d=int(input('Enter Your Choice: '))
            if d==1:
                print('Your Balance is:')
                print(b)
            elif d==2:
                w=int(input('Enter amount to withdraw:'))
                if w<b:
                    print('withdraw successful')
                    b=b-w
                else:
                    print('insufficient funds')
        else:
            print('Successfully Logged Out')
    else:
        print('***********Invalid Password*************')
        chances=chances-1
        if chances==0:
            print('**************************Account Blocked********************************')
            break