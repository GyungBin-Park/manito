from django.contrib import admin
from django.urls import path, include
from . import views


### 2차 url임!!!!!!!!!!!!!!!


urlpatterns = [
    path('', views.main_page, name='index'),
    path('kospi200_page/', views.kospi200_page, name='kospi200_page'),  #코스피200 화면 페이지
    path('jongmok/<str:code_name>/', views.jongmok_name, name='jongmok_name'),# 종목 상세 페이지
    path('jongmok/', views.jm_list, name='jm_search'),  # 종목 검색 삭제예정
    # path('post_list/',views.post_list),
    # path('list/<int:page>', views.post_list, name='list'),
]
