my_list_of_protocols = ["RIP", "OSPF", "ISIS", "EIGRP"]

if "BGP" not in my_list_of_protocols:
    print("Ther is no path vector protocol!")
else:
    print("Path vector detected!")