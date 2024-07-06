import smtplib
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from time import sleep

from environs import Env

from src.cfg.config import debug_logger
from src.utils.cleaner import get_list_addresses

env = Env()
env.read_env()


# Параметры SMTP сервера Google
smtp_server = env('SMTP_SERVER')
smtp_port = env('SMTP_PORT')  # SSL порт
sender_email = env("SENDER_EMAIL")
password = env("SENDER_PASSWORD")

try:
    with open('src/data/to_send.eml', 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
except Exception as e:
    debug_logger(f"Ошибка при чтении файла .eml: {e}")


def sender_emails(list_addresses: list):
    with smtplib.SMTP_SSL(host=smtp_server, port=smtp_port) as smtp:
        for address in list_addresses:
            message = EmailMessage()
            message['Subject'] = 'Доброе слово для кошки'
            message['From'] = sender_email
            message['To'] = address
            message.set_content(msg)
            try:
                smtp.login(user=sender_email, password=password)
                smtp.send_message(message)
                sleep(0.5)
            except Exception as e:
                debug_logger(f'Ошибка при отправке письма: {e}')


if __name__ == '__main__':
    list_addresses = get_list_addresses()
    sender_emails(list_addresses=list_addresses)
