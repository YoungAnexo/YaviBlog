from operator import setitem
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import delete_task, actualizar, list_tasks, create_task
from .views import eliminar

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Contactos', views.Contactos, name='Contactos'),
    path('Anuncios', views.Anuncios, name='Anuncios'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:task_id>/', eliminar, name='eliminar'),
    path('libros/editar/<int:task_id>/', views.editar, name='editar'),
    path('publicacion/', views.publicacion, name='publicacion'),
    path('Comentarios1/', views.Comentarios, name='Comentarios1'),
    path('actualizar/<int:task_id>/',actualizar, name='actualizar' ),
    path('Comentarios/', list_tasks, name='Comentarios'),
    path('new_task/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('actualizar/<int:task_id>/',actualizar, name='actualizar' )
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)