#!/usr/bin/env python

import flask
import pymysql
import os
import re
import HTMLParser

class MLStripper(HTMLParser.HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

app = flask.Flask(__name__)
templateDir = "/home/makin/mysite/templates"
try:
	os.listdir(templateDir)
except:
	templateDir = templateDir[templateDir.rfind(r"/")+1:]
blogurl = "/blog/"

@app.route('/')
def index():
	#-- ambil blog yg ada
	files = os.listdir(templateDir)
	blogsdata = re.compile("blog_(\w*)").findall(str(files))
	blogsrange = range(len(blogsdata))
	blogs = [blogsdata, blogsrange]

	#-- ambil excerpt nya
	i = 0
	excerptsdata = []
	for i in blogs[1]:
		f = open(templateDir+"/blog_"+blogs[0][i]+".html","r")
		data = f.read()
		f.close()
			
		excerpt = data[data.find("{% block excerpt %}")+len("{% block excerpt %}"):] #-- better than regex
		excerpt = excerpt[:excerpt.find("{% endblock %}")] #-- better than regex
		excerpt = strip_tags(excerpt)
		excerptsdata.append(excerpt)
	excerptsrange = range(len(excerptsdata))
	excerpts = [excerptsdata, excerptsrange]

	return flask.render_template('index.html', blogs=blogs, excerpts=excerpts, templateDir=templateDir, blogurl=blogurl)

@app.route(blogurl+'<judul>')
def templates(judul):
	return flask.render_template('blog_'+judul+'.html',judul=judul.replace("_"," "))

@app.route('/\\')
def tes():
	#-- ambil blog yg ada
	return ("well not an 404 but i guess that's nice url writing.")
	files = os.listdir(templateDir)
	blogs = re.compile("blog_(\w*)").findall(str(files))
	return str(blogs)

if __name__ == "__main__":
	app.run(debug=True)
