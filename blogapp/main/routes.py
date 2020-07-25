from flask import render_template, request, Blueprint, redirect, url_for
from blogapp.models import Post, Amount, Choice
from blogapp.main.forms import ProfileForm, DebitCreditForm
from blogapp import db

main = Blueprint('main',__name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', title='Home Title', posts=posts)

@main.route('/funds', methods=['GET', 'POST'])
def funds():
    form = ProfileForm()

    if form.validate_on_submit():
        if form.debitcredit.data:
            return redirect(url_for('main.debitcredit'))
        if form.statement.data:
            return redirect(url_for('main.statement'))

    return render_template('fund.html', title='Funds', form=form)

@main.route('/debitcredit', methods=['GET', 'POST'])
def debitcredit():

    form = DebitCreditForm()
    balance = 0
    amount = Amount.query.all()
    for amt in amount:
        balance = amt.balance
        print(amt.date_created)
        print(amt.category)
        print(amt.camount)
        print(amt.damount)
        print(amt.balance)

    #if form.validate_on_submit():
    if request.method == 'POST':
        print ('working')
        print (balance)
        if form.debit.data:
            cat = form.option.data
            amt = int(form.amount.data)
            balance = balance - int(form.amount.data)
            amount = Amount(category=cat, camount=0, damount=amt, balance=balance)
            db.session.add(amount)
            db.session.commit()

        if form.credit.data:
            cat = form.option.data
            amt = int(form.amount.data)
            print (balance)
            print (int(form.amount.data))
            balance = balance + int(form.amount.data)
            print (balance)
            amount = Amount(category=cat, camount=amt, damount=0, balance=balance)
            db.session.add(amount)
            db.session.commit()

    return render_template('debitcredit.html', form=form, balance = balance, title='Transactions')

@main.route('/statement', methods=['GET', 'POST'])
def statement():

    #form = StatementForm()
    statement = Amount.query.all()

    for tranamt in statement:
        tranbalance = tranamt.balance

    return render_template('statement.html', statement=statement, tranbalance = tranbalance, title='Statments')

@main.route('/choices')
def choices():
    opt = Choice.query.all()
    list_choices = [r.as_dict() for r in opt]
    return jsonify(list_choices)

@main.route('/about')
def about():
    return render_template('about.html', title='About Title')
