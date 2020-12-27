# Run server
# 1. environment path : set FLASK_APP=server.py
# 1-1. if we want to use DEBUG mode : set FLASK_ENV=development
#       수정된 코드를 서버 재시작하지 않고도 반영.
# 2. flask run

# 3. Web app 배포 : pythonanywhere.com에 접속하여 배포 가능.
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

"""
# Not recommeded : 같은 형태의 코드가 반복 됨.
@app.route('/')
def my_home():
    return render_template("./index.html")

@app.route('/about.html')
def about():
    return render_template("./about.html")

@app.route('/works.html')
def work():
    return render_template("./works.html")

@app.route('/contact.html')
def work():
    return render_template("./contact.html")
"""
@app.route('/')
def my_home():
    return render_template("./index.html")

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject, message])




# Recommeded : 같은 형태 코드를 한 번만 사용.
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# Request
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #data = request.form['message'] # this also be possible
            print(data)
            #write_to_file(data)
            write_to_csv(data)

            #return 'form submitted by POST'
            # Redirect
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong.'
    return 'form submitted hooorayy'


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    """
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    """
    return render_template('login.html', error=error)
