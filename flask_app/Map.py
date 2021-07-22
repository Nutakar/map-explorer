import psycopg2
import math
import array as arr
from psycopg2 import Error
import config_DB


params = config_DB.config()
print ('555Connecting to the PostgreSQL DB')
print(params)
print ('pidor')

connection = psycopg2.connect(**params)
cursor = connection.cursor()




def create_table(cursor = cursor, connection = connection):
    create_table_query = '''CREATE TABLE dots
        (NAME     TEXT     NOT NULL,
        LON      REAL     NOT NULL,
        LAT      REAL     NOT NULL); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created")

# connection = psycopg2.connect(user="postgres",
#                             password="secret",
#                             host="127.0.0.1",
#                             port="5432",
#                             database="stage")

#         # Create a cursor to perform database operations
# cursor = connection.cursor()

# def close_connection():
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")




#  # SQL query to create a new table

# create_table_query = '''CREATE TABLE dots
#      (NAME     TEXT     NOT NULL,
#       LON      REAL     NOT NULL,
#       LAT      REAL     NOT NULL); '''

# cursor.execute(create_table_query)
# connection.commit()
# print("Table created")

def add_dots(dots, cursor = cursor, connection = connection):
    # cursor = connection.cursor()

    #Add records to DB
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
    # close_connection()


# My geo
def count_distance(distance, lon, lat, cursor = cursor, connection = connection):
    # cursor = connection.cursor()
    # GPS = [distance, 61.692573, 50.819956]

    result = {}
    # Main
    cursor.execute("SELECT * FROM \"dots\"")
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
        # print(d)
        if d<=distance:

            result[row[0]]= {
                    'lon': row[1],
                    'lat': row[2]
                }

    # close_connection()

    return result


def show_all_dots(cursor = cursor, connection = connection):

    # cursor = connection.cursor()
    # GPS = [distance, 61.692573, 50.819956]

    result = {}
    # Main
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

    # close_connection()

    return result


def close_DBconnection(cursor = cursor, connection = connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")



# finally:
#     if server1.except(KeyboardInterrupt):


