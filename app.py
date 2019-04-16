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

    '/reportes', 'application.controllers.reportes.index.Index',
    '/reportes/view/(.+)', 'application.controllers.reportes.view.View',
    '/reportes/edit/(.+)', 'application.controllers.reportes.edit.Edit',
    '/reportes/delete/(.+)', 'application.controllers.reportes.delete.Delete',
    '/reportes/insert', 'application.controllers.reportes.insert.Insert',

    '/api_reportes/?', 'application.api.reportes.api_reportes.Api_reportes',
    
    #'/api_table_name/?', 'application.api.table_name.api_table_name.Api_table_name',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()
