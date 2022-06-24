
###############################################
#          Import some packages               #
###############################################
import flask
from flask import Flask, render_template, request, url_for, redirect, send_file, flash
import os

from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'secretKey'
###############################################
#       Render Contact page                   #
###############################################
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return send_file('static/docs/resume.pdf', attachment_filename='resume.pdf')



@app.route("/sendemail/", methods=['POST'])
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        your_name = "Juma Liko"
        your_email = "jumaliko711@gmail.com"
        your_password = "yqpofahwpjongczv"

        # Logging in to our email account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(your_email, your_password)

        # Sender's and Receiver's email address
        sender_email = "jumaliko711@gmail.com"
        receiver_email = "wise_mercy@yahoo.com"

        msg = EmailMessage()
        msg.set_content("First Name : "+str(name)+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage : "+str(message))
        msg['Subject'] = 'Website Visitor Form Request'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
            flash('Message sent successfully')
        except:
            pass
    return redirect('/')



  #       msg['To'] = receiver_email
		# "https://api.mailgun.net/v3/sandbox3da66b652fdc484891fda8fcf710e888.mailgun.org/messages",
		# auth=("api", "c3a27e5910eb9aa3b5f82b08421678fe-c3d1d1eb-db4415f8"),
		# data={"from": "Mailgun Sandbox <postmaster@sandbox3da66b652fdc484891fda8fcf710e888.mailgun.org>",
		# 	"to": "juma liko <jumaliko711@gmail.com>",
		# 	"subject": "Portfolio Contact ",
		# 	"text": msg})



# @app.route('/successmessage', methods=['GET', 'POST'])
# def successmessage():
#     error = None
#     if request.method == 'POST':
        
#             flash('message sent successfully')
#             return redirect(url_for('index'))
#     return render_template('index.html', error=error)



###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True)