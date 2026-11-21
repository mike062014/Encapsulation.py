class Myclass():
    __privateValue = 10

    def __Privatemethod(self):
        print("Im inside this class privately")
    def hello():
        print("Private value:",Myclass.__privateValue)
foo = Myclass
foo.hello()
foo.Privatemethod