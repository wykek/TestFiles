def  UStoEC():
    USD = 1
    while USD != 0:
        USD = input("Enter a US value or 0 to exit\n")
        XCD = USD * 2.7169
        print("%.2f USD \n%.2f XCD" % (USD, XCD))
        print
def ECtoUS():
    XCD = 1
    while XCD != 0:
        XCD = input("Enter an EC value or 0 to exit\n")
        USD = XCD / 2.7169
        print("%.2f XCD \n%.2f USD" % (XCD, USD))
        print

def main():
    response = 100
    while response != 0:
        response = input("Enter: \n1 for USD to XCD\n2 for XCD to USD\n0 to exit\n")
        if response == 1:
            UStoEC()
        elif response == 2:
            ECtoUS()

main()
