import random
pin_numbers=[1234,1245,1256,1267,1290]
valid=0
while valid==0:
    pin=int(input('enter the 4-digit password:'))
    for i in pin_numbers:
        if i==pin:
            print('correct password')
            valid+=1
            break
        else:
            print('enter correct password')
            valid=0
            break
           
count=0
while count==0:
    language=int(input('select language to continue\n 0 for telugu\n 1 for english\n 2 for hindi :'))
   
    if language==0:
        print("language selected is telugu")
        count+=1
    elif language==1:
        print('language selceted is english')
        count+=1
    elif language==2:
        print('language selceted is hindi')
        count+=1
    else:
        print('please select provide language')
        count=0
account=int(input('enter \n o for withdrawal \n 1 for balance enqiury\n 2 for cancellation:'))
if account==0:
    print("you selected for withdrawal")
    amount=int(input('enter the amount:'))
    while amount>100:
        print('transaction processing {}'.format(amount))
        print('please take the amount')
        reciept=input('you want reciept yes or no:')
        if reciept=='yes':
            print('collect reciept')
            print("thank you")
        else:
            print("thank you")
        
        break
    else:
        print('enter amount above 100')
elif account==1:
    print('please wait for balance:')
    b=random.randint(0,10000)
    print(b)
elif account==2:
    print("your transaction is cancelled")
