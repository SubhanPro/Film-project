from django.contrib import admin
from film.models import FilmModel, ActorModel, LikeModel, CommentModel, CategoryModel

admin.site.register(FilmModel)
admin.site.register(ActorModel)
admin.site.register(LikeModel)
admin.site.register(CommentModel)
admin.site.register(CategoryModel)