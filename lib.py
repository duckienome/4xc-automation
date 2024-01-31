from rich.console import Console
from styles import colors
console = Console()

# abort msg variable
abort_msg = f"[{colors["error"]}]Aborting..."




def get_int(value):
    '''Take integer and repeat until an integer is given'''
    try:
        int_value = int(console.input(f"[{colors["input"]}]{value}"))
        return int_value
    except ValueError:
        console.print(f"[{colors["warn"]}]Specify an Integer")
        get_int(value)




def get_file(file_path):
    '''
    Ask your for file and retrun the files content in a list
    If file is not found ask user to abort or to provide a correct file name.
    '''
    file_name = console.input(f"[{colors["input"]}]{file_path}")
    try:
        with open(file_name,'r') as file:
            apps = file.read().splitlines()   
        return apps
    except FileNotFoundError:
        console.print(f"[{colors["error"]}]File not Found [/] [{colors["warn"]}](0 to Abort)")
        if file_name == '0':
            console.print(abort_msg)
            exit(3)
        get_file(file_path)

