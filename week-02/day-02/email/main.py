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


class Email(object):
    def __init__(self,subject,unread,spam):
        self.subject = subject
        self.unread = unread
        self.spam = spam

emails = [
    Email("Hey, how it going?", True, False),
    Email("Hey, how it going?", True, False),
    Email("Status Report", False, False),
    Email("Free TidePods", True, True),


]

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        template_vars = {
        'inbox': emails,
        }
        #Step 3: Use the Jinja environment to get our HTML
        template = jinja_env.get_template("templates/inbox.html")
        self.response.write(template.render(template_vars))



# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler



], debug=True)
