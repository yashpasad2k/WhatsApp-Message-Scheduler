# app.py
from flask import Flask, render_template, request, flash, redirect, url_for
from twilio.rest import Client
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flash messages

class WhatsAppMessenger:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_number = '+14155238886'  # Twilio sandbox number
        
        if not all([self.account_sid, self.auth_token]):
            raise ValueError("Missing Twilio credentials")
        
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, to_number, message):
        try:
            # Format the number
            if not to_number.startswith('+'):
                to_number = '+' + to_number
            
            message = self.client.messages.create(
                from_=f'whatsapp:{self.from_number}',
                body=message,
                to=f'whatsapp:{to_number}'
            )
            return True, message.sid
        except Exception as e:
            return False, str(e)

# Initialize WhatsApp messenger
messenger = WhatsAppMessenger()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        message = request.form.get('message')
        scheduled_date = request.form.get('scheduled_date')
        scheduled_time = request.form.get('scheduled_time')

        if not all([recipient, message]):
            flash('Please fill in all required fields', 'error')
            return redirect(url_for('index'))

        # Send message
        success, result = messenger.send_message(recipient, message)
        
        if success:
            flash('Message sent successfully!', 'success')
        else:
            flash(f'Error sending message: {result}', 'error')
        
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)