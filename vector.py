from datetime import datetime

def parse_command(user_input):
    return user_input.strip().lower()


def hello_command():
    print("Hello Partha, how can I assist you?")

def force_command():

    try:
        mass = float(input("Mass(kg): "))
        acceleration = float(input("Acceleration(m/s^2): "))
        force = mass * acceleration

        print(f"Force: {force} N")
    
    except ValueError:
        print("Please enter valid numbers.")


def time_command():

    print(datetime.now().strftime("%H:%M:%S"))

def help_command():
    print("""
Available commands:
hello
force
time
help
exit
""")
    
commands = {
    "hello": hello_command,
    "force": force_command,
    "time": time_command,
    "help": help_command
}

while True:

    user_input = input("Vector >> ")

    command = parse_command(user_input)

    if command == "exit":
        break

    elif command in commands:
        commands[command]()

    else: 
        print("Invalid Input. Type <help> for helps.")





