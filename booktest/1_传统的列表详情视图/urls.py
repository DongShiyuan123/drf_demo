from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.BookInfoView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoDetailView.as_view()),# \d匹配[0-9]和其他数字字符。 “+”表示数字中必须至少有一个或多个数字
]
