from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

class Topic(models.Model):
    topic_title = models.CharField('Название раздела', max_length=250)
    description = models.TextField('Описание раздела')
    topic_photo = models.ImageField('Фото', upload_to='images', default='', blank=True)
    topic_slug = models.SlugField(max_length=70, unique=True)

    def topic_photo_preview(self):
        if self.topic_photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.topic_photo.url)
        else:
            return 'No Image Found'

    topic_photo_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def __str__(self):
        return self.topic_title

class Stih(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    task = models.TextField('Описание заказа')
    stih_title = models.CharField('Название', max_length=250)
    stih_text = models.TextField('Текст')
    stih_photo = models.ImageField('Фото', upload_to='images', default='', blank=True)
    stih_slug = models.SlugField(max_length=70, unique=True)
    dateUploaded = models.DateTimeField('Дата обновления', default=datetime.now, blank=True, )

    def stih_photo_preview(self):
        if self.stih_photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.stih_photo.url)
        else:
            return 'No Image Found'

    stih_photo_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'стихотворение'
        verbose_name_plural = 'стихи'
        ordering = ['-dateUploaded']

    def __str__(self):
        return self.stih_title


class Feedback2(models.Model):
    holiday = models.CharField('Праздник', max_length=50, blank=True,)
    adresat = models.CharField('Кому', max_length=500, blank=True,)
    age = models.CharField('Лет', max_length=50, blank=True,)
    kem_prihodit = models.CharField('Кем приходится', max_length=50, blank=True,)

    you_choices = (('ty', 'Ты'), ('vy', 'Вы'))
    you = models.CharField(max_length=2, choices=you_choices, blank=True,)

    about = models.TextField('Инфо для стихов', blank=True,)
    wishes = models.CharField('Пожелания', max_length=300, blank=True,)

    style_choice = (
        ('uva', "Уважительном"),
        ('shu', "Шуточном"),
        ('vos', "Восхваляющем"),
        ('lir', "Лирическом"),
    )
    style = models.CharField(max_length=3, choices=style_choice, blank=True,)

    how_many_choice = (
        ('one', "От одного человека"),
        ('few', "От нескольких"),
    )
    how_many = models.CharField(max_length=3, choices=how_many_choice, blank=True, )

    deadline = models.CharField('Срок', max_length=50, blank=True,)
    special = models.CharField('Особые пожелания', max_length=300, blank=True,)

    on_site_choice = (
        ('yes', "Да"),
        ('no', "Нет"),
    )
    on_site = models.CharField(max_length=3, choices=on_site_choice, blank=True, )

    name = models.CharField('Ваше имя', max_length=50, blank=True,)
    tel = models.CharField('Телефон', max_length=50, blank=True,)
    Email = models.EmailField('Емейл', max_length=50, blank=True,)

    class Meta:
        verbose_name = 'Заказ на стихи'
        verbose_name_plural = 'Заказы на стихи'

    def __str__(self):
        return self.name