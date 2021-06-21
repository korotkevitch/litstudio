from django.contrib import admin

from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_title', 'description', 'topic_photo_preview', 'topic_slug')
    prepopulated_fields = {'topic_slug': ('topic_title',)}

admin.site.register(Topic, TopicAdmin)

from .models import Stih

class StihAdmin(admin.ModelAdmin):
    list_display = ('stih_title', 'topic', 'task', 'stih_text', 'stih_photo', 'stih_slug', 'dateUploaded')
    prepopulated_fields = {'stih_slug': ('stih_title',)}
admin.site.register(Stih, StihAdmin)

from .models import Feedback2
class Feedback2Admin(admin.ModelAdmin):
    list_display = ('holiday', 'adresat', 'age', 'kem_prihodit', 'you', 'about', 'wishes', 'style', 'how_many',
                    'deadline', 'special', 'on_site', 'name', 'tel', 'Email',)
admin.site.register(Feedback2, Feedback2Admin)


