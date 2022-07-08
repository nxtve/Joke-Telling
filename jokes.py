#Written by nxt & panguin6010 & llamalectric

import time

print('Want to hear a joke?')
userchoice = raw_input()

if userchoice == 'yes':
    print('Did you hear about the first restaurant to open on the moon?')
    raw_input()
    print('It had great food, but no atmosphere')
    time.sleep(.5)
    print('Want to hear another joke?')
    userchoice2 = raw_input()

    if userchoice2 == 'yes':
        print('Do you want to hear a construction joke')
        raw_input()
        print('im still working on it')
        time.sleep(.3)
        for i in range(3):
            time.sleep(1)
            print("Ha")
        print('Want to hear another joke?')
        userchoice2 = raw_input()

        if userchoice2 == 'yes':
            print('Why dont eggs tell jokes?')
            raw_input()
            print('Theyd crack each other up.')
            time.sleep(.5)
            print('tehe')
            time.sleep(.5)
            print('tehe')
            quit()
        
        else:
            print(';(')
            quit()


    else:
        print(';(')
        quit()
    

else:
    print(';(')
    quit()

