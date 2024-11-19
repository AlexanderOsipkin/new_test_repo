import requests
import random
import string


def generate_temp_email():
    #Генерирует случайный временный email
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "1secmail.com"
    return username, f"{username}@{domain}"


def get_messages(username, domain):
    #Получает список сообщений для временного email
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Возвращает список сообщений
    return []


def read_message(username, domain, message_id):
    #Читает содержимое конкретного сообщения
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Возвращает данные сообщения
    return {}


# Генерация временного email
username, temp_email = generate_temp_email()
print(f"Ваш временный email: {temp_email}")

# Проверка сообщений
print("Ожидаем входящих сообщений...")
messages = get_messages(username, "1secmail.com")
if messages:
    print("Сообщения получены!")
    for message in messages:
        print(f"ID: {message['id']}, От: {message['from']}, Тема: {message['subject']}")
        # Чтение сообщения
        content = read_message(username, "1secmail.com", message['id'])
        print(f"Содержимое сообщения:\n{content}")
else:
    print("Почтовый ящик пока пуст.")
