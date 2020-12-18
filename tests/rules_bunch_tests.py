import unittest
from pyvdk.api import ABCAPI
from pyvdk.types import Message
from pyvdk.rules import (
    RulesBunch,
    TextRule
)


class FakeAPI(ABCAPI):
    def message_gen(self, text: str) -> Message:
        return Message(
            text=text,
            date=1,
            from_id=1,
            id=1,
            out=1,
            peer_id=1,
            api=self,
            raw_data={'foo': 'bar'}
        )


fapi = FakeAPI(0)


class RulesBunchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mes = [
            fapi.message_gen(text=i)
            for i in ('Foo', 'foo', 'bar')
        ]

    def test_generate_from_rules(self):
        # Arrange
        bunch = (TextRule('foo', lower=False) & TextRule('foo')) | TextRule('bar')

        # Act
        act = [
            bunch.check(i)
            for i in self.mes
        ]

        # Assert
        self.assertFalse(act[0])
        self.assertTrue(act[1])
        self.assertTrue(act[2])

    def test_bunch(self):
        # Arrange
        bunch = RulesBunch(
            TextRule('foo'),
            alternative_rule=TextRule('Foo', lower=False)
        )

        # Act
        act = [
            bunch.check(i)
            for i in self.mes
        ]

        # Assert
        self.assertTrue(act[0])
        self.assertTrue(act[1])
        self.assertFalse(act[2])

    def test_all_operations_check(self):
        # Arrange
        rule = TextRule("Foo", lower=False)
        bunch = rule & ((rule != rule) | (rule == rule))
        mes = self.mes[0]

        # Act
        bunch.check(mes)