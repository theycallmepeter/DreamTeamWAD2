from django.conf.urls import url
from gliocas_app import views
from gliocas_app.views import PostLikeRedirect

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^subjects/', views.subjects, name='subjects'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/$', views.show_subject, name='show_subject'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/add_question/$', views.add_question, name='add_question'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/$', views.show_course, name='show_course'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/$', views.show_question, name='show_question'),
    # url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)//(?P<question_slug>[\w\-]+)/like/$', PostLikeRedirect.as_view(), name='like_question'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]