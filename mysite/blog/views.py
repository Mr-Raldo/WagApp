#views.py

from django.shortcuts import render, redirect
from .forms import ResponseForm

def submit_response(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or return a success message
            return redirect('questionnaire_page.html')  # Replace 'success_page' with the actual name of your success page URL
    else:
        form = ResponseForm()
    return render(request, 'questionnaire_page.html', {'form': form})
