class Activity:
    def __init__(self):
        self.input_activity = ()
        self.input_edit = input("")
        

    def add_activity(self, name):
        self.input_activity = (name)
    def edit_activity(self, name):
        self.input_edit = (name)
    def delete_activity(self):
        del()
