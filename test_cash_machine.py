from decimal import Decimal

from python.bankaccount.cash_machine import CashMachine


def test_nothing():
    assert True


def test_withdraw_negative():
    cash_machine = CashMachine()
    assert cash_machine.withdraw("town", "Arthur", Decimal(-1)) is False

def test_withdraw_zero():
    cash_machine = CashMachine()
    assert cash_machine.withdraw("town", "Arthur", Decimal(0)) is False

def test_withdraw_more_than_zero_less_than_balance():
    cash_machine = CashMachine()
    assert cash_machine.withdraw("town", "Arthur", Decimal(1)) is True
    assert cash_machine.get_balance_from_account("town", "Arthur") == Decimal(799_999_999)

def test_withdraw_balance():
    cash_machine = CashMachine()
    assert cash_machine.withdraw("town", "Arthur", Decimal(800_000_000)) is False
def test_withdraw_more_than_balance():
    cash_machine = CashMachine()
    assert cash_machine.withdraw("town", "Arthur", Decimal(800_000_001)) is False

def test_get_balance():
    cash_machine = CashMachine()
    assert cash_machine.get_balance_from_account("town", "Arthur") == Decimal(800_000_000)