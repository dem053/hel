from django.shortcuts import render

from dogs.models import Category, Dog


def index(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list[0:3],
        'title': 'Питомник - Главное'
    }
    return render(request, 'dogs/index.html', context)


def categories(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Питомник - наши породы'
    }
    return render(request, 'dogs/categories.html', context)


def category_dogs(request,pk):
    category_item = Category.objects.get(pk=pk)
    dog_list = Dog.objects.filter(category_id=pk)
    context = {
        'object_list': dog_list,
        'title': f'Собаки породы - {category_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)
