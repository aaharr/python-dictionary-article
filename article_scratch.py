import lavalamp

"""
Dictionary Creation
"""
my_dict = {'key1': 1, 'key2': 2}

my_dict = dict(key1=1, key2=2)

my_dict = {}

my_dict = dict()

my_dict['key'] = 123

# Define a dict with some string values and keys
my_dict = {
    'my_nested_dict':
        {
            'a_key': 'a_value',
            'another_key': 'another_value',
        }
}

my_variable = my_dict['my_nested_dict']

"""
Practical Use Cases
"""
bill = {'email': 'bill@gmail.com',
        'address': '123 Acme Dr.',
        'password': 'secret-password',
        'url': 'http://www.bill.com'}


def send_email(user_dict):
    pass


# smtp email logic …

send_email(bill['email'])  # bracket notation or …
send_email(bill.get('email'))  # .get() method is handy, too
