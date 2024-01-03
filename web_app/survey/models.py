from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Employe(models.Model):
    is_favourite = models.BooleanField(verbose_name='Избранное', default=False)
    note = models.TextField(verbose_name='Заметка о кандидате',
                            max_length=7000,
                            blank=True,
                            null=True)

    name = models.CharField(verbose_name='ФИО', max_length=70, blank=False, null=False)
    age = models.PositiveIntegerField(verbose_name='Возраст (лет)',
                                      validators=[MinValueValidator(18, message='Вам должно быть 18+'),
                                                  MaxValueValidator(60, message='Вам должно быть 60-')],
                                      blank=False,
                                      null=False)
    experience = models.BooleanField(verbose_name='Есть опыт продажи недвижимости')
    previous_job = models.TextField(verbose_name='Предыдущие места работы', max_length=3000, blank=True, null=True)
    about_me = models.TextField(verbose_name='О себе', max_length=5000, blank=False, null=False)
    phone = PhoneNumberField(verbose_name='Номер телефона',
                             blank=False,
                             null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('name',)
