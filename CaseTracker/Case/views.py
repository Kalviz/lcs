from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import caseoverview
from .forms import AddCase

# Create your views here.
def index(request):
    return render(request, 'case/index.html')


def case(request):
    entres = caseoverview.objects.all()
    return render(request, 'Case/case.html', {'entri': entres})


def add(request):
    if request.method == 'POST':
        form = AddCase(request.POST)

        if form.is_valid():
            caseid = form.cleaned_data['caseid']
            title = form.cleaned_data['title']
            owner = form.cleaned_data['owner']
            catagory = form.cleaned_data['catagory']
            subcatagory = form.cleaned_data['subcatagory']
            status = form.cleaned_data['status']
            progress = form.cleaned_data['progress']
            progressDetails = form.cleaned_data['progressDetails']
            #incidentReporter = {{ request.user.username }}
            incidentReporter = form.cleaned_data['incidentReporter']
            incidentOwner = form.cleaned_data['incidentOwner']
            priority = form.cleaned_data['priority']

            caseoverview.objects.create(
                caseid=caseid,
                title=title,
                owner=owner,
                catagory=catagory,
                subcatagory=subcatagory,
                status=status,
                progress=progress,
                progressDetails=progressDetails,
                incidentReporter=incidentReporter,
                incidentOwner=incidentOwner,
                priority=priority,
            ).save()

            return HttpResponseRedirect('/')

    else:
        form = AddCase()

    return render(request, 'Case/forms.html', {'form': form})



def delete(request,pk):
    if request.method == 'DELETE':
        entry = get_object_or_404(caseoverview, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')









