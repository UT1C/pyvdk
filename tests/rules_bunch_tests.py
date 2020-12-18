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
        bunch1 = TextRule('foo') | TextRule('Foo', lower=False)
        bunch2 = (TextRule('foo', lower=False) & TextRule('foo')) | TextRule('bar')

        # Act
        act1 = [
            bunch1.check(i)
            for i in self.mes
        ]
        act2 = [
            bunch2.check(i)
            for i in self.mes
        ]

        # Assert
        self.assertTrue(act1[0])
        self.assertTrue(act1[1])
        self.assertFalse(act1[2])
        self.assertFalse(act2[0])
        self.assertTrue(act2[1])
        self.assertTrue(act2[2])

    def test_all_operations_check(self):
        # Arrange
        rule = TextRule("Foo", lower=False)
        bunch = rule & ((rule != rule) | (rule == rule)) ^ ~rule
        mes = self.mes[0]

        # Act
        result = bunch.check(mes)

        # Assert
        self.assertTrue(result)