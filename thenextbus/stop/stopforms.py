from django import newforms as forms
from google.appengine.ext.db import djangoforms

class StopForm(forms.Form):
	"""Very simple for to get a stop number"""
	stop_number = forms.CharField(required=True, label='Stop Number')