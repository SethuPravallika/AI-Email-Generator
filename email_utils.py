import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipients_str, body):
    try:
        # Parse recipients
        recipients = [r.strip() for r in recipients_str.split(',') if r.strip()]
        
        if not recipients:
            print("No valid recipients found")
            return False
            
        # Create message
        msg = MIMEMultipart()
        msg['Subject'] = "AI Generated Email"
        msg['From'] = EMAIL
        msg['To'] = ', '.join(recipients)
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Gmail SMTP configuration
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()  # Enable encryption
            smtp.login(EMAIL, PASSWORD)
            smtp.sendmail(EMAIL, recipients, msg.as_string())
            
        print(f"Email sent successfully to: {', '.join(recipients)}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return False