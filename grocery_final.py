import mysql.connector as db
import pandas as pd

person_count = 0

try:
    # Connect to the MySQL database
    conn = db.connect(
        host="localhost",
        user="root",
        password="12345",
        database="grocery"
    )
    cur = conn.cursor()

    # Updated including vegetables, fruits, and groceries
    veg = ['beans', 'brinjal', 'broccoli', 'cabbage', 'capsicum', 'carrot', 'chilli', 'coriander', 'cucumber',
           'garlic', 'ginger', 'lemon', 'mushroom', 'onion', 'peas', 'potato', 'pumpkin', 'radish',
           'spinach', 'tomato', 'apple', 'banana', 'orange', 'grapes', 'pineapple',
           'Maggi', 'wheat', 'rice', 'pulses', 'sugar', 'salt', 'tea', 'coffee', 'oil', 'biscuits',
           'chocolates', 'flour', 'bread', 'butter', 'cheese', 'jam', 'honey', 'vinegar',
           'mayonnaise', 'ketchup', 'mustard']

    # Quantities in kgs or units
    quantity = [5, 6, 4, 7, 5, 15, 5, 3, 10, 6, 3, 10, 6, 20, 3, 15, 5, 2, 3, 16,
                8, 10, 12, 5, 7,
                50, 100, 80, 60, 100, 120, 150, 200, 100, 50, 80, 60,
                40, 30, 25, 35, 20, 25, 15, 20, 25, 30]
    
    # Backup quantity to track changes
    bkp_quantity = quantity.copy()

    # Sale price
    sp = [70, 50, 250, 40, 60, 70, 90, 90, 70, 250, 250, 150, 110, 50, 90, 50, 250, 50, 60,
          60, 90, 40, 60, 120, 80,
          150, 60, 80, 120, 60, 25, 40, 50, 180, 90, 120, 140,
          30, 25, 40, 60, 45, 50, 35, 40, 45, 50]

    # Cost price
    cp = [50, 30, 150, 25, 35, 50, 50, 50, 50, 180, 190, 100, 80, 40, 60, 30, 150, 40, 40,
          30, 70, 30, 40, 100, 70,
          100, 40, 50, 80, 40, 15, 25, 30, 120, 70, 90, 100,
          20, 15, 30, 40, 25, 30, 10, 15, 20, 25]  # Adjust prices as per your cost structure

    print('*' * 10, 'GROCERY SHOP', '*' * 10)
    print()

    print("Are You A Customer or Owner : Enter C for Customer |  Enter O for Owner")
    user = input().lower()

    if user == 'o':
        print("Kindly Enter Credentials To login")
        username = input("Enter User Name: ")
        password = input("Enter Password: ")  # Password should be a string
        if username == 'chakri' and password == 'pass':
            while True:
                
                print("1. Insert New Items")
                print("2. Update The Items Quantities")
                print("3. Update the Prices")
                print("4. View the Available Items")
                print("5. View Total Summary")
                print("6. View Customers Info")
                print("7. View Sales Transactions")
                print("8. Remove Items")
                print("9. Exit")

                owner_choice = int(input("Choose an option: "))
                if owner_choice == 1:
                    # Insert new items to the database
                    item = input("Enter item name: ")
                    if item in veg:
                        print(f"{item} is already available in the database")
                        continue
                    quantity1 = int(input(f"Enter Quantity of {item}: "))
                    sale_price = int(input(f"Enter Sale Price of {item}: "))
                    cost_price = int(input(f"Enter Cost Price of {item}: "))

                    # Updating to veg, quantity, sp, cp lists
                    veg.append(item)
                    quantity.append(quantity1)
                    sp.append(sale_price)
                    cp.append(cost_price)

                    cur.execute('''
                        INSERT INTO inventory_management (item, quantity, sale_price, cost_price)
                        VALUES (%s, %s, %s, %s)
                    ''', (item, quantity1, sale_price, cost_price))
                    conn.commit()
                    print(f"{item} has been added to the inventory.")

                elif owner_choice == 2:
                    item = input("Enter item to update their quantities: ")
                    if item in veg:
                        new_qty = int(input(f"Enter the new quantity of {item}: "))
                        idx = veg.index(item)
                        quantity[idx] = new_qty
                        cur.execute("UPDATE inventory_management SET quantity = %s WHERE item = %s", (new_qty, item))
                        conn.commit()
                        print(f"Quantity of {item} updated successfully.")
                    else:
                        print("Item not available in the database")

                elif owner_choice == 3:
                    item = input("Enter Item Name to Update Prices: ")
                    if item in veg:
                        idx = veg.index(item)
                        new_sale_price = int(input(f"Enter new sale price of {item}: "))
                        sp[idx] = new_sale_price

                        new_cost_price = int(input(f"Enter new cost price of {item}: "))
                        cp[idx] = new_cost_price

                        cur.execute("UPDATE inventory_management SET sale_price = %s, cost_price = %s WHERE item = %s",
                                    (new_sale_price, new_cost_price, item))
                        conn.commit()
                        print(f"Prices for {item} updated successfully.")
                    else:
                        print("Item not found in the database")

                elif owner_choice == 4:
                    #Items Info
                    try:
                        print('*' * 16, 'ITEMS INFO', '*' * 16)
                        print()

                        cur.execute('SELECT * FROM inventory_management')
                        ITEM_data = cur.fetchall()  # Fetch all the data

                        # Create a DataFrame from the fetched data
                        df = pd.DataFrame(ITEM_data, columns=['ITEM NAME', 'QUANTITY', 'SALE PRICE', 'COST PRICE'])

                        # Display the DataFrame as a table
                        print(df.to_string(index=False))
                        print('-' * 60)
                        print('-' * 60)
                        print()
                        print()
                        print()
                        print()
                        print()
                       # rows = cur.fetchall()
                        #print("Inventory:")
                        #for row in rows:
                         #   print(row)
                    except db.Error as e:
                        print(f"Error fetching profit summary: {e}")

                elif owner_choice == 5:
                    try:
                        print('*' * 16, 'Summary', '*' * 16)
                        print()

                        # Query to select all data from the profit_data table
                        cur.execute('SELECT * FROM profit_data')
                        profit_data = cur.fetchall()  # Fetch all the data

                        # Create a DataFrame from the fetched data
                        df = pd.DataFrame(profit_data, columns=['GROCERIES', 'QUANTITY', 'QUANTITY BOUGHT', 'PROFIT PER UNIT', 'PROFIT'])

                        # Display the DataFrame as a table
                        print(df.to_string(index=False))

                        # Calculate total profit
                        total_profit = df['PROFIT'].sum()

                        # Display total profit
                        print('-' * 60)
                        print(f"Total Profit: {total_profit}")
                        print()

                    except db.Error as e:
                        print(f"Error fetching profit summary: {e}")


                elif owner_choice == 6:
                    try:
                        print('*' * 16, 'CUSTOMERS INFORMATION', '*' * 16)
                        print()
                        #View Customers Info
                        cur.execute("select * from customers")
                        cus=cur.fetchall()
                        df=pd.DataFrame(cus,columns=['customer_id', 'customer_name', 'customer_mobile_number', 'subtotal'])
                        # Display the DataFrame as a table
                        print(df.to_string(index=False))
                        print('-' * 60)
                    except db.Error as e:
                        print(f"Error fetching profit summary: {e}")

                elif owner_choice==7:
                    try:
                        print('*' * 16, 'SALES INFORMATION', '*' * 16)
                        print()
                        #view Sales Transactions
                        cur.execute("select * from sales_transactions")
                        cus=cur.fetchall()
                        df=pd.DataFrame(cus,columns=['customer_id','item','quantity','price_per_unit','total_price'])
                        # Display the DataFrame as a table
                        print(df.to_string(index=False))
                        print('-' * 60)
                    
                    except db.Error as e:
                        print(f"Error fetching profit summary: {e}")
                elif owner_choice==8:
                    
                    if veg==[]:
                            print('Your Database is already empty')
                            print()
                    else:    
                        item_remove= input('Which ITEM do you want to remove?')
                            
                        if item_remove in veg:
                                
                            idx=veg.index(item_remove)
                            veg.remove(item_remove)
                            quantity.remove(quantity[idx])
                            sp.remove(sp[idx])
                            cp.remove(cp[idx])
                            # Add quantity back to inventory
                            cur.execute(f"DELETE FROM inventory_management WHERE item = '{item_remove}'")
                            conn.commit()
                            
                            print(f"{item_remove} has been Deleted")
                        else:
                                print(f"{item} not found")          
                elif owner_choice==9:
                    print()
                    break

                    
                    

                else:
                    print("Please choose a valid option")
        else:
            print("Incorrect Credentials, Access Denied")

    elif user == 'c':
        # Purchasing Code
        cur.execute('SELECT * FROM inventory_management')
        rows = cur.fetchall()
        print("Available items in the store:")
        for row in rows:
            print(row)

        # Bill
        while True:
            person_veg = []
            person_qty = []
            person_price = []
            person_count += 1
            print('CUSTOMER', person_count)
            print("Enter Your Name")
            name = input()
            print("Hello", name, ": Enter Your Mobile Number")
            mobile = int(input('Enter mobile number: '))

            while True:
                print(name, "what do you want to buy?")
                item = input()

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
                        # Reduce quantity in inventory
                        cur.execute(f"UPDATE inventory_management SET quantity = quantity - {qty} WHERE item = '{item}'")
                        conn.commit()
                    elif quantity[idx]==0:
                        print('OUT OF STOCK')
                    else:
                        while True:
                                #code for if item is available sufficienty when person choosen more quantitu
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
                                    cur.execute(f"UPDATE inventory_management SET quantity = quantity - {qty} WHERE item = '{item}'")
                                    conn.commit()
                                    break
                            
                            else:
                                break

                    
                else:
                    print(f"Sorry! The {item} is not available.")
                
                while True:
                
                    print('1. ADD MORE GROCERIES')
                    print('2. REMOVE GROCERIES')
                    print('3. VIEW CART')
                    print('4. CHECK OUT')
                
                    ch=input('Choose an option: ')
                    if ch=='1':
                        break
                    elif ch=='2':
                        if person_veg==[]:
                            print('Your cart is already empty')
                            print()
                        else:    
                            item_remove= input('Which ITEM do you want to remove?')
                            
                            if item_remove in person_veg:
                                
                                idx_r=person_veg.index(item_remove)
                                idx_r1=veg.index(item_remove)
                                removed_qty=person_qty[idx_r]
                                quantity[idx_r1]=quantity[idx_r1]+person_qty[idx_r]#to reset the quantity back to initial
                                # Add quantity back to inventory
                                cur.execute(f"UPDATE inventory_management SET quantity = quantity + {removed_qty} WHERE item = '{item_remove}'")
                                conn.commit()
                                person_veg.remove(item_remove)
                                person_qty.remove(person_qty[idx_r])
                                person_price.remove(person_price[idx_r])
                                
                                idx_r1=veg.index(item_remove)
                                print(item_remove,'has been removed from your cart')
                                print()
                                
                            else:
                                print(item_remove,'is not there in your cart')
                            
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
                    
                            
                    elif ch == '4':
                        customer_id = cur.lastrowid
                        print('*' * 17, 'BILL', '*' * 17)
                        print('GROCERY', ' ' * 10, 'QUANTITY', 'PRICE PER KG', 'PRICE')

                        subtotal = 0
                        for v in zip(person_veg, person_qty, person_price):
                            subtotal += v[1] * v[2]
                            print(v[0], '--->', ' ' * 10, v[1], ' ' * 2, v[2], ' ' * 2, v[1] * v[2])

                            cur.execute('''
                                INSERT INTO sales_transactions (customer_id, item, quantity, price_per_unit, total_price)
                                VALUES (%s, %s, %s, %s, %s)
                            ''', (customer_id, v[0], v[1], v[2], v[1] * v[2]))
                            

                        print('SUBTOTAL = ', subtotal)
                        print('PLEASE PAY', subtotal, '.Rs')
                        print('*' * 40)

                        cur.execute('''
                            INSERT INTO CUSTOMERS(customer_id, customer_name, customer_mobile_number, subtotal)
                            VALUES (%s, %s, %s, %s)
                        ''', (customer_id, name, mobile, subtotal))
                        

                        total_profit = 0
                        for i in range(len(quantity)):
                            if quantity[i] != bkp_quantity[i]:
                                profit_veg = sp[i] - cp[i]
                                qty_bgt = bkp_quantity[i] - quantity[i]
                                total_profit += profit_veg * qty_bgt
                                print(veg[i], '--->', ' ' * 10, bkp_quantity[i], ' ' * 5, qty_bgt, ' ' * 6, profit_veg, ' ' * 6, profit_veg * qty_bgt)
                                cur.execute('''
                                    INSERT INTO profit_data (item, quantity, quantity_purchased, profit_per_unit, total_profit)
                                    VALUES (%s, %s, %s, %s, %s)
                                ''', (veg[i], bkp_quantity[i], qty_bgt, profit_veg, profit_veg * qty_bgt))
                                conn.commit()
                        conn.commit()
                        break
                        
                    else:
                        print('Please choose the correct option')
                    
                if ch=='4':
                    break

                
            print("****BILL****")
            print("Name:", name)
            print("Mobile:", mobile)
            print("Items Bought:")

            total_bill = 0
            for i in range(0, len(person_veg)):
                print(person_veg[i], "--->", person_qty[i], "kg/unit--->", person_price[i])
                total_bill += person_price[i]
            print("Total Bill:", total_bill)
            print()

            print("Press (yes/no) TO Proceed to Next Customer")
            cont_shopping = input().lower()
            if cont_shopping == 'no':
                break

finally:
    # Closing the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
