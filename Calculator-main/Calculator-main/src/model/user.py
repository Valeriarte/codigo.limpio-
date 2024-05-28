class Usuario:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def esIgual(self, compare_with):
        assert(self.name == compare_with.name)
        assert(self.age == compare_with.age)
        
        
