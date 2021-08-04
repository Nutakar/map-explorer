from flask import Flask, redirect, url_for, jsonify, request
import Map

server = Flask(__name__)
# curl --data "[{\"name\": \"garage\", \"lon\": 61.69608, \"lat\": 50.82968}, {\"name\": \"beauty_hall\", \"lon\": 61.69624, \"lat\": 50.80921}"] --header "Content-Type: application/json" http://localhost:8000/add_dots
# curl http://localhost:8000/add_dots -d '[{"title" : "garage", "lon": 61.69608, "lat": 50.82968}]' -H 'Content-Type: application/json'


@server.route('/get_dots', methods = ['POST'])
# curl http://localhost:8000/get_dots -d '{"distance":1.5, "lon": 61.692573, "lat": 50.819956}' -H 'Content-Type: application/json'
def get_dots_by_distance():
    request_data = request.get_json()

    distance = request_data["distance"]
    lon = request_data["lon"]
    lat = request_data["lat"]

    result = Map.count_distance(distance, lon, lat)
    print('POST request: /get_dots')
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
    print('POST request: /add_dots')
    return 'Dots have been added'


@server.route('/all_dots', methods = ['GET'])
def show_all_dots():
    result = Map.show_all_dots()
    print('GET request: /all_dots')
    return result

@server.route('/count_dots', methods = ['GET'])
def count_all_dots():
    result = Map.count_number_of_dots()
    print('GET request: /count_dots')
    return result
