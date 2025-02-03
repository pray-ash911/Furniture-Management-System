def read_furniture_details(filename):
    """
        Reads furniture details from a file and returns them as a list of lists.
        filename (str): Name of the file with furniture data.
    """
    furniture_datalist = []# initializing empty list to store furniture details
    file = open('furnituredatas.txt', 'r')# opening file for reading
    for eachlines in file:
        furniture_details = eachlines.replace("\n", "").split(',')# Removing newline character and split line by commas
        furniture_datalist.append(furniture_details)
    file.close()
    return furniture_datalist # Returning 2d list of furniture details


