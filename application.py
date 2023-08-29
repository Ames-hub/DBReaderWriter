import psycopg2, os, dotenv, dotenv
from functions.vars import colours, clear_console
from functions.connection_creator import connection_creator

os.makedirs("connections/", exist_ok=True)

def main():
    # Handles loading the connection details from the .env file.
    if os.path.exists("connections/"):
        # From here, we can know connections folder exists and that we should ask if they want to create a new connection or use an existing one.
        while True:
            connections = os.listdir("connections/")
            if len(connections) == 0:
                connection_creator()
                # No connections exist, so we should create one.
            elif len(connections) == 1:
                # Only one connection exists, so we should use that.
                inp = input("Would you like to use the existing connection? (Yes/No) default is Yes: ").lower()
                if "y" in inp or inp == "":
                    dotenv.load_dotenv("connections/" + connections[0])
                    break
                else:
                    print(colours["green"] + "Lets make a new one then." + colours["reset"])
                    connection_creator()

            else:
                # Get the user's choice.
                while True:
                
                    # Prints each connection in the connections folder.
                    print(colours["cyan"] + "Please select a connection to use:" + colours["reset"])
                    for i in range(len(connections)):
                        print(colours["cyan"] + str(i) + ". " + colours["reset"] + connections[i].replace(".env", ""))

                    try:
                        choice = int(input("Please enter the number of the connection you want to use: "))
                        if choice >= len(connections) or choice < 0:
                            print(colours["red"] + "That is not a valid choice." + colours["reset"])
                            raise ValueError("Please enter a valid number.")

                        # Get connection details
                        connection_choice = connections[choice]
                        dotenv.load_dotenv("connections/" + connection_choice)
                        if os.environ.get("host") == None:
                            host = "localhost"
                        break  # This is to break the inner while loop
                    except ValueError:
                        continue
                break  # This is to break the outer while loop
    else:
        connection_creator()

    # Connect to the database
    try:
        conn = psycopg2.connect(
            host=os.environ.get("host"),
            database=os.environ.get("database"),
            port=os.environ.get("port"),
            user=os.environ.get("dbusername"),
            password=os.environ.get("password")
        )
        cur = conn.cursor()
        print(colours["green"] + "Connected to \""+os.environ.get("database")+"\" database!" + colours["reset"])
    except psycopg2.OperationalError as err:
        print(colours["red"] + "Failed to connect to database.\n"+str(err) + colours["reset"])
        exit()

    # From here, let the user interact with the database in a try-except block for a psycopg2.OperationalError and keyboard interrupt.
    try:
        command = ""
        while True:
            try:
                print(colours["cyan"]+"Please enter a command to execute line by line.\nPress CTRL + C to exit.\ntype \"RUN\" to execute."+colours["reset"])
                line = input(">>> ")
                if line.lower() == "run":
                    print("RUNNING THE FOLLOWING SQL CODE AND PRINTING ALL THAT RETURNS:")
                    for line in command.split("\n"):
                        print(colours["black"]+"    "+line+colours["reset"])
                    cur.execute(command)
                    try:
                        result = cur.fetchall()
                        for instance in result:
                            print(instance)
                    except:
                        pass
                    conn.commit()
                    command = ""
                    print(colours["green"] + "Executed!" + colours["reset"])
                    continue

                # Continues to take in lines from the user until they type "RUN", adds them to the command variable.
                command += line + "\n"

            except psycopg2.ProgrammingError as err:
                print(colours["red"] + "That is not a valid command.\n"+str(err) + colours["reset"])
                continue
    except KeyboardInterrupt:
        print(colours["green"] + "Exiting..." + colours["reset"])
        exit()
    except psycopg2.OperationalError as err:
        print(colours["red"] + "Lost connection to database.\n"+str(err) + colours["reset"])
        exit()

if __name__ == "__main__":
    main()