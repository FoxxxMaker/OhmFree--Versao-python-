# Lei de Ohm: V = R * I

# cores: preto: 0, marrom: 1, vermelho: 2, laranja: 3, amarelo: 4, verde: 5, azul: 6, violeta: 7, cinza: 8, branco: 9

# 1ª faixa: 1º dígito, 2ª faixa: 2º dígito, 3ª faixa: multiplicador, 4ª faixa: tolerância (opcional)


    
cores = {
     "preto": 0,
     "marrom": 1,
     "vermelho": 2,
     "laranja": 3,
     "amarelo": 4,
     "verde": 5,
     "azul": 6,
     "violeta": 7,
     "cinza": 8,
     "branco": 9
    }

def calcular_resistencia(cor1, cor2, cor3):
    valor1 = cores[cor1]
    valor2 = cores[cor2]
    multiplicador = 10 ** cores[cor3]
    
    resistencia = (valor1 * 10 + valor2) * multiplicador
    if resistencia >= 1000:
        resistencia = resistencia / 1000
        return f"{resistencia} k"
    elif resistencia >= 1000000:
        resistencia = resistencia / 1000000
        return f"{resistencia} M"
    return resistencia