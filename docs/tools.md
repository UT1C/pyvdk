# Инструменты

[TOC]

Модуль `tools` содержит вспомогательные инструменты для генерации таких объектов, как клавиатура.

## Клавиатура (Keyboard) { #keyboard }
С pyvdk можно легко создать клавиатуру.
<br>Сперва импортируем класс `Keyboard` и нужные виды кнопок, создаем объект клавиатуры.

```python
from pyvdk.tools import Keyboard, TextButton


kb = Keyboard(one_time=True)
```

Теперь создадим и добавим кнопки.
Полный список кнопок можно найти [здесь](api_reference.md#buttons).

```python
b1 = TextButton(
    color=kb.BLUE,
    label="text1",
    payload="button1"
)
b2 = TextButton(
    color=kb.B,
    label="text2",
    payload="button2"
)

kb.append(b2)
kb.appendleft(b1)
```

Данные о клавиатуре хранятся в виде *collections.deque*, так что нам доступны `appendleft` и `extendleft`.

!!! danger
    Всвязи с принципом работы *deque*, если привысить лимит кнопок в строке, то лишние будут автоматически удалены без предупреждения. Подробнее [здесь](https://docs.python.org/3/library/collections.html#collections.deque).

В классе `Keyboard` присутствуют константы цветов. Информацию о них можно найти [здесь](api_reference.md#color-data).
<br>Если указать параметр `payload` строкой, то он будет автоматически обернут в *dict* по формату `{"command": payload}`.

!!! hint
    Цвет кнопки можно так же указать строкой. Его можно указать сокращенно или полностью.
    <br>`color="w"`
    <br>`color="white"`

!!! note
    Константы цветов так же доступны из класса кнопки.
    <br>`TextButton.RED`

Кнопки можно добавлять в определенную строку через `keyboard[row: int]`. Строки нумеруются сверху вниз, от 0 до текущего лимита. Пустые строки автоматически удаляются из клавиатуры.

```python
row = (
    TextButton(
        color=kb.PRIMARY,
        label="text3",
        payload={"button": "1"}
    ),
    TextButton(
        color=kb.RED,
        label="text4",
        payload={"button": "2"}
    )
)

kb[1].extend(row)
```

!!! note
    Для добавления кнопок так же можно просто указать параметр `row` у данных методов.
    <br>`kb.append(button, row=3)`

Теперь мы можем отправить объект клавиатуры.

```python
msg(..., keyboard=kb)
```

Если же вам понадобится клавиатура в формате json, то просто вызовите объект.
```python
json_keyboard = kb()
```

## Упоминание (Mention) { #mention }

Для поиска упоминаний в тексте сообщения можно использовать класс `Mention`

```python
from pyvdk.tools import Mention

def handler(msg: Message):
    mention = Mention.find(msg.text)
    if mention is not None:
        if mention.user:
            print(f"mentioned user vk.com/id{mention.id}")
        elif mention.club:
            print(f"mentioned club vk.com/club{mention.id}")
```

Можно так же и создавать упоминания

```python
def handler(msg: Message):
    msg(f"{Mention(204697425, text="@макс")}, сервера сегодня не будет")
```

(хотя вручную выходит чуть короче)
