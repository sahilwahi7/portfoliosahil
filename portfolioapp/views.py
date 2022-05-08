from django.shortcuts import render
from portfolioapp.models import About, Resume, Projects

# Create your views here.


def home(request, methods=['GET', 'POST']):

    details = About.objects.all()
    resume_details = Resume.objects.all()
    project_details = Projects.objects.all()
    aboutdetails = details[0]
    resume_details = resume_details[0]
    project_details = project_details[0]
    context = {'aboutdetails': aboutdetails,
               'resumedetails': resume_details, 'projectdetails': project_details}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)

        return render(request, 'index.html', context=context)

    return render(request, 'index.html', context=context)
