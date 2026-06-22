# ===== PARTE B =====

def clasificar_arma(poder):
   
    if poder >= 80:
        return "Legendaria"
    elif poder >= 40:
        return "Media"
    else:
        return "Debil"

def es_critico(es_magica, nivel):
    return es_magica or nivel >= 10

def dano_base(ataque, poder, defensa):
   return (ataque + poder) - defensa

def dano_total(ataque, poder, defensa, critico):
       base = dano_base(ataque, poder, defensa)
    if critico:
        return base * 2
    else:
        return base
