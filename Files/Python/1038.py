# -*- coding: utf-8 -*-

cod,quant = input().split()
cod = int(cod)
quant = int(quant)

if cod == 1:
    valor = quant*4
    print("Total: R$ %.2f" % (valor))
elif cod == 2:
    valor = quant*4.5
    print("Total: R$ %.2f" % (valor))
elif cod == 3:
    valor = quant*5
    print("Total: R$ %.2f" % (valor))
elif cod == 4:
    valor = quant*2
    print("Total: R$ %.2f" % (valor))
elif cod == 5:
    valor = quant*1.5
    print("Total: R$ %.2f" % (valor))
else:
    print("código não encontrado.")
    
    