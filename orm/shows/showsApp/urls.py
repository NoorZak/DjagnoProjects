from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('viewShow/<int:my_val>', views.viewShow),
    path('viewShow/<int:my_val>/deleteShow', views.deleteShow),

    path('../<int:my_val>/goToEdit', views.goToEdit),
    path('<int:my_val>/goToEdit', views.goToEdit),
    path('<int:my_val>/editShow', views.editShow),

    path('insertShow', views.insertShow),
    path('goToInsert', views.goToInsert),

    #path('insertBook', views.insertBook),
    #path('viewBook/<int:my_val>/addSelectedAuthor', views.addSelectedAuthor),
   # path('authors', views.authors),
   # path('insertAuthor', views.insertAuthor),
    #path('viewAuthor/<int:my_val>/addSelectedBook', views.addSelectedBook),
#    path('viewAuthor/<int:my_val>', views.viewAuthor),

]