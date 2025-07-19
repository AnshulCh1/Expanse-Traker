from crud import add_product, view_products, update_quantity, delete_product,search_product, low_stock_report, get_all_products_for_chart
from database import init_db
import matplotlib.pyplot as plt
import pyfiglet
from colorama import Fore, Style

init_db()

def show_quantity_chart():
    data = get_all_products_for_chart()
    if not data:
        print("No data to display.")
        return
    
    names = [item[0] for item in data]
    quantities = [item[1] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(names, quantities, color='lightblue')
    plt.xlabel('Product Name')
    plt.ylabel('Quantity')
    plt.title('Inventory Quantities')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def menu():
    print("***************************************************************")
    print("***************************************************************") 
    # Fancy big title using pyfiglet with red color
    ascii_banner = pyfiglet.figlet_format("EXPANSE TRAKER", font="slant")
    print(Fore.RED + ascii_banner + Style.RESET_ALL)  # Set the banner in red

    while True:
        print("***************************************************************")
        print("***************************************************************") 
        print("\n  Inventory Management Menu")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Quantity")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Low Stock Report")
        print("7. Show Inventory Chart 📊")
        print("8. Exit")
        print("*******************************************")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Product Name: ")
            category = input("Category: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            add_product(name, category, quantity, price)

        elif choice == '2':
            products = view_products()
            for p in products:
                print(p.id, p.name, p.category, p.quantity, p.price)

        elif choice == '3':
            pid = int(input("Product ID: "))
            qty = int(input("New Quantity: "))
            update_quantity(pid, qty)

        elif choice == '4':
            pid = int(input("Product ID to Delete: "))
            delete_product(pid)

        elif choice == '5':
            name = input("Product name to search: ")
            results = search_product(name)
            for p in results:
                print(p.id, p.name, p.quantity)

        elif choice == '6':
            threshold = int(input("Enter quantity threshold: "))
            results = low_stock_report(threshold)
            for p in results:
                print(p.id, p.name, p.quantity)

        elif choice == '7':
            show_quantity_chart()

        elif choice == '8':
            print(" Exiting Inventory System.")
            break

        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    menu()