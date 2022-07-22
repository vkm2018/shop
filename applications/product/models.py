from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

User = get_user_model()

class Category(models.Model):
    title = models.TextField(max_length=100)
    slug = models.SlugField(primary_key=True, max_length=100, unique=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    def save(self, *args, **kwargs):
        self.slug = self.title.lower()
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.slug}'

        else:
            return self.slug



class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    # image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Like(models.Model):
    """
    Модель Лайк
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='Владелец лайка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes', verbose_name='Товар')
    like = models.BooleanField('лайк', default=False)

    def __str__(self):
        return f'{self.product}{self.like}'


class Rating(models.Model):
    """
    Модель рейтинга
    """
    serializer = ...
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings',  verbose_name='Владелец рейтинга')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings', verbose_name='Товар')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    def __str__(self):
        return f'{self.product} {self.rating}'

class Comment(models.Model):
    """
    Модель комментарии
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)









