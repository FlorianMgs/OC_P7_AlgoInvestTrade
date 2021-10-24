from views.dataset_selection import dataset_selection
from views.algo_selection import algo_selection


def main_menu():

    while True:
        user_input = input("--- AgloInvest&Trade ---\n\n"
                           "0 - Load dataset\n"
                           "q - Quit\n\n"
                           "> "
                           )

        match user_input:
            case "0":
                algo_selection(dataset_selection())
            case "q":
                break
            case _:
                continue
