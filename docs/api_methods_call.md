# Вызов методов API

[TOC]

## Создание экземпляра { #create-instance }
Для `RawAPI`/`API` требуется экземпляр [Config](api_reference#config).
```python
from pyvdk.api import RawAPI, API


api = RawAPI(config)
# или же
api = API(config)
```

## RawAPI

`RawAPI` не содержит в себе категорий, и соответственно без подсказок.

```python
# вызываем https://vk.com/dev/users.get
r = api.method("users.get", user_ids=[1])["response"][0]

assert f"{r['first_name']} {r['last_name']}" == "Павел Дуров"


# https://vk.com/dev/utils.getServerTime
r = api.method("utils.getServerTime")["response"]

print("server:", r)
print("local time:", time.time())
```

## API

Класс `API` наследуется от `RawAPI`, а значит все методы `RawAPI` доступны.
Экземпляр `API` имеет аннотации категорий, методов, и их аргументов.

```python
# https://vk.com/dev/messages.send
r = api.messages.send(
    message="Сервера сегодня не будет",
    domain="lightmanlp",
    random_id=random.getrandbits(64)
)
```
