from app.calculations import add, divide, multiply, subtract,BankHolder
import pytest

@pytest.fixture
def zero_bank_account():
    return BankHolder()

@pytest.fixture
def bank_amount():
    return BankHolder(50)


@pytest.mark.parametrize('num1,num2,expected',[
#---------Add Paramterize to check test on many cases-------
 (1,2,3),
 (4,4,8),
 (9,0,9),
 (8,8,16)
])
def test_add(num1,num2,expected):
    print("Testing add function .. ")
    assert add(num1,num2) == expected
    
def test_subtract():
    assert subtract(4,2)==2

def test_multiply():
    assert multiply(7,2)==14
    
def test_divide():
    assert divide(2,2)==1
    
def test_default_amount(zero_bank_account):
    assert zero_bank_account.balance==0

def test_set_initial_amount(bank_amount):
    assert bank_amount.balance == 50

def test_deposit_amount(bank_amount):
    bank_amount.deposit(40)
    assert bank_amount.balance == 90

def test_withdraw_amount(bank_amount):
    bank_amount.withdraw(30)
    assert bank_amount.balance == 20

def test_collect_interest(bank_amount):
    bank_amount.collect_interest()
    assert round(bank_amount.balance,2) == 55

