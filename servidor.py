from flask import Flask, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


@app.route('/enviar', methods=['POST'])
def enviar_correo():
    nombre = request.form.get('nombre')
    correo_reclutador = request.form.get('correo')
    mensaje_reclutador = request.form.get('mensaje')

    
    print("\n" + "="*50)
    print("💼 ¡NUEVO MENSAJE DE TRABAJO RECIBIDO!")
    print(f"👤 De: {nombre} ({correo_reclutador})")
    print(f"📝 Mensaje: {mensaje_reclutador}")
    print("="*50 + "\n")

   
    
    '''
    try:
        msg = EmailMessage()
        msg['Subject'] = f'Nuevo contacto de Portafolio: {nombre}'
        msg['From'] = "tu_correo_de_envio@outlook.com"
        msg['To'] = "anima2545@outlook.com"
        msg.set_content(f"Nombre: {nombre}\nCorreo: {correo_reclutador}\nMensaje:\n{mensaje_reclutador}")

        # Conexión al servidor de Outlook
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login("tu_correo_de_envio@outlook.com", "TU_CONTRASEÑA_DE_APLICACION")
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Error al enviar el correo:", e)
    '''

    
    return """
    <body style="background-color: #e0cdb5; text-align: center; font-family: 'Montserrat', sans-serif;">
        <h1 style="color: #2c3e50; margin-top: 100px;">¡Mensaje enviado con éxito!</h1>
        <p style="color: #383733; font-size: 18px;">Gracias por contactarme. Me pondré en contacto contigo a la brevedad.</p>
        <button onclick="history.back()" style="background-color: #8F7454; color: white; padding: 15px 30px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 20px;">Volver al Portafolio</button>
    </body>
    """

if __name__ == '__main__':
    
    app.run(port=5000)