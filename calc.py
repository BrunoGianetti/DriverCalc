print (' ')
print (' ')
print (' ')
print ('\033[7;33;40;m                                         \033[m')
print ('\033[7;33;40;m         CALCULADORA DE CORRIDAS         \033[m')
print ('\033[7;33;40;m                                         \033[m')
print (' ')
km=float (input ('Qual a distância em KM: '))
print (' ')
temp=float (input ('Qual o tempo em minutos: '))
print (' ')
din=float (input ('Digite o valor do preço dinâmico: '))
print (' ')
ped=float (input ('Digite o valor dos pedágios: '))
print (' ')
estac=float (input ('Digite o valor do estacionamento: '))
print(' ')
desc=str(input('Foi resgatado cashback? [S/N] '))
valor=(((km*0.85)+(temp*0.65))*din)+ped+estac
if valor < 7:
   valor=7
else:
   valor=valor
if km<60 or temp<40:
   valor=valor*1
elif km>=60 and km<80 or temp>=40 and temp<60:
    valor=valor*1.1
elif km>=80 and km<100 or temp>=60 and temp<80:
    valor=valor*1.125
elif km>=100 and km<120 or temp>=80 and temp<100:
    valor=valor*1.15
elif km>=120 and km<140 or temp>=100 and temp<120:
    valor=valor*1.165
elif km>=140 and km<160 or temp>=120 and temp<140:
    valor=valor*1.15
elif km>=160 and km<180 or temp>=140 and temp<160:
    valor=valor*1.15
elif km>=180 and km<200 or temp>=160 and temp<180:
    valor=valor*1.15
print (' ')
print (' 》》','O valor da corrida é \033[3;33;40mR ${:.2f}\033[m'.format (valor),'《《')
print (' ')
print ('     >>> Aceito débito e crédito <<<')
print (' ')
print ('•'*41)
print ('    App developed by BRUNO GIANETTI')
print ('•'*41)
print (' ')
print ('social media:')
print (' ')
print ('whatsapp: (19) 98192-2647')
print ('instagran: @ubertraderitaliano')
print ('twitter: @bruno_gianetti')
print ('facebook: Bruno Gianetti')
print ('linkedin: Bruno Gianetti')
print (' ')
print ('Copyright 2019 - v1.4')