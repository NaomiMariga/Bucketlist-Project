class Bucketlist:
    def __init__(self):
        self.created_bucketlist = {}
        self.updated_bucketlist = input("")

    def create_bucketlist(self, name):
        self.created_bucketlist = {"bucketlist_name":name}
    def edit_bucketlist(self, name):
        self.updated_bucketlist = input(name)
    def delete_bucketlist(self):
        del()