from django.shortcuts import render, redirect
from django.http import JsonResponse
import pytesseract
from PIL import Image
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import ScanPage, Translation
from django.utils import timezone


def home(request):
    """Strona główna"""
    return render(request, 'home.html')


@login_required
def upload_scan(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        model_name = request.POST.get("model_name") or "baseline"
        if image:
            page = ScanPage.objects.create(owner=request.user, image=image, uploaded_at=timezone.now())
            # Tu robimy OCR – na razie test
            recognized = "Sample OCR result..."  # <-- tu wstawisz właściwe rozpoznanie
            Translation.objects.create(page=page, model_name=model_name, text=recognized)
            return redirect("my_scans")
    return render(request, "upload.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()            # tworzy użytkownika + hasło (hash)
            messages.success(request, "Konto utworzone. Zalogowano.")
            login(request, user)          # automatyczne logowanie po rejestracji
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def my_scans(request):
    scans = ScanPage.objects\
        .filter(owner=request.user)\
        .prefetch_related("translations")
    return render(request, "my_scans.html", {"scans": scans})
