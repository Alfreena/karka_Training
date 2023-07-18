print("Olde Keychain Shoppe")
a=0
keychain_cost=10
sales_tax=8.25/100
shipping_cost=5
per_shipping=1
#num_keychain=a
#pr=num_keychain*keychain_cost
def add_keychains(a):
    add=int(input(f"You have {a} keychain.How many to add?:"))
    return a+add
    print(f"You have {a} keychain")

def remove_keychains(a):
    remove=int(input(f"You have {a} keychain.How many to remove?:"))
    a-=remove
    print(f"You have {a} keychain")
    return a
def view_order(a,keychain_cost,sales_tax,shipping_cost,per_shipping):
    print(f"You have {a} keychain")
    print(f"keychain cost 10 each\nTotal cost is",(10*a))
def checkout(a,keychain_cost,sales_tax,shipping_cost,per_shipping):
    name=input("what is your name? ")
    print(f"You have {a} keychain.\nkeychain cost 10 each\nTotal cost is ",a*10)
    print(f"Thanks for your order, {name}!")
while True:
    print("1.Add Keychain To Order\n2.Remove Keychain From Order\n3.View Current Order\n3.Checkout")
    choice=int(input("Please enter your choice: "))
    if choice==1:
        a=add_keychains(a)
    elif choice==2:
        a=remove_keychains(a)
    elif choice==3:
        a=view_order(a,keychain_cost,sales_tax,shipping_cost,per_shipping)
    elif choice==4:
        a=checkout(a,keychain_cost,sales_tax,shipping_cost,per_shipping)
    else:
        print("wrong choice")
        break