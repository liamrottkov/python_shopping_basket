print("""
Shopping Basket Options
-----------------------
1: Add item
2: Remove item
3: View basket
0: Exit program
""")

option = int(input('Enter an option: '))

shopping_basket = {}

while option != 0:
    if option == 1:
        item = input('Enter an item: ')
        qnty = int(input('Enter the quantity: '))
        shopping_basket[item] = qnty

    elif option == 2:
        item = input('Enter an item: ')
        del(shopping_basket[item])

    elif option == 3:
        for item in shopping_basket:
            print(item,':',shopping_basket[item])

    elif option != 0:
        print("You didn't enter a valid number.")

    option = int(input('\n\nEnter an option: '))

else:
    print('Shopping basket program closed.')
