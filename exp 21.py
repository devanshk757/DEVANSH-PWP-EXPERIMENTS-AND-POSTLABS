import requests
# Define the API endpoint
# url = 'https://jsonplaceholder.typicode.com/posts'

# # Make a GET request
# response = requests.get(url)

# # Check the status code
# if response.status_code == 200:
#     # Parse JSON response
#     posts = response.json()
#     print("Fetched Posts:")
#     for post in posts[:5]:  # Print the first 5 posts
#         print(f"Title: {post['title']}")
# else:
#     print(f"Failed to retrieve posts. Status code: {response.status_code}")


# # Define the API endpoint
# url = 'https://jsonplaceholder.typicode.com/posts'

# # Define the data to send
# new_post = {
#     "title": "My New Post",
#     "body": "This is the content of my new post.",
#     "userId": 1
# }

# Make a POST request
# response = requests.post(url, json=new_post)

# Check the status code
# if response.status_code == 201:
#     # Parse JSON response
#     created_post = response.json()
#     print("Created Post:")
#     print(f"Title: {created_post['title']}")
#     print(f"Body: {created_post['body']}")
# else:
#     print(f"Failed to create post. Status code: {response.status_code}")



# import requests
# url = 'https://jsonplaceholder.typicode.com/posts/1000'  # Non-existent post
# response = requests.get(url)
# if response.status_code == 200:
#     post = response.json()
#     print("Fetched Post:", post)
# else:
#     print(f"Error: {response.status_code} - {response.reason}")


#-----------------------------------------------------------------POST-LAB-----------------------------------------------------------------

# class APIClient:
#     def __init__(self, base_url):
#         self.base_url = base_url

#     def get_posts(self):
#         url = f"{self.base_url}/posts"
#         response = requests.get(url)
#         return response.json() if response.status_code == 200 else None

#     def create_post(self, title, body, userId):
#         url = f"{self.base_url}/posts"
#         data = {"title": title, "body": body, "userId": userId}
#         response = requests.post(url, json=data)
#         return response.json() if response.status_code == 201 else None


# client = APIClient("https://jsonplaceholder.typicode.com")

# posts = client.get_posts()
# print(posts[:5])

# new_post = client.create_post("Demo Title", "Demo Body", 1)
# print(new_post)