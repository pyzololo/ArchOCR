from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import ScanPage, Translation
from django.utils import timezone

from .services import available_model_names
from .services.ocr_service import ocr_service


def home(request):
    return render(request, 'home.html')


# @login_required
# def upload_scan(request):
#     if request.method == "POST":
#         image = request.FILES.get("image")
#         model_name = request.POST.get("model_name") or "baseline"
#         if image:
#             page = ScanPage.objects.create(owner=request.user, image=image, uploaded_at=timezone.now())
#             # Tu robimy OCR – na razie test
#             recognized = "Sample OCR result..."  # <-- tu wstawisz właściwe rozpoznanie
#             Translation.objects.create(page=page, model_name=model_name, text=recognized)
#             return redirect("my_scans")
#     return render(request, "upload.html")

@login_required
def studio(request, pk=None):
    page = None
    last_result = None
    available_models = available_model_names()
    default_model = available_models[0] if available_models else "baseline"

    if pk is not None:
        page = get_object_or_404(ScanPage, pk=pk, owner=request.user)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "upload":
            image = request.FILES.get("image")
            if image:
                new_page = ScanPage.objects.create(owner=request.user, image=image, uploaded_at=timezone.now())
                return redirect("studio_detail", pk=new_page.pk)

        elif action == "recognize" and page:
            model_name = request.POST.get("model_name") or default_model
            tr = ocr_service.run(page=page, model_name=model_name)
            last_result = tr.text   # pokaż świeży wynik po prawej

    translations = page.translations.order_by("-created_at") if page else []
    return render(request, "studio.html", {
        "page": page,
        "available_models": available_models,
        "default_model": default_model,
        "translations": translations,
        "last_result": last_result,
    })


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
