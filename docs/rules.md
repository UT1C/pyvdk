# Правила

[TOC]

## Основная информация { #main }
Правила - инструмент для задания условий выполнения хендлера. Все правила находятся в модуле `pyvdk.rules`.
<br>Пример создания правила:

```python
from pyvdk.rules import TextRule


TextRule('Foo', lower=False)
```
Полный список правил можно найти [здесь](api_reference.md#rules).

Так же разные правила можно совмещать, используя побитовые операции. При этом образуется [`RulesBunch`](rules.md#bunch).

```python
bunch = rule1 & rule2 | rule3
```
Побитовые операторы, доступные для работы с правилами на данный момент: `&`, `|`.

## RulesBunch { #bunch }
Сам по себе `RulesBunch` является сгруппированным пучком правил. Его можно применять как обычное правило или как декоратор. Условием выполнения хендлера становятся выполнение условий, указанных при лейблинге, и условий банча.

```python
from pyvdk.rules import RulesBunch

...
bunch = RulesBunch(rule1, rule2, alternative_rule=rule3)  # эквивалент rule1 & rule2 | rule3
...

@bot.on.message_new(bunch, text="foo")
def handler1(msg):
    ...


@bot.on.message_new(text="bar")
@bunch
def handler2(msg):
    ...
```

Причем декорировать им можно не только функции, но и классы.

```python
@bunch
class Foo:
    @bot.on.message_new()
    def handler3(msg):
        ...

    @bot.on.message_new(text="foobar")
    def _handler4(msg):
        ...
```

!!! tip
    При декорировании класса банчем, все хендлеры, название которых начинается с `_`, игнорируются.