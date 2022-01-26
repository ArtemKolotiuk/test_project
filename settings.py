import os

#host = os.environ.get('HOST')
port = os.environ.get('PORT')

host = 'http://localhost'
#port = '5000'
root_url = f"{host}:{port}"
user_created = 201
status_ok = 200
user_created_invalid = 400
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
create_user_payload = {'username': 'new_user', 'email': 'test@mail.com', 'password': '123'}
url = f"{root_url}/users"
create_user_invalid_payload = {'email': 'invalid_test@mail.com', 'password': '1234'}


created = 201
updated = 201
success = 200
bad_request = 400
post_create_payload = {'title': 'a', 'text': 'b', 'author_id': 1}
url_posts = f"{root_url}/posts"
url_users = f"{root_url}/users"
post_create_invalid_payload = {'text': 'b', 'author_id': 1}
post_create_payload = {'title': 'a', 'text': 'b', 'author_id': 1}
url_posts_id = f"{root_url}/posts/{1}"