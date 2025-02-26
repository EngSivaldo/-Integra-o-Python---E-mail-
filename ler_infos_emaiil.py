from imap_tools import MailBox, AND

usuario = "engsoftwaresivaldoalmeida@gmail.com"
senha = "fpxp cqpq yysm jmrr"

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

# ver as pastas do meu email disponíveis
# for pasta in meu_email.folder.list():
#     print(pasta)

# meu_email.folder.set('[Gmail]/E-mails enviados')

lista_emails = meu_email.fetch(AND(from_="engsoftwaresivaldoalmeida@gmail.com", to="sivaldovieiradealmeida@gmail.com"))


# for email in lista_emails:
#     if len(email.attachments) > 0:
#         print(email.subject)
#         print(email.text)
#         print(email.html)
#         for anexo in email.attachments:
#             print("Anexo:", anexo.filename)
