# ===== PARTE A =====
def nombre_valido(nombre):
    if len(nombre) >= 3 and nombre.isalpha():
        return true
    else:
        return false
def crear_codename(nombre, nivel):
    return nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
    return 100 + nivel ** 2 * 5

    nom=input("Ingresar un usuario")
    




