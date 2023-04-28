PRODUCTS = []

def readFromDataBase():
    f = open("07\dataBase.txt")
    for line in f:
        result = line.split(",")
        myDic = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        PRODUCTS.append(myDic)
    f.close

def writeToDataBase():
    pass

def showMenu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- ShowList")
    print("6- Buy")
    print("7- Exit")

def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    newProduct = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(newProduct)

def edit():
    productCode = input('enter product code for edit: ')
    for product in PRODUCTS:
        if product['code'] == productCode:
            print('\nwhich item do you want to edit:')
            print("1- Name")
            print("2- Price")
            print("3- Count")
            item = int(input('your choice: '))
            if item > 3:
                print('enter valid item menu!')
                break
            else:
                newValue = input('enter new value: ')
                if item == 1:
                    product['name'] = newValue
                    print('edit name successful done')
                    break
                elif item == 2:
                    product['price'] = newValue
                    print('edit price successful done')
                    break
                elif item == 3:
                    product['count'] = newValue
                    print('edit count successful done')
                    break
    else:
        print('enter valid product code!!!')
        
def remove():
    pass

def search():
    userInput = input("type your keyword:")
    for product in PRODUCTS:
        if product['code'] == userInput or product['name'] == userInput:
            print(product['code'], '\t\t', product['name'], '\t\t', product['price'])
            break
    else:
        print('not found')

def showList():
    print("code\t\tname\t\tprice\t\tcount")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"],
               "\t\t", product["count"])

def buy():
    pass

print("WELCOME to My Store")
print("Loading...")
readFromDataBase()
print("Data Loaded")

while(True):
    showMenu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        showList()
    elif choice == 6:
        buy()
    elif choice == 7:
        writeToDataBase()
        exit(0)
    else:
        print("enter valid number")