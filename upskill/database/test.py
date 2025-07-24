
import psycopg2
def database():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="krun@l",
            host="localhost",  
            port="5432"       
        )

        cursor = conn.cursor()

        # Execute query
        cursor.execute("SELECT * FROM students;")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()
database()