import telepot
import mysql.connector
import traceback
import time
import openpyxl #pip install openpyxl
from config import TOKEN, DB_HOST, DB_USER, DB_PASS, DB_NAME, waiting_for_input, nomes_tec_array

# Agora você pode usar essas variáveis normalmente
print(DB_HOST)

# Conectar ao banco de dados
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
cursor = db_connection.cursor()

# Função para apresentar o menu
def show_menu(chat_id):
    menu = "Opções de Consulta:\n"
    menu += "/menu - Menu\n\n"
    menu += "/dados - Consultar todas as Ordem de Serviços\n"
    menu += "/tec_atendimento - Tecnicos Em atendimento\n"
    menu += "/nao_atendida - OS sem Atendimento\n"
    menu += "/solicitacao - Consultar em Solicitação\n"
    menu += "/aberto - Consultar em Aberto\n\n"
    menu += "/os_manu - OS da Manutenção\n"
    menu += "/os_bancada - OS da Bancada\n"
    menu += "/os_suporte - OS da Suporte\n"
    menu += "/os_ti_adm - OS da TI ADM\n"
    menu += "/tec_garden - Localização do Tec. Garden\n"
    menu += "/tec_g_peres - Localização do Tec. Gabirel Peres\n"
    menu += "/tec_g_neves - Localização do Tec. Gabriel Neves\n"
    menu += "/tec_edgar - Localização do Tec. Edgar\n"
    menu += "/tec_herick - Localização do Tec. Herick\n"
    menu += "/tec_kauan - Localização do Tec. Kauan\n"
    menu += "/tec_sara - Localização do Tec. Sara\n"
    menu += "/tec_weslley - Localização do Tec. Weslley\n"
    menu += "/consistorio - Eventos do Consistório\n"
    bot.sendMessage(chat_id, menu)

def handle(msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']

            if command == '/start' or command == '/menu':
                # Mostrar o menu quando o usuário inicia a conversa ou solicita o menu
                show_menu(chat_id)

            elif command == '/dados':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(3)
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os")
                rows = cursor.fetchall()
                 
                # Enviar dados ao usuário
                for row in rows:
                    
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                    time.sleep(1)
#fim                    
            elif command == '/tec_atendimento':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(3)
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os  WHERE nm_servico_descricao = 'Em Atendimento' ORDER BY nm_nome_funcionario ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:

                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                    time.sleep(1)
#fim
            elif command == '/nao_atendida':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(1)
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_servico_descricao IS NULL ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                   bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço:\n Funcionaria: \n Data do Atendimento: \n Horário do Atendimento: \n" , parse_mode='Markdown')
                   time.sleep(1)
#fim
            elif command == '/solicitacao':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(1)
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_solicitacao = 'Solicitação' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                   bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim             
            elif command == '/aberto':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(1)
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_solicitacao = 'Aberto' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                    time.sleep(1)
#fim  
            elif command == '/os_manu':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(1)
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'Manutenção de Computadores' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                    time.sleep(1)
#fim  
            elif command == '/os_bancada':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(1)
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'Bancada' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                    time.sleep(1)
#fim  
            elif command == '/os_suporte':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(1)
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'Suporte' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                    time.sleep(1)
#fim  
            elif command == '/os_ti_adm':
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                time.sleep(1)
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'TI-ADM' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                    time.sleep(1)
#fim  
            elif command == '/tec_garden':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[0]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[0]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/tec_g_peres':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[1]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[1]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/tec_g_neves':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[2]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[2]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/tec_edgar':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[3]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[3]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/tec_herick':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[4]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[4]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/tec_kauan':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[5]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[5]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/tec_sara':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[6]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[6]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/tec_weslley':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                    # Aguardar a mensagem do usuário
                    time.sleep(1)
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nomes_tec_array[7]}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Localização do(a)  *{row[12]} - {nomes_tec_array[7]}*:\n\n CÓDIGO: *{row[0]}*\n Setor: *{row[6]}*\n Localidade: *{row[7]}*\n" , parse_mode='Markdown')
                        time.sleep(1)
#fim                        
            elif command == '/consistorio':
                   # Abrir o arquivo Excel
                workbook = openpyxl.load_workbook('./arquivos/calculo_horas_extras.xlsx')
                sheet = workbook.active

                # Enviar os dados da planilha de volta para o usuário
                bot.sendMessage(chat_id, "Aguarde um momento, por favor:")
                time.sleep(1)
                # Iterar por todas as linhas e colunas da planilha
                for row in sheet.iter_rows(values_only=True):
                    # Converter a linha em uma string formatada
                    row_string = '\n'.join([f"{value}" for value in row])
                    
                    # Enviar a linha de volta para o usuário
                    bot.sendMessage(chat_id, row_string)
#fim                        
            # show_menu(chat_id) ao concluir comando ele exibi o o menu ou clicar qlqr tecla
    except Exception as e:
        traceback.print_exc()

# Configurar e iniciar o bot
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Aguardando comandos...')

# Manter o bot em execução
while True:
    pass
