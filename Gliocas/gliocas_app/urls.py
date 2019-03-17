from django.conf.urls import url
from gliocas_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^subjects/', views.subjects, name='subjects'),
    url(r'^subjects/add_subject/', views.add_subject, name='add_subject'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/$', views.show_subject, name='show_subject'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/add_course/$', views.add_course, name='add_course'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/add_question/$', views.add_question, name='add_question'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/$', views.show_course, name='show_course'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/$', views.show_question, name='show_question'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/answer/$', views.answer_question, name='answer_question'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/(?P<answer_key>[\d]+)/reply/$', views.reply_answer, name='reply_answer'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/like/(?P<like>[\d])/$', views.like_question, name='like_question'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
]
