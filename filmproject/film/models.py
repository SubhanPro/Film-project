from django.db import models
from django.contrib.auth.models import User

class FilmModel(models.Model):
    #fields
    name = models.CharField(max_length=256, help_text = "Please, enter film name")
    poster = models.ImageField(upload_to="posters/")  # required
    video = models.FileField(upload_to = "videos/")
    rating = models.FloatField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    about = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to="banners/", blank=True, null=True)

    class Meta:
        verbose_name = "Film"
        # verbose_name_plural = "Films"

    def __str__(self):
        return self.name

'''
film = FilmModel.object.get(name="The Terminal")
actors = film.actors
'''


class ActorModel(models.Model):
    films = models.ManyToManyField(FilmModel, related_name="actors")
    name = models.CharField(max_length=150, help_text = "Enter your name")
    surname = models.CharField(max_length=150, help_text = "Enter your surname")
    age = models.IntegerField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Actor"
        # verbose_name_plural = "Actors"

'''
1. OneToOne
2. ManyToOne
3. ManyToMany

One - ev - ev telefonu - one
One - Sinif - Sagirdler - Many
Many - Istifadeciler - Qruplar - Many 
'''
class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_likes")


    class Meta:
        verbose_name = "Like"
        #verbose_name_plural = "Likes"

    def __str__(self):
        return self.user.username + " | " + self.film.name
    
class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name="film_comments")
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Comment"
        ordering = ('-id', )

    def __str__(self):
        return self.user.username + " | " + self.film.name
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=150)
    films = models.ManyToManyField(FilmModel, related_name="categories")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name