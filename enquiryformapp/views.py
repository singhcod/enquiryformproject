from django.shortcuts import render,redirect
from .models import Enquiry_data
from .forms import EnquiryForm
from django.http.response import HttpResponse



def enquiryform_view(request):
    if request.method == "GET":
        form = EnquiryForm()
        context = {'singh': form}
        return render(request,'enquiryfile.html',context)

    else:
         form = EnquiryForm(request.POST)
         if form .is_valid():
             name =  request.POST.get('name')
             email = request.POST.get('email')
             mobile = request.POST.get('mobile')
             course = form.cleaned_data.get('course')
             faculties = form.cleaned_data.get('faculties')
             locations = form.cleaned_data.get('locations')
             color = form.cleaned_data.get('color')
             gender = form.cleaned_data.get('gender')
             start_date = form.cleaned_data.get('start_date')

             Enquiry_data(
                 name=name,
                 email=email,
                 mobile=mobile,
                 course=course,
                 faculties=faculties,
                 locations=locations,
                 color = color,
                 gender=gender,
                 start_date=start_date
             ).save()
             return redirect('/')

         else:
             return redirect("/")
