import requests
url = "https://api.example.com/graphql"
query = """
{
    user(id: 1) {
        name
        email
        posts {
            title
        }
    }
}
"""
response = requests.post(url, json={"query": query})
if response.status_code == 200:
    print(response.json())  # Print the user data
