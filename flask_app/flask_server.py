from flask import Flask, redirect, url_for, jsonify, request
import Map

server = Flask(__name__)

@server.route('/list_of_dots')
def list_of_dots(result):
    return 'List of dots: ', result

@server.route('/get_dots', methods = ['POST'])
def get_dots_by_distance():
    request_data = request.get_json()
    distance = request_data["distance"]
    lon = request_data["lon"]
    lat = request_data["lat"]
    result = Map.count_distance(distance, lon, lat)
    # return jsonify(request_data)
    return result

@server.route('/add_dots', methods = ['POST'])
def add_dots_to_db():
    request_data = request.get_json()
    dots = []

    for dict in request_data:
        name = dict['title']
        lon = dict['lon']
        lat = dict['lat']
        dot = (name, lon, lat)
        dots.append(dot)

    Map.add_dots(dots)
    return 'Dots have been added'

