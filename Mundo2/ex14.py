def exibir_mensagem(nome):
    print(f' Seja bem vindo {nome}')


exibir_mensagem('Bruno')


def salvar_carro(marca, modelo, ano, placa, /, *, chassi, combustível):
    print(f'Veículo cadastrado com sucesso! {marca, modelo, ano, placa, chassi, combustível}')


salvar_carro('Jeep', 'Renegade', 2018, 'KYO6C48', chassi='0094447575554', combustível='flex')
