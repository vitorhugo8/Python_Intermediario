class Connection:
    def __init__(self, host="localhost"):
        self.host = host 
        self.user = None 
        self.password = None 
    
    # configurando os valores através dos métodos da classe. 
    # essa é uma prática comum em qualquer linguagem de programação, o Python tem outro método para isso, mas vamos estudar isso depois 
    def set_user(self, user): 
        self.user = user # Método de instãncia sempre que usar 'self' 

    def set_password(self, password):
        self.password = password 
    
    @classmethod # Este classmethod também é uma factorie, por coincidência 
    def create_with_auth(cls, user, password): # Método de classe sempre que usar 'cls'
        connection = cls()
        connection.user = user 
        connection.password = password
        return connection
    
    @staticmethod 
    def soma(x, y):
        return x + y

# c1 = Connection()
c1 = Connection.create_with_auth("Luiz", "1234")
print(c1.user)
print(c1.password)
# c1.set_user("Luiz") 
# print(c1.user) 
# c1.set_password("123")
# print(c1.password) 
print(Connection.soma(2, 4))   
