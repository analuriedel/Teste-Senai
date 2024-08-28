notaA=float(input("Informe a primeira nota "))
notaB=float(input("Informe a segunda nota "))

#calcular média
mediafinal = (notaA+notaB)/2

#verificação
if mediafinal >= 7.0:
    print("A média: %.1f - aprovado "% mediafinal)
elif mediafinal >5 and mediafinal <6.9:
    print("A média: %.1f - em exame "% mediafinal)
else:
    print("A média: %.1f - reprovado "% mediafinal)
