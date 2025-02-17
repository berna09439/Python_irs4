import os 
import platform

def calcular_salario_liquido(b, e=0, desconto_dependente=0):
    if b <= 870:
        return b
    elif b <= 992:
        c = b * 0.13 - 0.13 * 2.60 * (1208.32 - b) - (desconto_dependente * e)
    elif b <= 1070:
        c = b * 0.165 - 0.165 * 1.35 * (1477.67 - b) - (desconto_dependente * e)
    elif b <= 1136:
        c = b * 0.165 - 90.81 - (desconto_dependente * e)
    elif b <= 1187:
        c = b * 0.22 - 153.29 - (desconto_dependente * e)
    elif b <= 1787:
        c = b * 0.25 - 188.90 - (desconto_dependente * e)
    elif b <= 2078:
        c = b * 0.32 - 313.99 - (desconto_dependente * e)
    elif b <= 2432:
        c = b * 0.355 - 386.72 - (desconto_dependente * e)
    elif b <= 3233:
        c = b * 0.3872 - 465.03 - (desconto_dependente * e)
    elif b <= 5547:
        c = b * 0.4005 - 508.03 - (desconto_dependente * e)
    elif b <= 20221:
        c = b * 0.4495 - 779.83 - (desconto_dependente * e)
    else:
        c = b * 0.4717 - 1228.74 - (desconto_dependente * e)
    
    return b - c

while True:
    print("\nEscolha seu estado:")
    print("1 - Sem dependentes e não casado")
    print("2 - Não casado com um ou mais dependentes")
    print("3 - Casado único titular")
    print("4 - Casado com um ou mais dependentes")
    
    try:
        a = int(input("Estado atual? (1-4) = "))
        if a not in [1, 2, 3, 4]:
            raise ValueError("Opção inválida!")
        b = float(input("Salário bruto: "))
        e = 0
        desconto_dependente = 0
        
        if a in [2, 4]:  # Estados que possuem dependentes
            e = int(input("Número de dependentes: "))
            desconto_dependente = 34.29 if a == 2 else 42.86
        
        salario_liquido = calcular_salario_liquido(b, e, desconto_dependente)
        print(f"O salário líquido é: {salario_liquido:.2f}")
        
    except ValueError as erro:
        print(f"Erro: {erro}. Digite valores válidos!")
    
    continuar = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
    if continuar != 's':
        break
    else: 
      if platform.system() = 'Windows':
        os.system('cls')
      else: 
        os.system('clear')
