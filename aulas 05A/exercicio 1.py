Vhora = float(input("digite o valor da hora trabalhada:"))
total_horas = int(input("total de horas trabalhada"))
sal_bruto = Vhora * total_horas
if sal_bruto <= 900:
    ir = 0
    aliquota = 0
elif sal_bruto <= 1500:
    ir = sal_bruto * 0.05
    aliquota = 5
elif sal_bruto <= 2500:
    aliquota = 10
else:
    ir = sal_bruto *0.2
    aliquota = 20

inss = sal_bruto * 0.1
fgts = sal_bruto * 0.11
imp_sind = sal_bruto * 0.03
total_descon = ir + inss
sal_liquido = sal_bruto - total_descon
Vhora = 5
total_horas = 220
sal_bruto = Vhora * total_horas
print("salario bruto:(",Vhora, "*", total_horas,"): R$", sal_bruto)
print("(-)ir(",aliquota,"%         :R$", ir)
print("(-)INSS (10%)               :R$", inss)
print("FGTS(11%)                   :R$", fgts)
print("total de desconto           :R$", total_descon)
print("salario liquido             :R$", sal_liquido)

