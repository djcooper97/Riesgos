
import numpy as np
import pandas as pd
import math
from datetime import date

fecha_valuacion = date.today()
fecha_vencimiento = date(2026,3,5)

dias_al_vencimiento = (fecha_vencimiento - fecha_valuacion).days
periodo_cupon = 182
valor_nominal = 100
tasa_cupon = 0.0575
tasa_descuento = 0.0688


cupones_vencer = dias_al_vencimiento / periodo_cupon
cupones_reales = math.ceil(cupones_vencer)
dias_devengados = (cupones_reales - cupones_vencer) * periodo_cupon
valor_cupon = valor_nominal * tasa_cupon * periodo_cupon / 360
dias_vencer_cc = periodo_cupon - dias_devengados

# Series iniciales para calcular valor presente
flujos = np.zeros(cupones_reales)
valor_presente = np.zeros(cupones_reales)

# Establecer valores 
flujos[:] = valor_cupon
flujos[-1] = valor_nominal + valor_cupon
for num_cupon in range(cupones_reales):
    dias_pago_cupon = dias_vencer_cc + periodo_cupon * num_cupon
    factor_descuento = 1/(1+tasa_descuento*periodo_cupon/360)**(dias_pago_cupon/periodo_cupon)
    valor_presente[num_cupon] = flujos[num_cupon]*factor_descuento
    print(valor_presente[num_cupon])

