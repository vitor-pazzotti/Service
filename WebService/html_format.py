def home():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        body{
            }
        
        h1   {color: red;}
        p    {color: black;}
        .div-pai {
            display: flex;
        }
        .div-text {
            background-color: white;
            width: 40%;
        }
        .div-img {
            width: 60%;
        }
        .div-img img {
            background-color:black;
            width: 20%;
        }
        </style>
        </head>
        <body>
        ''' + f'''
        <div class="div-pai">
            <div class="div-text">

                <h1>Home</h1>
                <p> Exemplos de Funções presentes para utilização: </p>
                <li>Números Romanos: <form action="http://0.0.0.0:8080/romano/45"><input type="submit" value="Submit"></form></li>
                <p><small>Link Romano : http://0.0.0.0:8080/romano/defina_valor </small></p><br />
                <li>Validador de CPF: <form action="http://0.0.0.0:8080/valida_cpf/485.111.048-01"> <input type="submit" value="Submit"></form></li>
                <p><small>http://0.0.0.0:8080/valida_cpf/defina_valor</small></p><br />
                <li>Distância de Zeros: <form action="http://0.0.0.0:8080/dist_zeros/a 00000000 a0 0000000000000"> <input type="submit" value="Submit"></form></li>
                <p><small>http://0.0.0.0:8080/dist_zeros/definal_valor</small></p><br />
                <li>Gerador de Senha: <form action="http://0.0.0.0:8080/gera_senha"> <input type="submit" value="Submit"></form></li>
                <p><small>http://0.0.0.0:8080/gera_senha</small></p>

            </div>
            <div class="div-img"> 
                <img src="https://www.abcdacomunicacao.com.br/wp-content/uploads/SEMANTIX-LOGO.jpg" align="center" />
            </div>
        </div>

        </body>
        </html>
    '''

def romanos(parameter):
    return '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        body{
            background-color : PaleGreen   ;
            }
        div{
            color : pink;
            background: white;
            display: flex;
            font-weight : 300;
            flex-direction: column;
            justify-content: center;
            text-align: center;
            line-height : 600px;
            margin : 0 0 16px;
        }
        </style>
        </head>
        <body>
        ''' + f''' 
        <div class="text">
            <h1> {parameter} </h1>
        </div>
        </body>
        </html>
    '''

def validacao(num, cpf):
    if cpf != 'CPF Inválido':
        return '''
            <!DOCTYPE html>
            <html>
            <head>
            <style>
            body{
                background-color : #e6ffe6;
                }
            .text h1,
            .text h2{
                color : #ff4d4d;
                background: #99ff99;
                display: flex;
                font-weight : 100;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                line-height : 200px;
                margin : 0 0 16px;
                font-family : Courier New;
            }
            </style>
            </head>
            <body>
            ''' + f''' 
            <div class="text">
                <h1>CPF ~~> {num}</h1>
                <h2> {cpf}</h2>
            </div>
            </body>
            </html>
        '''
    else:
        return '''
            <!DOCTYPE html>
            <html>
            <head>
            <style>
            body{
                background-color : #e6ffe6;
                }
            .text h1,
            .text h2{
                color : #ffffcc;
                background: #ff1a1a;
                display: flex;
                font-weight : 100;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                line-height : 200px;
                margin : 0 0 16px;
                font-family : Courier New;
            }
            </style>
            </head>
            <body>
            ''' + f''' 
            <div class="text">
                <h1>CPF ~~> {num}</h1>
                <h2> {cpf}</h2>
            </div>
            </body>
            </html>
        '''

def distancias(value):
    return '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        body{
            background-color : #ef6946;
            }
        .text h1{
            color : #000000;
            background:#efccff;
            top: 50px;
            border: 3px solid #ffffff;
            position: fixed;
            top: 50%;
            left: 50%;
              transform: translate(-50%, -50%);
          }
        }
        </style>
        </head>
        <body>
        ''' + f''' 
        <div class="text">
            <h1>A maior distância de zeros é ~~> {value}</h1>
        </div>
        
        </body>
        </html>
    '''
