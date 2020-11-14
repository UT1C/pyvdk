from copy import deepcopy
from unittest import TestCase, mock
import os

from pyvdk.config import Config


class ConfigTests(TestCase):
    def setUp(self):
        self.config = Config(
            token='bar',
            v=1.103,
            group_id=0,
            confcode='foobar',
            secret='barfoo'
        )
    
    def config_assert(self, config: Config):
        self.assertEqual(config.token, 'foo')
        self.assertEqual(config.v, 1.103)
        self.assertEqual(config.group_id, 0)
        self.assertEqual(config.confcode, 'foobar')
        self.assertEqual(config.secret, 'barfoo')
        self.assertTrue(isinstance(config.group_id, int))
        self.assertTrue(isinstance(config.v, float))
    
    def test_from_yaml(self):
        # Arrange
        config = Config.from_yaml('tests/config_test.yaml')

        # Assert
        self.config_assert(config)
    
    @mock.patch.dict(
        os.environ,
        {
            "PYVDK_TOKEN": "foo",
            "PYVDK_GROUP_ID": "0",
            "PYVDK_CONFIRMATION_CODE": "foobar",
            "PYVDK_SECRET": "barfoo",
            "PYVDK_API_VERSION": "1.103"
        }
    )
    def test_from_environ(self):
        # Arrange
        config = Config.from_environ()

        # Asssert
        self.config_assert(config)

    def test_edit_from_args(self):
        # Arrange
        config = deepcopy(self.config)

        # Act
        config.edit_from_args(token='foo')

        # Assert
        self.config_assert(config)