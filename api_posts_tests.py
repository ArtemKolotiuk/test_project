import json
import random

import pytest
import requests
from settings import root_url, created, updated, success, bad_request, headers, url_posts, post_create_invalid_payload, \
    post_create_payload, url_posts_id


# Create post
def test_create_post():
    res = requests.post(url_posts, data=json.dumps(post_create_payload), headers=headers)
    status = res.status_code
    body = res.json()
    assert status == created
    assert body.get("title") == post_create_payload.get("title")
    assert body.get("text") == post_create_payload.get("text")
    assert body.get("author_id") == post_create_payload.get("author_id")
           

 # GET not existing posts
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
        update_post_resp = requests.put(post_url, headers=headers)
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
