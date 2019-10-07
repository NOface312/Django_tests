from django.db import models

class Users(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField(max_length = 200)
    price = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to = 'images')


class Author(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Имя")
    surname = models.CharField(max_length = 50, verbose_name = "Фамилия")
    date_birth = models.DateField(auto_now = False, verbose_name = "Дата рождения")

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    CHOISE_GENRE = {
        ('comedy',"Comedy"),
        ('tragedy',"Tragedy"),
        ('drama',"Drama"),
    }

    author = models.ForeignKey(Author , on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    text = models.TextField(max_length = 1000)
    genre = models.CharField(max_length = 50, choices = CHOISE_GENRE)

    def __str__(self):
        return self.title


class Place(models.Model):
    name =  models.CharField(max_length = 50)
    address =  models.CharField(max_length = 80)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete = models.CASCADE)
    serves_hot_dogs = models.BooleanField(default = False)
    serves_pizza = models.BooleanField(default = False)

    def __str__(self):
        return self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length = 30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )


class Article(models.Model):
    headline = models.CharField(max_length = 100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline', )
