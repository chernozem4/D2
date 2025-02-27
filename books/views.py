
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from . import models

# Для отображения полной информации о книге
def book_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(models.Post, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'post_id': post_id
            }
        )




# вывод не полной информации
def book_list_view(request):
    if request.method == "GET":
        # query запрос
        post_object = models.Post.objects.all()
        return render(
            request,
            template_name='book_list.html',
            context={
                'post_object': post_object
            }
        )




























#def about_me(request):
#    return HttpResponse("Информация обо мне: Ваше имя, возраст, увлечения.")

#def about_friend(request):
#    return HttpResponse("Информация о друге: Имя друга, возраст, увлечения.")

#def current_time(request):
#    now = datetime.now()
#    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
#    return HttpResponse(f"Текущее время: {current_time}")

