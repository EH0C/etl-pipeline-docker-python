# script.py
from datetime import datetime
from sqlalchemy import create_engine, text, bindparam
import pandas as pd

print(f"Python script ran at {datetime.now()}")

# Source Database connection info
sourcedb_host = "source_mariadb"
sourcedb_user = "root"
sourcedb_password = "rootpassword"
sourcedb_name = "sourcedb"

# Target Database connection info
targetdb_host = "target_mariadb"
targetdb_user = "root"
targetdb_password = "rootpassword"
targetdb_name = "targetdb"

# STEP 1: EXTRACT
query = """
    SELECT *
    FROM `users`;
"""
print("ETL script start")
try:
    print(f"Connecting to database {sourcedb_name} at {sourcedb_host}")
    engine = create_engine(f"mysql+pymysql://{sourcedb_user}:{sourcedb_password}@{sourcedb_host}/{sourcedb_name}")
    with engine.connect() as connection:
        print(f"Connected to {sourcedb_name}")
        try:
            df = pd.read_sql_query(query, connection)
            print(f"Query returned {len(df)} rows")
        except Exception as e:
            print(f"Querying Error: {str(e)}")
            raise
    print("ETL script End")
except Exception as e:
    print(f"ETL script Error: {str(e)}")
    raise

# STEP 2: TRANSFORM
# STEP 2: TRANSFORM
print("Transforming column values: add _y to name column")
df["name"] = df["name"] + "_z"
newdf = df.copy()
print(newdf.head())

# STEP 3: LOAD
try:
    print(f"Connecting to target database {targetdb_name} at {targetdb_host}")
    target_engine = create_engine(
        f"mysql+pymysql://{targetdb_user}:{targetdb_password}@{targetdb_host}/{targetdb_name}"
    )
    with target_engine.connect() as target_conn:
        print(f"Connected to target {targetdb_name}")
        table_name = "users"
        table_exists = target_engine.dialect.has_table(target_conn, table_name)
        if not table_exists:
            print(f"Table '{table_name}' does not exist. Creating and loading data...")
            newdf.to_sql(table_name, target_conn, index=False, if_exists='replace')
            print(f"Created table '{table_name}' and inserted {len(newdf)} rows.")
        else:
            print(f"Table '{table_name}' exists. Removing rows with same IDs...")
            ids_to_delete = newdf["id"].tolist()
            if ids_to_delete:
                # Manually build the IN clause
                placeholders = ",".join([str(i) for i in ids_to_delete])
                delete_query = f"DELETE FROM {table_name} WHERE id IN ({placeholders})"
                target_conn.execute(text(delete_query))
                target_conn.commit()
                print(f"Deleted existing rows with IDs: {ids_to_delete}")
            else:
                print("No IDs to delete.")
            print("Appending new data...")
            newdf.to_sql(table_name, target_conn, index=False, if_exists='append')
            print(f"Appended {len(newdf)} rows into '{table_name}'.")
except Exception as e:
    print(f"ETL Load Error: {str(e)}")
    raise