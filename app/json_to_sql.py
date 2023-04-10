import json
import psycopg2

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

def insert_data(connection, table_name, data):
    cursor = connection.cursor()
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

    try:
        cursor.execute(query, list(data.values()))
        connection.commit()
    except Exception as e:
        print(f"Error inserting data into {table_name}: {e}")

def json_to_sql(json_data, database, user, password, host, port, table_name):
    connection = connect_to_db(database, user, password, host, port)

    if connection:
        json_object = json.loads(json_data)
        if isinstance(json_object, list):
            for item in json_object:
                create_table(connection, table_name, item)
                insert_data(connection, table_name, item)
        else:
            create_table(connection, table_name, json_object)
            insert_data(connection, table_name, json_object)

        close_connection(connection)

if __name__ == '__main__':
    # Example usage
    json_data = '''
    [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 22}
    ]
    '''

    database = "your_database_name"
    user = "your_user"
    password = "your_password"
    host = "your_host"
    port = "your_port"
    table_name = "your_table_name"

    json_to_sql(json_data, database, user, password, host, port, table_name)
