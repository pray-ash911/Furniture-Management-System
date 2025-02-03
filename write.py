# Writing the text file
def write_furniture_details(filename, furniture_datalist):
    """
    Writes furniture details to a file.
    filename (str): Name of the file to write to.
    furniture_datalist (list): A list where each item is a list of furniture details.
    """
    file = open("furnituredatas.txt", 'w')# opening file for writing
    for furniture in furniture_datalist:
        line = ','.join(furniture) + '\n'# joining furniture details with commas and adding newline at end
        file.write(line)# writing line to file
    file.close()
 
