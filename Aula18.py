"""
CONSTANTE =  "Váriaveis" que não vão mudar
muitas condições no mesmo 'if' (ruim)
<-contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro =  101  # local em que o carro está na estrada

RADAR_1 = 60  # Velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde está o radar

vel_carro_pass_radar_1 = velocidade >RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1
if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do aradar 1')
if  carro_passou_radar_1:
    print('carro passou radar 1')
    
