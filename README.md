# Обрезка ссылок с помощью Битли
Скрипт сделан для создания `битлинков`, а также для подсчёта количества кликов по ним.

Битлинки - это обрезанные ссылки, которые перенаправляют на определённый сайт.
### Пример
`https://bit.ly/3BIc8M9` - этот битлинк ведёт на сайт [google.ru](https://www.google.com/).

## Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

    pip install -r requirements.txt

Для того, чтобы пользоваться сервисом необходим токен от [bit.ly](https://app.bitly.com/).

Далее нужно создать файл `.env` в папке скрипта. Его содержимое должно выглядеть так:

    BITLINK_TOKEN=23nhiusd8983nfkdjs454jdufru784


Для применения токена в скрипте необходимо использовать функцию `os.environ`:
```python
def main():
    token = os.environ["BITLINK_TOKEN"]
```

## Использование
Теперь вы можете использовать этот сервис для создания битлинков,
а также для подсчёта кликов по нему.

При запуске скрипта передайте ему аргумент - ссылку для сокращения или битлинк.

### Примеры успешного запуска скрипта

### №1
    C:\Users\hp\bitly>main.py https://app.bitly.com/
    Битлинк https://bitly.is/35QVu32

    C:\Users\hp\bitly>
В примере был запущен `main.py` с аргументом `https://app.bitly.com/` - ссылкой для сокращения.

### №2
    C:\Users\hp\bitly>main.py https://bitly.is/35QVu32
    Колличество перехождений по ссылке 0

    C:\Users\hp\bitly>
В примере был запущен `main.py` с аргументом `https://bitly.is/35QVu32` - битлинком для подсчёта кликов по нему.