from django.contrib import admin

# Register your models here.


from .models import Choice, Question, Members

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.register(Members)
#admin.site.register(Question)