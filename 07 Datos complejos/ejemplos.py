def init(self):
    self.items = [1, 5, "algo"]

def esta_vacia(self):
    return len(self.items) == 0

def apilar(self, item):
    self.items.append(item)

def desapilar(self):
    return self.items.pop()

def ver_tope(self):
    return self.items[-1]

nombres = {"oxigeno": 10, "Nitrogeno": 5, "Sodio": 3}
nombre = ["oxigeno", "Nitrogeno", "Sodio"]

nombres["Nitrogeno"] += 5
nombres["hierro"] = nombres.get("regla", 0) + 1

print(nombre[1])