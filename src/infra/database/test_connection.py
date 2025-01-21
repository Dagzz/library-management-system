from database_connection import get_engine

# Test the connection to the database

if __name__ == "__main__":
    try:
        engine = get_engine()
        with engine.connect() as connection:
            print("Successfully connected to MySQL database!")
    except Exception as e:
        print(f"Error while connecting: {e}")