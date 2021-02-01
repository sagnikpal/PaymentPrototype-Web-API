import requests

base = "http://127.0.0.1:5000/"


# test endpoint:  check api behaviour for different request
def test_invalidate_endPoint(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code == 404:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid envdpoint sequence
def test_invalidate_endPoint_Sequence(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid CreditCardNumber
def test_invalidate_CreditCardNumber(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid CardHolder
def test_invalidate_CardHolder(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid ExpirationDate
def test_invalidate_ExpirationDate(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid SecurityCode
def test_invalidate_SecurityCode(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid Amount
def test_invalidate_Amount(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test valid payment
def test_validPayment(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code == 200:
        print("Valid Payment Test: Passed")
    else:
        print("Valid Payment Test: Failed")


# invalid endpoint testing
print("\n" + "-" * 10 + "Invalid End Point Test" + "-" * 10)
test_invalidate_endPoint("/payment")
print("-" * 25 + "\n")

# invalid endpoint sequence testing
print("\n" + "-" * 10 + "Invalid endpoint sequence Test" + "-" * 10)
test_invalidate_endPoint("/10-23/333/SPal/ProcessPayment/20.8/0545362587961578")
test_invalidate_endPoint("/9123-4567-8912-3456/John/12-23/134/4544.8/ProcessPayment")
print("-" * 25 + "\n")

# invalid CreditCardNumber testing
print("\n" + "-" * 10 + "Invalid CreditCardNumber Test" + "-" * 10)
test_invalidate_CreditCardNumber("/ProcessPayment/0524362587961578/SPal/2020-10-23/333/20.8")
test_invalidate_CreditCardNumber("/ProcessPayment/5124456789123456/John/2020-10-23/333/45.8")
print("-" * 25 + "\n")

# invalid CardHolder testing
print("\n" + "-" * 10 + "Invalid CardHolder Test" + "-" * 10)
test_invalidate_CardHolder("/ProcessPayment/3123446789123456/mi34ke23/2040-10-23/343/100.8")
test_invalidate_CardHolder("/ProcessPayment/3123454789123456/241/2020-10-23/343/900.8")
print("-" * 25 + "\n")

# invalid ExpirationDate testing
print("\n" + "-" * 10 + "Invalid ExpirationDate Test" + "-" * 10)
test_invalidate_CardHolder("/ProcessPayment/3123456784123456/SPal/2020-10-23/333/600.8")
test_invalidate_CardHolder("/ProcessPayment/3123456789423456/John/2020-10-23/333/12.8")
print("-" * 25 + "\n")

# invalid SecurityCode testing
print("\n" + "-" * 10 + "Invalid SecurityCode Test" + "-" * 10)
test_invalidate_CardHolder("/ProcessPayment/3123456789124456/SPal/2020-10-23/ABC/5000.34")
test_invalidate_CardHolder("/ProcessPayment/3123456789124456/John/2020-10-23/3A3/34.8")
print("-" * 25 + "\n")

# invalid Amount testing
print("\n" + "-" * 10 + "Invalid Amount Test" + "-" * 10)
test_invalidate_CardHolder("/ProcessPayment/3123456789123456/SPal/2020-10-23/1234/john")
test_invalidate_CardHolder("/ProcessPayment/3123456789423456/John/2020-10-23/3333/SPal")
print("-" * 25 + "\n")

# valid endpoint
print("\n" + "-" * 10 + "Valid Payment Test" + "-" * 10)
test_validPayment("/ProcessPayment/3123456789123456/SPal/2021-10-23/333/4.9")
test_validPayment("/ProcessPayment/3123456789123456/SPal/2021-10-23/333/34.9")
test_validPayment("/ProcessPayment/9123-4567-8942-3456/Andrew/2021-10-23/134/4564.8")
print("-" * 25 + "\n")
