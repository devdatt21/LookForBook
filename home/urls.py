from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name="index"),
    path('books/',views.books,name="books"),
    path('book_details/<str:bid>',views.book_details,name="book_details"),
    path('sendmsg/',views.sendmsg,name="sendmsg"),
    path('signup/',views.signup,name="signup"),
    path('edit/',views.edit,name="edit"),
    path('edit/edit_process/',views.edit_process,name="edit_process"),
    path('login/',views.login,name="login"),
    path('add_book/',views.add_book,name="add_book"),
    path('request/',views.request,name="request"),
    path('donate/',views.donate,name="donate"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('user_book_list/',views.user_book_list,name="user_book_list"),
    path('user_request/',views.user_request,name="user_request"),
    path('active/',views.active,name="active"),
    path('donate_list/',views.donate_list,name="donate_list"),
     path('accepted/',views.accepted,name="accepted"),
     path('deny/',views.deny,name="deny"),
]
