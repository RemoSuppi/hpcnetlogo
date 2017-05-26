
"""Forms"""
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    """ Form for Upload Files"""
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """ Fields in the form """
        model = Job
        #  fields: 'file_first', 'file_second', 'file_third', 'file_forth',
        #          'email', 'hostname', 'username', 'password'
        fields = ['file_first', 'experiment_name', 'e_e', 'model_name',
                  'cluster_number', 'hostname', 'username', 'password']
