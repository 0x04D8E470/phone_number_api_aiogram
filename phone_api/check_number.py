import requests
import time
import json
from config import NumberOnline, NumberOffline, ErrorMessage

def check_number(number):
    try:
        ts = time.time() # получаем время в ts, чтобы передать в запрос
        check = requests.get(f"https://vak-sms.com/api/check_sms/?tel={number}&ts={int(ts)}") # Отправляем запрос со всем содержимым
        response = check.text
        status = json.loads(check.text) # Получаем ответ и обрабатываем его как json
        if status['status_tel'] == True:
            return NumberOnline
        elif status['status_tel'] == False:
            return NumberOffline
    except:
        print("Произошла ошибка в запросе!")
        return ErrorMessage