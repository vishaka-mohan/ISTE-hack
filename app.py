from flask import Flask,render_template,redirect,request,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



from flask_login import login_user, current_user, logout_user, login_required
from flask_login import UserMixin

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import os
import pathlib

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from ML import pipelines
from ML import Question_Answer
from ML import Keyword_Generator
from ML import  FormulaExtract
from ML import ocr
from ML import pdf_gen

app=Flask(__name__)
app.config['SECRET_KEY']='346c5081b20bc391b121a0c3832dbfd7'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class RegistrationForm(FlaskForm):
    username = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired(), Email()])
    password = PasswordField('', validators=[DataRequired()])
    confirm_password = PasswordField('', 
    validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):

    email = StringField('', validators=[DataRequired(), Email()])
    password = PasswordField('', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


@app.route('/')
@login_required
def landing():
    return render_template('landing.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)



@app.route('/login',methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('unsuccessful. pls check')
    
    return render_template('signin.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))




@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        file1 = request.files['file1']
        
        my_result = ''
        if file1:
            filename1 = file1.filename
            target = os.path.join(APP_ROOT, 'images\\')
            print(target)
        
            if not os.path.isdir(target):
                os.mkdir(target)
            directory_current = pathlib.Path.cwd()
            img_fol = (os.path.join(directory_current, "images/"))
            if len(os.listdir(img_fol) ) != 0:
                os.remove(os.path.join(directory_current, "images/test.png"))
            destination = "\\".join([target, filename1])
            file1.save(destination)
            d= os.path.join(target, "test.png")
            os.rename(destination, d)
            my_result = ocr.readText()

            return render_template('home.html', ocr_text=my_result)

        else:
            text = request.form['text']
            scientific_formulas = FormulaExtract.GetFormula(text)
            chemical_formula = FormulaExtract.chemData(text)
            keywords=[]
            keywords = Keyword_Generator.get_hotwords(text)
            one_word_ans=Question_Answer.GetQuestionAnswer(text)
            short_answers = Question_Answer.short_question_generation(text)
            summary = FormulaExtract.summary(text)
            #pdf_gen.generate_pdf(summary, scientific_formulas, chemical_formula, one_word_ans, keywords)
            return render_template('results.html',one_word_ans=one_word_ans,short_answers = short_answers,keywords=keywords,chemical_formula=chemical_formula,scientific_formulas=scientific_formulas, summary=summary)
            #return render_template('results.html',one_word_ans='',short_answers = '',keywords='',chemical_formula='',scientific_formulas='', summary=text)
    else:
        return render_template('home.html')
    
 
if __name__=='__main__':
    app.run(debug=False)



    
