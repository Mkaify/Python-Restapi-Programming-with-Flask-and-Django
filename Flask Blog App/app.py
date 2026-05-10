from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='pic.jpg')
    email = db.Column(db.String(60), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    

posts = [
    {
        'author': 'M Kaif',
        'title': 'Post 1',
        'content': 'Software engg.',
        'date_posted': 'March, 05 2025'
    },
    {
        'author': 'kashi',
        'title': 'Post 2',
        'content': 'Fashion',
        'date_posted': 'Dec 6 2025'
    },
    {
        'author': 'Bhaaijan',
        'title': 'Post 3',
        'content': 'Data Scientist',
        'date_posted': 'Dec 7 2025'
    }
]    
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('That email is already registered.', 'danger')
        elif User.query.filter_by(username=form.username.data).first():
            flash('That username is already taken.', 'danger')
        else:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data),
            )
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])    
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            flash("You have been logged in", 'success')
            return redirect(url_for('home'))
        flash("Login Unsuccessful. Please check email and password", 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    