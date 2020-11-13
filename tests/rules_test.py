from typing import Tuple
import re
import unittest

from pyvdk.rules import (
    MessageTextRule,
    MessageRegexRule,
    MessageVBMLRule,
    ABCRule
)
from pyvdk.types import Message


def construct_output(
    rules: Tuple[ABCRule],
    msgs: Tuple[Message]
) -> list:

    o = list()
    
    for rule in rules:
        for msg in msgs:
            o.appened(rule.check(msg))
    
    return o


class TestRules(unittest.TestCase):
    def test_message_text_rule(self):
        # Arrange
        rules = (
            MessageTextRule('/foo'),
            MessageTextRule('/foo', lower=False)
        )
        msgs = (
            Message(text='/Foo'),
            Message(text='/foo'),
            Message(text='/bar')
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
    
    #def test_message_regex_rule(self):
    #    # Arrange
    #    rules = (
    #        MessageRegexRule(r'/[]')
    #    )