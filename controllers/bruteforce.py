from data.actions import actions
from models.wallet import Wallet
from time import time
import itertools
from operator import itemgetter


def bruteforce(actions: list) -> list:
    """
    :param actions: list of actions
    :return: list of all possible combinations of actions
    """
    combinations = []

    """
    There is 2**len(actions) combinations of possible wallets. 
    We create a list of binary words representing possible combinations of actions with itertools.
    """
    possible_combinations = map(list, itertools.product([False, True], repeat=len(actions)))

    """
    Creation of possible wallets with binary words created earlier.
    """
    for combination in possible_combinations:
        possible_wallet = {}
        for action, choice in zip(actions, combination):
            possible_wallet[action] = choice
        combinations.append(possible_wallet)
    return combinations


def create_all_wallets(combinations: list) -> list:
    """
    :param combinations: all possible wallet combinations {action1 -> tuple: choice1 -> bool, etc...}
    :return: list of all wallet objects
    We iter all possible combinations.
    If an action is choosen (==True), we append it to the wallet.
    When wallet is populated, we set price, earnings and roi
    """
    wallets = []

    for combination in combinations:
        wallet = Wallet()
        for action, choice in combination.items():
            if choice:
                wallet.set_action(action)
        wallet.set_earnings()
        wallet.set_roi()
        wallets.append(wallet)

    return wallets


def keep_valid_wallets(wallets: list) -> list:
    """
    :param wallets: list of all possible Wallet objects
    :return: list of wallets with price < 500$
    """
    valid_wallets = []
    for wallet in wallets:
        if wallet.get_price() <= 500:
            valid_wallets.append(wallet)
    return valid_wallets


def get_best_wallet(wallets: list) -> Wallet:
    """
    :param wallets: list of all valid wallets (price <= 500$)
    :return: the most optimized wallet
    we sort all the wallets by their respective earnings in descending order.
    we return the first item of the sorted list
    """
    return sorted(wallets, key=itemgetter("earnings"), reverse=True)[0]


def launch_bruteforce():
    exec_time_start = time()

    print("Generating all possible wallets...")
    all_wallets = create_all_wallets(bruteforce(actions))

    print("Filtering wallets...")
    valid_wallets = keep_valid_wallets(all_wallets)

    print("Getting wallet with best earnings...")
    best_wallet = get_best_wallet(valid_wallets)

    exec_time_end = time()

    print(f'\n--- Execution time: {exec_time_end - exec_time_start} sec ---\n')
    print(str(best_wallet)+ "\n\n")