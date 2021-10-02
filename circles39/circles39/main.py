import os 
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'circles39/3.txt'), 'r') as f:
    signuped = f.read()
def acnt(account):
    global signuped
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'circles39/3.txt'), 'w') as f:
        f.write(account)
    signuped = account
def check():
    global signuped
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'circles39/3.txt'), 'r') as f:
        signuped = f.read()
        print(signuped)
    if signuped != '-':
        return True
    else:
        return False