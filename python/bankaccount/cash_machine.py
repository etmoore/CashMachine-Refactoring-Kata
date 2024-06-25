from decimal import Decimal

from python.bankaccount.branch_finder import BranchFinder


class CashMachine:
    def __init__(self):
        self.branch_finder = BranchFinder()

    def get_balance_from_account(self, town: str, customer:str) -> Decimal:
        """ignore me! test helper"""
        return self.branch_finder \
            .find_branch_for_town(town) \
            .personal_accounts \
            .get_account_for_customer(customer) \
            .balance

    def withdraw(self, town: str, customer: str, amount: Decimal):
        return self.branch_finder \
            .find_branch_for_town(town) \
            .personal_accounts \
            .get_account_for_customer(customer) \
            .withdraw(amount)
