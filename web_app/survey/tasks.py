from django.core.mail import EmailMessage
from employe.settings import EMAIL_HOST_USER
from celery import shared_task


@shared_task()
def send_confirmation_email_task(emails, subject: str, message: str):
    email = EmailMessage(subject=subject,
                         body=message,
                         from_email=EMAIL_HOST_USER,
                         to=emails)
    email.send()
