i = 1
somavalor = 0
somaPos = 0
contNeg = 0
while i <= 20:
    valor = int ( input ("Digite um valor: "))
    somavalor += valor
    if valor >= 0:
        somaPos=+valor
    else:
        contNeg += 1
    i += 1
print ('A soma dos valores positivos é: ', somavalor )
print ('A quantidade de números negativos é: ', contNeg)
