from django.contrib import admin
from django.urls import path
from filmapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', views.film_list),
    path('films/<int:id>', views.film_detail),
    path('home/', views.get_detail),
    path('home/<int:id>', views.get_film, name='get_film'),
    path('home/post/', views.post_data, name='post_data'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
