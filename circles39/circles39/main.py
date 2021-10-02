signuped = False
def acnt(account):
    global signuped
    if account == '-':
        signuped = False
    else:
        with open('signup.txt', 'w') as f:
            f.write(account)
def check():
    global signuped
    with open('signup.txt', 'r') as f:
        signuped = f.read()
    if signuped != '':
        return True
    else:
        return False