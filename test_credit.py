from bank import 

# --------------------sum

def test_Sum_1(summ):
    assert summ(0) == False
    
def test_Sum_2(summ):
    assert summ < 0 == False
    
def test_Sum_3(summ):
    assert summ > 0 == True
    
# --------------interestRate

def test_interestRate_1(interestRate):
    assert interestRate(0) == False
    
def test_interestRate_2(interestRate):
    assert interestRate < 0 == False
    
def test_interestRate_3(interestRate):
    assert interestRate > 0 == True
    
# -------------------period    
    
def test_period_1(period):
    assert period(0) == False
    
def test_period_2(period):
    assert period < 0 == False
    
def test_period_3(period):
    assert period > 0 == True