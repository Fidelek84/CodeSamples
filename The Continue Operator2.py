device_list = ["Gi0/0", "Gi0/1", "Gi0/2", "Gi0/3", "Gi0/4", "Gi0/5", "Gi0/6", "Loopback0", "Loopback2"]

#for device in device_list:
 #   if device == "Gi0/2":
  #      continue
   # print(device)
    
for device in device_list:
    if device.startswith("G"):
        continue
    print(device)
