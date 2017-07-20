class Activity:
    def __init__(self):
        self.input_activity = ()
        self.input_edit = input("")
        

    def Add_activity(self, name):
        self.input_activity = (name)
    def Edit_activity(self, name):
        self.input_edit = (name)
    def Delete_activity(self):
        del()
