from django.urls import path

from webapp.views.articles import add_view, detail_view
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view, name = 'index'),
    path('task/', index_view),
    path('task/add/', add_view, name = 'task_add'),
    path('task/<int:pk>', detail_view, name = 'task_detail')
]