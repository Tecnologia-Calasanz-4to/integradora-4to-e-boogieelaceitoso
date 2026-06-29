# ===== PARTE C =====
def porcentaje_vida(actual, maxima):
    return (actual/ maxima )* 100
def estado_vida(porcentaje):
    if porcentaje <= 25:
        return str("CRITICO")
    elif porcentaje <= 50:
        return str("HERIDO")
    else:
        return str("SANO")
def comprar_pociones(monedas, precio):
    return monedas// precio, monedas % precio

def main():
    actual = int(input("Vida actual: "))
    maxima = int(input("Vida maxima: "))
    monedas = int(input("Monedas: "))
    porcentaje = porcentaje_vida(actual, maxima)
    print(estado_vida(porcentaje))
    cantidad,vuelto=comprar_pociones(monedas,25)
    print(cantidad)
    print(vuelto)

main()


