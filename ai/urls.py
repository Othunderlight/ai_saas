 
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.error, name="home"),
    path('try/', views.tryit, name="tryit"),
    path('pick-model/', views.pick_model, name="pick-model"),
    path('chat-model/', views.chat_model, name="chat-model"),
    path('model-page/<str:ai_model_name>', views.model_page, name="model-page"),
    path('login/', views.login_usr, name="login"),
    path('logout/', views.logout_usr, name="logout"),
    # path('signup/', views.signup_usr, name="signup"),
    # path('reset-password/', views.reset_password, name="reset-password"),
    path('start/<str:ai_model_name>', views.start, name="start"),
    # path('overview/', views.overview, name="overview"),
    # path('settings/', views.settings, name="settings"),
    # path('account/', views.account, name="account"),
    # path('help/', views.help, name="help"),
    # path('notification/', views.notification, name="notification"),
    path('error/', views.error, name="error"),
    # path('notfound/', views.notfound, name="notfound"),
    path('chat/room/<chatroom_name>', views.chat_model, name="chatroom"),
    # path('chat/get-room/<destination_url>', views.get_room, name="get-room"),
    # path('chat/delete/<chatroom_name>', views.chatroom_delete, name="chatroom-delete"),


]
