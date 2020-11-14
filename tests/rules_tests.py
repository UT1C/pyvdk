from typing import Tuple
import re
import unittest

from pyvdk.rules import (
    TextRule,
    RegexRule,
    VBMLRule,
    ABCRule
)
from pyvdk.vk_api import ABCAPI
from pyvdk.types import Message


class FakeAPI(ABCAPI):
    pass


def construct_output(
    rules: Tuple[ABCRule],
    msgs: Tuple[Message]
) -> list:

    o = list()
    
    for rule in rules:
        for msg in msgs:
            o.append(rule.check(msg))
    
    return o


def message_gen(text: str) -> Message:
    return Message(
        text=text,
        date=1,
        from_id=1,
        id=1,
        out=1,
        peer_id=1,
        api=fake_api
    )


fake_api = FakeAPI(0)


class RulesTests(unittest.TestCase):
    def test_message_text_rule(self):
        # Arrange
        rules = (
            TextRule('/foo'),
            TextRule('/foo', lower=False)
        )
        msgs = (
            message_gen('/Foo'),
            message_gen('/foo'),
            message_gen('/bar')
        )

        # Act
        o = construct_output(rules, msgs)

        # Assert
        self.assertTrue(o[0])
        self.assertTrue(o[1])
        self.assertFalse(o[2])

        self.assertFalse(o[3])
        self.assertTrue(o[4])
        self.assertFalse(o[5])
    
    def test_message_regex_rule(self):
        # Arrange
        rules = (
            RegexRule(r'foobar\d'),
            RegexRule(re.compile(r'foobar\d'), fullmatch=True)
        )
        msgs = (
            message_gen('foobar1'),
            message_gen('barfoo1'),
            message_gen('foo foobar2 bar')
        )

        # Act
        o = construct_output(rules, msgs)
        args = list()
        o[2].add_to(args)

        # Assert
        self.assertTrue(o[0])
        self.assertFalse(o[1])
        self.assertTrue(o[2])

        self.assertTrue(o[3])
        self.assertFalse(o[4])
        self.assertFalse(o[5])