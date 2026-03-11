from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import PasswordReserOTP, User
from datetime import timedelta
from django.utils import timezone
from .models import User, Profile



@shared_task
def send_otp_email(user_id, otp):
    print("TASK STARTED")
    try:
        user = User.objects.get(id=user_id)
        send_mail(
            subject="Your OTP Code",
            message=f"Hello {user.username}, your OTP is: {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        print("EMAIL SENT")
        return f"OTP sent to {user.email}"
    except User.DoesNotExist:
        return "User not found"
    


@shared_task
def send_welcome_email(user_id):
    try:
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)

        message = f"""
            Hello {profile.full_name or user.username},

            We are excited to welcome you as a new member of Glowmi. Thank you for joining our community.

            Your submitted information:

            Membership ID: {user.username}
            Name         : {profile.full_name}
            Email        : {user.email}
            Phone        : {profile.contact_number}
        
            Our team will use this information to give you a better skincare experience.

            Best Regards,
            Glowmi Team
            """

        send_mail(
            subject="Welcome to Glowmi ✨",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        return f"Welcome email sent to {user.email}"

    except User.DoesNotExist:
        return "User not found"



@shared_task
def cleanup_expired_otps():
    expired = PasswordReserOTP.objects.filter(
        is_verified=False,
        created_at__lt=timezone.now() - timedelta(minutes=5)
    )
    count = expired.count()
    expired.delete()
    return f"{count} expired OTPs deleted"