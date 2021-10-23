from contextlib import suppress


class Wallet:
    def __init__(self):
        self.actions = []
        self.price = 0
        self.earnings = 0
        self.roi = 0

    def __str__(self):
        representation = f'Actions: {str(self.get_actions())}\n' + \
                         f'Price: {self.get_price()} $\n' + \
                         f'Earnings: {self.get_earnings()} $\n' + \
                         f'ROI: {self.get_roi()} %'
        return representation

    def __getitem__(self, item):
        match item:
            case "actions":
                return self.get_actions()
            case "price":
                return self.get_price()
            case "earnings":
                return self.get_earnings()
            case "roi":
                return self.get_roi()

    """
    
    ACCESSORS
 
    """

    def set_action(self, action: tuple):
        """
        :param action: tuple
        append action to wallet, update price
        """
        self.actions.append(action)
        self.price += action[1]

    def rem_action(self, index: int):
        """
        :param index: index of action to remove from wallet
        remove action from wallet, then update price
        """
        with suppress(IndexError):
            del self.actions[index]
            self.price -= self.actions[index][1]

    def get_actions(self):
        return self.actions

    def set_price(self):
        for action in self.actions:
            self.price += action[1]

    def get_price(self):
        return self.price

    def set_earnings(self):
        for action in self.actions:
            self.earnings += action[1] * action[2] / 100

    def get_earnings(self):
        return self.earnings

    def set_roi(self):
        with suppress(ZeroDivisionError):
            self.roi = self.earnings / self.price * 100

    def get_roi(self):
        return self.roi

