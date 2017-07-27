import unittest
from  models.activity import Activity

class TestActivity(unittest.TestCase):  

    def test_add_activity(self):
        self.assertEqual(self.activity.add_activity({"name":"The gods must be crazy"}), "Activity added")
    def test_edit_activity(self):
        self.assertEqual(self.activity.edit_activity({"name":"The gods must be crazy"}), "updated")
    def test_delete_activity(self):
        self.assertEqual(self.activity.delete_activity({"name"}),"Activity deleted")
    
    
