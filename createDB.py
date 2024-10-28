import sqlite3

# Connect to the SQLite database (creates one if not exists)
conn = sqlite3.connect('reactor_data.db')
cursor = conn.cursor()

# Function to create tables with specific columns for each measurement type
def create_table(table_name, thickness_type):
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_id TEXT,
        property_name TEXT,
        database_type TEXT,
        reactor_type TEXT,
        reactor_name TEXT,
        Year TEXT,
        HOY TEXT,
        Length TEXT,
        Entry_by TEXT,
        Entry_Date TEXT,
        Remark TEXT,
    """
    
    # Add columns for each cell up to Cell 100 with Position and specified thickness/diameter type
    for i in range(1, 101):
        create_table_sql += f"    Cell{i}_Position_mm REAL,\n"
        create_table_sql += f"    Cell{i}_{thickness_type}_mm REAL,\n"

    # Remove the last comma and close the SQL statement
    create_table_sql = create_table_sql.rstrip(",\n") + "\n);"
    
    # Execute the create table command
    cursor.execute(create_table_sql)
    print(f"Table '{table_name}' created successfully.")

# Create tables with the specified thickness/diameter type
create_table("reactor_data_min_thickness", "Min_Thickness")
create_table("reactor_data_max_thickness", "Max_Thickness")
create_table("reactor_data_min_inner_diameter", "Min_Inner_Diameter")
create_table("reactor_data_max_inner_diameter", "Max_Inner_Diameter")
create_table("reactor_data_avg_outside_diameter", "Avg_Outside_Diameter")

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("All tables created successfully in the reactor_data.db database.")
