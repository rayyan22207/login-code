import time
username = {}
def signup():
    print('''Hello
Please enter your name and password''')
    while True:
        name = input('Please enter your name: ')
        if name in username:
            print('Name already in database')
            continue
        else:
            password = input('Please enter your password: ')
            username[name] = password
            break

def login():
    done = False
    count = 0
    while not done:
        name = input('Please enter your name: ')
        if name in username:
            man = False
            while not man:
                print('Please wait checking in database')
                time.sleep(3)
                password = input('Please enter your password: ')
                if password in username[name]:
                    print('ACCESS GRANTED')
                    man = True
                    done = True
                else:
                    print('ACCESS DENIED! If you are unsure press enter and try again later')
                    count += 1
                    if count <3:
                        print('Please try again in a few minutes')
                        time.sleep(60)
                    if count < 5:
                        print('Please try later')
                        time.sleep(360)
                    continue
                if password =='':
                    man = True
        else:
            print('name not in database.(if you wish to stop press enter)')
            if name =='':
                time.sleep(10)
                done = True

signup()
login()
