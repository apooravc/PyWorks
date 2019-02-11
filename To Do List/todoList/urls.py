from django.contrib import admin
from django.urls import path
from todoApp.views import appView, addItem, deleteItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoList/', appView),
    path('addItem/', addItem),
    path('deleteItem/<int:item_id>/', deleteItem)
]
