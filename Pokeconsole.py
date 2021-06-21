## Main menu, this script is basically the main menu. Because it is a main menu script, and main menu scripts put you in the main menu of the main of the menue mauinajdof.
def clear_console():
    import os
    clear = lambda: os.system('cls')
    clear()


print("Hello, welcome to Pokeconsole! A pokemon game that's played in the python console/nControls: ENTER: next speech in dialouge, that's it!")
press_enter_to_start = input("Press Enter to continue...")
clear_console()
exec(open('frommainmenu.py').read())
