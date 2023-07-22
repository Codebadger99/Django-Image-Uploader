from django.shortcuts import render
from .models import Photo
from .forms import UploadForm

# Create your views here.

def gallery(request):
    photos = Photo.objects.all()
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save(commit=True)
    context = {
        'photos':photos,
        'form'  : form
    }
    return render(request,'Home.html', context)