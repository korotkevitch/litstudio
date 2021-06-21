from django import forms
from django.forms import ModelForm
from .models import Feedback2

class UserForm2(forms.Form):
    holiday = forms.CharField(label='С каким праздником поздравляем', max_length=50, required=False)
    adresat = forms.CharField(label='Кого поздравляем, ФИО поздравляемого, работа, должность', max_length=500, widget=forms.Textarea, required=False)
    age = forms.CharField(label='Возраст поздравляемого', max_length=50, required=False,)
    kem_prihodit = forms.CharField(label='Кем он вам приходится', max_length=50, required=False)
    you = forms.ChoiceField(label='Форма обращения', choices=(('ty', "Ты"), ('vy', "Вы")), required=False)
    about = forms.CharField(label='Охарактеризуйте поздравляемого. Расскажите о нем: семья, работа, друзья, хобби, характер, '
                           'отношения с близкими. Интересные случаи из жизни', max_length=500, widget=forms.Textarea, required=False)
    wishes = forms.CharField(label='Ваши пожелания', max_length=300, required=False)

    style = forms.ChoiceField(label='В каком стиле пишем', choices=(
        ('uva', "Уважительном"),
        ('shu', "Шуточном"),
        ('vos', "Восхваляющем"),
        ('lir', "Лирическом"),
    ))

    how_many = forms.ChoiceField(label='От скольких человек поздравление', choices=(
        ('one', "От одного человека"),
        ('few', "От нескольких"),
    ), required=False)

    deadline = forms.CharField(label='Срок написания стихов', max_length=50, required=False)
    special = forms.CharField(label='Особые пожелания к стихам', max_length=300, required=False)

    on_site = forms.ChoiceField(label='Можно ли разместить стихи на сайте', choices=(
        ('yes', "Да"),
        ('no', "Нет"),
    ), required=False)

    name = forms.CharField(label='Ваше имя (*)', max_length=50, required=True)
    tel = forms.CharField(label='Телефон', max_length=50, required=False)
    Email = forms.EmailField(label='Емейл (*)', max_length=50, required=True)
