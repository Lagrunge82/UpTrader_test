from django.db import models
from django.urls import reverse


class MenuItems(models.Model):
    name = models.CharField(max_length=16, verbose_name='Name')
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='children',
                               db_index=True, verbose_name='Parent menu item')

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.name


class OtherMenuItems(models.Model):
    name = models.CharField(max_length=16, verbose_name='Name')
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='children',
                               db_index=True, verbose_name='Parent menu item')

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Other Menu item'
        verbose_name_plural = 'Other Menu items'

    def __str__(self):
        return self.name
