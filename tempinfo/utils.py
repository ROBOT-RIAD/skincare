from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_temp_info_email(instance):
    subject = "Welcome to Glowmi ✨"

    html_content = f"""
    <div style="font-family: Arial; line-height:1.6;">
        <h2>Welcome to Glowmi ✨</h2>

        <p>Hello <b>{instance.full_name}</b>,</p>

        <p>
        We are excited to welcome you as a new member of <b>Glowmi</b>.
        Thank you for joining our community.
        </p>

        <p>Your submitted information:</p>

        <ul>
            <li><b>Name:</b> {instance.full_name}</li>
            <li><b>Email:</b> {instance.email}</li>
            <li><b>Phone:</b> {instance.contact_number}</li>
            <li><b>Skin Type:</b> {instance.skin_type}</li>
        </ul>

        <p>
        Our team will use this information to give you a better skincare experience.
        </p>

        <p>
        Best Regards,<br>
        <b>Glowmi Team</b>
        </p>
    </div>
    """

    email = EmailMultiAlternatives(
        subject=subject,
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[instance.email],
    )

    email.attach_alternative(html_content, "text/html")
    email.send()
