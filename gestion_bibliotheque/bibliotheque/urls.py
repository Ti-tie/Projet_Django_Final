from django.urls import path
from .views import livre_create, liste_livres, livre_detail, livre_update, livre_delete, signup

urlpatterns = [
    path('livre/creer/', livre_create, name='creer_livre'),
    path('', liste_livres, name = 'liste_livres'),
    path('livre/<int:pk>', livre_detail, name = 'detail_livre'),
    path('livre<int:pk>/modifier/', livre_update, name='modifier_livre'),
    path('livre<int:pk>/supprimer/', livre_delete, name='supprimer_livre'),
    path('signup/', signup, name='signup'), 
]