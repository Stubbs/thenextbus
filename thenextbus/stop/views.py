from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from BeautifulSoup import BeautifulSoup
from stopforms import *

from google.appengine.api import urlfetch

import sys
import logging
import re

def render(template, payload):
	"""docstring for render"""
	return render_to_response(template, payload)

def index(request):
	"""docstring for index"""
	payload = dict(stop_form=StopForm())
	return render('index.html', payload)

def redirect(request):
	"""docstring for redirect"""
	if request.method == 'GET':
		return HttpResponseRedirect('/')
	else:
		form = StopForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/stop/%s/' % form.clean_data['stop_number'])
		else:
			return HttpResponseRedirect('/')

def stop(request, stop_number):
	"""Retrieves information about the given stop number and renders it to the screen"""
	payload = dict()
	
	try:
		# http://tsy.acislive.com/pip/stop_simulator.asp?naptan=37022440
		result = urlfetch.fetch('http://tsy.acislive.com/pip/stop_simulator_table.asp?NaPTAN=' + stop_number)
		
		if result.status_code == 200:
			# Rather than use something like minidom or BeautifulSoup, I've had to resort
			# to regexps to pull out the timetable info, the HTML just refuses to parse for various reasons.

			# Find the table.
			table = re.search("<table.*>(.*)</table>", result.content)
			
			if table != None:
				error = None
				rows = re.split('</tr>', table.group(0))
		
				buses = []
				for row in rows:
					a = [td.group(1) for td in re.finditer("(?:<td.*?>)(.*?)</td>", row)]
					if len(a) > 0:
						buses.append(a)
			else:
				error = 'There are no buses from this stop.'
				buses = None

			return render('stop.html', {'buses': buses, 'error': error})
		else:
			return render('error.html', payload)

	except ValueError:
		return render('error.html', payload)

