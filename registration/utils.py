from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.conf import settings

def send_verification_email(user, request):
    # Generate verification link
    verification_link = request.build_absolute_uri(
        reverse('verify-email') + f"check/?token={user.verification_token}"
    )

    # Load email HTML template
    html_template = get_template('frontend/auth/email_verification_template.html')
    context = {
        'user': user,
        'verification_code': user.verification_code,
        'verification_link': verification_link,
    }

    # Render the HTML email
    html_content = html_template.render(context)

    # Create email message
    email = EmailMultiAlternatives(
        subject='Verify Your Email Address',
        body=f'Your verification code is: {user.verification_code}',
        from_email='ayoub.achak01@gmail.com',
        to=[user.email],
    )
    email.attach_alternative(html_content, 'text/html')

    # Send the email
    email.send()


def send_password_reset_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = request.build_absolute_uri(reverse('password-reset', args=[uid, token]))

    html_template = get_template('frontend/auth/email_password_reset_template.html')
    context = {'reset_link': reset_link, 'user': user}
    html_content = html_template.render(context)

    email = EmailMultiAlternatives(
        subject='Password Reset for VividSync',
        body=f'Please go to the following link to reset your password: {reset_link}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()