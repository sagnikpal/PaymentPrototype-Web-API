from flask_restful import abort
import datetime
from APPLICATION.paymentValidation import *


def abortInvalidated_CreditCardNumber(CreditCardNumber):
    if not validate_CreditCardNumber(CreditCardNumber):
        abort(400,  description="Issue with Credit Card Number")


def abortInvalidated_CardHolder(CardHolder):
    if not validate_CardHolderName(CardHolder):
        abort(400,  description="Issue with Card Holder ")


def abortInvalidated_ExpirationDate(ExpirationDate):
    if not validate_ExpirationDate(ExpirationDate):
        abort(400,  description="Issue with Expiration Date")


def abortInvalidated_SecurityCode(SecurityCode):
    if not validate_SecurityCode(SecurityCode): abort(400,  description="Issue with SecurityCode")


def abortInvalidated_Amount(Amount):
    if not validate_Amount(Amount): abort(400,  description="Issue with Amount")


def dataAbort(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
    abortInvalidated_CreditCardNumber(CreditCardNumber)
    abortInvalidated_CardHolder(CardHolder)
    abortInvalidated_ExpirationDate(ExpirationDate)
    abortInvalidated_SecurityCode(SecurityCode)
    abortInvalidated_Amount(Amount)
