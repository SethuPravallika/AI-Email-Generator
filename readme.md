# AI-Email-Generator ✉️🤖

This is a full-stack Flask web application that generates AI-powered email content using the Groq API. Users can input a prompt, generate an email using AI, edit it, and send it via Gmail.

---

## 📁 Project Structure

```

AI-Email-Generator/
│
├── ai\_utils.py              # Handles AI email generation via Groq API
├── email\_utils.py           # Handles sending emails via Gmail SMTP
├── main.py                  # Entry point (Flask application)
├── .env                     # Stores API keys and email credentials (NOT PUBLIC)
├── .gitignore               # Hides .env and venv folder from Git
├── requirements.txt         # Lists required Python packages
├── readme.md                # Project documentation
│
├── static/
│   └── style.css            # Custom styling for the frontend
│
├── templates/
│   └── index.html           # Frontend HTML template
│
└── venv/                    # Python virtual environment (excluded from Git)

````

---

## 🔐 .env Configuration

Your `.env` file should contain the following (DO NOT push this file to GitHub):

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Email Configuration
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Email-Generator.git
cd AI-Email-Generator
```

### 2. Create and Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🧠 How It Works

* Enter recipient email(s) and a prompt for the email content.
* The app uses Groq's AI model to generate an email based on the prompt.
* You can edit the email content before sending.
* Email is sent via Gmail using your credentials securely stored in the `.env` file.

---

## 📦 Dependencies

The project uses the following main packages:

* `Flask` - Web framework
* `gunicorn` - WSGI server for deployment
* `requests` - To interact with the Groq API
* `groq` - Groq API client
* `python-dotenv` - Load environment variables from `.env`

Check `requirements.txt` for exact versions.

---

## ☁️ Deployment

### GitHub

Code is pushed to GitHub, but the `.env` file is excluded for security reasons via `.gitignore`.

### Render (Recommended)

You can deploy this app easily on **[Render](https://render.com/)**:

1. Create a new Web Service.
2. Connect your GitHub repo.
3. Add the following environment variables under **Environment > Secret Files**:

   * `GROQ_API_KEY`
   * `EMAIL_ADDRESS`
   * `EMAIL_PASSWORD`
4. Use the following build and start commands:

```bash
# Build Command:
pip install -r requirements.txt

# Start Command:
gunicorn main:app
```

---

## 🔐 Security Note

* Do **NOT** share your `.env` file or push it to public repositories.
* Use app passwords if you’re using Gmail with 2FA enabled.
* For production deployment, always use HTTPS and secure credentials handling.

---

## 👨‍💻 Author

Developed by \[Your Name].

---

