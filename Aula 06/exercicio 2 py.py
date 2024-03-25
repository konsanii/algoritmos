x1 = float(input("digite o valor da compra por favor"))



if x1 <= 1000:
  des1 = x1 *10/100
  print("sua compra de R$", x1, "ficou com 10% de desconto no o valor de R$" ,des1)

elif x1>1000 and x1< 5000:
 des2 = x1*20/100
 print("sua compra de R$", x1 ,"ficou com 20% de desconto no o valor de R$" ,des2)

elif x1>5000:
  des3 = x1*30/100
  print("sua compra de R$" ,x1 , "ficou com 20% de desconto no o valor de R$" ,des3)




