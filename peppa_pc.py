from pyfiglet import Figlet
from peppa_pc.controler import run, option


def banner():
    banner_ = Figlet(font='slant')
    print(banner_.renderText('Peppa-Poc'))
    print("<---------WELCOME TO USE THIS PROGRAM--------->")
    print("<---------v1.0 - Author - nJcx86--------->")
    print("\n")


if __name__ == "__main__":
    banner()
    run(option())
