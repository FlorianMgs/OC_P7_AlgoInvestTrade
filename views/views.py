from controllers.optimized import launch_optimized
from controllers.bruteforce import launch_bruteforce


def main_menu():

    while True:
        user_input = input("--- AgloInvest&Trade ---\n\n"
                           "1 - Bruteforce\n"
                           "2 - Optimized\n"
                           "q - Quit\n\n"
                           "> "
                           )

        match user_input:
            case "1":
                launch_bruteforce()
            case "2":
                launch_optimized()
            case "q":
                break
            case _:
                continue
