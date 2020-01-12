from django.urls import path
from . import views
from accounts import views as acc_views
from articles import views as art_views

urlpatterns = [
    path('', views.index),
    path('accounts/sign-up', acc_views.sign_up),
    path('accounts/sign-in', acc_views.sign_in),
    path('accounts/my-account', acc_views.my_account),
    path('accounts/friends/<str:user>', acc_views.get_friends),
    path('articles/dashboard', art_views.dashboard),
    path('articles/dashboard/<int:year>', art_views.dashboard),
    path('articles/<int:id>', art_views.article_by_id),
    path('articles/tag/<str:tag>', art_views.articles_by_tag),
    path('articles/check-age', art_views.check_age),
    # допишите новый путь для subscribe
    path('articles/subscribe', art_views.subscribe)
    
]
