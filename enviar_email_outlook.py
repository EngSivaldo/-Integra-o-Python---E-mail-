import win32com.client as win32
import os

outlook = win32.Dispatch("outlook.application")

email = outlook.CreateItem(0)

email.To = "falseta_fake_0@hotmail.com"
email.Cc = "pythonimpressionador@gmail.com;falseta_fake+copia@hotmail.com"
email.Bcc = "pythonimpressionador+oculto@gmail.com"
email.Subject = "Email enviado pelo Outlook"
# email.Body = "Texto do email"
email.HTMLBody = """<p>Meu primeiro paragrafo</p>"""


email.Send()