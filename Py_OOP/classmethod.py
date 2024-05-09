
class Scope:
    name = 'Local Scope'
    print(name)
    
    @classmethod
    def name(cls, name):
        cls.name = name
        
p = Scope()
p.name('Change Local')
print(Scope.name)




