import psycopg2
import distance
from psycopg2.extras import DictCursor
from contextlib import closing


LONGITUDE_KEY = 'longitude'
latitudekey = 'latitude'
residential_complexes = []
complex_stops = {}
with closing(psycopg2.connect(dbname='mostranstest', user='postgres', password='1234', port='5432')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute('select * from jk')
        residential_complexes = cursor.fetchall()
        assert len(residential_complexes) != 0, "no residential complex data"
        for complex in residential_complexes:
            longdelta, latdelta = distance.getdeltavals(complex[LONGITUDE_KEY], complex[latitudekey])
            cursor.execute(f"""select name, longitude, latitude from stops
            where longitude between {complex[LONGITUDE_KEY]} - {longdelta} and {complex[LONGITUDE_KEY]} + {longdelta}
            and latitude between {complex[latitudekey]} - {latdelta} and {complex[latitudekey]} + {latdelta}""")
            complex_stops[complex['name']] = cursor.fetchall()
