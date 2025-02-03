from read import read_furniture_details
from operation import display_furniture, update_furniture_stock, generate_invoice, create_transaction_detail
from write import write_furniture_details

print("                                                                             BRJ FURNITURE Nepal                                                                                   ")
print("                                                             MANAMAIJU, Kathmandu | Phone no: 9876643245                                                                      ")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                                Welcome                                                                                         ")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def main():
    """
    Main function to manage furniture store operations: displaying furniture, selling to customers,
    and ordering from manufacturers.
    """
    filename = "furnituredatas.txt"
    furniture_datalist = read_furniture_details(filename)

    while True:
        #displaying options for user
        print("1. Display the furnitures available in BRJ FURNITURE Nepal")
        print("2. Sell furnitures to customers ")
        print("3. Order furnitures from manufacturers")
        print("4. Exit the program")
        choicebyuser = input("Please enter the S.N of your choice: ")

        if choicebyuser == '1':
            display_furniture(furniture_datalist)# displaying available furniture

        elif choicebyuser == '2':# process of selling furniture
            customer_name = input("Enter customer name: ")
            while not customer_name.isalpha():# checking if customer name only contain letters
                print("Invalid input. Customer name can contain only alphabetical letters.")
                customer_name = input("Enter customer name: ")

            transaction_details = []# empty list to store transaction details for invoice
            while True:
                furniture_id = input("Enter furniture ID you want to purchase (or type 'done' to finish): ")
                if furniture_id.lower() == 'done':
                    break
                if not furniture_id.isdigit():
                    print("There is no Furniture Id that you requested, please enter a valid Furniture ID.")
                    continue
                try:
                    quantity = int(input("Enter the quantity of furniture you want to order: "))
                except ValueError:
                    print("Error: Quantity change must be a number, please enter a valid quantity number value.")
                    continue

                if update_furniture_stock(furniture_datalist, furniture_id, -quantity):
                    transaction_detail = create_transaction_detail(furniture_datalist, customer_name, furniture_id, quantity, is_sale=True)
                    if transaction_detail:
                        transaction_details.append(transaction_detail)
                else:
                    print("Invalid furniture ID or there is insufficient stock")

            if transaction_details: # asking for shipping option
                shipping = input("Do you want shipping? (yes/no): ").lower()
                while shipping not in ['yes', 'no']:
                    print("Please enter 'yes' or 'no'.")
                    shipping = input("Do you want shipping? (yes/no): ").lower()

                if shipping == 'yes':
                    shipping_cost = 50
                else:
                    shipping_cost = 0
                generate_invoice("sale", transaction_details, is_sale=True, shipping_cost=shipping_cost)
                write_furniture_details('furnituredatas.txt', furniture_datalist)

        # process of buying furniturew
        elif choicebyuser == '3':
            employee_name = input("Enter employee name: ")
            while not employee_name.isalpha():# checking if employee name only contain letters
                print("Invalid input. Employee name can contain only alphabetical letters")
                employee_name = input("Enter employee name: ")

            transaction_details = []# empty list to store transaction details for invoice
            while True:
                furniture_id = input("Enter furniture ID you want to order (or type 'done' to finish): ")
                if furniture_id.lower() == 'done':
                    break
                if not furniture_id.isdigit():
                    print("There is no Furniture Id that you requested, please enter a valid Furniture ID.")
                    continue
                try:
                    quantity = int(input("Enter quantity of furniture you want to order: "))
                except ValueError:
                    print("Error: Quantity change must be a number, please enter a valid quantity number value.")
                    continue

                if update_furniture_stock(furniture_datalist, furniture_id, quantity):
                    # if stock update is successful, create a transaction details
                    transaction_detail = create_transaction_detail(furniture_datalist, employee_name, furniture_id, quantity, is_sale=False)
                    if transaction_detail:
                        transaction_details.append(transaction_detail)
                else:
                    print("Invalid furniture ID")

            if transaction_details:
                # generate invoice for purchase 
                generate_invoice("purchase", transaction_details, is_sale=False)
                write_furniture_details('furnituredatas.txt', furniture_datalist)

        # option for existing program
        elif choicebyuser == '4':
            print("You are exiting the program, see you next time!")
            break
        #if user input invalid option number then, displaying error message
        else:
            print(" You have enterd invalid choice. Please select a valid option.")


main()
