from colorama import Fore
import time


def red(str_):
    print(Fore.RED + '[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '   ' + str_)


def yellow(str_):
    print(Fore.YELLOW + '[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '   ' + str_)


def green(str_):
    print(Fore.GREEN + '[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '   ' + str_)


def lightcyan(str_):
    print(Fore.LIGHTCYAN_EX + '[{}]'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '   ' + str_)


if __name__ == "__main__":
    red('test')
