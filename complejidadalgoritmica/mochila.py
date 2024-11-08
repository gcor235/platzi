def mochila(tamano_mochila, pesos, valores, n):

    if n == 0 or tamano_mochila == 0:
        return 0 #para regresar el valor maximo

    if pesos[n - 1] > tamano_mochila: 
        return mochila(tamano_mochila, pesos, valores, n - 1)
#para escoger el valor maximo
    return max(valores[n - 1] + mochila(tamano_mochila - pesos[n - 1], pesos, valores, n - 1),
                mochila(tamano_mochila, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [30, 60, 90]
    pesos = [10, 20, 30]
    tamano_mochila = 55
    n = len(valores) #valor maximo de la mescla de los valores

    resultado = mochila(tamano_mochila, pesos, valores, n)
    print(resultado)