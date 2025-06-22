import psycopg2 as db
from api_request import mock_fetch_data, fetch_data

def connect_to_db():
  print("Connecting to PostgreSQL database...")
  
  try:
    conn = db.connect(host='db', port=5432, dbname='db', user='user', password='user')
    return conn
  except db.Error as e:
    print(f"Database connection failed: {e}")
    raise
  
def create_table(conn):
  print("Creating table...")
  try:
    cursor = conn.cursor()
    cursor.execute("""
      CREATE SCHEMA IF NOT EXISTS dev;
      CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
        id SERIAL PRIMARY KEY,
        city TEXT,
        temperature FLOAT,
        weather_description TEXT,
        wind_speed FLOAT,
        time TIMESTAMP,
        inserted_at TIMESTAMP DEFAULT NOW(),
        utc_offset TEXT
      );
    """)
    conn.commit()
    print("Table was created.")
  except db.Error as e:
    print(f"Failed to create table: {e}")
    raise
  
def insert_records(conn, data):
  print("Inserting data to the database...")
  try:
    location = data['location']
    weather = data['current']
    
    cursor = conn.cursor()
    cursor.execute("""
      INSERT INTO dev.raw_weather_data (
        city,
        temperature,
        weather_description,
        wind_speed,
        time,
        inserted_at,
        utc_offset
      ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
    """, (
      location['name'],
      weather['temperature'],
      weather['weather_descriptions'][0],
      weather['wind_speed'],
      location['localtime'],
      location['utc_offset'] 
    ))
    conn.commit()
    print("Data successfully inserted!")
  except db.Error as e:
    print(f"Failed to insert data: {e}")  
    raise
  
def main():
  try:
    # data = mock_fetch_data()
    data = fetch_data()
    conn = connect_to_db()
    create_table(conn)
    insert_records(conn, data)
  except Exception as e:
    print(f"An error occured: {e}")
  finally:
    if 'conn' in locals():
      conn.close()
      print("Database connection closed.")
  
  
main()