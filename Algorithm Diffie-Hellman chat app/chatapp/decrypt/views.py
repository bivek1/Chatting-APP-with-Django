from django.shortcuts import render, HttpResponseRedirect
from .forms import cha, cha2
from .models import chat, chat2
# Create your views here.
def homepage(request):
    return render(request, "index.html")
def dashboard(request):
    chatform = cha(request.POST or None)
    chat_text = chat.objects.all()
    chatform2 = cha2(request.POST or None)
    chat2_text = chat2.objects.all()
    dict = {
        'fora': chatform,
        'textdata': chat_text,
        'fora2': chatform2,
        'text2': chat2_text
    }
    if chatform.is_valid():
        # stext = chatform.cleaned_data['textline']
        chatform.save()
        return HttpResponseRedirect("/dashboard")
    elif chatform2.is_valid():
        # ctext = chatform2.cleaned_data['textfie']
        chatform2.save()
        return HttpResponseRedirect("/dashboard")
    else:
        return render(request, "dashboard.html", dict)