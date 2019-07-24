#main.py
# the import section
import webapp2
import logging
#Step 1: Import Jinja and os
import jinja2
import os

#Step 2: Set up Jinja environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request

        #Step 3: Use the Jinja environment to get our HTML
        template = jinja_env.get_template("templates/madlibs.html")
        self.response.write(template.render())

    def post(self):
        template_vars = {
            "adjective1": self.request.get("adjective1"),
            "adjective2": self.request.get("adjective2"),
            "noun1": self.request.get("noun1"),
            "noun2": self.request.get("noun2"),
            "pNoun1": self.request.get("pNoun1"),
            "verb1": self.request.get("verb1"),
            "verb2": self.request.get("verb2"),
            "pNoun2": self.request.get("pNoun2"),
            "verb3": self.request.get("verb3"),
            "noun3": self.request.get("noun3"),
            "plant": self.request.get("plant"),
            "bodyPart": self.request.get("bodyPart"),
            "place": self.request.get("place"),
            "verb3": self.request.get("verb3"),
            "adjective3": self.request.get("adjective3"),
            "number": self.request.get("number"),
            "pNoun4": self.request.get("pNoun4"),
        }
        template = jinja_env.get_template("templates/story.html")
        self.response.write(template.render(template_vars))



# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler


], debug=True)
