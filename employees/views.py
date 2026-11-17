from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import User


def get_employees():
    # суперпользователи - это администраторы сайта, а не сотрудники
    return User.objects.filter(is_superuser=False).prefetch_related('skills')


class IndexView(ListView):
    template_name = 'employees/index.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return get_employees()


class EmployeeListView(ListView):
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return get_employees()


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

    def get_queryset(self):
        return User.objects.filter(is_superuser=False).prefetch_related(
            'employee_skills__skill'
        )
