import telepot
import mysql.connector
import traceback
import time
from config import TOKEN, DB_HOST, DB_USER, DB_PASS, DB_NAME, waiting_for_input

# Agora você pode usar essas variáveis normalmente
print(TOKEN)
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
    menu += "/consulta_nome - Consultar por nome\n"
    menu += "/consulta_cd_os - Consultar por Ordem de Serviço\n"
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
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os")
                rows = cursor.fetchall()
                 
                # Enviar dados ao usuário
                for row in rows:
                    
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim                    
            elif command == '/tec_atendimento':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os  WHERE nm_servico_descricao = 'Em Atendimento' ORDER BY nm_nome_funcionario ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:

                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim
            elif command == '/nao_atendida':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_servico_descricao IS NULL ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                   bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim
            elif command == '/solicitacao':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_solicitacao = 'Solicitação' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                   bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim             
            elif command == '/aberto':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_solicitacao = 'Aberto' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: {row[5]}\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim  
            elif command == '/os_manu':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'Manutenção de Computadores' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim  
            elif command == '/os_bancada':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'Bancada' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim  
            elif command == '/os_suporte':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'Suporte' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim  
            elif command == '/os_ti_adm':
                # Consulta ao banco de dados
                cursor.execute("SELECT * FROM tb_os WHERE nm_tipo_os = 'TI-ADM' ORDER BY cd_codigo ASC")
                rows = cursor.fetchall()

                # Enviar dados ao usuário
                for row in rows:
                   
                    bot.sendMessage(chat_id, f"CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
#fim  

            elif command == '/consulta_nome':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Por favor, digite o nome:")
                    # Aguardar a mensagem do usuário
                    time.sleep(5)
                    nome = ''  # Obtém o texto da mensagem
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nome}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Resultado da pesquisa para *{nome}*:\n\n CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
# Fim
            elif command == '/consulta_cd_os':
                    # Solicitar nome ao usuário
                    bot.sendMessage(chat_id, "Por favor, digite Numero da OS:")
                    # Aguardar a mensagem do usuário
                    time.sleep(5)
                    nome = ''  # Obtém o texto da mensagem
                    cursor.execute(f"SELECT * FROM tb_os WHERE nm_nome_funcionario = '{nome}' ORDER BY cd_codigo ASC")
                    rows = cursor.fetchall()
                    for row in rows:
                    # Enviar o resultado da pesquisa de volta para o usuário
                        bot.sendMessage(chat_id, f"Resultado da pesquisa para *{nome}*:\n\n CÓDIGO: *{row[0]}*\n\n Descrição da OS: *{row[1]}*\n Data: {row[2]} / Hora: {row[3]}\n\n Tipo Solicitação: {row[4]}\n Tipo OS: *{row[5]}*\n Setor: {row[6]}\n Localidade: {row[7]}\n Oficina: {row[8]}\n Nome do Solicitante: {row[9]}\n Observação: *{row[10]}*\n\n *SERVIÇOS*\n Descrição do Serviço: *{row[11]}*\n Funcionaria: *{row[12]} - {row[13]}*\n Data do Atendimento: {row[14]}\n Horário do Atendimento: {row[15]}\n" , parse_mode='Markdown')
                        # Mostrar o menu novamente
            show_menu(chat_id)
    except Exception as e:
        traceback.print_exc()

# Configurar e iniciar o bot
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Aguardando comandos...')

# Manter o bot em execução
while True:
    pass
