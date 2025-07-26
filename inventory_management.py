inventory = {
    'apples' : {'price' : 100 , 'quantity' : 200},
    'banana' : {'price' : 50 , 'quantity' : 100},
    'mango' : {'price' : 150 , 'quantity' : 300},
}

inventory['green-apple'] = {'price' : 90 , 'quantity' : 30}
print(inventory)

inventory['mango']['price'] = 200
print(inventory)



for key,value in inventory.items():
    # selling apples
    if(key == 'apple'):
        value['quantity'] -= 50
    
print(inventory)


for key,value in inventory.items():
    if(value['quantity'] < 100):
        print(key)
