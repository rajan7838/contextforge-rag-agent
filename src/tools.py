import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Do math calculations like 15 * 23 or 100/4"""
    try:
        allowed = set("1234567890-+/*. Locker()")
        if not all(c in allowed for c in expression):
            return "Error: Only numbers and math symbols allowed"
        return str(eval(expression))
    except:
        return "Error: Try Again"

@tool
def get_time(query: str = "") -> str:
    """Get current date and time with AM/PM indicators"""
    return datetime.now().strftime("%Y-%m-%d : %I:%M:%S %p")

@tool
def word_count(text: str) -> str:
    """Count number of words in a text"""
    return str(len(text.split()))

@tool
def reverse_text(text: str) -> str:
    """Reverse any text string"""
    return text[::-1]

@tool
def get_weather(city: str) -> str:
    """Get current weather for any city"""
    try:
        city = city.strip().replace(" ", "+")
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        return f"Could not get weather for {city}"
    except Exception as e:
        return "Weather unavailable"

@tool
def send_email(recipient: str, subject: str, message: str) -> str:
    """Send email to any recipient using SMTP"""
    try:
        sender_email = os.getenv("EMAIL_SENDER")
        sender_password = os.getenv("EMAIL_PASSWORD")
        
        if not sender_email or not sender_password:
            return "Error: Email credentials not configured"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        return f"Email sent to {recipient}"
    except Exception as e:
        return "Email failed"