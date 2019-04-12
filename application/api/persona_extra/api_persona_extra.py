import web
import config
import json


class Api_persona_extra:
    def get(self, id_persona):
        try:
            # http://0.0.0.0:8080/api_persona_extra?user_hash=12345&action=get
            if id_persona is None:
                result = config.model.get_all_persona_extra()
                persona_extra_json = []
                for row in result:
                    tmp = dict(row)
                    persona_extra_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(persona_extra_json)
            else:
                # http://0.0.0.0:8080/api_persona_extra?user_hash=12345&action=get&id_persona=1
                result = config.model.get_persona_extra(int(id_persona))
                persona_extra_json = []
                persona_extra_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(persona_extra_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            persona_extra_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(persona_extra_json)

# http://0.0.0.0:8080/api_persona_extra?user_hash=12345&action=put&id_persona=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user):
        try:
            config.model.insert_persona_extra(nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user)
            persona_extra_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(persona_extra_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_persona_extra?user_hash=12345&action=delete&id_persona=1
    def delete(self, id_persona):
        try:
            config.model.delete_persona_extra(id_persona)
            persona_extra_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(persona_extra_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_persona_extra?user_hash=12345&action=update&id_persona=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_persona, nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user):
        try:
            config.model.edit_persona_extra(id_persona,nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user)
            persona_extra_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(persona_extra_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            persona_extra_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(persona_extra_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_persona=None,
            nombre_persona=None,
            ape_pat_persona=None,
            ape_mat_persona=None,
            edad=None,
            fecha_extravio=None,
            curp_persona=None,
            sexo=None,
            email_user=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_persona=user_data.id_persona
            nombre_persona=user_data.nombre_persona
            ape_pat_persona=user_data.ape_pat_persona
            ape_mat_persona=user_data.ape_mat_persona
            edad=user_data.edad
            fecha_extravio=user_data.fecha_extravio
            curp_persona=user_data.curp_persona
            sexo=user_data.sexo
            email_user=user_data.email_user
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_persona)
                elif action == 'put':
                    return self.put(nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user)
                elif action == 'delete':
                    return self.delete(id_persona)
                elif action == 'update':
                    return self.update(id_persona, nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
