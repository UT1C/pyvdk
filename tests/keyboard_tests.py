import unittest
import json
from pyvdk.tools import Keyboard, KeyboardButton


class KeyboardTests(unittest.TestCase):
    def test_limit(self):
        # Arrange
        keyboard = Keyboard(inline=True)
        b = [
            KeyboardButton(
                color='w',
                action=KeyboardButton.text(str(i)),
                payload=str(i)
            )
            for i in range(6)
        ]
        
        # Assert
        with self.assertRaises(Exception):
            keyboard.extend(b)
            keyboard[1].extend(b)
        
        with self.assertRaises(Exception):
            keyboard.extend(b)
    
    def test_structure(self):
        # Arrange
        keyboard = Keyboard(one_time=True)
        b = [
            KeyboardButton(
                color='w',
                action=KeyboardButton.text(str(i + 1)),
                payload=str(i + 1)
            )
            for i in range(3)
        ]
        keyboard.extend(b[:2])
        keyboard[2].append(b[2])

        # Act
        data = json.loads(keyboard())

        # Assert
        self.assertTrue(data['one_time'])
        self.assertFalse(data['inline'])
        self.assertEqual(len(data['buttons'][0]), 2)
        self.assertEqual(len(data['buttons'][1]), 1)
        self.assertEqual(data['buttons'][0][1]['action']['label'], "2")
        self.assertEqual(data['buttons'][1][0]['action']['payload'], "{\"command\": \"3\"}")