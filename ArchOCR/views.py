from django.shortcuts import render, redirect
from django.http import JsonResponse
import pytesseract
from PIL import Image
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ScanPage


def home(request):
    """Strona główna"""
    return render(request, 'home.html')


def process_image(request):
    """Przetwarzanie obrazu i zwracanie tekstu OCR"""
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        image = Image.open(image_file)
        recognized_text = pytesseract.image_to_string(image)
        return JsonResponse({'text': recognized_text})
    return JsonResponse({'error': 'Niepoprawne żądanie!'}, status=400)


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
    scans = ScanPage.objects.filter(owner=request.user).prefetch_related("translations")
    return render(request, "my_scans.html", {"scans": scans})
