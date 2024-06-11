from dataclasses import dataclass, field

from python.bankaccount.accounts_manager import PersonalAccountsManager


@dataclass
class Branch:
    manager: str = field(default='Mr Gringotts Goblin')

    def __init__(self):
        self.personal_accounts = PersonalAccountsManager()
