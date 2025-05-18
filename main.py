import os
import requests
import json
import sys


# Get the input
repo_url = os.environ.get("REPO_URL")
ref_name = os.environ.get("REF_NAME")
api_token = os.environ.get("API_TOKEN")
timestamp = os.environ.get("TIMESTAMP")
stage = os.environ.get("STAGE")
services = os.environ.get("SERVICES")
api_endpoint = "https://public-api.linearb.io/api/v1/deployments"

# Validate inputs
if not (repo_url.startswith("https://") and repo_url.endswith(".git")):
    raise ValueError(f"Invalid repo URL format: {repo_url}. Must start with 'https://' and end with '.git'")

# Set up headers with API token
headers = {
    "x-api-key": api_token,
    "Content-Type": "application/json"
}

# Prepare payload
payload = {
    "repo_url": repo_url,
    "ref_name": ref_name
}

# Add optional parameters
if timestamp is not None and timestamp != "":
    payload["timestamp"] = timestamp
if stage is not None and stage != "":
    payload["stage"] = stage
if services is not None and services != "":
    payload["services"] = services.split(",")

# Print payload before sending
print(f"Sending payload: {json.dumps(payload, indent=2)}")

# Send POST request
response = requests.post(api_endpoint, headers=headers, json=payload)

# Print response details
print(f"Response status code: {response.status_code}")
print(f"Response body: {json.dumps(response.json(), indent=2)}")
sys.stdout.flush()  # Flush the print buffer before handling the response

# Handle response
response.raise_for_status()
