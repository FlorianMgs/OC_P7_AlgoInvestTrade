from contextlib import suppress


class Wallet:
    def __init__(self):
        self.actions = []
        self.price = 0
        self.earnings = 0
        self.roi = 0

    def __str__(self):
        representation = f'Actions: {str(self.actions)}\n' + \
                         f'Price: {self.price} $\n' + \
                         f'Earnings: {self.earnings} $\n' + \
                         f'ROI: {self.roi} %'
        return representation

    def __getitem__(self, item):
        """
        make wallet a subscriptable object, so we are able to call itemgetter on it
        """
        match item:
            case "actions":
                return self.actions
            case "price":
                return self.price
            case "earnings":
                return self.earnings
            case "roi":
                return self.roi

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

    def set_price(self):
        for action in self.actions:
            self.price += action[1]

    def set_earnings(self):
        for action in self.actions:
            self.earnings += action[1] * action[2] / 100

    def set_roi(self):
        with suppress(ZeroDivisionError):
            self.roi = self.earnings / self.price * 100

