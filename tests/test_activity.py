import unittest
from  models.activity import Activity

class ActivityTest(unittest.TestCase):  

    def setUp(self):
        self.activity = Activity()

    def test_add_activity(self):
        self.assertEqual(self.activity.add_activity({"name":"The gods must be crazy"}), "Activity added")
    def test_edit_activity(self):
        self.assertEqual(self.activity.edit_activity({"name":"The gods must be crazy"}), "updated")
    def test_delete_activity(self):
        self.assertEqual(self.activity.delete_activity({"name"}),"Activity deleted")
    
    
