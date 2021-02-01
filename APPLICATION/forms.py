import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, validators, FloatField
from wtforms.validators import DataRequired, Length, equal_to, ValidationError
from wtforms_components import DateRange



def validate_creditCardNumber(form, field):
    if not  len(str(field.data)) == 16:
        raise ValidationError('Please enter a valid Card Number.')



def validate_dateRange(form, field):
    if not datetime.datetime.strptime(str(field), '%Y-%m-%d') > datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d'):
        raise ValidationError('Expiration Date Cannot be less than current date')

class PaymentForm(FlaskForm):
    creditCardNumber = StringField( label=('Enter Credit Card Number:'), validators=[DataRequired("Invalid Credit Card Number."), validate_creditCardNumber
                                            ,validators.Regexp('^[0-9]*$', message="Card must contain only numbers")])
    confirm_creditCardNumber = StringField('Confirm Credit Card Number',
                                           validators=[DataRequired(), equal_to('creditCardNumber')])
    cardHolder  = StringField('Card Holder', validators=[DataRequired(), Length(min=2,max=100)])
    expirationDate =  DateField('Expiration Date (YYYY-MM-DD)', format='%Y-%m-%d', validators=[DataRequired("Invalid Date Field"), DateRange(min=datetime.date.today())])
    securityCode = IntegerField('Security Code', validators=[DataRequired("Invalid Security Code"), validators.NumberRange(min=100, max=999)])
    amount = FloatField('Amount', validators=[DataRequired("Invalid Amount")])

    submit = SubmitField('Pay')




