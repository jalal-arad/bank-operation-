import csv
import datetime
import matplotlib.pyplot as plt
from csv import DictWriter
import pandas as pd
import numpy as np


print("1. sign up")
print("2. log in")
process_num = input()

field_names = ['fullname', 'phone', 'username', 'password', 'favoritething', 'accountnumber', 'balance', 'shaba']

username_valid = False

if int(process_num) == 1:

    full_name = input("please enter your full name: ")
    phone = input("enter yur phone number: ")
    username = input("choose an username: ")
    password = input("pick a strong password: ")
    favoritething = input("what is your favorite thing: ")
    account_number = input("choose an account number: ")
    balance = input("how much is your balance? ")
    shaba = input("type a shaba number that starts with IR")
    df = pd.read_csv('users.csv')
    ds = pd.DataFrame(df)

    def username_validation(un):
        for i in range(len(ds)):
            if ds.loc[i, 'username'] == un:
                print("choose an other username")
                return False

        dict = {'fullname' : full_name, 'phone': phone, 'username': un,'password': password,'favoritething': favoritething, 'accountnumber': account_number, 'balance': balance, 'shaba': shaba}
        with open('users.csv', 'a') as f_object:

            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        
            dictwriter_object.writerow(dict)
        
            f_object.close()

        global next_step 
        next_step = True
        return True

    while username_validation(username) == False:
        full_name = input()
        phone = input()
        username = input()
        password = input()
        favoritething = input()


elif int(process_num) == 2:
    df = pd.read_csv('users.csv')
    ds = pd.DataFrame(df)
    forgot = input("if you can not remember your password type y.")
    
    if forgot == "y":
        favori = input("type your favoritething: ")
        for i in range(len(ds)):
            if ds.loc[i, 'favoritething'] == favori:
                print("username: ", ds.loc[i, 'username'],"~ password: " ,ds.loc[i, 'password'])
                next_step = True
    else:
        username = input("please enter your username: ")
        password = input("what is your password? ")


        
        def validation(name, pw):
            for i in range(len(ds)):
                if ds.loc[i, 'username'] == name and ds.loc[i, 'password'] == pw:
                    return True

        if validation(username,password):
            for i in range(len(ds)):
                if ds.loc[i, 'username'] == username:
                    print(f"welcome {ds.loc[i, 'fullname']}")
                    next_step = True


#next move why is client hear?
    
