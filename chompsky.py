#!/usr/bin/env python
from __future__ import print_function
from flask import Flask, url_for, redirect, render_template, send_file
from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html') 

@app.route("/<width>/<height>")
def get_image(width, height):
    return send_file("static/images/IMG_6612.jpg")
    
@app.route("/tshirt/<size>")
def get_tshirt(size):
    if size == "small":
        return send_file("static/images/small.jpg")
    elif size == "large":
        return send_file("static/images/large.jpg")
    else:
        return "We don't have that size"

@app.route("/kris/<width>/<height>")
def get_kris(width, height):
    w = int(width)
    h = int(height)
    ratio = float(w/h)
    photo = random.choice(os.listdir("static/images/{0}".format(ratio)))
    f = Image.open(photo)
    new = f.resize(w, h))
    new.save("static/images/new_chompsky.png")
    return send_file("static/images/new_chompsky.png")

if __name__ == "__main__":
    app.run(debug=True)
