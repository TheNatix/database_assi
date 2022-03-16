import mysql.connector as ms


def main_menu():
    dbconn = ms.connect(user='root', password='root', host='localhost', database= "Cafe")
    cursor = dbconn.cursor()
    while True:
        print("Main Menu \n 1. Returns the price of the cheapest product \n 2. Shows how much we have after searching by the type like coffee or cake. \n 3. show names of the employees that successfully delivered the food \n 4. To quickly give the number to customers that want call employee with complaint \n 5. To Count how many products we have by the ingredients \n 6. To show view \n 7. To check what food emloyee delivered \n Q. Quit \n --------")
        x = input("Please choose one option: ")
        if x == "1":
            cursor.execute("SELECT Min(price) AS SmallestPrice FROM `products`")
            results = cursor.fetchall()
            for x in results:
                print(x)
            input("Press any key to continue")
        if x == "2":
            t = input("Enter the name of the ingredient ")
            sql = 'SELECT SUM(available) FROM `products` WHERE ingredients = "' + str(t) + '"'
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                print(x)
            input("Press any key to continue")
        if x == "3":
            sql = 'SELECT employee.name FROM `orders` JOIN employee on orders.id_e = employee.id where status = "delivered"'
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                print(x)
            input("Press any key to continue")
        if x == "4":
            sql = 'SELECT customer.name,employee.phone_number FROM `orders` JOIN employee on orders.id_e = employee.id join customer on orders.id_c = customer.id where status = "undelivered"'
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                print(x)
            input("Press any key to continue")
        if x == "5":
            sql = 'SELECT COUNT(name) FROM `products` GROUP by ingredients'
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                print(x)
            input("Press any key to continue")
        if x == "6":
            sql = 'SELECT * FROM `sales`'
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                print(x)
            input("Press any key to continue")
        if x == "7":
            t = input("Enter the order id")
            sql = 'SELECT products.name,employee.name FROM `products` JOIN orders ON products.id = orders.id_p JOIN employee on employee.id = orders.id_e where orders.id = "' + str(t) +'"'
            cursor.execute(sql)
            results = cursor.fetchall()
            for x in results:
                print(x)
            input("Press any key to continue")
        if x == "Q":
            exit()