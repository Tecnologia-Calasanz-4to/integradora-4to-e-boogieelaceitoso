# ===== PARTE A =====
def nombre_valido(nombre):
    if len(nombre) >= 3 and nombre.isalpha():
        devolver = True
    else:
        devolver = False
    return devolver
def crear_codename(nombre, nivel):
    return nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
    return 100 + nivel ** 2 * 5
def main():
    nombre = input("ingresa un nombre")
    if nombre_valido(nombre)==True:
         nombre = nombre.capitalize()
    else:
        nombre = "heroe"
        
    nivel = int(input("ingrese un nivel"))
    codename = crear_codename(nombre, nivel)
    vida = vida_maxima(nivel)

    print("codename:", codename)
    print("vida maxima:", vida)
    
main()




