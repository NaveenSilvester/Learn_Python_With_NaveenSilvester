print ("####################################################################################################")
import requests

# URL to GitHub issues API
url = "https://api.github.com/repos/NaveenSilvester/Learn_Python_With_NaveenSilvester/issues"

# Sending a GET request to fetch issues
response = requests.get(url)

# Checking the status and printing the result
if response.status_code == 200:
    issues = response.json()
    for issue in issues:
        print(f"Issue Title: {issue['title']}")
        print(f"Issue URL: {issue['html_url']}\n")
else:
    print(f"Failed to fetch issues. HTTP Status Code: {response.status_code}")