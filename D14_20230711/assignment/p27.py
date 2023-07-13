print("Olde Keychain Shoppe")
print("\n")
a=0
def keychain():
    global a
    print("1.Add Keychain To Order\n2.Remove Keychain From Order\n3.View Current Order\n3.Checkout")
    print("\n")
    choice=int(input("Please enter your choice: "))
    print("\n")
    if choice==1:
        add_keychains()
    if choice==2:
        remove_keychains()
    if choice==3:
        view_order()
    if choice==4:
        checkout()

def add_keychains():
    global a
    add=int(input(f"You have {a} keychain.How many to add?:"))
    a+=add
    print(f"You have {add} keychain")
    keychain()

def remove_keychains():
    global a
    remove=int(input(f"You have {a} keychain.How many to remove?:"))
    a-=remove
    print(f"You have {a} keychain")
    keychain()

def view_order():
    global a
    print(f"You have {a} keychain")
    print(f"keychain cost 10 each\nTotal cost is",(10*a))
    keychain()

def checkout():
    global a
    name=input("what is your name? ")
    print(f"You have {a} keychain.\nkeychain cost 10 each\nTotal cost is ",(a*10))
    print(f"Thanks for your order, {name}!")
key=keychain()