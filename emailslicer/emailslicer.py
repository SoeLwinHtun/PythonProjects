import re

# simple program that take the input for of an email and seperate them into username and domain. This kind of email slicing will be necessary in web apps with login system.

def is_email(email):
	# regular expression pattern for email form of inputs

	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

	if re.match(pattern,email):
		return True
	else:
		return False

while True:
	email = input("Enter email, or enter 'exit' to exit : ")

	if email.lower() == "exit":
		break

	if is_email(email):
		
		username = email[:email.index("@")]
		domain_name = email[email.index("@")+1:]
		format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
		print(format_)

		break
	else:
		print('Enter a valid email address.')