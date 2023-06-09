def automato_a(cadeia, estado_atual="q0"):
    estados_finais = ["q0", "q1", "q2"]
    if cadeia == "":
        return estado_atual in estados_finais

    if estado_atual == "q0":
        if cadeia[0] == "a":
            return automato_a(cadeia[1:], "q1")
    if estado_atual == "q1":
        if cadeia[0] == "a":
            return automato_a(cadeia[1:], "q1")
        if cadeia[0] == "b":
            return automato_a(cadeia[1:], "q1")
        if cadeia[0] == "c":
            return automato_a(cadeia[1:], "q2")

    if estado_atual == "q2":
        if cadeia[0] == "a":
            return automato_a(cadeia[1:], "q1")
        if cadeia[0] == "c":
            return automato_a(cadeia[1:], "q2")
    return False


def automato_b(cadeia, estado_atual="q0"):
    estados_finais = ["q3", "q7"]
    if cadeia == "":
        return estado_atual in estados_finais

    if estado_atual == "q0":
        if cadeia[0] == "a":
            return automato_b(cadeia[1:], "q1")
        if cadeia[0] == "b":
            return automato_b(cadeia[1:], "q4")
        if cadeia[0] == "c":
            return automato_b(cadeia[1:], "q4")

    if estado_atual == "q1":
        if cadeia[0] == "a":
            return automato_b(cadeia[1:], "q2")

    if estado_atual == "q2":
        if cadeia[0] == "a":
            return automato_b(cadeia[1:], "q3")

    if estado_atual == "q3":
        if cadeia[0] == "b":
            return automato_b(cadeia[1:], "q3")
        if cadeia[0] == "c":
            return automato_b(cadeia[1:], "q3")

    if estado_atual == "q4":
        if cadeia[0] == "a":
            return automato_b(cadeia[1:], "q5")
        if cadeia[0] == "b":
            return automato_b(cadeia[1:], "q4")
        if cadeia[0] == "c":
            return automato_b(cadeia[1:], "q4")

    if estado_atual == "q5":
        if cadeia[0] == "a":
            return automato_b(cadeia[1:], "q6")

    if estado_atual == "q6":
        if cadeia[0] == "a":
            return automato_b(cadeia[1:], "q7")
    return False


def automato_c(cadeia, estado_atual="q0"):
    estados_finais = ["q1", "q3", "q4"]
    if cadeia == "":
        return estado_atual in estados_finais

    if estado_atual == "q0":
        if cadeia[0] == "a":
            return automato_c(cadeia[1:], "q1")
        if cadeia[0] == "b":
            return automato_c(cadeia[1:], "q3")

    if estado_atual == "q1":
        if cadeia[0] == "a":
            return automato_c(cadeia[1:], "q2")
        if cadeia[0] == "b":
            return automato_c(cadeia[1:], "q4")

    if estado_atual == "q2":
        if cadeia[0] == "a":
            return automato_c(cadeia[1:], "q2")
        if cadeia[0] == "b":
            return automato_c(cadeia[1:], "q3")

    if estado_atual == "q4":
        if cadeia[0] == "b":
            return automato_c(cadeia[1:], "q4")
    return False


def automato_d(cadeia, estado_atual="q0"):
    estados_finais = ["q1", "q3"]
    if cadeia == "":
        return estado_atual in estados_finais

    if estado_atual == "q0":
        if cadeia[0] == "a":
            return automato_d(cadeia[1:], "q1")
        if cadeia[0] == "b":
            return automato_d(cadeia[1:], "q2")

    if estado_atual == "q1":
        if cadeia[0] == "a":
            return automato_d(cadeia[1:], "q1")
        if cadeia[0] == "b":
            return automato_d(cadeia[1:], "q2")
        if cadeia[0] == "c":
            return automato_d(cadeia[1:], "q3")

    if estado_atual == "q2":
        if cadeia[0] == "a":
            return automato_d(cadeia[1:], "q3")
        if cadeia[0] == "b":
            return automato_d(cadeia[1:], "q2")

    if estado_atual == "q3":
        if cadeia[0] == "c":
            return automato_d(cadeia[1:], "q3")
    return False
