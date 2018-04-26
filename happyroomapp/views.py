from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import hrusers
from . serializers import hruserSerializers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class hruserList(APIView):

    def get(self, request):
        hrusers1 = hrusers.objects.all()
        serializer = hruserSerializers(hrusers1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class UserFormView(View):
    form_class = UserForm
    template_name = 'happyrooms/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form': form})

    # process form data
    def post(self, request):
        pass




