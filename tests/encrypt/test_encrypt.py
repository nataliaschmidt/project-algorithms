import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    '''Para uma key par:
    divide message no índice key,
    inverte a posição das partes,
    inverte os caracteres de cada parte,
    e retorna a união das partes novamente com "_" entre elas'''
    assert encrypt_message("Let's Go", 4) == "oG s_'teL"

    '''Para uma key ímpar:
    divide message no índice key,
    inverte os caracteres de cada parte,
    e retorna a união das partes novamente com "_" entre elas'''
    assert encrypt_message("Let's Go", 3) == "teL_oG s'"

    '''Se key não possuir o tipo corretos, uma exceção deve ser lançada'''
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Let's Go", "3")

    '''Se message não possuir o tipo corretos, uma exceção deve ser lançada'''
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)

    '''Se key não for um índice positivo válido de message,
    retorna a string message invertida '''
    assert encrypt_message("Let's Go", 20) == "oG s'teL"
