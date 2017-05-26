""" Views Classes """

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required

from .forms import JobForm
from .models import Job
from . import commands


class JobDeleteView(DeleteView):
    """ Delete View """
    model = Job
    success_url = reverse_lazy('job-list')

@login_required
def run(request, id):
    """ Execute a Job """
    data = Job.objects.get(pk=id)
    try:
        data.state = True
        data.result = commands.submit_job(data, data.hostname, data.username,
                                          data.password, data.model_name,
                                          data.cluster_number)
        data.save()
    except Exception as error:
        print(error)
        print("error: invalid nlogo file")
    return redirect('job-list')

@login_required
def stop(request, id):
    """ Stop a Job """
    data = Job.objects.get(pk=id)
    data.state = False
    data.save()
    return redirect('job-list')

@login_required
def upload_job_view(request):
    """ Upload the view """
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'job_manager/job_upload.html', {'form': form})
    else:
        form = JobForm()
        return render(request, 'job_manager/job_upload.html', {'form': form})

class JobListView(ListView):
    """ Shows List """
    model = Job

