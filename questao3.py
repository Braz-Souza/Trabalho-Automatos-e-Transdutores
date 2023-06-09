def automato_maquina_refri(cadeia, estado_atual = "q0", saida = []):
    if cadeia == []: return saida

    if estado_atual == "q0":
        if cadeia[0] == 25:
            estado_atual = "q25"
            saida.append(0)
        if cadeia[0] == 50:
            estado_atual = "q50"
            saida.append(0)
        if cadeia[0] == 100: 
            estado_atual = "q0"
            saida.append(1)

    elif estado_atual == "q25":
        if cadeia[0] == 25:
            estado_atual = "q50"
            saida.append(0)
        if cadeia[0] == 50:
            estado_atual = "q75"
            saida.append(0)
        if cadeia[0] == 100: 
            estado_atual = "q25"
            saida.append(1)

    elif estado_atual == "q50":
        if cadeia[0] == 25:
            estado_atual = "q75"
            saida.append(0)
        if cadeia[0] == 50:
            estado_atual = "q0"
            saida.append(1)
        if cadeia[0] == 100: 
            estado_atual = "q50"
            saida.append(1)

    elif estado_atual == "q75":
            if cadeia[0] == 25:
                estado_atual = "q0"
                saida.append(1)
            if cadeia[0] == 50:
                estado_atual = "q25"
                saida.append(1)
            if cadeia[0] == 100: 
                estado_atual = "q75"
                saida.append(1)

    return automato_maquina_refri(cadeia[1:], estado_atual, saida)
