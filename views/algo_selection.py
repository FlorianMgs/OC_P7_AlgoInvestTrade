from controllers.optimized import launch_optimized
from controllers.bruteforce import launch_bruteforce


def algo_selection(actions: list):
    """
    :param actions: list of actions
    :return: print best wallet
    """

    while True:
        user_input = input("--- AgloInvest&Trade ---\n\n"
                           "0 - Bruteforce\n"
                           "1 - Optimized\n\n"
                           "b - Back\n\n"
                           "> "
                           )

        match user_input:
            case "0":
                launch_bruteforce(actions)
            case "1":
                launch_optimized(actions)
            case "b":
                break
            case _:
                continue
