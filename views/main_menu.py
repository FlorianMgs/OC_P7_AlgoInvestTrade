from views.dataset_selection import dataset_selection
from views.algo_selection import algo_selection
from views.time_complexity import time_complexity_choice


def main_menu():

    while True:
        user_input = input("--- AgloInvest&Trade ---\n\n"
                           "0 - Load dataset\n"
                           "1 - Time complexity\n"
                           "q - Quit\n\n"
                           "> "
                           )

        match user_input:
            case "0":
                algo_selection(dataset_selection())
            case "1":
                time_complexity_choice()
            case "q":
                break
            case _:
                continue
