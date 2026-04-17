from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import EmailOTP
from django.utils import timezone
from datetime import timedelta



def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()

        if not email:
            return render(request, 'EmailOTP/send_otp.html',
                          {'error': 'Please enter a valid email address.'})

        otp = str(random.randint(100000, 999999))

        EmailOTP.objects.update_or_create(
            email=email,
            defaults={'otp': otp}
        )

        try:
            send_mail(
                'Your OTP Code — SecureAuth',
                f'Your verification code is: {otp}\n\nThis code expires in 10 minutes. Do not share it with anyone.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
        except Exception as e:
            return render(request, 'EmailOTP/send_otp.html', {'error': f'Failed to send email: {e}'})

        return render(request, 'EmailOTP/verify_otp.html', {'email': email})

    return render(request, 'EmailOTP/send_otp.html')


def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        entered_otp = request.POST.get('otp', '').strip()

        if not email or not entered_otp:
            return render(request, 'EmailOTP/verify_otp.html',
                          {'email': email, 'error': 'Please enter both email and OTP.'})

        try:
            otp_record = EmailOTP.objects.get(email=email)
            if str(otp_record.otp).strip() == entered_otp:
                otp_record.delete()
                return render(request, 'EmailOTP/success.html', {'email': email})
            else:
                return render(request, 'EmailOTP/verify_otp.html',
                              {'email': email, 'error': 'Invalid OTP. Please try again.'})
        except EmailOTP.DoesNotExist:
            return render(request, 'EmailOTP/verify_otp.html',
                          {'email': email, 'error': 'Email not found. Please request a new OTP.'})

    return redirect('send_otp')


def success(request):
    # This view is kept for direct URL access; normally reached via verify_otp
    email = request.GET.get('email', '')
    return render(request, 'EmailOTP/success.html', {'email': email})


# Inside verify_otp, after fetching otp_record:
def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        entered_otp = request.POST.get('otp', '').strip()

        if not email or not entered_otp:
            return render(request, 'EmailOTP/verify_otp.html',
                          {'email': email, 'error': 'Please enter both email and OTP.'})

        try:
            otp_record = EmailOTP.objects.get(email=email)
            if str(otp_record.otp).strip() == entered_otp:
                if timezone.now() - otp_record.created_at > timedelta(minutes=10):
                    otp_record.delete()
                    return render(request, 'EmailOTP/verify_otp.html',
                                  {'email': email, 'error': 'OTP expired. Please request a new one.'})
                otp_record.delete()
                return render(request, 'EmailOTP/success.html', {'email': email})
            else:
                return render(request, 'EmailOTP/verify_otp.html',
                              {'email': email, 'error': 'Invalid OTP. Please try again.'})
        except EmailOTP.DoesNotExist:
            return render(request, 'EmailOTP/verify_otp.html',
                          {'email': email, 'error': 'Email not found. Please request a new OTP.'})

    return redirect('send_otp')


def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        entered_otp = request.POST.get('otp', '').strip()

        if not email or not entered_otp:
            return render(request, 'EmailOTP/verify_otp.html',
                          {'email': email, 'error': 'Please enter both email and OTP.'})

        try:
            otp_record = EmailOTP.objects.get(email=email)

            # ✅ Expiry check
            if timezone.now() - otp_record.created_at > timedelta(minutes=10):
                otp_record.delete()
                return render(request, 'EmailOTP/verify_otp.html',
                              {'email': email, 'error': 'OTP expired. Please request a new one.'})

            if str(otp_record.otp).strip() == entered_otp:
                otp_record.delete()
                return render(request, 'EmailOTP/success.html', {'email': email})
            else:
                return render(request, 'EmailOTP/verify_otp.html',
                              {'email': email, 'error': 'Invalid OTP. Please try again.'})

        except EmailOTP.DoesNotExist:
            return render(request, 'EmailOTP/verify_otp.html',
                          {'email': email, 'error': 'Email not found. Please request a new OTP.'})

    return redirect('send_otp')