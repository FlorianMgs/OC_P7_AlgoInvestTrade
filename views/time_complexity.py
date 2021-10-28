from controllers.time_complexity import get_exec_times


def time_complexity_choice():
    while True:
        user_input = input("--- AgloInvest&Trade ---\n\n"
                           "0 - Bruteforce\n"
                           "1 - Optimized\n"
                           "q - Quit\n\n"
                           "> "
                           )

        match user_input:
            case "0":
                get_exec_times(bruteforce=True)
            case "1":
                get_exec_times(bruteforce=False)
            case "q":
                break
            case _:
                continue
