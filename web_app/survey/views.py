from .forms import EmployeForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from .tasks import send_confirmation_email_task
from employe.settings import SEND_TO, CONTACT_PHONE, RECAPTCHA_PUBLIC_KEY


class CreateEmploye(FormView):
    form_class = EmployeForm
    template_name = 'create_employe.html'
    # редирект на ту же страницу
    success_url = reverse_lazy('create_employe')

    phone_footer = f'{CONTACT_PHONE[:2]} ' \
                   f'{CONTACT_PHONE[2:5]} {CONTACT_PHONE[5:8]} {CONTACT_PHONE[8:10]} {CONTACT_PHONE[10: ]}'

    phone_widget = CONTACT_PHONE[1:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_key'] = RECAPTCHA_PUBLIC_KEY
        context['phone_footer'] = self.phone_footer
        context['phone_widget'] = self.phone_widget
        return context

    def form_valid(self, form):
        try:
            form.save()

            bool_mapping = {True: 'Да', False: 'Нет'}

            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')

            subject = f'Резюме {name} {phone}'
            message = '\n'.join([f'{field.label}:\n'
                                 f'{bool_mapping.get((val := field.value()), val)}\n'
                                 for field in form])

            is_check = name.lower() == 'тест' and phone.national_number == 9999999999

            send_confirmation_email_task.delay(SEND_TO if not is_check else [SEND_TO[0]],
                                               subject=subject,
                                               message=message)

            messages.success(self.request, 'Анкета успешно отправлена. Благодарим Вас за резюме!')

        except Exception:
            messages.error(self.request, 'Ошибка, анкета не отправлена')

        return HttpResponseRedirect(self.get_success_url())
