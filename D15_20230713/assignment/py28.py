print("Olde Keychain Shoppe")
a=0
sales_tax=8.25/100
shipping_cost=4
per_shipping=1
while True:
    print("1.Add Keychain To Order\n2.Remove Keychain From Order\n3.View Current Order\n3.Checkout")
    choice=int(input("Please enter your choice: "))
    if choice==1:
        add_keychains(a)
    if choice==2:
        remove_keychains(a)
    if choice==3:
        view_order()
    if choice==4:
        checkout()
def add_keychains(a):
    add=int(input(f"You have {a} keychain.How many to add?:"))
    a+=add
    print(f"You have {add} keychain")
    keychain()
def remove_keychains(a):
    remove=int(input(f"You have {a} keychain.How many to remove?:"))
    a-=remove
    print(f"You have {a} keychain")
    keychain()
def view_order():
    print(f"You have {a} keychain")
    print(f"keychain cost 10 each\nTotal cost is",(10*a))
    keychain()
def checkout():
    name=input("what is your name? ")
    print(f"You have {a} keychain.\nkeychain cost 10 each\nTotal cost is ",(a*10))
    print(f"Thanks for your order, {name}!")
key=keychain()