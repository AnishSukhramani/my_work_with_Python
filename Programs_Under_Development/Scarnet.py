from flask import Flask , render_template, request


scarnet= Flask(__name__)
@scarnet.route('/')
def scar():
    name=request.form('')
    