try:
    if next_step:
        users_acc = pd.read_csv('users.csv')
        ua = pd.DataFrame(users_acc)
        print("1. deposit")
        print("2. withdraw")
        print("3. transfer")
        process = input("what can i do for you? (type 1 or 2 or 3)")
        for i in range(len(ua)):
            if ua.loc[i, 'username'] == username:
                account_number = ua.loc[i, 'accountnumber']
                balance = ua.loc[i, 'balance']


                if process == "1":
                    field_names2 = ['subject','date','amount','field']
                    subject = input("write a subject for deposition: ")
                    field = "deposit"
                    date = datetime.datetime.now()
                    d_amount = int(input("how much you are gonna deposit? "))

                    # reading the csv file 
                    df = pd.read_csv("users.csv") 
                    
                    # updating the column value/data 
                    df.loc[i, 'balance'] = str(int(balance) + d_amount)
                    
                    # writing into the file 
                    df.to_csv("users.csv", index=False) 
                    done = 1
                    dict2 = {'subject' : subject, 'date': str(date), 'amount': d_amount,'field': field}
                    with open('transactions.csv', 'a') as f_object:

                        dictwriter_object = DictWriter(f_object, fieldnames=field_names2)
                    
                        dictwriter_object.writerow(dict2)
                    
                        f_object.close()

                if process == "2":
                    field_names2 = ['subject','date','amount','field']
                    subject = input("write a subject for withdraw: ")
                    field = "withdraw"
                    date = datetime.datetime.now()
                    w_amount = int(input("how much money you are gonna withdraw? "))
                    if w_amount < int(balance):
                        # reading the csv file 
                        df = pd.read_csv("users.csv") 
                        
                        # updating the column value/data 
                        df.loc[i, 'balance'] = str(int(balance) - w_amount)
                        
                        # writing into the file 
                        df.to_csv("users.csv", index=False) 
                        done = 2
                        dict2 = {'subject' : subject, 'date': str(date), 'amount': w_amount,'field': field}
                        with open('transactions.csv', 'a') as f_object:

                            dictwriter_object = DictWriter(f_object, fieldnames=field_names2)
                        
                            dictwriter_object.writerow(dict2)
                        
                            f_object.close()

                    else:
                        print("You don't have enough funds to withdraw.")
                        exit()
                if process == "3":
                    target_account = input("type your target account (shaba or accountnumber or phone): ")
                    transfer_amount = int(input("how much do you want to transfer? "))
                    if transfer_amount < balance:    
                        for j in range(len(ua)):
                            if str(ua.loc[j, 'accountnumber']) == target_account:
                                field_names2 = ['subject','date','amount','field']
                                subject = input("write a subject for transfer: ")
                                field = "transfer"
                                date = datetime.datetime.now()
                                # reading the csv file 
                                df = pd.read_csv("users.csv") 
                                
                                # updating the column value/data 
                                df.loc[j, 'balance'] = str(int(df.loc[j, 'balance']) + transfer_amount)
                                df.loc[i, 'balance'] = str(int(balance) - transfer_amount)
                                # writing into the file 
                                df.to_csv("users.csv", index=False) 
                                done = 3
                                dict2 = {'subject' : subject, 'date': str(date), 'amount': transfer_amount,'field': field}
                                with open('transactions.csv', 'a') as f_object:

                                    dictwriter_object = DictWriter(f_object, fieldnames=field_names2)
                                
                                    dictwriter_object.writerow(dict2)
                                
                                    f_object.close()

                            if ua.loc[j, 'shaba'] == target_account:
                                field_names2 = ['subject','date','amount','field']
                                subject = input("write a subject for transfer: ")
                                field = "transfer"
                                date = datetime.datetime.now()
                                # reading the csv file 
                                df = pd.read_csv("users.csv") 
                                
                                # updating the column value/data 
                                df.loc[j, 'balance'] = str(int(df.loc[j, 'balance']) + transfer_amount)
                                df.loc[i, 'balance'] = str(int(balance) - transfer_amount)
                                # writing into the file 
                                df.to_csv("users.csv", index=False) 
                                done = 3
                                dict2 = {'subject' : subject, 'date': str(date), 'amount': transfer_amount,'field': field}
                                with open('transactions.csv', 'a') as f_object:

                                    dictwriter_object = DictWriter(f_object, fieldnames=field_names2)
                                
                                    dictwriter_object.writerow(dict2)
                                
                                    f_object.close()

                            if str(ua.loc[j, 'phone']) == target_account:
                                field_names2 = ['subject','date','amount','field']
                                subject = input("write a subject for transfer: ")
                                field = "transfer"
                                date = datetime.datetime.now()
                                # reading the csv file 
                                df = pd.read_csv("users.csv") 
                                
                                # updating the column value/data 
                                df.loc[j, 'balance'] = str(int(df.loc[j, 'balance']) + transfer_amount)
                                df.loc[i, 'balance'] = str(int(balance) - transfer_amount)
                                # writing into the file 
                                df.to_csv("users.csv", index=False) 
                                done = 3
                                dict2 = {'subject' : subject, 'date': str(date), 'amount': transfer_amount,'field': field}
                                with open('transactions.csv', 'a') as f_object:

                                    dictwriter_object = DictWriter(f_object, fieldnames=field_names2)
                                
                                    dictwriter_object.writerow(dict2)
                                
                                    f_object.close()
                    else:
                        print("you can not transfer this amount of money!")

                if done == 1:
                    print(f"{ua.loc[i, 'fullname']} Deposited {d_amount} $. Current balance is: {df.loc[i, 'balance']}")
                elif done == 2:
                    print(f"{ua.loc[i, 'fullname']} Withdrew {w_amount} $. Current balance is: {df.loc[i, 'balance']}")
                elif done == 3:
                    print(f"{transfer_amount} $ transfered from {ua.loc[i, 'phone']} to {target_account}")


except:
    print("something went wrong!")

try:
    sort = input("do yo want to get sorted form of transactions, type (y or n) : ")
    if sort == "y":
        trans = pd.read_csv("transactions.csv") 
        print(trans.sort_values(by = ['date']))
        x = []
        y = []
        for i in range(len(trans)):
            x.append(trans.loc[i,'date'])
            y.append(trans.loc[i, 'field'])
        
        fig, ax = plt.subplots(figsize=(5, 3), layout='constrained')
        ax.bar(x, y)
        plt.show()

except:
    print("something went wrong!")

try:
    show = input("type what subject you want to see? ")
    trans = pd.read_csv("transactions.csv")
    want = []
    for i in range(len(trans)):
        if trans.loc[i, 'subject'] == show:
            want.append(trans.loc[i])
        
    print(want)

except:
    print("something went wrong!")

expenses = []
incomes = []
trans = pd.read_csv('transactions.csv')
for i in range(len(trans)):
    if trans.loc[i, 'field'] == "deposit":
        incomes.append(trans.loc[i])
    elif trans.loc[i, 'field'] == "withdraw" or trans.loc[i, 'field'] == "transfer":
        expenses.append(trans.loc[i])
print("------------------------------------")
print("incomes")
print(incomes)
print("------------------------------------")
print("expenses")
print(expenses)