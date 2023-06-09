from questao1 import *
from questao3 import *

# Testes automato a)
def teste_automato_a_1():
    assert automato_a("abbbccca") == True

def teste_automato_a_2():
    assert automato_a("") == True

def teste_automato_a_3():
    assert automato_a("a") == True

def teste_automato_a_4():
    assert automato_a("abc") == True

def teste_automato_a_5():
    assert automato_a("abbcc") == True

def teste_automato_a_6():
    assert automato_a("aaabbccabcaabcaaaabcabcabc") == True

def teste_automato_a_7():
    assert automato_a("aaaaaa") == True

def teste_automato_a_8():
    assert automato_a("bc") == False

def teste_automato_a_9():
    assert automato_a("abcacb") == False

def teste_automato_a_10():
    assert automato_a("acb") == False

# Testes automato b)
def teste_automato_b_1():
    assert automato_b("aaabc") == True

def teste_automato_b_2():
    assert automato_b("bcaaa") == True

def teste_automato_b_3():
    assert automato_b("aaa") == True

def teste_automato_b_4():
    assert automato_b("aaabbbbcccbbcb") == True

def teste_automato_b_5():
    assert automato_b("bcbcbbcbbbbbccccaaa") == True

def teste_automato_b_6():
    assert automato_b("") == False

def teste_automato_b_7():
    assert automato_b("aaaaaa") == False

def teste_automato_b_8():
    assert automato_b("bc") == False

def teste_automato_b_9():
    assert automato_b("a") == False

def teste_automato_b_10():
    assert automato_b("bcbaaabcb") == False

# Testes automato c)
def teste_automato_c_1():
    assert automato_c("abbb") == True

def teste_automato_c_2():
    assert automato_c("aaaab") == True

def teste_automato_c_3():
    assert automato_c("ab") == True

def teste_automato_c_4():
    assert automato_c("abbbbbbbbbbb") == True

def teste_automato_c_5():
    assert automato_c("aaaaaaaaaaab") == True

def teste_automato_c_6():
    assert automato_c("aabb") == False

def teste_automato_c_7():
    assert automato_c("") == False

def teste_automato_c_8():
    assert automato_c("aaaabb") == False

def teste_automato_c_9():
    assert automato_c("baaaa") == False

def teste_automato_c_10():
    assert automato_c("bbbba") == False

# Testes automato d)
def teste_automato_d_1():
    assert automato_d("a") == True

def teste_automato_d_2():
    assert automato_d("ac") == True

def teste_automato_d_3():
    assert automato_d("acccc") == True

def teste_automato_d_4():
    assert automato_d("aaac") == True

def teste_automato_d_5():
    assert automato_d("aaaccc") == True

def teste_automato_d_6():
    assert automato_d("bbbbac") == True

def teste_automato_d_7():
    assert automato_d("bac") == True

def teste_automato_d_8():
    assert automato_d("abac") == True

def teste_automato_d_9():
    assert automato_d("abbbacccc") == True

def teste_automato_d_10():
    assert automato_d("") == False

def teste_automato_d_11():
    assert automato_d("bbbccc") == False

def teste_automato_d_12():
    assert automato_d("c") == False

def teste_automato_d_13():
    assert automato_d("abc") == False

def teste_automato_d_14():
    assert automato_d("abacb") == False

def teste_automato_d_15():
    assert automato_d("abbbaaaaccc") == False
