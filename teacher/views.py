from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from datetime import datetime
from django.views import View, generic
from .models import Teacher
import io, csv



class TeacherUploadView(View):
    def get(self, request):
        template_name = 'teacher/importteacher.html'
        return render(request, template_name)

    def post(self, request):
        user = request.user  # get the current login user details
        paramFile = io.TextIOWrapper(request.FILES['teacherfile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
            Teacher(
                First_Name=row['First_Name'],
                Last_Name=row['Last_Name'],
                Email_Address=row['Email_Address'],
                Phone_Number=row['Phone_Number'],
                Room_Number=row['Room_Number'],
                Subjects_taught=row['Subjects_taught'],
            )
            for row in list_of_dict
        ]
        try:
            msg = Teacher.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ', e)
            returnmsg = {"status_code": 500}

        return JsonResponse(returnmsg)

class TeacherListView(generic.ListView):
    model = Teacher
    def TeacherList(request):
         teacher = Teacher.objects.all()
         context = {'teacher': teacher}
         return render(request, 'teacher/teacher_list.html', context)


class TeacherDetailView(generic.DetailView):
    model = Teacher
    def TeacherDetail(request, primary_key):
        try:
            teacher = Teacher.objects.get(pk=primary_key)
        except Teacher.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'teacher/teacher_detail.html', context={'teacher': teacher})