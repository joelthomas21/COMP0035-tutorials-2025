from db import create_db

if __name__ == "__main__":
    sql_file_path = "paralympics_schema.sql"   # <- update if your file name/path is different
    db_file_path = "db.py"           # or "paralympics.sqlite"

    create_db(sql_file_path, db_file_path)
    print("success")
