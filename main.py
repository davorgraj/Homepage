#!/usr/bin/env python
import jinja2
import os
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("home.html")


class AboutMeHandler(BaseHandler):
    def get(self):
        return self.render_template("about_me.html")


class ProjectsHandler(BaseHandler):
    def get(self):
        return self.render_template("projects.html")


class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")


class ContactHandler(BaseHandler):
    def get(self):
        return self.render_template("contact.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/about_me', AboutMeHandler),
    webapp2.Route('/projects', ProjectsHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/contact', ContactHandler),
], debug=True)
