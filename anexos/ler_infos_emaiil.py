from imap_tools import MailBox, AND

# Definindo credenciais de login
usuario = "engsoftwaresivaldoalmeida@gmail.com"
senha = "fpxp cqpq yysm jmrr"  # Use a senha de aplicativo gerada pelo Google

# Conectando à caixa de correio
meu_email = MailBox("imap.gmail.com").login(usuario, senha)

# (Comentado) Ver as pastas do meu email disponíveis
# for pasta in meu_email.folder.list():
#     print(pasta)

# (Comentado) Selecionar a pasta '[Gmail]/E-mails enviados'
# meu_email.folder.set('[Gmail]/E-mails enviados')

# Buscando emails enviados de e para o seu próprio endereço
lista_emails = meu_email.fetch(AND(from_="engsoftwaresivaldoalmeida@gmail.com", to="engsoftwaresivaldoalmeida@gmail.com"))

# Iterando sobre os emails encontrados
for email in lista_emails:
    if len(email.attachments) > 0:  # Verifica se o email tem anexos
        print(email.subject)  # Imprime o assunto do email
        print(email.text)     # Imprime o texto do email
        print(email.html)     # Imprime o conteúdo HTML do email
        for anexo in email.attachments:  # Itera sobre os anexos do email
            print("Anexo:", anexo.filename)  # Imprime o nome do arquivo anexo
