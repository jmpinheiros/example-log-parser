
log_file = open('log_file.log', 'r')
output_file = open('log_file_processado_noparse.log', 'w')


def log_process(log_file, output_file):

    for line in log_file:
        # Separe a linha em campos usando um separador específico, por exemplo, uma vírgula
        fields = line.strip().split(',')

        # Extraia as informações necessárias de cada campo
        ip_address = fields[0]
        user = fields[1]
        message = fields[2]

        # Crie uma nova string com as informações processadas
        processed_line = f"IP: {ip_address}, User: {user}, Message: {message}"

        # Escreva a nova string no arquivo de saída
        output_file.write(processed_line + '\n')

    log_file.close()
    output_file.close()

    return 'sucess process'


print(log_process(log_file, output_file))
