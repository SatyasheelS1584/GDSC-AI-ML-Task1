c = ""
s = []


def push(st, e):
    st.append(e)
    return st

def pop(st):
    if len(st) == 0:
        print("underflow :'(")
    else:
        print("popped ~_~ item -> " + str(st.__getitem__(len(st)-1)))
        st.__delitem__(len(st)-1)
    return st

while True:

    print("1. push")
    print("2. pop")
    print("3. print")
    print("4. exit")
    print("----------------")

    c = input().strip()

    if c == "exit":
        print("ok byeeee!!! UwU")
        break

    if c == "push":
        while True:
            try:
                f = float(input())
            except ValueError:
                print("Enter a number XD")
                continue
            break
        s = push(s,f)

    elif c == "pop":
        s = pop(s)

    elif c == "print":
        if(len(s) == 0):
            print("empty stack ;-;")
        else:
            print("current stack ;)")
            for i in range(len(s)):
                print("{0:.4f}".format(s[len(s)-i-1]))

    else:
        print("Enter a valid input o_o")
        continue
    print("________________")