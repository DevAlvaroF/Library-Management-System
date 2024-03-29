from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', views.BookCreate.as_view(), name='create_book'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('vip_view/', view=views.vipView, name='vipView'),
    path('signup/', view=views.SignupView.as_view(), name='signup'),
    path('profile/', views.BorrowedBooksView.as_view(), name='profile')

]
