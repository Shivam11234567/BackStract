import imaplib
import email
from email.header import decode_header
import re
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

EMAIL_ACCOUNT = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")

def extract_otp(email_body):
    """Extract OTP from email using BeautifulSoup instead of regex."""
    soup = BeautifulSoup(email_body, "html.parser")

    # Find OTP inside <div class="otp">
    otp_div = soup.find("div", class_="otp")

    if otp_div:
        otp = otp_div.get_text(strip=True)
        print(f"Extracted OTP from HTML: {otp}")
        return otp

    # Fallback: Use regex if no OTP found in HTML
    import re
    otp_pattern = r"\b\d{4,6}\b"
    match = re.findall(otp_pattern, email_body)
    return match[0] if match else None

def get_otp_from_email():
    mail = None  # Initialize mail to None to avoid UnboundLocalError
    try:
        print("Entered get_otp_from_email function")

        if not EMAIL_ACCOUNT or not EMAIL_PASSWORD:
            print("Email credentials are missing.")
            return None

        # Connect to Gmail
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        mail.select("inbox")

        # Search for emails from the OTP sender (Fixed IMAP Query)
        status, messages = mail.search(None, 'FROM', 'support@backstract.io')

        if status != "OK":
            print("Failed to search emails.")
            return None

        email_ids = messages[0].split()
        if not email_ids:
            print("No OTP email found.")
            return None

        print(f"Found {len(email_ids)} emails from support@backstract.io")

        # Fetch the latest email
        latest_email_id = email_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

        if status != "OK":
            print("Failed to fetch the latest email.")
            return None

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])  # Parse email

                # Decode subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')

                print(f"Email Subject: {subject}")

                # Extract email body
                email_body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/html":
                            email_body = part.get_payload(decode=True).decode(errors="ignore")
                            break  # Stop after finding the first plain text part
                else:
                    email_body = msg.get_payload(decode=True).decode(errors="ignore")

                print(f"Email Body:\n{email_body}")

                # Extract OTP
                otp = extract_otp(email_body)
                if otp:
                    print(f"OTP Found: {otp}")
                    return otp
                else:
                    print("No OTP found in the email body.")

        return None

    except Exception as e:
        print(f"Error retrieving OTP: {str(e)}")
        return None

    finally:
        if mail:
            mail.logout()

# Test the function
otp = get_otp_from_email()
if otp:
    print(f"Extracted OTP: {otp}")
else:
    print("Failed to extract OTP.")
