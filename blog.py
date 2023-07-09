from flask import Flask, render_template, url_for, request
from forms import ContactForm
from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a0a6e3c473a07ba264f44a9411c2724b'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USS_SSL'] = True
app.config['MAIL_USERNAME'] = 'jlawer90@gmail.com'
app.config['MAIL_PASSWORD'] = 'newicui4cu2'

mail.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('/index.html')

@app.route('/about')
def about():
    return render_template('/profile.html')

@app.route('/projects')
def projects():
    return render_template('/projects.html')


# contact form on homepage
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate == False:
            flash('Please fill all fields.')
            return render_template('/contact.html', form=form)
        else:
            message =  Message(sender='jlawer90@gmail.com', recipients=['jhay_quin@icloud.com'])
            message.body= """ From: %s <%s> %s """ % (form.name.data, form.email.data, form.message.data)
            mail.send(message)

            return 'Message Sent.'

    elif request.method == 'GET':
        return render_template('/contact.html', form=form) 

if __name__ == '__main__':
    app.debug = True
    app.run()