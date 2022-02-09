import pytest
from brownie import accounts, Calculator, Machine, Storage
from nose.tools import assert_equal


@pytest.fixture
def calculator():
    account = accounts[0]
    return Calculator.deploy({'from': account})


@pytest.fixture
def machine(calculator):
    account = accounts[0]
    return Machine.deploy(calculator, {'from': account})


@pytest.fixture
def storage():
    account = accounts[0]
    return Storage.deploy(0, {'from': account})


def test_call(machine, calculator):
    machine.addValuesWithCall(calculator, 1, 2)
    assert_equal(machine.calculateResult(), 0)
    assert_equal(calculator.calculateResult(), 3)


def test_delegatecall(machine, calculator):
    machine.addValuesWithDelegateCall(calculator, 1, 2)
    assert_equal(machine.calculateResult(), 3)
