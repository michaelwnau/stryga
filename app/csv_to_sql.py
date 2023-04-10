import csv
import psycopg2

'''
Replace your_database_name, your_user, your_password, your_host, 
your_port, and your_table_name with your actual PostgreSQL connection 
details and desired table name.
'''

def connect_to_db(database, user, password, host, port):
    try:
        connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()

def create_table(connection, table_name, columns):
    cursor = connection.cursor()
    column_definitions = ', '.join([f"{name} {type}" for name, type in columns.items()])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"

    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(f"Error creating table {table_name}: {e}")

def insert_data(connection, table_name, row_data, columns):
    cursor = connection.cursor()
    placeholders = ', '.join(['%s'] * len(columns))
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders});"

    try:
        cursor.execute(query, row_data)
        connection.commit()
    except Exception as e:
        print(f"Error inserting data into {table_name}: {e}")

def parse_column_types(header, rows):
    columns = {}
    for col_name in header:
        col_type = "TEXT"
        for row in rows:
            try:
                float(row[col_name])
                col_type = "FLOAT"
            except ValueError:
                pass
            columns[col_name] = col_type
    return columns

def csv_to_sql(csv_file_path, database, user, password, host, port, table_name):
    connection = connect_to_db(database, user, password, host, port)

    if connection:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            header = csv_reader.fieldnames
            rows = [row for row in csv_reader]

        columns = parse_column_types(header, rows)
        create_table(connection, table_name, columns)

        for row in rows:
            insert_data(connection, table_name, [row[col] for col in header], header)

        close_connection(connection)

if __name__ == '__main__':
    # Example usage
    csv_file_path = "input.csv"
    database = "your_database_name"
    user = "your_user"
    password = "your_password"
    host = "your_host"
    port = "your_port"
    table_name = "your_table_name"

    csv_to_sql(csv_file_path, database, user, password, host, port, table_name)
