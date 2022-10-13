from os import system, name 

def clear():
    # windows 
    if name == 'nt':
        _ = system('cls')
    # mac 
    else:
        _ = system('clear')