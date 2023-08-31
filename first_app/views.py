from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Student  #enda loodud asi, seetottu peab viimasena olema, jrk oluline importidel
from .models import Teacher
from .models import Subject


# Create your views here.
class MyHomeView(TemplateView):
    template_name = 'first_app/home.html'


class StudentListView(ListView):
    # model_list.html -> student_list.html
    model = Student #Connected to Models Student-siit tuleb info
    queryset = Student.objects.order_by('name')  # nime jargi sorteeritud, result ordered by name
    context_object_name = 'students' # default object_list is now students
    paginate_by = 10 # 10 per page in ListView

class StudentDetailView(DetailView):
    # Return only one model entry, tagastab ainult 1 tulemuse, ainult selle isiku andmed saab kellele klikitakse
    #default template model_detail.html => student_detail.html
    model = Student

class StudentCreateView(CreateView):
    template_name = 'first_app/student_form_create.html'
    model = Student  # info tuleb modelist Student classist?
    fields = '__all__' # tahame, et saaks muuta koiki v2ljasid
    success_url = reverse_lazy('first_app:student_list')

class StudentUpdateView(UpdateView):
    # model_form.html => student_form.html
    model = Student
    fields = ['name', 'weight'] # update only name and weight
    success_url = reverse_lazy('first_app:student_list')

class StudentDeleteView(DeleteView):
    # form -> confirm delete button
    # default template name => model_confirm_delete.html ->
    # -> student_confirm_delete.html
    model = Student
    success_url = reverse_lazy('first_app:student_list')  # ehk kuhu peale kustutamist l'heb, student list lehele

class TeacherListView(ListView):
    # model_list.html -> student_list.html
    model = Teacher
    queryset = Teacher.objects.order_by('name')  # nime jargi sorteeritud, result ordered by name
    context_object_name = 'teachers'  # default object_list is now students
    #paginate_by = 10  # 10 per page in ListView
class TeacherCreateView(CreateView):
    template_name = 'first_app/teacher_form_create.html'
    model = Teacher  # info tuleb modelist teacher classist?
    fields = '__all__' # tahame, et saaks muuta koiki v2ljasid
    success_url = reverse_lazy('first_app:teacher_list')
class SubjectListView(ListView):
    # model_list.html -> student_list.html
    model = Subject #Connected to Models Student-siit tuleb info
    queryset = Subject.objects.order_by('id')  # nime jargi sorteeritud, result ordered by name
    context_object_name = 'subjects' # default object_list is now students
    paginate_by = 10 # 10 per page in ListView
class SubjectCreateView(CreateView):
    template_name = 'first_app/subject_form_create.html'
    fields = "__all__"
    model = Subject
    success_url = reverse_lazy('first_app:subject_list')
class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ['name']
    success_url = reverse_lazy('first_app:subject_list')
class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('first_app:subject_list')