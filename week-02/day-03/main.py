#main.py
import webapp2
import logging
import jinja2
import os
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        #name = self.request.get('name') or 'World'
        movies_list = Movie.query().fetch()
        template_vars = {
        'movies' : movies_list,
        }
        template = jinja_env.get_template("main.html")
        self.response.write(template.render(template_vars))

# 1. New handler for /populateDatabase
# --> Adds a few movies and stars
# 2. After adding, redirect back to '/'

#print Movie.query().fetch()
#print Movie.query().filter()
#print Movie.query().fetch()
#movie_query = Movie.query().filter(
#    Movie.rating > 9).order(-Movie.rating)
#movie_list = movie_query.fetch()
#for movie in movie_list:
#    print movie.title
#print movie_list





class Movie(ndb.Model):
    title = ndb.StringProperty(required =True)
    runtime = ndb.IntegerProperty(required =True)
    rating = ndb.FloatProperty(required =True,default=0)
    star_names = ndb.StringProperty(
    required=False,
    # default=[],
    repeated = True
    )


    def describe(self): #for a get request
        return "%s is %d minute(s) long, with a rating of %f" % (self.title, self.runtime, self.rating)

class Star(ndb.Model):
    name = ndb.StringProperty(required=True)
    oscarsWon = ndb.IntegerProperty(required=True)
    retired = ndb.BooleanProperty(required=True)

    def describe(self):
        if not self.retired:
            return "%s has won %s Oscars and is not retired" % (self.name, self.oscarsWon)

        else:
            return "%s has won %s Oscars and is retired" % (self.name, self.oscarsWon)


class populateDatabase(webapp2.RequestHandler):
    def get(self):
        spiderverse = Movie(
            title ="Into the Spiderverse",
            runtime = 117,
            rating = 9.99

        )
        shameik_moore = Star(
            name = "Shameik Moore",
            oscarsWon = 5,
            retired = False
        )
        #template = jinja_env.get_template("movies.html")
        spiderverse.put()
        shameik_moore.put()


        #redirect back to MainPage
        #self.redirect('/')
        #localhost:8000 to view dev board

#print spiderverse.describe()
#print shameik_moore.describe()

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/populateDatabase', populateDatabase),

], debug=True)
