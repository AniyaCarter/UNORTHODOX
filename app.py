from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
	# return "Hello Meke!"
	return render_template('home.html')

@app.route('/home')
def home2():
	# return "Hello Meke!"
	return render_template('home.html')


@app.route('/about')
@app.route('/About')
def about():
	return render_template('about.html')


@app.route('/contact')
@app.route('/Contact')
def contact():
	# return "Hello Meke!"
	return render_template('contact.html')


@app.route('/faq')
@app.route('/Faq')
@app.route('/FAq')
@app.route('/FAQ')
@app.route('/fAQ')
@app.route('/faQ')
def faq():
	return render_template('faq.html')

@app.route('/formal')
@app.route('/Formal')
def formal():
	# return "Hello Meke!"
	return render_template('formal.html')


@app.route('/informal')
@app.route('/Informal')
def informal():
	return render_template('informal.html')


@app.route('/men')
@app.route('/Men')
def men():
	return render_template('men.html')


@app.route('/payment')
@app.route('/Payment')
def payment():
	return render_template('payment.html')


@app.route('/thankyou')
@app.route('/Thankyou')
@app.route('/ThankYou')
def thankyou():
	return render_template('thankyou.html')

@app.route('/*')
def home3():
	# return "Hello Meke!"
	return render_template('home.html')

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))