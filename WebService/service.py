from aiohttp import web
from romanos import transform_roman
from cpf import cpf, valida
from distancia_zero import conta_texto
from senha import geraSenha, valida_senha, hash_md5

routes = web.RouteTableDef()

@routes.get('/romano/{numero}')
async def romano(request):
    var = int(request.match_info['numero'])
    num = transform_roman(var)
    
    return web.Response(text=num)
app = web.Application()
app.add_routes([web.get('/romano/{numero}', romano)])

@routes.get('/valida_cpf/{cpf}')
async def cpf_request(request):
    var = str(request.match_info['cpf'])
    num = cpf(var)
    value = valida(var)

    return web.Response(text=f'CPF: {num} - {value}')
app = web.Application()
app.add_routes([web.get('/valida_cpf/{cpf}', cpf_request)])

@routes.get('/dist_zeros/{string}')
async def dist_zeros(request):
    var = str(request.match_info['string'])
    num = conta_texto(var)
    
    return web.Response(text=num)
app = web.Application()
app.add_routes([web.get('/dist_zeros/{string}', dist_zeros)])

@routes.get('/gera_senha')
async def gera_senha(request):
    senha = geraSenha()
    valida = valida_senha(senha)
    hash_senha = hash_md5(senha)

    return web.Response(text=f'Sua senha é: {senha}\nClassificação: {valida}\nHash: {hash_senha} ')
app = web.Application()
app.add_routes([web.get('/gera_senha', gera_senha)])
    

web.run_app(app)