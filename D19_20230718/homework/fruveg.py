items_list=[
    {'name':'Apple','category':'Fruits'},
    {'name':'Carrot','category':'Vegetables'},
    {'name':'Banana','category':'Fruits'},
    {'name':'Broccoli','category':'Vegetables'}
    ]
# fruits=[]
# vegetable=[]
# for i in items_list:
#     item=i['category']
#     if item=='Fruits':
#         fruits.append(i['name'])
#     else:
#         vegetable.append(i['name'])
# dect={"Fruits":fruits,"Vegetable":vegetable}
# print(dect)
#
a={"fruitss":[],"vege":[]}
for i in items_list:
    item=i['category']
    if item=='Fruits':
        a['fruitss'].append(i['name'])
    else:
        a['vege'].append(i['name'])
print(a)