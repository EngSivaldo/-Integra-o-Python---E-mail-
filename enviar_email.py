import smtplib
import email.message

def enviar_email():
    msg = email.message.EmailMessage()
    msg['Subject'] = 'email enviado com python'
    msg['From'] = 'engsoftwaresivaldoalmeida@gmail.com'
    msg['To'] = 'engsoftwaresivaldoalmeida@gmail.com'
    msg['Cc'] = 'engsoftwaresivaldoalmeida+copia@gmail.com'
    msg['Bcc'] = 'engsoftwaresivaldoalmeida@gmail.com'
    
    corpo_email = '<p>Boa tarde</p>'
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    
    # Substitua 'sua_senha_aqui' pela sua senha de aplicativo gerada pelo Google
    servidor.login(msg['From'], 'senha app')
    
    servidor.send_message(msg)
    servidor.quit()
    print('email enviado')

enviar_email()
