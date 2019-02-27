from django.contrib import admin
from gliocas.models import Course, Subject, Question
# Register your models here.

#class SubjectAdmin(admin.ModelAdmin):
    #list_display = ('title', 'category', 'url')

#class QuestionAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Subject)#, SubjectAdmin)
admin.site.register(Course)#, CourseAdmin)
admin.site.register(Question)#, QuestionAdmin)
