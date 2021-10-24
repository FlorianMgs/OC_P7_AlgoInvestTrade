from data.actions import actions
from models.wallet import Wallet
from time import time


def sort_actions(actions: list) -> list:
    """
    :param actions: list of actions
    :return: list of sorted actions
    Calculate ratio ROI / price for each action.
    Sort them in descending order.
    """
    return sorted(actions, key=lambda x: x[2] / x[1], reverse=True)


def create_wallet(actions: list) -> Wallet:
    """
    :param actions: list of actions
    :return: most optimized wallet
    Iter all sorted actions, create the wallet with best ROI
    """
    wallet = Wallet()
    for action in actions:
        if wallet["price"] < 500:
            wallet.set_action(action)
        else:
            wallet.rem_action(index=-1)
            break
    wallet.set_earnings()
    wallet.set_roi()
    return wallet


def launch_optimized():
    exec_time_start = time()

    best_wallet = create_wallet(sort_actions(actions))

    exec_time_end = time()

    print(f'\n--- Execution time: {exec_time_end - exec_time_start} sec ---\n')
    print(str(best_wallet) + "\n\n")
