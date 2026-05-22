from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
        name=models.CharField(max_length=50)
        description=models.TextField()
        is_popular=models.BooleanField(default=False)

        def __str__(self):
            return self.name


class Author(models.Model):

    EXPERIENCE_CHOICES = [
        ('BEGINNER' , 'Почетник'),
        ('PROFESSIONAL' , 'Професионалец'),
        ('ESTABLISHED ' , ' Етаблиран автор')
    ]

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    biography=models.TextField()
    experience=models.CharField(max_length=20,choices=EXPERIENCE_CHOICES)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    summary=models.TextField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cover_image=models.ImageField(upload_to='covers/')
    rental_price=models.DecimalField(max_digits=6,decimal_places=2)
    available_copies=models.IntegerField()

    def __str__(self):
        return self.title


