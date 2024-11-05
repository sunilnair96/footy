import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv(dotenv_path=r'C:\Users\sunil\Projects\footy\backend\.env')

# Database connection parameters
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '5432')  # Default PostgreSQL port

def connect_db():
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        print("Database connection established.")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def import_players(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Connect to the database
    conn = connect_db()
    if conn is None:
        return
    # Use a context manager for the database connection
    with conn:
        # Use a context manager for the cursor
        with conn.cursor() as cursor:
            for index, row in df.iterrows():
                player_name = row['Player']
                date_of_birth = row['DOB']
                height = row['Height']
                weight = row['Weight']
                draft_rank = row['DraftRank']
                draft_type = row['DraftType']
                draft_year = row['DraftYear']
                primary_position = row['PrimaryPos']
                secondary_position = row['DualPos']

                # Attempt to update existing player
                cursor.execute("""
                    UPDATE players
                    SET height = %s, weight = %s, draft_rank = %s, draft_type = %s, 
                        draft_year = %s, primary_position = %s, secondary_position = %s
                    WHERE player_name = %s AND date_of_birth = %s
                """, (height, weight, draft_rank, draft_type, draft_year, primary_position, secondary_position, player_name, date_of_birth))

                # Check if the update affected any rows
                if cursor.rowcount == 0:
                    # Insert data into the players table
                    with conn.cursor() as cursor:
                        for index, row in df.iterrows():
                            print (row['Height'])
                            cursor.execute(
                                """
                                INSERT INTO players (player_name, date_of_birth, height, weight, draft_rank, draft_type, draft_year, primary_position, secondary_position)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """,
                                (row['Player'], row['DOB'], row['Height'], row['Weight'], row['DraftRank'], row['DraftType'], row['DraftYear'], row['PrimaryPos'], row['DualPos'])
                            )
    # The context manager automatically commits and closes the cursor and connection
    conn.close()

    print("Players imported successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python import_players.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    print ('import_players :filePath:', file_path)
    import_players(file_path)