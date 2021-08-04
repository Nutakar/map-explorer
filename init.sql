CREATE TABLE dots (
    title    TEXT     NOT NULL,
    lon      REAL     NOT NULL,
    lat      REAL     NOT NULL
); 
CREATE INDEX lon_index ON dots (
    lon 
);
CREATE INDEX lat_index ON dots (
    lat
);