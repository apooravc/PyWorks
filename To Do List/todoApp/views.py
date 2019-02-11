from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def appView(request):
    return render(request, 'todoList.html', {
        'list_items': TodoItem.objects.all()
        })

def addItem(request):
    new_item = TodoItem(text = request.POST['inputText'])
    new_item.save()
    return HttpResponseRedirect('/todoList/')

def deleteItem(request, item_id):
    delete_item = TodoItem.objects.get(id = item_id)
    delete_item.delete()
    return HttpResponseRedirect('/todoList/')
