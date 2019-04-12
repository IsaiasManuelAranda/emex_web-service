import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_persona, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_persona) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_persona, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_persona) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_persona, **k):

    @staticmethod
    def POST_EDIT(id_persona, **k):
        
    '''

    def GET(self, id_persona, **k):
        message = None # Error message
        id_persona = config.check_secure_val(str(id_persona)) # HMAC id_persona validate
        result = config.model.get_persona_extra(int(id_persona)) # search for the id_persona
        result.id_persona = config.make_secure_val(str(result.id_persona)) # apply HMAC for id_persona
        return config.render.edit(result, message) # render persona_extra edit.html

    def POST(self, id_persona, **k):
        form = config.web.input()  # get form data
        form['id_persona'] = config.check_secure_val(str(form['id_persona'])) # HMAC id_persona validate
        # edit user with new data
        result = config.model.edit_persona_extra(
            form['id_persona'],form['nombre_persona'],form['ape_pat_persona'],form['ape_mat_persona'],form['edad'],form['fecha_extravio'],form['curp_persona'],form['sexo'],form['email_user'],
        )
        if result == None: # Error on udpate data
            id_persona = config.check_secure_val(str(id_persona)) # validate HMAC id_persona
            result = config.model.get_persona_extra(int(id_persona)) # search for id_persona data
            result.id_persona = config.make_secure_val(str(result.id_persona)) # apply HMAC to id_persona
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/persona_extra') # render persona_extra index.html
