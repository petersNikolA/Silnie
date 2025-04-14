from django.shortcuts import render
from .forms import VideoForm

def index(request):
    form = VideoForm()
    return render(request, 'summarizer/index.html', {'form': form})

def result(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            return render(request, 'summarizer/result.html', {
                'pdf_url': '/media/mock_summary.pdf'
            })
    return render(request, 'summarizer/index.html', {'form': form})
