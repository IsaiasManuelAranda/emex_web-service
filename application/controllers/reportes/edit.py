import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_reporte, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_reporte) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_reporte, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_reporte) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_reporte, **k):

    @staticmethod
    def POST_EDIT(id_reporte, **k):
        
    '''

    def GET(self, id_reporte, **k):
        message = None # Error message
        id_reporte = config.check_secure_val(str(id_reporte)) # HMAC id_reporte validate
        result = config.model.get_reportes(int(id_reporte)) # search for the id_reporte
        result.id_reporte = config.make_secure_val(str(result.id_reporte)) # apply HMAC for id_reporte
        return config.render.edit(result, message) # render reportes edit.html

    def POST(self, id_reporte, **k):
        form = config.web.input()  # get form data
        form['id_reporte'] = config.check_secure_val(str(form['id_reporte'])) # HMAC id_reporte validate
        # edit user with new data
        result = config.model.edit_reportes(
            form['id_reporte'],form['nombre'],form['edad'],form['latitud'],form['longitud'],
        )
        if result == None: # Error on udpate data
            id_reporte = config.check_secure_val(str(id_reporte)) # validate HMAC id_reporte
            result = config.model.get_reportes(int(id_reporte)) # search for id_reporte data
            result.id_reporte = config.make_secure_val(str(result.id_reporte)) # apply HMAC to id_reporte
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/reportes') # render reportes index.html
