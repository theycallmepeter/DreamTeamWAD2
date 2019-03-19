from django.conf.urls import url
from gliocas_app import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


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
    url(r'^likequestion/$', views.like_question_new, name='like_question_new'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/like/(?P<like>[\d])/$', views.like_question, name='like_question'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/delete/$', views.delete_question, name='delete_question'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/(?P<answer_key>[\d]+)/deleteanswer/$', views.delete_answer, name='delete_answer'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/(?P<answer_key>[\d]+)/likeanswer/(?P<like>[\d])/$', views.like_answer, name='like_answer'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/(?P<reply_key>[\d]+)/deletereply/$', views.delete_reply, name='delete_reply'),
    url(r'^subject/(?P<subject_slug>[\w\-]+)/(?P<course_slug>[\w\-]+)/(?P<question_slug>[\w\-]+)/(?P<reply_key>[\d]+)/likereply/(?P<like>[\d])/$', views.like_reply, name='like_reply'),
    url(r'^user/(?P<username>[\w\-@_+.]+)/$', views.user, name='user'),
    url(r'^user/(?P<username>[\w\-@_+.]+)/questions/$', views.user_questions, name='user_questions'),
    url(r'^user/(?P<username>[\w\-@_+.]+)/answers/$', views.user_answers, name='user_answers'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^reset-password/$',PasswordResetView.as_view(),name="reset_password"),
    url(r'^reset-password/done/$',PasswordResetDoneView.as_view(),name="password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    url(r'^reset-password/complete/$',PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
