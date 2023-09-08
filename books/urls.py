from django.urls import path
from books import views

app_name = 'book'

urlpatterns = [
    # path('', views.Book_AllList, name='book_AllList'),
    path('<slug:book_slug>/', views.Book_AllList, name='book_list_by_category'),
    path('<int:id>/<slug:slug>/', views.book_AllDetail, name='book_AllDetail'),
    path('', views.Book_PublishedList, name='book_PublishedList'),
    path('<int:id>/', views.book_PublishedDetail, name='book_PublishedDetail'),
]
