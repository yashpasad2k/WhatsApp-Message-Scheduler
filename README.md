# WhatsApp Message Scheduler with Flask & Twilio

This project is a **WhatsApp Message Scheduler** built with **Flask and Twilio**. It allows users to schedule WhatsApp messages to be sent at a specific date and time.

## 🚀 Features
- Schedule WhatsApp messages using a simple web interface
- Uses **Twilio API** to send messages
- Validates user input (phone number, date, and time)
- Runs a background job to send messages at the right time

## 🛠 Tech Stack
- **Python** (Flask for backend)
- **Twilio API** (for sending WhatsApp messages)
- **HTML, CSS, JavaScript** (for frontend)

---

## 📌 Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/whatsapp-scheduler.git
cd whatsapp-scheduler
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up Twilio Credentials
1. Sign up for a [Twilio Account](https://www.twilio.com/try-twilio)
2. Get your **Account SID** and **Auth Token** from [Twilio Console](https://www.twilio.com/console)
3. Verify your WhatsApp number in the Twilio Sandbox
4. Create a **.env** file and add:
   ```env
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886  # Twilio Sandbox Number
   ```

### 5️⃣ Run the Flask App
```bash
python app.py
```

The app will be available at **http://127.0.0.1:5000**.

---

## 📷 Screenshots
| Home Page | Schedule Message |
|-----------|----------------|
| ![Home](screenshots/home.png) | ![Schedule](screenshots/schedule.png) |

---

## 📜 Usage
1. Enter the **recipient's WhatsApp number**.
2. Type your **message**.
3. Select a **date & time**.
4. Click **Schedule Message**.
5. The message will be sent automatically at the scheduled time!

---

## 🐞 Troubleshooting
- **Message not received?**
  - Ensure the recipient has joined the Twilio Sandbox by sending:
    ```
    join your-sandbox-code
    ```
  - Check [Twilio Message Logs](https://www.twilio.com/console/sms/logs) for errors.
- **Invalid phone number?**
  - Make sure the number is in **E.164 format** (e.g., `+919876543210`).
- **Time mismatch?**
  - Ensure your system timezone matches the scheduled time.

---

## 📜 License
This project is **open-source** under the [MIT License](LICENSE).

---

## 🙌 Contributing
Feel free to **fork** this repo, create a **pull request**, or open an **issue**!


---

### ⭐ Don't forget to **star** this repo if you find it useful! ⭐

