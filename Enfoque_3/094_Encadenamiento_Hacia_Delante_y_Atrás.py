# Intentamos deducir un hecho partiendo desde el objetivo hacia las causas
base_conocimiento = ["A => B", "B => C", "A"]

def encadenamiento_atras(base, objetivo):
    hechos = {r for r in base if "=>" not in r}

    def probar(objetivo):
        if objetivo in hechos:
            return True
        for regla in base:
            if "=>" in regla:
                antecedente, consecuente = [x.strip() for x in regla.split("=>")]
                if consecuente == objetivo:
                    return probar(antecedente)
        return False

    return probar(objetivo)

print("¿Se puede deducir C con encadenamiento hacia atrás?:", encadenamiento_atras(base_conocimiento, "C"))
# Intentamos deducir un hecho partiendo desde el objetivo hacia las causas
base_conocimiento = ["A => B", "B => C", "A"]

def encadenamiento_atras(base, objetivo):
    hechos = {r for r in base if "=>" not in r}

    def probar(objetivo):
        if objetivo in hechos:
            return True
        for regla in base:
            if "=>" in regla:
                antecedente, consecuente = [x.strip() for x in regla.split("=>")]
                if consecuente == objetivo:
                    return probar(antecedente)
        return False

    return probar(objetivo)

print("¿Se puede deducir C con encadenamiento hacia atrás?:", encadenamiento_atras(base_conocimiento, "C"))
