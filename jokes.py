#Written by nxt & panguin6010 & llamalectric

import time

print('Want to hear a joke?')
userchoice = raw_input()

if userchoice.lower() != 'no':
    print('Did you hear about the first restaurant to open on the moon?')
    raw_input()
    print('It had great food, but no atmosphere')
    time.sleep(.5)
    print('Want to hear another joke?')
    userchoice = raw_input()

    if userchoice.lower() != 'no':
        print('Do you want to hear a construction joke')
        raw_input()
        print('I\'m still working on it')
        time.sleep(.3)
        for i in range(3):
            print("Ha")
            time.sleep(1)
        print('Want to hear another joke?')
        userchoice = raw_input()


        if userchoice.lower() != 'no':
            print('Why don\'t eggs tell jokes?')
            raw_input()
            print('They\'d crack each other up.')
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

