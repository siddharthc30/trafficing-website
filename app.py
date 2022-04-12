from flask import Flask, render_template, redirect, request, flask
import random
import os


app = Flask()

@app.route('/')
def index():
    return render_template("index.html")






app.run(debug = True)
