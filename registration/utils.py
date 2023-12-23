from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

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
