from django.shortcuts import render
from .forms import registrationform, loginform
from .models import UserDetails
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def registeruser(request):
    if request.method == "POST":
        regform = registrationform(request.POST)
        if regform.is_valid():
            name = regform.cleaned_data['name']
            country = regform.cleaned_data['country']
            nationality = regform.cleaned_data['nationality']
            mobile = regform.cleaned_data['mobile']
            role = regform.cleaned_data['role']
            email = regform.cleaned_data['email']
            password = regform.cleaned_data['password']

            user = User.objects.create_user(
                first_name=name,
                username=email,
                password=password
            )
            user.save()
            user_details = UserDetails(

                country=country,
                nationality=nationality,
                mobile=mobile,
                role=role
            )
            user_details.user = user
            user_details.save()

            return HttpResponseRedirect(reverse('login'))

        else:
            regform = registrationform()
            return render(request, 'user/registeruser.html', {'form': regform})

    else:
        regform = registrationform()
        return render(request, 'user/registeruser.html', {'form': regform})


def homepage(request):
    return render(request, 'user/homepage.html')


def checkstudent(person):
    if person.userdetails.role == 'student':
        return True
    else:
        return False


def checkstaff(person):
    if person.userdetails.role == 'staff':
        return True
    else:
        return False


def checkadmin(person):
    if person.userdetails.role == 'admin':
        return True
    else:
        return False


def checkeditor(person):
    if person.userdetails.role == 'editor':
        return True
    else:
        return False


@user_passes_test(checkstudent, login_url=reverse_lazy('redirect'))
def student(request):
    return render(request, 'user/student.html')


@user_passes_test(checkstaff, login_url=reverse_lazy('redirect'))
def staff(request):
    return render(request, 'user/staff.html')


@user_passes_test(checkadmin, login_url=reverse_lazy('redirect'))
def admin(request):
    return render(request, 'user/admins.html')


@user_passes_test(checkeditor, login_url=reverse_lazy('redirect'))
def editor(request):
    return render(request, 'user/editor.html')


def loginuser(request):

    if request.method == 'POST':

        lform = loginform(request.POST)
        if lform.is_valid():
            email = lform.cleaned_data['email']
            password = lform.cleaned_data['password']

            person = authenticate(username=email, password=password)

            if person is not None:
                login(request, person)

                if person.userdetails.role == 'staff':

                    return HttpResponseRedirect(reverse('staff'))

                if person.userdetails.role == 'student':

                    return HttpResponseRedirect(reverse('student'))

                if person.userdetails.role == 'admin':

                    return HttpResponseRedirect(reverse('admins'))

                if person.userdetails.role == 'editor':

                    return HttpResponseRedirect(reverse('editor'))

            else:
                return render(request, 'user/login.html', {'form': lform})
        else:
            return render(request, 'user/login.html', {'form': lform})

    else:
        lform = loginform()
        return render(request, 'user/login.html', {'form': lform})


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def redirect(request):
    return render(request, 'user/redirect.html')
