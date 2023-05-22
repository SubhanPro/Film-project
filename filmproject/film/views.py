from django.shortcuts import render, redirect
from film.models import FilmModel, ActorModel, CommentModel, LikeModel, CategoryModel
from django.http import Http404


def index(request):
    films = FilmModel.objects.all()
    search = request.GET.get("search")
    categories = CategoryModel.objects.all()
    if search:
        films = FilmModel.objects.filter(name__contains = search)
    context = {
        'films': films,
        'categories': categories
    }
    return render(request, 'index.html', context)
    

def detail(request, id):
    film = FilmModel.objects.get(id = id)
    film_likes = len(film.film_likes.all())
    categories = CategoryModel.objects.all()
    context = {
        'film': film,
        'film_likes': film_likes,
        'categories': categories
    }
    if request.method == "POST":
        choice = request.POST["choice"]
        if choice == 'comment':
            content = request.POST["content"]
            film_id = request.POST["film_id"]

            film_obj = FilmModel.objects.get(id = film_id)
            comment = CommentModel.objects.create(
                user = request.user,
                film = film_obj,
                content = content
            )
        elif choice == 'like':
            film_id = request.POST["film_id"]
            film_obj = FilmModel.objects.get(id = film_id)
            if not LikeModel.objects.filter(user = request.user, film = film_obj).exists():
                like = LikeModel.objects.create(
                    user = request.user,
                    film = film_obj
                )
            else:
                like = LikeModel.objects.get(user = request.user, film = film_obj)
                like.delete()
    return render(request, 'detail.html', context)

def delete_comment(request, id):
    comment = CommentModel.objects.get(id = id)
    comment.delete()
    return redirect('detail', id = comment.film.id)

def category(request, id):
    category = CategoryModel.objects.get(id = id)
    films = FilmModel.objects.filter(categories = category)
    categories = CategoryModel.objects.all()
    context = {
        'category': category,
        'films': films,
        'categories': categories
    }
    return render(request, 'category.html', context)
