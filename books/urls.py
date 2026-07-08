from django.urls import path
from . import views

urlpatterns=[

    path("add/",views.add_book),

    path("",views.get_books),

    path("update/<int:book_id>/",views.update_book),

    path("delete/<int:book_id>/",views.delete_book),

]