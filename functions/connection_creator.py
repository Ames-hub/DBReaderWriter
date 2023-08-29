from functions.vars import colours, clear_console
import os

def connection_creator():
    # Handle getting the connection host
    clear_console()
    while True:
        try:
            host = input("Please enter your host name or IP: ")
            # Checks if a port was included in the host.
            if ":" in host:
                port = host.split(":")[1] # This one is always first
                host = host.split(":")[0]
            
            # Validate host.
            if host == "" or "." not in host:
                print(colours["red"] + "That hostname or IP address is not valid.\nA valid hostname or IP address will look like \"1.146.252.54\"" + colours["reset"])
                raise ValueError("Please enter a host name or IP address.") # retry
            
            print(colours["green"] + "Host set to " + host +"!"+ colours["reset"])
            break
        except ValueError: # If host is invalid, retry.
            continue

    while True:
        try:
            port = input("Please enter your port: ")
            # Validate port.
            if port == "" or not port.isdigit():
                print(colours["red"] + "That port is not valid.\nA valid port will be a number." + colours["reset"])
                raise ValueError("Please enter a port.") # retry
            
            print(colours["green"] + "Port set to " + port +"!"+ colours["reset"])
            break
        except ValueError:
            continue

    # Handle getting the connection's database
    while True:
        try:
            database = input("Please enter your database's name: ")
            # Validate database.
            if database == "":
                print(colours["red"] + "That database name is not valid.\nA valid database name will look like 'ExampleDB'\n\nThis is seperate to the host/IP" + colours["reset"])
                raise ValueError("Please enter a database name.") # retry
            
            print(colours["green"] + "Database name set to \"" + database +"\"!"+ colours["reset"])
            break
        except ValueError:
            continue

    # Handle getting the connection's username
    while True:
        try:
            username = input("Please enter your username: ")
            # Validate username.
            if username == "" or username == " ":
                print(colours["red"] + "That username is not valid.\nA valid username will look like 'ExampleUser'\n\nThis is seperate to the host/IP" + colours["reset"])
                raise ValueError("Please enter a username.") # retry
            
            print(colours["green"] + "Username set to " + username +"!"+ colours["reset"])
            break
        except ValueError:
            continue

    # Handle getting the connection's password
    while True:
        try:
            password = input("Please enter your password: ")
            # Validate password.
            if password == "":
                print(colours["red"] + "That password is not valid.\nA valid password will look like 'ExamplePassword'\n\nThis is seperate to the host/IP" + colours["reset"])
                raise ValueError("Please enter a password.") # retry
            
            print(colours["green"] + "Password set to " + password +"!"+ colours["reset"])
            break
        except ValueError:
            continue

    os.makedirs("connections/", exist_ok=True)
    with open("connections/" + database + ".env", "w") as f:
        f.write("host=" + host + "\n")
        f.write("port=" + port + "\n")
        f.write("database=" + database + "\n")
        f.write("dbusername=" + username + "\n") # Can't user "username" as it's a environment variable for windows.
        f.write("password=" + password + "\n")