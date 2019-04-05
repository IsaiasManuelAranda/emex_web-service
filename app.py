#Author : Salvador Hernandez Mendoza
#Email  : salvadorhm@gmail.com
#Twitter: @salvadorhm
import web
import application

ssl = False #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    '''
    Use OpenSSL to generate  keys

    user@host$ openssl genrsa -out server.key 1024
    user@host$ openssl req -new -key server.key -out server.csr
    user@host$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

    '''
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

urls = (
    '/', 'application.controllers.main.index.Index',

    '/persona_extra', 'application.controllers.persona_extra.index.Index',
    '/persona_extra/view/(.+)', 'application.controllers.persona_extra.view.View',
    '/persona_extra/edit/(.+)', 'application.controllers.persona_extra.edit.Edit',
    '/persona_extra/delete/(.+)', 'application.controllers.persona_extra.delete.Delete',
    '/persona_extra/insert', 'application.controllers.persona_extra.insert.Insert',

    '/usuario', 'application.controllers.usuario.index.Index',
    '/usuario/view/(.+)', 'application.controllers.usuario.view.View',
    '/usuario/edit/(.+)', 'application.controllers.usuario.edit.Edit',
    '/usuario/delete/(.+)', 'application.controllers.usuario.delete.Delete',
    '/usuario/insert', 'application.controllers.usuario.insert.Insert',
    
    #'/api_table_name/?', 'application.api.table_name.api_table_name.Api_table_name',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
