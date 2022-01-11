import requests
import json
import random
import pytest
from settings import status_ok, invalid_create_user_payload, user_created_invalid

host = 'http://localhost'
port = '5000'
root_url = f"{host}:{port}"
created = 201
updated = 201
success = 200
bad_request = 400
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
post_create_payload = {'title': 'a', 'text': 'b', 'author_id': 1}
url_posts = f"{root_url}/posts"
url_users = f"{root_url}/users"
post_create_invalid_payload = {'text': 'b', 'author_id': 1}
post_create_payload = {'title': 'a', 'text': 'b', 'author_id': 1}
url_posts_id = f"{root_url}/posts/{1}"


def test_create_post():
    try:
        res = requests.post(url_posts, data=json.dumps(post_create_payload), headers=headers)
        status = res.status_code
        if status == created:
            try:
                body = res.json()
                if body.get("title") != post_create_payload.get("title"):
                    print(f"Wrong data in {body.get('title')}. Status code: {status}")
                elif body.get("text") != post_create_payload.get("text"):
                    print(f"Wrong data in {body.get('text')}. Status code: {status}")
                elif body.get("author_id") != post_create_payload.get("author_id"):
                    print(f"Wrong data-type in author_id: {body.get('author_id')} given. Status code: {status}")
                else:
                    print(f"Post created successfully!. Created data {body} Status code: {status}")
                return True
            except Exception:
                raise Exception(f"Exception with jsonifying content: {res.content}")
        else:
            print(f"Post creation has failed with wrong response status code: {status}")
    except Exception as e:
        raise Exception(f"Request to {url_posts} failed with exception: {e}")


def test_get_users():
    try:
        res = requests.get(url_users)
        status = res.status_code
        if status == status_ok:
            try:
                body = res.json()
                if type(body) == list:
                    print(f"Users extracted successfully. Status-code: {status}")
            except Exception as e:
                raise Exception(f"Failed with  {res.content}")
    except Exception as e:
        raise Exception(f"Request to {url_users} failed with exception: {e}")


def test_update_user():
    res = requests.get(url_users)

    users = res.json()
    if users:
        random_user = random.choice(users)
        current_username = random_user.get("username")
        random_user_id = random_user.get("id")
        random_user_url = f"{url_users}/{random_user_id}"

        updated_user_payload = random_user.copy()

        updated_username = ''.join(random.sample(current_username, len(current_username)))
        updated_user_payload["username"] = updated_username

        res = requests.put(random_user_url, data=json.dumps(updated_user_payload), headers=headers)
        updated_user = res.json()
        if updated_user != random_user:
            print(f"User {random_user} updated successfully to {updated_user}.")
        else:
            print(f"User updating failed, {updated_user} equals {random_user}.")
    else:
        print(f"Response body is empty, details: {users}")


def test_create_user_invalid_data():
    try:
        res = requests.post(url_users, data=json.dumps(invalid_create_user_payload), headers=headers)
        status = res.status_code
        if status == user_created_invalid:
            try:
                body = res.json()
                message = body.get("error_message")
                if message:
                    print(
                        f"User wasn't created, cause invalid input data with status-code: {status} \n and error_message: {message}")
            except Exception as e:
                raise Exception(f"Failed with exception {e}")
        else:
            print(f"ERROR: User created with invalid data. With status-code {status}")
    except Exception as e:
        raise Exception(f"Request to {url_users} failed with exception: {e}")


def generate_not_exists_post_id(posts_ids):
    random_id = posts_ids[0]
    while random_id in posts_ids:
        random_id = random.randint(posts_ids[-1] + 1, posts_ids[-1] + 50)
    return random_id

    url = f"{root_url}/posts"

    # GET posts
def test_get_posts_check_by_status():
    res = requests.get(url_posts)
    assert res.status_code == success

# GET posts
def test_get_posts_check_by_body():
    res = requests.get(url_posts)
    body = res.json()
    assert type(body) is list

# POST posts
def test_create_post_check_by_status():
    res = requests.post(url_posts, data=json.dumps(post_create_payload), headers=headers)
    assert res.status_code == created

# POST posts
def test_create_post_check_by_body():
    res = requests.post(url_posts, data=json.dumps(post_create_payload), headers=headers)
    body = res.json()
    del body["id"]
    assert body == post_create_payload

# POST invalid posts
def test_create_invalid_post_check_by_status():
    res = requests.post(url_posts, data=json.dumps(post_create_invalid_payload), headers=headers)
    status = res.status_code
    assert status == bad_request

# GET post/id
def test_post_check_by_status():
    res = requests.get(url_posts_id)
    assert res.status_code == success

def test_get_post_check_by_body():
    """GET post/id"""
    resp = requests.get(url_posts)
    posts = resp.json()
    posts = []
    if posts:
        post_id = posts[0].get("id")
        post_url = (f"{url_posts}/{post_id}")
        res = requests.get(post_url)
        body = res.json()
        assert type(body) is dict
    else:
        pytest.skip("There're no posts.")

def test_update_post():
    resp = requests.get(url_posts)
    posts = resp.json()
    if posts:
        post_id = posts[0].get("id")
        post_url = f"{url_posts}/{post_id}"
        res = requests.get(post_url)
        post = res.json()
        updated_post = post.copy()

        current_title = post.get("title")
        updated_title = ''.join(random.sample(current_title, len(current_title)))
        updated_post["title"] = updated_title

        update_post_resp = requests.put(post_url, data=json.dumps(updated_post), headers=headers)

        assert update_post_resp.status_code == updated
        res = requests.get(post_url)
        post = res.json()
        assert post == updated_post
    else:
        pytest.skip("There're no posts.")

def test_update_post_with_invalid_data():
    resp = requests.get(url_posts)
    posts = resp.json()
    if posts:
        post_id = posts[0].get("id")
        post_url = f"{url_posts}/{post_id}"
        res = requests.get(post_url)
        post = res.json()
        updated_post = post.copy()

        current_title = post.get("title")
        updated_title = ''.join(random.sample(current_title, len(current_title)))
        updated_post["title"] = updated_title
        print(updated_post)
        del updated_post["author_id"]
        print(updated_post)
        update_post_resp = requests.put(post_url, data=json.dumps(updated_post), headers=headers)
        assert update_post_resp.status_code == bad_request

def test_update_post_with_invalid_id():
    post_resp = requests.get(url_posts)
    existing_posts = post_resp.json()

    existing_ids = []
    for post in existing_posts:
        post_id = post.get("id")
        existing_ids.append(post_id)

    invalid_post_id = generate_not_exists_post_id(existing_ids)

    resp = requests.get(url_posts)
    posts = resp.json()
    if posts:
        post_id = posts[0].get("id")
        post_url = f"{url_posts}/{post_id}"
        res = requests.get(post_url)
        post = res.json()
        updated_post = post.copy()

        current_title = post.get("title")
        updated_title = ''.join(random.sample(current_title, len(current_title)))
        updated_post["title"] = updated_title

        new_post_url = f"{url_posts}/{invalid_post_id}"

        update_post_resp = requests.put(new_post_url, data=json.dumps(updated_post), headers=headers)

        assert update_post_resp.status_code == bad_request

        res = requests.get(post_url)
        post = res.json()

        assert post != updated_post
    else:
        pytest.skip("There're no posts.")
