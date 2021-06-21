from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Stih, Topic, Feedback2
from .forms import UserForm2
from datetime import datetime


def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "index.html")

def topics(request):
    topics = Topic.objects.all()  # получаем все разделы поздравлений (маме, папе, другу и т.д.)

    return render(request, "topics.html", {"topics": topics})  # через контекст публикуем их на странице topics

def poems(request, the_topic_slug):  # стихи раздела
    topic = get_object_or_404(Topic, topic_slug=the_topic_slug)  # выбираем раздел с заданным topic_slug
    all_topic_poems = topic.stih_set.all()  # берем все стихи этого раздела
    topic_title = topic.topic_title
    current_topic_photo = topic.topic_photo

    return render(request, "topic_poems.html", {"all_topic_poems": all_topic_poems, "topic_title": topic_title, 'current_topic_photo': current_topic_photo})

def stihi(request, the_poem_slug):
    stih = get_object_or_404(Stih, stih_slug=the_poem_slug)
    stih_title = stih.stih_title
    stih_text = stih.stih_text
    task = stih.task

    return render(request, "stih.html", {"stih": stih, "stih_title": stih_title, 'stih_text': stih_text, 'task': task})

def feedback2(request):
    if request.method == 'POST':
        form = UserForm2(request.POST)
        if form.is_valid():
            holiday = form.cleaned_data['holiday']
            adresat = form.cleaned_data['adresat']
            age = form.cleaned_data['age']
            kem_prihodit = form.cleaned_data['kem_prihodit']
            you = form.cleaned_data['you']
            about = form.cleaned_data['about']
            wishes = form.cleaned_data['wishes']
            style = form.cleaned_data['style']
            how_many = form.cleaned_data['how_many']
            deadline = form.cleaned_data['deadline']
            special = form.cleaned_data['special']
            on_site = form.cleaned_data['on_site']
            name = form.cleaned_data['name']
            tel = form.cleaned_data['tel']
            Email = form.cleaned_data['Email']
            f2 = Feedback2(holiday = holiday, adresat=adresat, age=age, kem_prihodit=kem_prihodit, you=you, about=about, wishes=wishes,
                           style=style, how_many=how_many, deadline=deadline, special=special, on_site=on_site, name = name, tel = tel, Email = Email,)

            f2.save()
        return render(request, 'thanks.html')

    else:
        form = UserForm2()
    return render(request, 'feedback2.html', {'form': form})

def politics(request):
    return render(request, "politics.html")

def price(request):
    return render(request, "price.html")