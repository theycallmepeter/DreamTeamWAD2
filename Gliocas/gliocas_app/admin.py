from django.contrib import admin
from gliocas_app.models import Course, Subject, Question, Answer, Reply, Followed
from gliocas_app.models import UpvoteQuestion, UpvoteAnswer, UpvoteReply
# Register your models here.

#class SubjectAdmin(admin.ModelAdmin):
    #list_display = ('title', 'category', 'url')

#class QuestionAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Subject)#, SubjectAdmin)
admin.site.register(Course)#, CourseAdmin)
admin.site.register(Question)#, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Reply)
admin.site.register(Followed)
admin.site.register(UpvoteQuestion)
admin.site.register(UpvoteAnswer)
admin.site.register(UpvoteReply)

