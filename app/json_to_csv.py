import requests
import json
import csv

def fetch_json_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching JSON data from API: {e}")
        return None

def get_csv_header(json_data):
    if isinstance(json_data, list) and json_data:
        return list(json_data[0].keys())
    elif isinstance(json_data, dict):
        return list(json_data.keys())
    else:
        return []

def write_csv_file(json_data, csv_file_path):
    header = get_csv_header(json_data)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)
        csv_writer.writeheader()

        if isinstance(json_data, list):
            for item in json_data:
                csv_writer.writerow(item)
        elif isinstance(json_data, dict):
            csv_writer.writerow(json_data)

def json_to_csv(api_url, csv_file_path):
    json_data = fetch_json_data(api_url)
    if json_data:
        write_csv_file(json_data, csv_file_path)

if __name__ == '__main__':
    # Example usage
    api_url = "https://api.example.com/data"
    csv_file_path = "output.csv"

    json_to_csv(api_url, csv_file_path)
