import web
import config
import json


class Api_reportes:
    def get(self, id_reporte):
        try:
            # http://0.0.0.0:8080/api_reportes?user_hash=12345&action=get
            if id_reporte is None:
                result = config.model.get_all_reportes()
                reportes_json = []
                for row in result:
                    tmp = dict(row)
                    reportes_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(reportes_json)
            else:
                # http://0.0.0.0:8080/api_reportes?user_hash=12345&action=get&id_reporte=1
                result = config.model.get_reportes(int(id_reporte))
                reportes_json = []
                reportes_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(reportes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            reportes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(reportes_json)

# http://0.0.0.0:8080/api_reportes?user_hash=12345&action=put&id_reporte=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,edad,latitud,longitud):
        try:
            config.model.insert_reportes(nombre,edad,latitud,longitud)
            reportes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(reportes_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_reportes?user_hash=12345&action=delete&id_reporte=1
    def delete(self, id_reporte):
        try:
            config.model.delete_reportes(id_reporte)
            reportes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(reportes_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_reportes?user_hash=12345&action=update&id_reporte=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_reporte, nombre,edad,latitud,longitud):
        try:
            config.model.edit_reportes(id_reporte,nombre,edad,latitud,longitud)
            reportes_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(reportes_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            reportes_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(reportes_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_reporte=None,
            nombre=None,
            edad=None,
            latitud=None,
            longitud=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_reporte=user_data.id_reporte
            nombre=user_data.nombre
            edad=user_data.edad
            latitud=user_data.latitud
            longitud=user_data.longitud
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_reporte)
                elif action == 'put':
                    return self.put(nombre,edad,latitud,longitud)
                elif action == 'delete':
                    return self.delete(id_reporte)
                elif action == 'update':
                    return self.update(id_reporte, nombre,edad,latitud,longitud)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
