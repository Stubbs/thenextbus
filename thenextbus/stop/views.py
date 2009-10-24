from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from stopforms import *

from google.appengine.api import urlfetch, memcache

import sys
import logging
import re

def render(template, payload):
	"""docstring for render"""
	return render_to_response(template, payload)

def getTimes(stop_number):
	"""docstring for getTimes"""
	return urlfetch.fetch('http://tsy.acislive.com/pip/stop_simulator_table.asp?NaPTAN=' + stop_number)

def getTitle(stop_number):
	"""retrieves the name of the given stop, and stores it in memcache"""
	title = memcache.get(stop_number)

	if title is not None:
		return title
	else:
		result = urlfetch.fetch('http://tsy.acislive.com/pip/stop_simulator.asp?NaPTAN=' + stop_number)
		title = re.search('(?:<title>[\n\w]*)(.*)</title>', result.content)
		memcache.set(stop_number, title.group(1))
		return title.group(1)

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
		# Get the title of this stop.
		stopTitle = getTitle(stop_number)
		
		# http://tsy.acislive.com/pip/stop_simulator.asp?naptan=37022440
		result = getTimes(stop_number)
		
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

			return render('stop.html', {'title': stopTitle, 'buses': buses, 'error': error})
		else:
			return render('error.html', payload)

	except ValueError:
		return render('error.html', payload)

def add_stop(request):
	"""Allows a user to add a new bus stop."""
	if request.method == 'GET':
		payload = dict(form=AddStopForm())
		return render('new_stop.html', payload)
	else:
		pass
	
def edit_stop(request, stop_number):
	"""Allows a user to edit a stop"""
	pass

def help_nearby(request):
	return render('whats_this.html', {})