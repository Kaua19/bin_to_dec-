def bin_to_dec():
    """
    Converte numero binario em decimal.

    parametros: 
    None

    Retorna: 
    decimal do numero binario digitado pelo usuario

    """
try:
    x = input("Digite um numero binario:")
    if len(x) > 8:
        print("Nao passe de 8 digitos;)")
    else:
        p = int(x, base=2)
        print(p)
except ValueError:
    print("Numeros binario utilizam-se somente uns (1) e zeros (0);)")

bin_to_dec()
