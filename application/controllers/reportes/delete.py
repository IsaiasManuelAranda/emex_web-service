import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_reporte, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_reporte) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_reporte, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_reporte) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_reporte, **k):

    @staticmethod
    def POST_DELETE(id_reporte, **k):
    '''

    def GET(self, id_reporte, **k):
        message = None # Error message
        id_reporte = config.check_secure_val(str(id_reporte)) # HMAC id_reporte validate
        result = config.model.get_reportes(int(id_reporte)) # search  id_reporte
        result.id_reporte = config.make_secure_val(str(result.id_reporte)) # apply HMAC for id_reporte
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_reporte, **k):
        form = config.web.input() # get form data
        form['id_reporte'] = config.check_secure_val(str(form['id_reporte'])) # HMAC id_reporte validate
        result = config.model.delete_reportes(form['id_reporte']) # get reportes data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_reporte = config.check_secure_val(str(id_reporte))  # HMAC user validate
            id_reporte = config.check_secure_val(str(id_reporte))  # HMAC user validate
            result = config.model.get_reportes(int(id_reporte)) # get id_reporte data
            result.id_reporte = config.make_secure_val(str(result.id_reporte)) # apply HMAC to id_reporte
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/reportes') # render reportes delete.html 
