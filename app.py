from flask import Flask
from flask import request
from whois import whois

app = Flask(__name__)

@app.route("/")
def index():
  return '<form action="whois" method="post"><label for="domain_name">Domain:</label><input type="text" name="domain_name"></form>'

@app.route("/whois", methods=['POST'])
def whois():
  return whois11.whois(request.form['domain_name'])
