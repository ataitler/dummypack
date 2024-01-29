class dummyclass:
    def __init__(self, name=None):
        self._name = name

    def SayMyName(self):
        if self._name is None:
            print("I have no name")
        else:
            print("my name is", self._name + "!")
