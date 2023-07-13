print("Olde Keychain Shoppe")
print("\n")
def keychain():
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
    print("ADD KEYCHAINS")
    keychain()

def remove_keychains():
    print("REMOVE KEYCHAINS")
    keychain()

def view_order():
    print("VIEW ORDER")
    keychain()

def checkout():
    print("CHECKOUT")
key=keychain()
print("\n")