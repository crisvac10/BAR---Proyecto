from django.urls import path , re_path
from .  import views


urlpatterns = [
    path(
        'api/menus/list/',
        views.ListAPIMenu.as_view(),
    )

]