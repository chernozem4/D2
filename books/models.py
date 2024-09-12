from django.db import models
class Post(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('fantasy', 'Fantasy'),
        ('science_fiction', 'Science Fiction'),
        ('mystery', 'Mystery'),
        ('biography', 'Biography'),
    ]
    LIKE_OR_DISLIKE = (
        ('👍🏻', '👍🏻'),
        ('👎🏻', '👎🏻'),

    )

    title = models.CharField(max_length=255, verbose_name='Название книги', null=True)
    author = models.CharField(max_length=255, verbose_name='Автор', null=True)
    genre = models.CharField(max_length=50,choices=GENRE_CHOICES, verbose_name='Жанр', null=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    cover_image = models.ImageField(upload_to='books/', verbose_name='Обложка книги', null=True, blank=True)
    like_or_dislike = models.CharField(max_length=100, choices=LIKE_OR_DISLIKE, verbose_name='Нравится или нет',
                                       null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)

# Create your models here.
def __str__(self):
    return f'{self.title} - {self.created_at}'