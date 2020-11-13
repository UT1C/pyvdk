import unittest
from pyvdk.rules import (
    MessageTextRule,
    MessageRegexRule,
    MessageVBMLRule
)


class TestRules(unittest.TestCase):
    def test_message_text_rule(self):
        # Arrange
        rule = MessageTextRule('/test')

        # Act
        rule.check()