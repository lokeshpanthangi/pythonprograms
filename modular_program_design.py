def addbook(self,x):
    print("AddedBooks")
def searchbook():
    print("SearchedBooks")
def display():
    print("Displayed")
def leave():
    print("Bye Bye")
    exit()

def main():
    print("1. Add Book\n2. Searchbook\n3. Display Inventory\n4. Exit")
    k = int(input("Enter Your Choice :"))
    if k == 1:
        addbook()
    elif k == 2:
        searchbook()
    elif k == 3:
        display()
    elif k == 4:
        leave()
    else:
        print("Try again")
        main()
main()

