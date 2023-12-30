import hashlib

listaUsuariosContrasenas = []

def addUsuario(usuario, contrasena):
    listaUsuariosContrasenas.append((usuario, hashlib.sha256(contrasena.encode()).hexdigest()))

addUsuario("Jaume", "1234")
addUsuario("Christian", "5678")
addUsuario("Navarro", "4321")
addUsuario("Luis", "8765")
addUsuario("Mariano", "9283")

def consulta(usuario, contrasena):
    has = hashlib.sha256(contrasena.encode()).hexdigest()
    for user, contr in listaUsuariosContrasenas:
        if usuario == user and has == contr:
            return True
    return False


print("Usuario", consulta("Jaume", "1234"))
print("Usuario", consulta("Luis", "8765"))
