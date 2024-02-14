import requests
import sys

def test_error_cases(base_url):
    print("\n--- Testing error cases ---")

    # Test GET with no keys
    print("\nGET request with no keys passed...")
    response = requests.get(f"{base_url}/app/v2/values/?keys=")
    print(f"Response code: {response.status_code}")
    print("Response body:", response.json())

    # Test POST with no data
    print("\nPOST request with no data passed...")
    response = requests.post(f"{base_url}/app/v2/values/", json={})
    print(f"Response code: {response.status_code}")
    print("Response body:", response.json())

    # Test PATCH with no data
    print("\nPATCH request with no data passed...")
    response = requests.patch(f"{base_url}/app/v2/values/", json={})
    print(f"Response code: {response.status_code}")
    print("Response body:", response.json())

def post_values(base_url):
    print("\n--- Posting new values ---")
    values = [
        {"id": 1, "type": "dog", "name": "cash"},
        {"id": 2, "type": "cat", "name": "kitty"},
        {"id": 3, "type": "bird", "name": "bird"}
    ]

    keys = []
    for value in values:
        payload = {"value": value}
        print(f"\nAbout to POST this payload: {payload}")
        response = requests.post(f"{base_url}/app/v2/values/", json=payload)

        if response.status_code == 201:  # Correct interpretation of 201 status
            print("POST successful.")
            response_data = response.json()
            print(f"Response: {response_data}")
            key = response_data.get('key')
            print(f"Received key: {key} for posted value.")
            keys.append(key)
        else:
            print(f"POST encountered an issue with status code: {response.status_code}")
            print("Response:", response.json())

    return keys

def get_values(base_url, keys):
    if not keys:
        print("\nNo keys available to perform GET request.")
        return

    print(f"\n--- Getting values for keys: {keys} ---")
    response = requests.get(f"{base_url}/app/v2/values/?keys={','.join(keys)}")
    print(f"Response code: {response.status_code}")
    print("Response body:", response.json())

def patch_values(base_url, keys):
    if not keys:
        print("\nNo keys available to perform PATCH request.")
        return

    print("\n--- Patching values ---")
    updates = [
        {"value": {"id": 1, "name": "good cash"}},
        {"value": {"id": 2, "type": "kitty-cat"}},
        {"value": {"id": 3, "type": "parrot", "name": "good bird"}}
    ]

    for key, update in zip(keys, updates):
        print(f"\nAbout to PATCH key: {key} with new value: {update}")
        response = requests.patch(f"{base_url}/app/v2/values/", json={key: update['value']})
        print(f"Response code: {response.status_code}")
        print("Response body:", response.json())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nError: No base URL provided.")
        print("Usage: python script_name.py http://0.0.0.0:8080")
        sys.exit(1)

    base_url = sys.argv[1]

    print(f"\nBase URL for testing: {base_url}")

    # Execute test scenarios
    test_error_cases(base_url)
    keys = post_values(base_url)
    get_values(base_url, keys)
    patch_values(base_url, keys)
    # Retrieve and display values after patching to verify updates
    get_values(base_url, keys)
