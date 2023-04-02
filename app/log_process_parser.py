"""
Observe que este exemplo é apenas uma simplificação e
deve ser adaptado ao formato e estrutura específicos do arquivo de log
que você está trabalhando.
Defina o padrão do log com a sintaxe do Grok.
Por exemplo, se o seu arquivo de log contiver registros no formato IP: 127.0.0.1, User: fulano, Message: Olá, mundo!,
você pode definir o seguinte padrão do Grok:
"""
import pygrok
import parser

log_file = open('log_file.log', 'r')
lines = log_file.readlines()
log_file.close()

pattern = '%{IP:ip_address}, User: %{WORD:user}, Message: %{GREEDYDATA:message}'

parsed_logs = []

for line in lines:
    parsed_logs.append(pygrok.parse(line, pattern))

output_file = open('log_file_processado_parse.log', 'w')

for log in parsed_logs:
    output_file.write(str(log) + '\n')
output_file.close()
