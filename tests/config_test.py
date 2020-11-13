import unittest
from pyvdk.config import Config


class TestConfig(unittest.TestCase):
    def test_init(self):
        # Act
        Config()

        # Act
        config = Config(token='str')

        # Assert
        self.assertEqual(config.token, 'str')
    
    def test_from_any(self):
        # Arrange
        config = Config(token='foo', secret='bar')

        # Act
        config.from_args(token='foobar')

        # Assert
        self.assertEqual(config.token, 'foobar')
        self.assertEqual(config.secret, 'bar')
    
    def test_from_yaml(self):
        # Arrange
        config = Config()
        
        # Act
        config.from_yaml('tests/config_test.yaml')

        # Assert
        self.assertEqual(config.token, 'foo')
        self.assertEqual(config.v, 'bar')
        self.assertEqual(config.group_id, 0)
        self.assertEqual(config.confcode, 'foobar')
        self.assertEqual(config.secret, 'barfoo')
        self.assertTrue(isinstance(config.group_id, int))
        self.assertTrue(isinstance(config.v, float))

    def test_from_args(self):
        # Arrange
        config = Config()

        # Act
        config.from_args(
            token='foo',
            v=1.1,
            group_id=0,
            confcode='foobar',
            secret='barfoo'
        )

        # Assert
        self.assertEqual(config.token, 'foo')
        self.assertEqual(config.v, 1.1)
        self.assertEqual(config.group_id, 0)
        self.assertEqual(config.confcode, 'foobar')
        self.assertEqual(config.secret, 'barfoo')
        self.assertTrue(isinstance(config.group_id, int))
        self.assertTrue(isinstance(config.v, float))