from django.shortcuts import render
from django.views.generic.detail import DetailView
from list.models import Student

# Create your views here.
class StudentDetail(DetailView):
    model = Student
    template_name = 'detail/student.html'
    context_object_name = 'stu'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['all_students'] = self.model.objects.all().order_by()
        return context