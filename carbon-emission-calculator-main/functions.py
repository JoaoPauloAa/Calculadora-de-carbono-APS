import os
import json
from time import sleep
from typing import List

def clean() -> None:

    os.system('cls' if os.name == 'nt' else 'clear')

def decorator_text(text: str, decorator: str, clean_screen: bool = False, color: str = '32') -> None:

    if clean_screen:

        clean()
    
    

        return

    

def text_formatter(text: str) -> None:

    count = 0

    for letter in text:

        print(letter, end='')
        
        if letter == ' ':
            count += 1

        if count == 13:
            
            print('\n', end='')
            count = 0

def remove_rs(num: str) -> list:
    
    num = num.lower()
    num = num.replace(',', '.')
    num = num.replace('r', '')
    num = num.replace('s', '')
    num = num.replace('$', '')
    num = num.replace(' ', '')

    try:
        return [float(num), True]
    except ValueError:
        return [num, False]

def number_formatter(num) -> str:

    count = 0
    sum = 0

    num2 = str(num).replace('.', ',')

    new_num = ''

    for number in num2[::-1]:

        new_num += number

        count += 1

        if number == ',':

            count = 0
            sum = 3
        
        if count % 3 == 0 and count != 0 and count + sum < len(str(num2)):

            new_num += '.'

    return f'{new_num[::-1]}'

def receive_company_sector() -> list:

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    print('''Qual tipo de empresa você opera? 

[0] Sair

[1] Varejo

[2] Software  

[3] Serviços

[4] Indústria

[5] Outro''')

    quit = False
    company_sector = False

    while not company_sector:

        company_sector = input('Escolha do Usuário:  ').strip().lower().replace('á', 'a').replace('ç', 'c').replace('ú', 'u')

        if company_sector == '1' or company_sector == 'varejo':

            company_sector = 'Varejo'

        elif company_sector == '2' or company_sector == 'software':
            
            company_sector = 'Software'

        elif company_sector == '3' or company_sector == 'serviços':

            company_sector = 'Serviços'

        elif company_sector == '4' or company_sector == 'indústria':

            company_sector = 'Indústria'

        elif company_sector == '5' or company_sector == 'outro':

            company_sector = 'Outro'

        elif company_sector == '0' or company_sector == 'sair': 
            
            quit = True
            company_sector = True
        
        else:

            company_sector = False

    return [company_sector, quit]

def check_fuel_expenditure() -> list:

    decorator_text('calculadora de Emissões de Carbono', '=', clean_screen=True)
    
    valid = False
    avg_fuel = 0
    while not valid:
        
        text_formatter('No último ano, qual a média de gasto da sua empresa com combustível em R$)?: ')
        
        avg_fuel, valid = remove_rs(input(''))

        if not valid: print('Insira um valor válido')
                
    decorator_text('calculadora de Emissões de Carbono', '=', clean_screen=True)

    print('''Qual o principal typo de combustível utilizado pela empresa?

[0] Sair

[1] Diesel

[2] Gasolina  

[3] Etanol

[4] Gás Natural''')

    quit = False

    while True:

        main_fuel = input('Escolha do Usuário:  ').strip().lower().replace('á', 'a')

        if main_fuel == '1' or main_fuel == 'diesel':

            main_fuel = 1
            multiplier = 0.0042
            break

        elif main_fuel == '2' or main_fuel == 'gasolina':

            main_fuel = 2
            multiplier = 0.003504
            break

        elif main_fuel == '3' or main_fuel == 'etanol':

            main_fuel = 3
            multiplier = 0.000024
            break

        elif main_fuel == '4' or main_fuel == 'gas natural':

            main_fuel = 4
            multiplier = 0.006708
            break

        elif main_fuel == '0' or main_fuel == 'sair': 
            
            multiplier = 0
            quit = True

            break
            
        else: main_fuel = 0

    annual_issue1 = avg_fuel * multiplier

    return [annual_issue1, quit]

def check_energy_expenditure(workers: int, sector: int) -> list:

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    quit = False

    while True:

        avg_energy_bill = input('Qual o valor médio do gasto mensal com energia (R$)?: ')

        avg_energy_bill, valid = remove_rs(avg_energy_bill)

        if not valid:

            print('Digite um valor válido')
        
        else: break

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    print('''A empresa utiliza energia solar? 

[0] Sair

[1] Não

[2] comprada de uma fazenda solar 

[3] Geração própria
''')

    while True:

        solar_energy = input('Escolha do Usuário: ').strip().lower().replace('ã', 'a')

        if solar_energy == '1' or solar_energy =='nao':

            if sector == 'Indústria' or sector == 'Outro':
            
                multiplier = 0.002424
            
            else:
            
                multiplier = 0.002136

            break

        if solar_energy == '2':

            if sector == 'Indústria' or sector == 'Outro': multiplier = 0.000936

            else: multiplier = 0.000816

            break

        if solar_energy == '3':

            if sector == 'Indústria' or sector == 'Outro': multiplier = 0.004728
            
            else: multiplier = 0.004164
            
            break

        if solar_energy == '0' or solar_energy == 'sair':
            
            quit = True
            multiplier = 0
            break
    
    if quit: return [0, quit]

    workers_emission, quit = calculate_distribution_workers(workers)
    
    energy_emission = avg_energy_bill * multiplier

    annual_emission2 = workers_emission + energy_emission

    return [annual_emission2, quit]

