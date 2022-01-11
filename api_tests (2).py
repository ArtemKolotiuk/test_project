
import requests
import json
import random
from settings import headers, create_user_payload, create_user_invalid_payload, root_url
import pytest

get_user_expected_status = 200
create_user_expected_status = 201
update_user_expected_status = 201
create_user_fail_status = 400
update_user_fail_status = 400
users_url = f"{root_url}/users"


def test_create_user():
	res = requests.post(users_url, data=json.dumps(create_user_payload), headers=headers)
	body = res.json()
	del body["id"]
	assert res.status_code == create_user_expected_status
	assert body == create_user_payload

def test_create_user_invalid_data():
	res = requests.post(users_url, data=json.dumps(create_user_invalid_payload), headers=headers)
	assert res.status_code == create_user_fail_status


def test_get_users():
	res = requests.get(users_url)
	body = res.json()
	assert res.status_code == get_user_expected_status
	assert type(body) is list
		

# def test_with_errors_in_code(self):
# 	res = requests.get(self.users_url)
# 	body = res.json()
# 	# нет self.
# 	assertTrue(type(body) is list)


@pytest.mark.skip(reason="This test skipped")
def test_with_errors_in_code_skipped():
	res = requests.get(users_url)
	body = res.json()
	assert type(body) is list


@pytest.mark.skipif(env == "dev", "skip for DEV-env")
def test_update_user():
	users_url = f"{root_url}/users"
	users = requests.get(users_url).json()
	if users:
		user = random.choice(users)
	else:
		logger.error(f"Users is empty: {users}")
		return False

	current_username = user.get("username")
	updated_username =  ''.join(random.sample(current_username,len(current_username)))
	user["username"] = updated_username
			
	user_id = user.get("id")
	user_url = f"{users_url}/{user_id}"
	update_user_res = requests.put(user_url, data=json.dumps(user), headers=headers)
	res = requests.get(user_url)
	body = res.json()

	assert body == user
	assert update_user_res.status_code == update_user_expected_status




def test_update_user_invalid_data():
	users_url = f"{root_url}/users"
	users = requests.get(users_url).json()
	if users:
		user = random.choice(users)
	else:
		logger.error(f"Users is empty: {users}")
		return False


	user["email"] = "invalid_email"			
	user_id = user.get("id")
	user_url = f"{users_url}/{user_id}"
	update_user_res = requests.put(user_url, data=json.dumps(user), headers=headers)

	assert update_user_res.status_code == update_user_fail_status

def raise_exception():
	raise Exception


def test_catch_exception():
	assert Exception == raise_exception



def test_catch_exception():
	res = requests.get(root_url)
	if res.status_code != 200:
		pytest.skip("external resource not available")


@pytest.mark.xfail
def test_endpoint_not_exist():
	res = requests.get(root_url)
	assert res.status_code == 200


