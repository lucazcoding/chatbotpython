from flask import Flask

app = Flask(__name__)

from routes import *

 #verifica se o código está sendo executado diretamente
                            #tambem tem um controle do servidor permitindo que nossas rotas
                            #sejam acessadas pelo navegador 
if __name__ == '__main__':
    app.run(debug=True)    
                                
    
    