from django.shortcuts import render

from .forms import *

# Create your views here.
def note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = NoteForm()

    return render(request, 'noteapp/note.html', {'form': form})

