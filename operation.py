import datetime
def display_furniture(furniture_datalist):
    """
    Displaying furniture details in table format
    furniture_datalist : A 2d list 
    """
    #Printing the header 
    header = "Id\tManufacturer\t\tProduct\t\t\tQuantity\tPrice"
    print(header)
    print("-" * 80)#  Printing dashes
    
    for furniture in furniture_datalist:

        # Adjusting tabs based on the length of the manufacturer and product names
        manufacturer_tabs = "\t" * (3 - len(furniture[1]) // 8)
        product_tabs = "\t" * (3 - len(furniture[2]) // 8)

        # Creating and printing the row with furniture details
        row = (furniture[0] + "\t" + furniture[1] + manufacturer_tabs +
               furniture[2] + product_tabs + furniture[3] + "\t\t" + furniture[4])
        print(row)


def update_furniture_stock(furniture_datalist, furniture_id, quantity_change):
    """
    It  updates the stock amount of a specific type of furniture.
    furniture_datalist (list): List of furniture details. It is a 2d list.
    furniture_id (str): The specific ID of the furniture that is to be updated.
    quantity_change (int): The number  that changes the quantity of available furnitures.

    Returns:
        bool: Returns true if update was successful or return false if error occured.
    """
    # Checking quantity change is valid number
    try:
        quantity_change = int(quantity_change)
    except ValueError:
        print("Error: Quantity change must be a number, please enter a valid quantity number value.")
        return False # Returns false if quantitity change isnot number
    
    #Using for each loop to find matching id of furniture
    for furniture in furniture_datalist:
        if furniture[0] == furniture_id:
            #calculating new quantity after applying change
            new_quantity = int(furniture[3]) + quantity_change

            if new_quantity < 0:
                print("Error: There is insufficient stock, we are unable to fulfill the request.")
                return False # Returning false if there isnot enough stock
            furniture[3] = str(new_quantity)# updating quantity in list
            return True # Return True if update was successful

    # if id of furniture not found, displaying error message
    print("Error: There is no Furniture Id that you requested, please enter a valid Furniture ID.")
    return False # Return false if id wasnot found

def create_transaction_detail(furniture_datalist, person_name, furniture_id, quantity, is_sale=True):
    """
    Creates a transaction detail for a sale or purchase of furniture.
    furniture_datalist (list):List of furniture details. It is a 2d list.
    person_name (str): The name of the customer(if sale) that made the purchase or the employee if the transaction was not a result of a sale.
    furniture_id (str): It is the ID of the furniture which is used in transaction.
    quantity (int): The amount of furniture which are being transacted.
    is_sale (bool): If True, it is a sales transaction and if False then it is a purchase transaction. Defaults to True.

    Returns:
    dict or None: A dictionary containing the transaction details, or None is the furniture ID is not found:

    """
    price = None # initializing price variable

    #finding price of furniture based on furniture id
    for item in furniture_datalist:
        if item[0] == furniture_id:
            price = int(item[4].replace('$', ''))# Removing dollar sign and converting price to integer
            break
    
    # if furniture id is not found, returning error message
    if price is None:
        print("Error: There is no Furniture Id that you requested, please enter a valid Furniture ID.")
        return None

    # calculating total amount for transaction
    amount = price * quantity

    # creating transaction detail dictionary
    transaction_detail = {}
    transaction_detail["Customer name" if is_sale else "Employee name"] = person_name
    transaction_detail["ID"] = furniture_id
    transaction_detail["Manufacturer"] = item[1]
    transaction_detail["Product"] = item[2]
    transaction_detail["Quantity"] = str(quantity)
    transaction_detail["Price"] = "$" + str(price)
    transaction_detail["Amount"] = "$" + str(amount)
    transaction_detail["Date"] = str(datetime.datetime.now())

    return transaction_detail# returning dictionary with transaction details


def generate_invoice(transaction_type, transaction_details, is_sale, shipping_cost=0):
    """
    Generates and stores an invoice for a transaction.
    transaction_type (str): Kind of transfer (e. g. , “sale” or “purchase”).
    transaction_details (list): A list that is comprised of dictionaries that have transaction details.
    is_sale (bool): True if the company is sellings goods and services, False if the company is buying goods and services.
    shipping_cost (float): Extra cost that emerge because of the transport. Defaults to 0.
    """
    #creating unique filename for invoice using transaction type and current date/ time
    filename = transaction_type + "_invoice_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
    invoice_content = []

    # adding header to invoice
    invoice_content.append("-" * 40 + "\n")
    header = "Customer name:" if is_sale else "Employee name:" #adding customer or employee name
    invoice_content.append(header + transaction_details[0].get("Customer name", transaction_details[0].get("Employee name")) + "\n")
    invoice_content.append("-" * 40 + "\n\n")

    # Adding transaction details to invoice
    for detail in transaction_details:
        invoice_content.append("ID: " + detail["ID"] + "\n")
        invoice_content.append("Manufacturer: " + detail["Manufacturer"] + "\n")
        invoice_content.append("Product: " + detail["Product"] + "\n")
        invoice_content.append("Quantity: " + detail["Quantity"] + "\n")
        invoice_content.append("Price: " + detail["Price"] + "\n")
        invoice_content.append("Date: " + detail["Date"] + "\n")
        invoice_content.append("-" * 40 + "\n\n")

    # Calculating total amount,vat and final amount
    total_amount = 0
    for detail in transaction_details:
        total_amount += float(detail["Amount"].replace('$', ''))

    vat = total_amount * 0.13
    final_amount = total_amount + vat + shipping_cost

    #adding calculation details to invoice
    invoice_content.append("Total Amount: $" + str(total_amount) + "\n")
    invoice_content.append("VAT: $" + str(vat) + "\n")
    invoice_content.append("Shipping Cost: $" + str(shipping_cost) + "\n")
    invoice_content.append("Total amount: $" + str(final_amount) + "\n")
    invoice_content.append("-" * 40 + "\n")

    # Printing invoice to shell
    for line in invoice_content:
        print(line, end='')

    # Saving invoice details to text file
    with open(filename, 'w') as file:
        file.writelines(invoice_content)

    # confirming message
    print("\n" + transaction_type.capitalize() + " invoice created and saved as " + filename)

