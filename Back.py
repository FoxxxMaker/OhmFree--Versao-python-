# Lei de Ohm: V = R * I

# cores: preto: 0, marrom: 1, vermelho: 2, laranja: 3, amarelo: 4, verde: 5, azul: 6, violeta: 7, cinza: 8, branco: 9

# 1ª faixa: 1º dígito, 2ª faixa: 2º dígito, 3ª faixa: multiplicador, 4ª faixa: tolerância (opcional)

def resistor(cor1, cor2, cor3, cor4=None):
    
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
    try:
        r = (cores[cor1] * 10 + cores[cor2]) * (10 ** cores[cor3])
        return r
    except KeyError:
        raise ValueError("Cor inválida")    