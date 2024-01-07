from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from dogs.models import Category, Dog


# def index(request):
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list[0:3],
#         'title': 'Питомник - Главное'
#     }
#     return render(request, 'dogs/index.html', context)

class IndexView(TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {'title': 'Питомник - наши породы'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data
# def categories(request):
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list,
#         'title': 'Питомник - наши породы'
#     }
#     return render(request, 'dogs/categories.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Питомник - наши породы'
    }


# def category_dogs(request,pk):
#     category_item = Category.objects.get(pk=pk)
#     dog_list = Dog.objects.filter(category_id=pk)
#     context = {
#         'object_list': dog_list,
#         'title': f'Собаки породы - {category_item.name}'
#     }
#     return render(request, 'dogs/dogs.html', context)

class DogListView(ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(id=self.kwargs.get('pk'))
        context_data['title'] = f'Собаки породы - {category_item.name}'
        return context_data


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'category', 'photo', 'birth_day',)
    success_url = reverse_lazy('dogs:categories')


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'category', 'photo', 'birth_day',)

    def get_success_url(self):
        return reverse('dogs:category_dogs', args=[self.object.category.pk])


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:categories')
