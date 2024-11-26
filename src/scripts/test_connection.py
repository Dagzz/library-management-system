from src.dal.database_connection import get_engine

# Test the connection to the database

if __name__ == "__main__":
    try:
        engine = get_engine()
        with engine.connect() as connection:
            print("Connexion réussie à la base de données MySQL !")
    except Exception as e:
        print(f"Erreur lors de la connexion : {e}")
