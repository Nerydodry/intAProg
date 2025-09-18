print("************ OPERAÇÕES MATEMÁTICAS ************")
print("Escolha uma das operações abaixo. Para encerrar, digite sair!!!")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Par ou Ìmpar")
print("6 - Primo")
print("7 - Fatorial")

opcao=input("Digite a opção desejada ou <SAIR> para encerrar!!!")
opcaoMaiusc=opcao.upper()
while opcaoMaiusc!="SAIR":
    if opcao=="1":
        num1=int(input("Digite o primeiro valor: "))
        num2=int(input("Digite o segundo valor: "))
        print("A soma dos valores é:", num1+num2)
    if opcao=="2":
        num1=int(input("Digite o primeiro valor: "))
        num2=int(input("Digite o segundo valor: "))
        print("A subtração dos valores é:", num1-num2)
    if opcao=="3":
        num1=int(input("Digite o primeiro valor: "))
        num2=int(input("Digite o segundo valor: "))
        print("A multiplicação dos produtos é:", num1*num2)
    if opcao=="4":
        num1=int(input("Digite o primeiro valor: "))
        num2=int(input("Digite o segundo valor: "))
        print("A divisão dos valores é de:", num1/num2)
input("Pressione ENTER para voltar ao menu!")
#os.sytem("cls")

print("Escolha uma das operações abaixo. Para encerrar, digite sair!!!")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Par ou Ìmpar")
print("6 - Primo")
print("7 - Fatorial")

if opcao=="5":
    num1=int(input("Digite um numéro para saber se ele é ímpar ou par: "))
    if num1%2==0:
        print("O número é par!")
    else:
        print("O número é ímpar:")
input("Pressione ENTER para voltar ao menu!")

print("Escolha uma das operações abaixo. Para encerrar, digite sair!!!")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Par ou Ìmpar")
print("6 - Primo")
print("7 - Fatorial")

if opcao=="6":
    num1=int(input("Digite um numero para saber se ele é primo ou não: "))
    



        

