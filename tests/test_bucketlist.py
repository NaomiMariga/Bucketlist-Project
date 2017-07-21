import unittest
from  models.bucketlist import Bucketlist

class bucketlistTest(unittest.TestCase):  

    def setUp(self):
        self.bucketlist = Bucketlist()
        
    def test_create_bucketlist(self):
        self.assertEqual(self.bucketlist.create_bucketlist({
            "name":"movies"
            }), "Buckelist created successfuly")
    def test_view_bucketlist(self):
        self.assertEqual(self.bucketlist.edit_bucketlist({
            "name":"movies"
            }), "updated")
    def test_delete_bucketlist(self):
        self.assertEqual(self.bucketlist.delete_bucketlist(), "Bucketlist deleted")

    
    
