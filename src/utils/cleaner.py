import re

from email.utils import parseaddr


def clean_email(email: str) -> str:
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    is_valid = email_regex.fullmatch(email)
    parsed_email = parseaddr(email)[1]
    if is_valid is not None and parsed_email == email:
        return email


def validate_subdomain(email: str) -> str:
    # Регулярное выражение, распознающее поддомены
    subdomain_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.\w+$")

    is_valid_with_subdomain = subdomain_email_regex.fullmatch(email)
    if is_valid_with_subdomain is not None:
        return email


def get_list_addresses():
    with (open('src/data/emails.txt', 'r') as f,
          open('src/data/new_emails.txt', 'w') as f_new):
        input_list = set(f.read().splitlines())
        clean_list = [clean_email(item) for item in input_list]
        [clean_list.append(validate_subdomain(item)) for item in input_list]
        unique_list = set(clean_list)
        for i in unique_list:
            f_new.write(f'{i}\n')
    return unique_list