def calculate_distribution_workers(workers: int) -> list:

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    print('''Como se aplicam os seus funcionarios

[0] Sair

[1] Majoritariamente presencial

[2] Híbrido

[3] Majoritariamente remoto
''')

    quit = False

    while True:

        distribution_workers = input('Escolha do Usuário: ').strip().lower().replace('í', 'i')

        if distribution_workers == '1' or distribution_workers == 'majoritariamente presencial':

            multiplier_workers = 0
            break

        if distribution_workers == '2' or distribution_workers == 'hibrido':

            multiplier_workers = 0.1
            break

        if distribution_workers == '3' or distribution_workers == 'majoritariamente remoto':

            multiplier_workers = 0.2
            break

        if distribution_workers == '0' or distribution_workers == 'sair':
            
            quit = True
            multiplier_workers = 0
            break 
    
    return [workers*multiplier_workers, quit]

def check_number_deliveries() -> int:

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    print('''Quantas vendas com frete sua empresa faz por mês?

[1] 0

[2] 1 - 200

[3] 200 - 500

[4] 500 - 1000

[5] 1000 - 2000

[6] Outro

Observação: considere aqui somente o frete entregue por uma empresa terceira (e.g. correios, loggi, etc.)''')
    
    while True:
        
        deliveries = input('Escolha do Usuário:').strip().lower()

        if deliveries == '1':

            deliveries = 0
            break

        if deliveries == '2' or deliveries == '1 - 200':

            deliveries = 100
            break

        if deliveries == '3' or deliveries == '200 - 500':
            deliveries = 350
            break

        if deliveries == '4' or deliveries == '500 - 1000':
            deliveries = 750
            break

        if deliveries == '5' or deliveries == '1000 - 2000':
            deliveries = 1500
            break
        
        if deliveries == '6' or deliveries == 'outro':

            while True:
                
                deliveries = input('\nInforme a quantidade de entregas por mês: ').strip().replace(',', '.')
                try:
                    deliveries = int(deliveries)
                    break

                except ValueError:
                    print('Digite um valor válido')

            break
    
    return deliveries

def receive_deliveries_weight() -> float:

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    while True:
        
        weight = input('Qual o peso médio do pacote que você envia no frete em quilos(kg)?: ').lower().strip()

        if weight.replace('k', '').replace('g', '').isnumeric():

            weight = weight.replace('k', '').replace('g', '')

            break

    return float(weight)

def location_consumers_is_1(locations_consumers: str, is_industry: bool) -> List[float]:

    if locations_consumers == '1':

        if is_industry:

            return [0.00432, 0.000171]
        
        return [0.0044055, 0]

    return [0, 0]

def location_consumers_is_2(locations_consumers: str, is_industry: bool) -> List[float]:

    if locations_consumers == '2':

        if is_industry:

            return [0.00432, 0.00042]
        
        return [0.00453, 0]

    return [0, 0]

def location_consumers_is_3(locations_consumers: str, is_industry: bool) -> List[float]:

    if locations_consumers == '3':

        if is_industry:

            return [0.00432, 0.00156]
        
        return [0.0051, 0]

    return [0, 0]

def location_consumers_is_4(locations_consumers: str, is_industry: bool) -> List[float]:

    if locations_consumers == '4':

        if is_industry:

            return [0.00432, 0.0036]
        
        return [0.00612, 0]

    return [0, 0]

def check_location_consumers(deliveries: int, company_sector: str) -> float:

    is_industry = False

    weight = 0

    if company_sector == 'Indústria' or company_sector == 'Outro':

        weight = receive_deliveries_weight()

        is_industry = True

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    print('''Onde se localizam a maioria dos seus consumidores? 

[1] Perto do meu município (até 50 km distante)

[2] Dentro do meu estado (50km a 300 km)

[3] Em um estado vizinho (300km a 1000 km)

[4] Em outra região do país (1000km a 2000 km)
''')

    while True:

        locations_consumers = input('Escolha do Usuário: ').strip()
        
        multiplier, multiplier2 = location_consumers_is_1(locations_consumers, is_industry)
        if multiplier == 0: multiplier, multiplier2 = location_consumers_is_2(locations_consumers, is_industry)
        if multiplier == 0: multiplier, multiplier2 = location_consumers_is_3(locations_consumers, is_industry)
        if multiplier == 0: multiplier, multiplier2 = location_consumers_is_4(locations_consumers, is_industry)

        if multiplier != 0: break

    if not is_industry:
        
        annual_issue3 = deliveries * multiplier

    else:

        result = 0.00432 * deliveries

        result2 = (multiplier2 * weight) * deliveries

        annual_issue3 = result + result2

    return annual_issue3

