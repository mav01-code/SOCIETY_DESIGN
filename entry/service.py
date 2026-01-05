def notify_resident(block, flat, visitor, visitor_type):
    pass

def request_entry(block, flat, visitor, visitor_type, mode):
    pass


if __name == "__main__":
    visitor = input("Enter the visitor name: ")
    visitor_type = input("(ZOMATO/SWIGGY/MAID/DELIVERY/GUEST/MAINTENANCE)")
    block = input("Enter block : ")
    flat = int(input("Enter flat number: "))
    mode = input("(QR/AUTO/INSTANT)")