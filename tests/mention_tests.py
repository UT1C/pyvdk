from unittest import TestCase

from pyvdk.tools import Mention


class MentionTests(TestCase):
    def setUp(self):
        ...

    def test_find(self):
        string = "[id1|@durov], вот дурашка"

        act = Mention.find(string)

        self.assertIsNotNone(act)
        self.assertEqual(act.id, 1)
        self.assertEqual(act.text, "@durov")
        self.assertEqual(act.user, True)
        self.assertEqual(act.club, False)
        self.assertEqual(act.club, False)
        self.assertEqual(str(act), "[id1|@durov]")

    def test_finditer(self):
        string = "[club1|Вконтакте API], [club28551727|VK API Change Log]"

        act = tuple(Mention.finditer(string))

        self.assertEqual(len(act), 2)
        self.assertEqual(act[0].id, 1)
        self.assertEqual(act[1].id, 28551727)
        self.assertEqual(act[0].text, "Вконтакте API")
        self.assertEqual(act[1].text, "VK API Change Log")
        self.assertEqual(act[0].club, True)
        self.assertEqual(act[1].club, True)
        self.assertEqual(act[0].user, False)
        self.assertEqual(act[1].user, False)

    def test_str(self):

        act = Mention(id=1, text="@durov")

        self.assertEqual(str(act), "[id1|@durov]")
        self.assertEqual(f"{act}", "[id1|@durov]")
