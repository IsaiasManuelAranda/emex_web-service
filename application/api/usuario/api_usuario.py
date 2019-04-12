import web
import config
import json


class Api_usuario:
    def get(self, email_user):
        try:
            # http://0.0.0.0:8080/api_usuario?user_hash=12345&action=get
            if email_user is None:
                result = config.model.get_all_usuario()
                usuario_json = []
                for row in result:
                    tmp = dict(row)
                    usuario_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(usuario_json)
            else:
                # http://0.0.0.0:8080/api_usuario?user_hash=12345&action=get&email_user=1
                result = config.model.get_usuario(int(email_user))
                usuario_json = []
                usuario_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(usuario_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuario_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)

# http://0.0.0.0:8080/api_usuario?user_hash=12345&action=put&email_user=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, ):
        try:
            config.model.insert_usuario()
            usuario_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuario?user_hash=12345&action=delete&email_user=1
    def delete(self, email_user):
        try:
            config.model.delete_usuario(email_user)
            usuario_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuario?user_hash=12345&action=update&email_user=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, email_user, ):
        try:
            config.model.edit_usuario(email_user)
            usuario_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuario_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            email_user=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            email_user=user_data.email_user
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(email_user)
                elif action == 'put':
                    return self.put()
                elif action == 'delete':
                    return self.delete(email_user)
                elif action == 'update':
                    return self.update(email_user, )
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
