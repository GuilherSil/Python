from PIL import Image

matriz_cinza = Image.getMatrizImagemCinza ("foto.jpg")

for i in len ( matriz_cinza ):
    for j in len ( matriz_cinza [i ]) :
        if matriz_cinza [i ][ j] > 128:
            matriz_cinza [i ][ j ] = 255
        else :
            matriz_cinza [i ][ j ] = matriz_cinza [i ][ j] - 64
    if matriz_cinza [i ][ j] < 0:
        matriz_cinza [i ][ j] = 0
Image.salvaImagemCinza("foto2.jpg", matriz_cinza)