def show_details_enterprise() -> bool:

    with open('enterprise.json', encoding='utf-8') as my_json:

        data = json.load(my_json)

    print('Escolha uma das opções abaixo\n')

    for indice, enterprise in enumerate(data['empresas']):
        
        if indice == 0:

            print(f'[0] - Sair\n')

        print(f"[{indice+1}] - {enterprise['nome']}, {enterprise['estado']}, {enterprise['cidade']}")

    while True:

        interprise_choiced = input('Escolha do Usuário: ')

        if interprise_choiced.isnumeric():

            if 0 < int(interprise_choiced) <= len(data['empresas']):
                
                break

        if interprise_choiced == '0':

            break
    
    if interprise_choiced == '0':
        
        return True

    interprise_choiced = int(interprise_choiced)-1

    info_interprise = data['empresas'][interprise_choiced]

    values = list(info_interprise['dados'].values())

    count = 0

    decorator_text('INFORMAÇÕES DA EMPRESA', '=', clean_screen=True)

    print(f'| Empresa: {info_interprise["nome"]}')
    print(f'| Estado: {info_interprise["estado"]}')
    print(f'| Cidade: {info_interprise["cidade"]}\n')

    decorator_text('dados da empresa', '=')

    for info in info_interprise['dados']:
        
        if info.title() == 'Gasto Combustivel' or info.title() == 'Gasto Energia':

            text = f'| {info.title()}: R$ {number_formatter(values[count])}'

            print(text)

        elif info.title() == 'Localizacao Consumidor':

            print(f'| {info.title()}: {number_formatter(values[count])}Km')

        elif info.title() == 'Peso Frete':

            print(f'| {info.title()}: {number_formatter(values[count])}Kg')
        
        elif info.title() == 'Co2 Emitido':

            print(f'| {info.title()}: {number_formatter(round(values[count]))}T')

        else:

            print(f'| {info.title()}: {values[count]}')
        
        count += 1

    return False

def receive_number_workers() -> int:

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    while True:

        workers = input('Quantos funcionarios trabalham em sua empresa: ')

        try:

            workers = int(workers)
            break
        
        except ValueError:

            print('Digite um valor válido')

    return workers

def user_says_informations() -> bool:

#                                                           # CHECANDO SETOR DA EMPRESA

    company_sector, quit = receive_company_sector()

    if quit: return True

#                                                 # CHECANDO QUANTIDADE DE FUNCIONÁRIOS NA EMPRESA

    workers: int = receive_number_workers()
            
#                                                         # CHECANDO GASTO COM COMBUSTIVEL

    annual_emission1, quit = check_fuel_expenditure()

    if quit: return True

#                                                           # CHECANDO GASTO COM ENERGIA

    annual_emission2, quit = check_energy_expenditure(workers, company_sector)

    if quit: return True

#                                                                 # CHECANDO FRETE

    deliveries = check_number_deliveries()

    if deliveries != 0:

        
        annual_emission3 = check_location_consumers(deliveries, company_sector)

    else:

        annual_emission3 = 0
#                                                      # MOSTRANDO A EMISSÃO DE CARBONO AO USUÁRIO

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

    total_annual_emission = round(annual_emission1 + annual_emission2 + annual_emission3)

    min_value = round(total_annual_emission * 12)
    
    max_value = round(total_annual_emission * 365)


    print(f'Sua pegada de carbono anual é de {number_formatter(total_annual_emission)} Toneladas')

    print('\nUm Crédito de Carbono equivale a 1 Tonelada de Carbono.')
    
    print(f'\nLogo, sua empresa terá que comprar {number_formatter(total_annual_emission)} Créditos.')

    print('\nO Crédito de Carbono no Brasil varia entre R$12,00 e R$365,00')

    print(f'\nSua empresa gastará por volta de R${number_formatter(min_value)},00 e R${number_formatter(max_value)},00')

    input('Pressione enter para continuar')

    return False

def user_only_sees() -> None:

    decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)
    
    result = show_details_enterprise()

    if not result: input('Pressione enter para continuar...')

def engine():

    while True:

        while True:

            decorator_text('calculadora de Emissão de Carbono', '=', clean_screen=True)

            user_choice = input('''Escolha uma das opções abaixo
              
[0] Sair

[1] Escolher uma empresa já calculada

[2] Fazer calculo de sua empresa  

 Escolha do Usuário:''')  # CHECANDO DO USUÁRIO 


            if user_choice == '0':  # ENCERRA O PROGRAMA

                break
                
            if user_choice == '2':  # PEDINDO OS DADOS PARA O USUÁRIO
            
                result = user_says_informations()

                if result: continue

            if user_choice == '1':  # MOSTRANDO OS DADOS DA EMPRESA ESCOLHIDA PELO USUÁRIO
                
                user_only_sees()
                
                break
        
        if user_choice == '1': continue

        text = 'Obrigado por experimentar esta aplicação!'
        
        for letter in text:

            print(letter, end='')
            sleep(0.0225)

        print()
        break
