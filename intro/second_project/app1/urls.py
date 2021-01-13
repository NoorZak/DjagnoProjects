from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.root),
    path('blogs', views.index),
    path('blogs/create', views.create),
    path('blogs/new', views.new),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/json', views.json)

]
