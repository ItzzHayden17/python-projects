def defang_ip(address):
    split_address= address.split(".")
    seperator = "[.]"
    new_address = seperator.join(split_address)
    return new_address

address = "180.121.362.5.1"

print(defang_ip(address))