import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_user) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_user) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_user, **k):

    @staticmethod
    def POST_EDIT(id_user, **k):
        
    '''

    def GET(self, id_user, **k):
        message = None # Error message
        id_user = config.check_secure_val(str(id_user)) # HMAC id_user validate
        result = config.model.get_usuario(int(id_user)) # search for the id_user
        result.id_user = config.make_secure_val(str(result.id_user)) # apply HMAC for id_user
        return config.render.edit(result, message) # render usuario edit.html

    def POST(self, id_user, **k):
        form = config.web.input()  # get form data
        form['id_user'] = config.check_secure_val(str(form['id_user'])) # HMAC id_user validate
        # edit user with new data
        result = config.model.edit_usuario(
            form['id_user'],form['nombre_user'],form['ape_pat_user'],form['ape_mat_user'],form['telefono_user'],form['email_user'],form['passwd'],
        )
        if result == None: # Error on udpate data
            id_user = config.check_secure_val(str(id_user)) # validate HMAC id_user
            result = config.model.get_usuario(int(id_user)) # search for id_user data
            result.id_user = config.make_secure_val(str(result.id_user)) # apply HMAC to id_user
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/usuario') # render usuario index.html
