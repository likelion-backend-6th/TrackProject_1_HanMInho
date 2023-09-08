from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:book_list_by_category')


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Book.Status.AVAILABLE)


class Book(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'AVA', 'Available'  # 대여 가능
        EQUIPMENT = 'EQU', 'Equipment'  # 대여 불가능
        DAMAGED = 'DGE', 'Damaged'  # 파손 및 손상
        LOSE = 'LOE', 'Lose'  # 분실
        REPLACEMENT = 'REP', 'Replacement'  # 대체
        OTHER = 'OTR', 'Other'  # 기타

    Category = models.ForeignKey(Category, related_name='Book', on_delete=models.CASCADE)  # 도서 제목
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    photo = models.ImageField(upload_to='booksImage')
    auther = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='book_list'
    )# 출판사
    writer = models.ManyToManyField(User, related_name='book_writer')  # 저자
    available = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.AVAILABLE,
        null=False
    )
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    publish = PublishedManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['name']),
            models.Index(fields=['-updated']),
        ]

    def get_absolute_url(self):
        return reverse('books:book_AllDetail')
