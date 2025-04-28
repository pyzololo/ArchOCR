from django.shortcuts import render
from django.http import JsonResponse
import pytesseract
from PIL import Image

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


