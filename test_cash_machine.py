from decimal import Decimal

from python.bankaccount.cash_machine import CashMachine


def test_nothing():
    assert True


def test_withdraw():
    cash_machine = CashMachine()
    assert cash_machine.withdraw("town", "Arthur", Decimal(-1)) is False