from django import newforms as forms
from google.appengine.ext.db import djangoforms
from thenextbus.stop.models import *

class StopForm(forms.Form):
	"""Very simple for to get a stop number"""
	stop_number = forms.CharField(required=True, label='Stop Number')
	
class AddStopForm(djangoforms.ModelForm):
	"""Form for adding new stops to the database"""
	class Meta:
		model = BusStop