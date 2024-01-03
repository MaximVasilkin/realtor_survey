from django import forms
from phonenumber_field.formfields import PhoneNumberField, RegionalPhoneNumberWidget
from .models import Employe
from django.utils.translation import gettext_lazy as _


class EmployeForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Иванов Иван Иванович')}),
                           label=_('ФИО'))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': _('18')}),
                             label=_('Возраст'))
    phone = PhoneNumberField(widget=RegionalPhoneNumberWidget(region='RU',
                                                              attrs={'placeholder': _('+79123456789')}),
                             label=_('Телефон'),
                             error_messages={'invalid': 'Введите корректный номер мобильного телефона '
                                                        '(например, +79123456789)'})

    class Meta:
        model = Employe
        exclude = ('created_at', 'note', 'is_favourite', 'id', )

