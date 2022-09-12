platform = input("what is your platform? ")
show_command = input("What show command do you want to send? ")

if platform == "cisco":
    command_to_send = f"enable\n{show_command}\n"
    print(command_to_send)