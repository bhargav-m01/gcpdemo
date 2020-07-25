from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError, validators
from flask_wtf.file import FileField,FileAllowed
from wtforms_sqlalchemy.fields import QuerySelectField

from flask_login import current_user
from blogapp.models import Choice

class ProfileForm(FlaskForm):
    debitcredit = SubmitField('Manage Account')
    statement   = SubmitField('Statement')

def choice_query():
    return Choice.query

class DebitCreditForm(FlaskForm):
    option = StringField('', validators=[DataRequired(),Length(max=40)], render_kw={"placeholder": "Type Here"})
    amount = StringField('Amount')
    debit = SubmitField('Debit')
    credit = SubmitField('Credit')
    balance = IntegerField('Balance')
