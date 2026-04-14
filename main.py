import products
import store

MENU = """
   Store Menu
   ----------   
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""
# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def list_products(my_store):
    print("------")
    i = 1
    for product in my_store.get_all_products():
        print(f"{i}. ", end=""), product.show()
        i += 1
    print("------")


def print_amount(my_store):
    quantity = my_store.get_total_quantity()
    print(f"Total of {quantity} items in store")


def make_order(my_store):
    list_products(best_buy)
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    all_products = my_store.get_all_products()
    while True:
        item = input("Which product # do you want? ")
        quantity = input("What amount do you want? ")
        if item == "":
            break
        try:
            product = all_products[int(item) - 1]
            quantity = int(quantity)
        except IndexError:
            print("Error adding product!")
        except ValueError:
            print(f"Error while making order! invalid literal for int() with base 10: '{quantity}'")
        else:
            shopping_list.append((product, quantity))
    try:
        payment = my_store.order(shopping_list)
        print(f"Order made! Total payment: ${payment}")
    except Exception as e:
        print(e)


def start():
    while True:
        print(MENU)
        choice = input("Please choose a number: ")
        if choice == "1":
            list_products(best_buy)
        elif choice == "2":
            print_amount(best_buy)
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            quit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    start()
