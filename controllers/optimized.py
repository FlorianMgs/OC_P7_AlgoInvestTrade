from models.wallet import Wallet
from time import time
from contextlib import suppress


def sort_actions(actions: list) -> list:
    """
    :param actions: list of actions
    :return: list of sorted actions
    Calculate earnings for each action.
    Sort them by earnings in descending order.
    """
    with suppress(ZeroDivisionError):
        actions = sorted(actions, key=lambda x: x[1] * x[2] / 100, reverse=True)
    return actions


def add_actions(actions: list, wallet: Wallet) -> Wallet:
    """
    :param actions: list of actions
    :param wallet: Wallet to populate with actions
    :return: most optimized wallet
    Iter all sorted actions, create the wallet with best ROI
    """

    for i, action in enumerate(actions):
        """
        First, add best performing action
        """
        if i == 0:
            wallet.set_action(action)

        """
        Then, add actions with price < remaining cash to spend
        """
        if i > 0 and 0 < action[1] < 500 - wallet["price"]:
            wallet.set_action(action)
    else:
        wallet.set_earnings()
        wallet.set_roi()
        return wallet


def launch_optimized(actions):
    exec_time_start = time()

    wallet = Wallet()
    best_wallet = add_actions(sort_actions(actions), wallet)

    exec_time_end = time()

    print(f'\n--- Execution time: {exec_time_end - exec_time_start} sec ---\n')
    print(str(best_wallet) + "\n\n")
