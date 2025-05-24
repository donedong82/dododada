from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('profile/delete/', delete_account, name='delete_account'),
]