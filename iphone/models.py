from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models




class Apple(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


SIM_CARDS = (
    ('O!', 'O!'),
    ('Beelin', 'Beelin'),
    ('MegaCom', 'MegaCom'),
)

class Iphone(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    image = models.ImageField(upload_to='iphone_images/', verbose_name='Фото')
    harakter = models.TextField(verbose_name='Характеристика')
    sim_card = models.CharField(max_length=10, choices=SIM_CARDS, verbose_name='Сим-карта')
    price = models.IntegerField(default=0, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    apple = models.ForeignKey(Apple, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Айфон"
        verbose_name_plural = "Айфоны"


class Comment(models.Model):
    iphone = models.ForeignKey(Iphone, on_delete=models.CASCADE, related_name='iphone', null=True)
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars} - {self.iphone}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"