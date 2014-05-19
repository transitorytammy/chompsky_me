#!/usr/bin/env python
from __future__ import print_function
from flask import Flask, url_for, redirect, render_template, send_file
from PIL import Image
from PIL import ImageCms
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

@app.route("/chompsky/<int:width>/<int:height>")
def get_chompsky(width, height):
    if width < 0 or height < 0:
        raise PyCMSError
    elif width == 0 and height == 0:
        width = 75 
        height = 75
    elif width == 0:
        width = 75 
    elif height == 0:
        height = 75 
    ratio = float(width)/height
    if ratio < 1.0:
        folder = 0
    elif ratio == 1.0:
        folder = 1
    elif ratio > 1.0:
        folder = 2
    path = "static/images/{0}".format(folder)
    photo = random.choice(os.listdir(path))
    f = Image.open(os.path.join(path, photo))
    (actual_width, actual_height) = f.size
    actual_ratio = float(actual_width)/actual_height
    required_height = int(actual_width/ratio)
    required_width = int(actual_height * ratio)
    if ratio > actual_ratio:
        diff_change = (actual_height - required_height)/2
        box = (0, diff_change, actual_width, actual_height-diff_change)
        new = f.crop(box)
    elif ratio < actual_ratio:   
        diff_change = (actual_width - required_width)/2
        box = (0 + diff_change, 0, actual_width - diff_change, actual_height)
        new = f.crop(box)
    elif actual_ratio == ratio:
        new = f.resize((width, height))
    #else:
        #return "height:{0}, {1}, {2}, width:{3}, {4}, {5}, ratio: {6}".format(required_height, height, actual_height, required_width, width, actual_width, ratio) 
    new = new.resize((width, height))
    new.save("static/images/new_chompsky.png")
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
