c = ""

class stack:

    st = []

    def push(self, e, st):
        st.append(float(e))
        return st

    def pop(self,st):
        if len(st) == 0:
            print("underflow :'(")
        else:
            print("popped ~_~ item -> " + str(st.__getitem__(len(st)-1)))
            st.__delitem__(len(st)-1)
        return st

    def print_stack(self,st):
        if (len(st) == 0):
            print("empty stack ;-;")
        else:
            print("current stack ;)")
            for i in range(len(st)):
                print("{0:.4f}".format(st[len(st) - i - 1]))

while True:
    s = stack()

    print("1. push")
    print("2. pop")
    print("3. print")
    print("4. exit")
    print("----------------")

    c = input().strip()

    if c == "exit":
        print("ok byeeee!!! UwU")
        break

    elif c == "push":
        while True:
            try:
                s.push(input(),s.st)
            except ValueError:
                print("Enter a number XD")
                continue
            break

    elif c == "pop":
        s.pop(s.st)

    elif c == "print":
        s.print_stack(s.st)

    else:
        print("Enter a valid input o_o")
        continue
    print("________________")