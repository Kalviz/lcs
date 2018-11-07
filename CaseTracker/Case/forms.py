from django import forms

class AddCase(forms.Form):
    caseid = forms.CharField(max_length=20)
    title = forms.CharField(max_length=125)
    owner = forms.CharField(max_length=125)
    catagory = forms.CharField(max_length=20)
    subcatagory = forms.CharField(max_length=20)
    status = forms.CharField(max_length=10)
    progress = forms.CharField(max_length=100)
    progressDetails = forms.CharField(widget=forms.Textarea)
    incidentReporter = forms.CharField(max_length=50)
    incidentOwner = forms.CharField(max_length=50)
    priority = forms.CharField(max_length=10)
    dateCreated = forms.DateTimeField()
