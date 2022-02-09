from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="название", max_length=64)
    # не обязательное поле только для симв данных
    description = models.TextField("описание", blank=True)
    # добавили новое поле, обязательно задать default= или blank=True
    short_descr = models.CharField(
        verbose_name="краткое описание", max_length=150, default=""
    )
    is_active = models.BooleanField(verbose_name='активная категория', default=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name", "-description"]

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="название", max_length=64)
    image = models.ImageField(upload_to="product_images", blank=True)
    description = models.TextField(verbose_name="описание", blank=True)
    short_desc = models.CharField(
        verbose_name="краткое описание", max_length=150, blank=True
    )
    price = models.DecimalField(
        verbose_name="цена", max_digits=8, decimal_places=2, default=0
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество на складе", default=0
    )
    is_active = models.BooleanField(verbose_name='активный продукт', default=True)
    slug = models.CharField(verbose_name='тэг', max_length=32, blank=True)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.category.name} (id={self.category_id}))"
