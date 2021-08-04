import psycopg2
import math
import config_DB
import time


params = config_DB.config()
print ('555Connecting to the PostgreSQL DB')
print(params)
print ('pidor')

connection = psycopg2.connect(**params)
cursor = connection.cursor()

# Count function time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        result = f(*args, **kwargs)
        print ('Time of function: %f' % (time.time()-t)) 
        return result
    return tmp

#Add records to DB
def add_dots(dots, cursor = cursor, connection = connection):

    # places = [
    #     ('home', 61.69132, 50.82074),
    #     ('school', 61.69095, 50.81769),
    #     ('dodo', 61.69319, 50.81534),
    #     ('maxi', 61.69864, 50.80271)
    # ]

    places = dots

    records_list_template = ','.join(['%s'] * len(places))
    insert_query = 'insert into dots (title, lon, lat) values {}'.format(records_list_template)
    cursor.execute(insert_query, places)
    connection.commit()

@timer
def count_distance(distance, lon, lat, cursor = cursor):

    # GPS = [distance, 61.692573, 50.819956]
    lon = float(lon)
    lat = float(lat)
    lat_rad = lat*3.14/180

    lon_start = lon - (distance/111.13486 + 0.5)
    lon_finish = lon + (distance/111.13486 + 0.5)
    lat_start = lat - (distance/(111.32138 * math.cos(lat_rad)) + 0.5)
    lat_finish = lat + (distance/(111.32138 * math.cos(lat_rad)) + 0.5)


    result = {}
    cursor.execute("""
        SELECT * FROM dots
        WHERE lat >= %s
        AND lat <= %s
        AND lon >= %s
        AND lon <= %s;
    """, (lat_start, lat_finish, lon_start, lon_finish))
    while True:
        row = cursor.fetchone()
        if row == None:
            break

        R = 6371
        lat1 = float(lat)
        lat2 = float(row[2])
        lon1 = float(lon)
        lon2 = float(row[1])

        fi1 = lat1*3.14/180
        fi2 = lat2*3.14/180
        dfi = (lat2-lat1)*3.14/180
        dlam = (lon2-lon1)*3.14/180
        a = math.sin(dfi/2)*math.sin(dfi/2) + math.cos(fi1)*math.cos(fi2)*math.sin(dlam/2)*math.sin(dlam/2)
        c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R*c
        if d<=distance:

            result[row[0]]= {
                    'lon': row[1],
                    'lat': row[2]
                }
    return result


def show_all_dots(cursor = cursor):

    result = {}
    cursor.execute("SELECT * FROM dots")
    while True:
        row = cursor.fetchone()
        if row == None:
            break

        lat = float(row[2])
        lon = float(row[1])

        result[row[0]]= {
                'lon': row[1],
                'lat': row[2]
            }
    return result


def count_number_of_dots(cursor = cursor):
    result = {}
    cursor.execute("SELECT COUNT(*) FROM dots")
    count_number = cursor.fetchone()
    result['number_of_dots'] = count_number[0]
    return result

def close_DBconnection(cursor = cursor, connection = connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
