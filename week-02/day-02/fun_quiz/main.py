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
        template = jinja_env.get_template("templates/quiz.html")
        self.response.write(template.render())

    def post(self):
        template_vars = {
            "originalName": self.request.get("originalName"),
            "playWord": self.request.get("playWord"),
        }
        template = jinja_env.get_template("templates/results.html")
        self.response.write(template.render(template_vars))



# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler


], debug=True)
