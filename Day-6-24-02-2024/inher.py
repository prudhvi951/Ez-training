class parent:
    def __init__(self):
        print("Parent Method")
class child(parent):
    def __init__(self):
        print("Child Method")
ob = child()

class parent:
    def __init__(self):
        print("Parent Method")
class child(parent):
    def __init__(self):
        super().__init__()
        print("Child Method")
ob = child()
