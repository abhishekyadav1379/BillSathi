from All_function import all_function

def cust_details():
    fn = all_function()
    id = "23080408"
    products = fn.select_db(f"select date,time,prod,quantity,rate,value,method from product where id = '{id}' order by date,time")
    money = fn.select_db(f"select date,time,give,total,method from money where id = '{id}' order by date,time")

    pro_len = len(products)
    mon_len = len(money)

    p,m = 0,0
    while p!=pro_len and m!=mon_len:
        if pro_len == 0:
            break
        if (products[p][0] + products[p][1]) != (money[m][0] + money[m][1]):
            print(money[m])
            m+=1
        else:
            print("------------------------------")
            while (p!=pro_len and m!=mon_len) and ( (products[p][0] + products[p][1]) == (money[m][0] + money[m][1])):
                print(products[p])
                p+=1
            print(money[m])
            m+=1

    print("-----------------------------------")
    while m != mon_len:
        print(money[m])
        m+=1
        
def daily_record():
    fn = all_function()
    date = "2023-08-18"
    products = fn.select_db(f"select id,name,date,time,prod,quantity,rate,value,method from product where date = '{date}' order by time")
    money = fn.select_db(f"select id,name,date,time,give,total,method from money where date = '{date}' order by time")
    
    pro_len = len(products)
    mon_len = len(money)

    p,m = 0,0
    while p!=pro_len and m!=mon_len:
        if pro_len == 0:
            break
        if (products[p][0] + products[p][3]) != (money[m][0] + money[m][3]):
            print("------------------")
            print(money[m])
            m+=1
        else:
            print("------------------------------")
            while (p!=pro_len and m!=mon_len) and ( (products[p][0] + products[p][3]) == (money[m][0] + money[m][3])):
                print(products[p])
                p+=1
            print(money[m])
            m+=1

    print("-----------------------------------")
    while m != mon_len:
        print("-----------------------")
        print(money[m])
        m+=1
        
daily_record()