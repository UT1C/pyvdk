# Вызов методов API

## import

Существует два класса для вызовов методов апи

`ABCAPI` не содержит в себе категорий, и соответственно без подсказок
```python
from pyvdk.api import ABCAPI
```

экземпляр `API` же будет подсказывать имя метода и аргументов
```python
from pyvdk.api import API
```

## Создание экземпляра

Для `ABCAPI`/`API` требуется экземпляр [Config](api_reference.md)
```python
api = ABCAPI(config)
# или же
api = API(config)
```

## ABCAPI

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

```python
# https://vk.com/dev/messages.send
r = api.messages.send(
    message="Сервера сегодня не будет",
    domain="lightmanlp",
    random_id=random.getrandbits(64)
)
```

Так же API имеет тот же `ABCAPI.method`.
