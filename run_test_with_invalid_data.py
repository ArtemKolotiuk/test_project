from api_posts_tests import test_create_post
s1 = 'test_create_post'
s2 = 'test_get_users'
s3 = 'test_update_user'
s4 = 'test_create_user_invalid_data'

if __name__ == '__main__':
	print(s1.upper(),'\n')
	test_create_post()
	print()

	#print(s2.upper())
	#test_get_users()
	#print()

	#print(s3.upper())
	#test_update_user()
	#print()
	
	#print(s4.upper())
	#test_create_user_invalid_data()