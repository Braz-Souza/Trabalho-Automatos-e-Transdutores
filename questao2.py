def automato_computador(cadeia, estado_atual="q0", ocorrencias=[], pos=0, i=0):
    if cadeia == "":
        if estado_atual == "q10":
            ocorrencias.append(pos)
        return ocorrencias

    novo_estado = "q11"
    if estado_atual == "q0" and cadeia[0] == "c":
        pos = i
        novo_estado = "q1"

    if estado_atual == "q1" and cadeia[0] == "o": novo_estado = "q2"
    
    if estado_atual == "q2" and cadeia[0] == "m": novo_estado = "q3"
    
    if estado_atual == "q3" and cadeia[0] == "p": novo_estado = "q4"
    if estado_atual == "q4" and cadeia[0] == "u": novo_estado = "q5"
    if estado_atual == "q5" and cadeia[0] == "t": novo_estado = "q6"
    if estado_atual == "q6" and cadeia[0] == "a": novo_estado = "q7"
    if estado_atual == "q7" and cadeia[0] == "d": novo_estado = "q8"
    if estado_atual == "q8" and cadeia[0] == "o": novo_estado = "q9"
    if estado_atual == "q9" and cadeia[0] == "r": novo_estado = "q10"
    if estado_atual == "q10" and cadeia[0] == " ":
        ocorrencias.append(pos)
        novo_estado = "q0"
    if estado_atual == "q11" and cadeia[0] == " ": novo_estado = "q0"
    
    return automato_computador(cadeia[1:], novo_estado, ocorrencias, pos, i + 1)