import smtplib
import email.message

def enviar_email():
    msg = email.message.EmailMessage()
    msg['Subject'] = 'email enviado com python'
    msg['From'] = 'engsoftwaresivaldoalmeida@gmail.com'
    msg['To'] = 'lucas2000@gmail.com'
    msg['Cc'] = 'engsoftwaresivaldoalmeida+copia@gmail.com'
    msg['Bcc'] = 'engsoftwaresivaldoalmeida@gmail.com'
    link_imagem = 'https://png.pngtree.com/png-vector/20220106/ourmid/pngtree-small-fresh-and-lovely-fruit-cartoon-image-longan-longan-vector-material-png-image_4089371.png'
    corpo_email = f"""<p>Boa tarde</p>
    <img src='{link_imagem}'>
    """
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    
    # Substitua 'sua_senha_aqui' pela sua senha de aplicativo gerada pelo Google
    servidor.login(msg['From'], 'fpxp cqpq yysm jmrr')
    
    servidor.send_message(msg)
    servidor.quit()
    print('email enviado')

enviar_email()
