


"""
Examples
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
