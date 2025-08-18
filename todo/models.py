from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200,verbose_name='Başlık')
    description = models.TextField(blank=True,null=True, verbose_name='Açıklama')
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')
    completed = models.BooleanField(default=False, verbose_name='Tamamlandı')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'To-do'
        verbose_name_plural = 'To-do Listesi'


        


