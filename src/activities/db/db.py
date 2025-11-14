import sqlite3

def create_db(sql_script_path, db_path):
    """
    Create an SQLite database using the SQL script provided.

    Parameters
    ----------
    sql_script_path : str
        Path to the .sql file containing the schema.
    db_path : str
        Path where the SQLite database file will be created.
    """
    # Read the SQL script from file
    with open(sql_script_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    # Connect to (or create) the database
    connection = sqlite3.connect(db_path)

    try:
        cursor = connection.cursor()
        # Execute the whole script (can contain multiple CREATE TABLE statements)
        cursor.executescript(sql_script)

        # Save changes
        connection.commit()
    finally:
        # Always close the connection
        connection.close()
