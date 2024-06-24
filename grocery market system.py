
person_count=0
#inventory has 20 vegetables
# Updated inventory including vegetables, fruits, and groceries
veg = ['beans', 'brinjal', 'broccoli', 'cabbage', 'capsicum', 'carrot', 'chilli', 'coriander', 'cucumber', 
       'garlic', 'ginger', 'lemon', 'mushroom', 'onion', 'peas', 'potato', 'pumpkin', 'radish', 'spinach', 
       'tomato', 'apple', 'banana', 'orange', 'grapes', 'pineapple',
       'Maggi', 'wheat', 'rice', 'pulses', 'sugar', 'salt', 'tea', 'coffee', 'oil', 'biscuits', 'chocolates',
       'flour', 'bread', 'butter', 'cheese', 'jam', 'honey', 'vinegar', 'mayonnaise', 'ketchup', 'mustard']

# Quantities in kgs or units (adjust quantities as needed)
quantity = [5, 6, 4, 7, 5, 15, 5, 3, 10, 6, 3, 10, 6, 20, 3, 15, 5, 2, 3, 16,
            8, 10, 12, 5, 7,
            50, 100, 80, 60, 100, 120, 150, 200, 100, 50, 80, 60,
            40, 30, 25, 35, 20, 25, 15, 20, 25, 30]  # Adjust quantities as per your stock

# Backup quantity to track changes
bkp_quantity = quantity.copy()

# Suggested selling prices per kg or unit (adjust prices as needed)
# These are approximate prices, please adjust based on your local market conditions
sp = [70, 50, 250, 40, 60, 70, 90, 90, 70, 250, 250, 150, 110, 50, 90, 50, 250, 50, 60, 
      60, 90, 40, 60, 120, 80,
      150, 60, 80, 120, 60, 25, 40, 50, 180, 90, 120, 140,
      30, 25, 40, 60, 45, 50, 35, 40, 45, 50]  # Adjust prices as per your pricing strategy

# Suggested cost prices per kg or unit (adjust prices as needed)
# These are approximate prices, please adjust based on your supplier costs
cp = [50, 30, 150, 25, 35, 50, 50, 50, 50, 180, 190, 100, 80, 40, 60, 30, 150, 40, 40, 
      30, 70, 30, 40, 100, 70,
      100, 40, 50, 80, 40, 15, 25, 30, 120, 70, 90, 100,
      20, 15, 30, 40, 25, 30, 10, 15, 20, 25]  # Adjust prices as per your cost structure


print('*'*10,'GROCERY SHOP','*'*10)
print()
while True:
    #bill 
    person_veg=[]
    person_qty=[]
    person_price=[]
    person_count=person_count+1
    print('CUSTOMER',person_count)
    
    while True:
        
        #each person
        
        item=input('What do you want to buy? ')

        if item in veg:
                
            idx= veg.index(item)
            print('How much quantity of',item,'do you want?(kgs)')
            qty=float(input())
                
            if qty<=quantity[idx]:
                    
                if item in person_veg:
                        
                    idx2=person_veg.index(item)
                    person_qty[idx2]=person_qty[idx2]+qty

                else:
                    
                    person_veg.append(item) #adding vegetables to the person's bill
                    person_qty.append(qty) #adding quantity to the person's bill
                    person_price.append(sp[idx]) #adding price of the vegetable to the bill

                quantity[idx]=quantity[idx]-qty #quantity reduction
                    
                
            elif quantity[idx]==0:

                print('OUT OF STOCK')

            else:
                while True:
                        
                    print('The available quantity of',item,'is',quantity[idx],'kgs.Do you want to change the quantity and buy?(y/n)')
                    ch1=input()
                    if ch1=='y':
                        qty=float(input('How much quantity do you want to buy?(kgs)'))
                        if qty<=quantity[idx]:
                            if item in person_veg:
                                idx2=person_veg.index(item)
                                person_qty[idx2]=person_qty[idx2]+qty

                            else:
                                person_veg.append(item) #adding vegetables to the person's bill
                                person_qty.append(qty) #adding quantity to the person's bill
                                person_price.append(sp[idx]) #adding price of the vegetable to the bill

                            quantity[idx]=quantity[idx]-qty #quantity reduction
                            break
                    
                    else:
                        break
        else:
            print(item,'is not available.')
        while True:
            
            print('1. ADD MORE GROCERIES')
            print('2. REMOVE GROCERIES')
            print('3. VIEW CART')
            print('4. CHECK OUT')
            
            ch=input('Choose an option: ')
            if ch=='1':
                break
                
            
            elif ch=='3':
                #print cart
                print('-'*17,'CART','-'*17)
                print()
                print('ITEMS',' '*5,'QUANTITY,','PRICE PER KG,','PRICE')
                subtotal=0
                for v in zip(person_veg,person_qty,person_price):
                            
                    subtotal=subtotal+(v[1]*v[2])
                    print(v[0],' '*10,v[1],' '*2,v[2],' '*2,v[1]*v[2])
                    print()
                print()
                print('CART TOTAL  = ',subtotal)
                print('-'*40)
                continue
            elif ch=='2':
                if person_veg==[]:
                    print('Your cart is already empty')
                    print()
                else:    
                    item_remove= input('Which ITEM do you want to remove?')
                    
                    if item_remove in person_veg:
                        
                        idx_r=person_veg.index(item_remove)
                        idx_r1=veg.index(item_remove)
                        quantity[idx_r1]=quantity[idx_r1]+person_qty[idx_r]#to reset the quantity back to initial
                        person_veg.remove(item_remove)
                        person_qty.remove(person_qty[idx_r])
                        person_price.remove(person_price[idx_r])
                        
                        idx_r1=veg.index(item_remove)
                        print(item_remove,'has been removed from your cart')
                        print()
                        
                    else:
                        print(item_remove,'is not there in your cart')
                    
                    
            elif ch=='4':
                # print bill
                print('*'*17,'BILL','*'*17)
                print()
                print('GROCERY',' '*10,'QUANTITY,','PRICE PER KG,','PRICE')
                        
                subtotal=0
                for v in zip(person_veg,person_qty,person_price):
                            
                    subtotal=subtotal+(v[1]*v[2])
                    print(v[0],'--->',' '*10,v[1],' '*2,v[2],' '*2,v[1]*v[2])
                    print()
                print()
                print('SUBTOTAL  = ',subtotal)
                print('PLEASE PAY',subtotal,'.Rs')
                print('*'*40)
                break
            else:
                print('Please choose the correct option')
            
        if ch=='4':
            break
        

    ch2= input('Do you want to close the shop?(y/n) ')
               
               
    if ch2== 'y':
                
        print('Closing the shop....')
        print()
        #report
        print('*'*16,'summary','*'*16)
        print()
        print('Total number of costumers: ',person_count)
        print('GROCERIES',' '*5,'QUANTITY,',' '*2,'QUANTITY BOUGHT,',' '*2,'PROFIT PER KG,'*2,'PROFIT')
        total_profit =0
        for i in range(0,len(quantity)):
            if quantity[i]!=bkp_quantity[i]:
                
                profit_veg=sp[i]-cp[i]
                qty_bgt=bkp_quantity[i]-quantity[i]
                total_profit=total_profit + (profit_veg*qty_bgt)
                
                print(veg[i],'--->',' '*10,bkp_quantity[i],' '*5, qty_bgt,' '*6,profit_veg,' '*6,(profit_veg*qty_bgt))
                print()

        print()
        print('TOTOAL PROFIT   = ',total_profit)
                   
        break 
                
                
          
            
            
            


