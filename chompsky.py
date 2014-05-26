#!/usr/bin/env python
from flask import Flask, url_for, redirect, render_template, send_file
from PIL import Image
import os
import random

app = Flask(__name__)

def check_parameters(width, height):
    if width < 0 or height < 0:
        pass
    if width == 0:
        width = 75 
    if height == 0:
        height = 75 
    return width, height

def get_path(ratio):
    if ratio < 1.0:
        folder = 0
    elif ratio == 1.0:
        folder = 1
    elif ratio > 1.0:
        folder = 2
    return "static/images/{0}".format(folder)

def available_photo(file_name):
    return os.path.isfile(file_name) 

@app.route("/")
def hello():
    return render_template('index.html') 

@app.route("/<int:width>/<int:height>")
def get_chompsky(width, height):
    width, height = check_parameters(width, height)     
    ratio = float(width)/height
    file_name = "{0}_{1}_{2}.png".format(ratio, width, height)
    path = get_path(ratio)
   
    cache_path = "static/images/cache"
    cached_photo_file = os.path.join(cache_path, file_name) 
    if available_photo(cached_photo_file):
        return send_file(cached_photo_file)

    # get photo
    photo = random.choice(os.listdir(path))
    f = Image.open(os.path.join(path, photo))
    
    (actual_width, actual_height) = f.size
    actual_ratio = float(actual_width)/actual_height
     
    if ratio > actual_ratio:
        required_height = int(actual_width/ratio)
        diff_change = (actual_height - required_height)/2
        box = (0, diff_change, actual_width, actual_height - diff_change)
        new = f.crop(box)
    elif ratio < actual_ratio:   
        required_width = int(actual_height * ratio)
        diff_change = (actual_width - required_width)/2
        box = (0 + diff_change, 0, actual_width - diff_change, actual_height)
        new = f.crop(box)
    elif actual_ratio == ratio:
        new = f.resize((width, height))
    new = new.resize((width, height))
    file_name = "{0}_{1}_{2}.png".format(ratio, width, height)
    new_path = os.path.join(cache_path, file_name)
    new.save(new_path)
    return send_file(new_path)
    
if __name__ == "__main__":
    app.run()
