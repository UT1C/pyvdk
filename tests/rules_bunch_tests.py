import unittest
from pyvdk.vk_api import ABCAPI
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
            api=self
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