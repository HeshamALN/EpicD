
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Project, About, Home
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {
        "home": Home.objects.all()
    }
    return render(request,"home.html", context)

def about(request):
    context = {
        "about": About.objects.all()
    }
    return render(request,"about.html", context)

def instagram(request):
    # return HttpResponse("My first APP")
    context = {

    }
    return render(request,"instagram.html", context)


def plans(request):
    # return HttpResponse("My first APP")
    context = {

    }
    return render(request,"plans.html", context)


def howItWorks(request):
    # return HttpResponse("My first APP")
    context = {

    }
    return render(request,"hiw.html", context)


def contact(request):
    # return HttpResponse("My first APP")
    form = ContactForm()
    return render(request,"1contact.html",{'form': form})

def project_list(request):
    projects_list = Project.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(projects_list, 3)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, "1project.html", { 'projects': projects })




def project_details(request, project_id):
    context = {
        "project": Project.objects.get(id=project_id)
    }
    return render(request,"1projectDetails.html", context)

def emailView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data['message']
            sender = form.cleaned_data["email"]
            recipients = ['halnukhailan@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, "Your message has been sent, we'll contact you soon!")
    return render(request, "1contact.html", {'form': form})




def error(request):
    # return HttpResponse("My first APP")
    context = {

    }
    return render(request,"404.html", context)