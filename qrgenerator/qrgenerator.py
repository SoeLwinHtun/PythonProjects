import pyqrcode

# ask for the string to generate qr code

string = input("Enter the string : ")


# ask for file name to be saved

filename = input("Enter the file name : ")+".svg"

#generate qr code

url = pyqrcode.create(string)

#save the file

url.svg(filename,scale = 8)