from django.shortcuts import render
from student_info.serializers import UserSerializer
from django.http import Http404
from student_info.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentList(APIView):

     # def display(request):
     #     list = Student.objects.all()
     #     serializer = UserSerializer(list, many=True)
     #     return render(request,'student_info/display.html',{'list': serializer.data})

     def get(self, request, format=None):
         students = Student.objects.all()
         serializer = UserSerializer(students, many=True)
        # self.display()
         return render(request, 'student_info/display.html', {'list': serializer.data})



     def post(self, request, format=None):
             serializer = UserSerializer(data=request.data)
             if not serializer.initial_data['username'].isdigit():
                if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):


         @staticmethod
         def get_object(pat):
             try:
                 return Student.objects.get(pk=pat)
             except Student.DoesNotExist:
                 raise Http404

         @staticmethod
         def get_objectuser(pat):
             try:
                 return Student.objects.get(username=pat)
             except Student.DoesNotExist:
                 raise Http404


         def get(self, request, pat, format=None):
             if pat.isdigit():
                 user = self.get_object(pat)
             else:
                 user = self.get_objectuser(pat)
             user = UserSerializer(user)
            # self.display()
             return render(request, 'student_info/display.html', {'list': user.data})

         def put(self, request, pat, format=None):
             user = self.get_object(pat)
             serializer = UserSerializer(user, data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

         def delete(self, request, pat, format=None):
             user = self.get_object(pat)
             user.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)

         # def display(request):
         #     list = Student.objects.all()
         #     serializer = UserSerializer(list, many=True)
         #     return render(request, 'student_info/display.html', {'list': serializer.data})
