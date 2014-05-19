#!/usr/bin/env python
from __future__ import print_function
from flask import Flask, url_for, redirect, render_template, send_file
from PIL import Image
import os
import random


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

@app.route("/tammy/<width>/<height>")
def get_tammy(width, height):
    requested_width = int(width)
    requested_height = int(height)
    path = "static/images"
    photo = random.choice(os.listdir(path))
    f = Image.open(os.path.join(path, photo))
    (actual_width, actual_height) = f.size
    width_diff = (actual_width - requested_width)/2
    height_diff = (actual_height - requested_height)/2
    if width_diff > 0 and height_diff > 0:
        upper = 0 + height_diff
        lower = actual_height - height_diff
        left = 0 + width_diff
        right = actual_width - width_diff
        box = (left, upper, right, lower)
        new_picture = f.crop(box)
    else:
        new_picture = f.resize((requested_width, requested_height))
    new_picture.save("static/images/new_chompsky.png")
    return send_file("static/images/new_chompsky.png")
 

@app.route("/kris/<width>/<height>")
def get_kris(width, height):
    w = int(width)
    h = int(height)
    ratio = float(w/h)
    if ratio < 1.0:
        folder = 0
    elif ratio == 1.0:
        folder = 1
    elif ratio > 1.0:
        folder = 2
    path = "static/images/{0}".format(folder)
    photo = random.choice(os.listdir(path))
    f = Image.open(os.path.join(path, photo))
    new = f.resize((w, h))
    new.save("static/images/new_chompsky.png")
    return send_file("static/images/new_chompsky.png")

if __name__ == "__main__":
    app.run(debug=True)
