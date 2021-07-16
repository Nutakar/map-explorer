from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import Map
from Map import count_distance
# from Map import close_DBconnection

print('pidor2')

class helloHandler(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self.set_headers()


    def do_GET(self):
        dots = Map.show_all_dots()
        self.wfile.write(json.dumps(dots).encode())
        self.wfile.write('\n'.encode())
        # self.wfile.write(Map.a.encode())
        self.set_headers()

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))

        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        
        if self.path.endswith('/get_dots'):

            # curl --data "{\"distance\":1.5, \"lon\": 61.692573, \"lat\": 50.819956}" --header "Content-Type: application/json" http://localhost:8000/get_dots

            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))

            distance = message.get("distance")
            lon = message.get("lon")
            lat = message.get("lat")

            self.set_headers()

            res = count_distance (distance, lon, lat)

            # res = Map.count_distance(distance, lon, lat)
            self.wfile.write(json.dumps(res).encode())
            self.wfile.write('\n'.encode())


        if self.path.endswith('/add_dots'):

            # curl --data "[{\"name\": \"garage\", \"lon\": 61.69608, \"lat\": 50.82968}, {\"name\": \"beauty_hall\", \"lon\": 61.69624, \"lat\": 50.80921}"] --header "Content-Type: application/json" http://localhost:8000/add_dots

            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))

            dots = []

            for dict in message:
                name = dict['name']
                lon = dict['lon']
                lat = dict['lat']
                dot = (name, lon, lat)
                dots.append(dot)
            
            Map.add_dots(dots)

            self.set_headers()
            self.wfile.write(str(dots).encode())
            self.wfile.write('\n'.encode())
            self.wfile.write(' Dots have been added'.encode())
            self.wfile.write('\n'.encode())
        

        # self.wfile.write(str(distance).encode())
        # return distance, lon, lat

        



def run(server_class = HTTPServer, handler_class = helloHandler, port = 8000):
    server_addres = ('', port)    
    httpd = server_class(server_addres, handler_class)
    print ('server running on port ', port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt as err:
        import Map
        Map.close_DBconnection()
        # config_DB.close_DB_connection() 
        print(err)

if __name__ == '__main__':
    run()

