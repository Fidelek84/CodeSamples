device_list = ["R1", "R2", "R3", "R4", "R5", ]
interface_list = ["int g0/0", "int g0/1", "int g0/2", "int g0/3", "int g0/4"]

for device in device_list:
    for interface in interface_list:
        print(f"{interface}\n description this is {interface} on {device}")
    
