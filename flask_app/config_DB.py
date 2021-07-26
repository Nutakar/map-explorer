import os

def config():
    db = {}
    db['user'] = os.environ['POSTGRES_USER']
    db['password'] = os.environ['POSTGRES_PASSWORD']
    db['host'] = os.environ['POSTGRES_HOST']
    db['port'] = os.environ['POSTGRES_PORT']
    db['database'] = os.environ['POSTGRES_DB']
    return db
    