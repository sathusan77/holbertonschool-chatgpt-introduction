class Checkbook:
    def __init__(self):
        """Initialize a checkbook with a balance of 0.0"""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
            amount (float): Amount of money to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if sufficient funds exist.

        Parameters:
            amount (float): Amount of money to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_float_input(prompt):
    """
    Prompt the user for a float input, retrying on invalid input.

    Parameters:
        prompt (str): The input message to display.

    Returns:
        float: The valid number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print

