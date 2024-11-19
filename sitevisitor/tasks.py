import random
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_otp_email(email, otp):
    otp = random.randint(100000, 999999)  # Generate a random 6-digit OTP
    subject = "Your OTP for Password Reset"
    message = f"Your OTP for resetting your password is: {otp}. It is valid for 2 minutes"
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    # Send email with OTP
    send_mail(subject, message, email_from, recipient_list)

@shared_task
def send_verification_email(email):
    subject = ' OTP verified successfully'
    message = f" Your OTP verified successfully. You can now reset your password."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, email_from, recipient_list)

@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome to ELECTRO!!'
    message = 'Thank you for registering at our website. We are excited to have you!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    send_mail(subject, message, email_from, recipient_list)


@shared_task
def send_account_status_email(email, status):
    subject = f'Your account has been {status}'
    message = f"Your account status has been updated to {status}."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)