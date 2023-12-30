import hashlib

diccUsuarios = {}

def addUsuario(usuario, contrasena):
    diccUsuarios[usuario] = hashlib.sha256(contrasena.encode()).hexdigest()

addUsuario("Jaume", "1234")
addUsuario("Christian", "5678")
addUsuario("Navarro", "4321")
addUsuario("Luis", "8765")
addUsuario("Mariano", "9283")

def consulta(usuario, contrasena):
    has = hashlib.sha256(contrasena.encode()).hexdigest()
    if usuario in diccUsuarios and diccUsuarios[usuario] == has:
        return True
    return False

print("Usuario", consulta("Jaume", "1234"))
print("Usuario", consulta("Navarro", "4321"))
