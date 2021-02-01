import re
import datetime

def validate_CreditCardNumber(CreditCardNumber):
    pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    valid = re.match(pattern, CreditCardNumber)
    return valid


def validate_CardHolderName(CardHolder):
    alpha_regex = "^[a-z A-Z]+$"
    if re.match(alpha_regex, CardHolder):
        return True
    else:
        False


def validate_ExpirationDate(ExpirationDate):
    return datetime.datetime.strptime(str(ExpirationDate), "%Y-%m-%d") > datetime.datetime.now()



def validate_SecurityCode(SecurityCode):
    if len(str(SecurityCode)) == 3 and str(SecurityCode).isdigit():
        return True
    else:
        False


def validate_Amount(Amount):
    return isinstance(Amount, int) or isinstance(Amount, float)
