from google.appengine.ext import db

class BusStop(db.Model):
	name = db.StringProperty()
	number = db.StringProperty()
	location = db.GeoPtProperty()