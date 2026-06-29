

def clasificar_arma(poder):
    """Devuelve 'Legendaria', 'Media' o 'Debil' según el poder del arma."""
    if poder >= 70:
        return "Legendaria"
    elif poder >= 40:
        return "Media"
    else:
        return "Debil"


def es_critico(es_magica, nivel):
    """Devuelve True si el arma es mágica o el nivel es 10 o más."""
    return es_magica or nivel >= 10


def dano_base(ataque, poder, defensa):
    """Calcula el daño base: (ataque + poder) - defensa."""
    return (ataque + poder) - defensa


def dano_total(ataque, poder, defensa, critico):
    """Si es crítico devuelve el doble del dano_base; si no, el daño normal."""
    base = dano_base(ataque, poder, defensa)
    if critico:
        return base * 2
    else:
        return base




def pedir_numero(mensaje):
    """Evita que el programa falle si el usuario ingresa texto en vez de números."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ ¡Error! Debes ingresar un número entero (ej: 10, 20, 50). Inténtalo de nuevo.")




print("--- CONFIGURA LAS ESTADÍSTICAS DEL COMBATE ---")


mi_ataque = pedir_numero("Introduce tu ataque: ")
poder_arma = pedir_numero("Introduce el poder del arma: ")
defensa_enemigo = pedir_numero("Introduce la defensa del enemigo: ")


respuesta_magica = input("¿El arma es mágica? (s/n): ").lower()
magica = respuesta_magica == 's' 

nivel_personaje = pedir_numero("Introduce el nivel de tu personaje: ")
print("-" * 45)




rareza = clasificar_arma(poder_arma)
metio_critico = es_critico(magica, nivel_personaje)
dano_final = dano_total(mi_ataque, poder_arma, defensa_enemigo, metio_critico)




print(f"--- ESTADÍSTICAS DEL COMBATE ---")
print(f"Rareza del arma: {rareza}")
print(f"¿Fue golpe crítico?: {'Sí' if metio_critico else 'No'}")
print(f"Daño total causado: {dano_final}")
