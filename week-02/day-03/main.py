#main.py
import webapp2
import logging
import jinja2
import os
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class Star(ndb.Model):
    name = ndb.StringProperty(required=True)
    oscars = ndb.IntegerProperty(required=True)

    def describe(self):
        return "%s has won %s Oscars" % (self.name, self.oscars)

class Movie(ndb.Model):
    title = ndb.StringProperty(required =True)
    runtime = ndb.IntegerProperty(required =True)
    rating = ndb.FloatProperty(required =True,default=0)
    star_keys = ndb.KeyProperty(
    kind=Star,
    required=False,
    repeated = True
    )


    def describe(self): #for a get request
        return "%s is %d minute(s) long, with a rating of %f" % (self.title, self.runtime, self.rating)

class populateDatabase(webapp2.RequestHandler):
    def get(self):
        shameik_key = Star(name='Shameik Moore', oscars = 1).put()#put returns a key
        seth_rogan = Star(name = 'Seth Rogan', oscars = 5).put()
        keanu_reeves = Star(name = 'Keanu Reeves', oscars = 5).put()
        james_earl_jones = Star(name = 'James Earl Jones', oscars = 365).put()
        #key -> unique ID to perticular identifier
        # sort of like your social sercuity #
        # .get() to get the key

        #print shameik_key.get().name


        Movie(
        title = "SpiderMan",
        runtime = 144,
        rating = 7.5,
        star_keys = [shameik_key, seth_rogan, keanu_reeves, james_earl_jones]).put()

        Movie(
        title = "Lion King",
        runtime = 118,
        rating = 8,
        star_keys = [shameik_key, seth_rogan]).put()


class MainPage(webapp2.RequestHandler):
    def get(self):
        movies_list = Movie.query().fetch()
        # TODO: Get Star list from query and fetching
        #Loop through the star
        # Populate dictionary with star name and # of oscars
        star_list = Star.query().fetch()


        template_vars = {
        'movies' : movies_list,
        'star_name' : star_list,

        }
        template = jinja_env.get_template("main.html")
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/populateDatabase', populateDatabase),

], debug=True)
