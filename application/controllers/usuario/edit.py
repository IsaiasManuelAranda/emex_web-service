import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, email_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(email_user) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, email_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(email_user) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(email_user, **k):

    @staticmethod
    def POST_EDIT(email_user, **k):
        
    '''

    def GET(self, email_user, **k):
        message = None # Error message
        email_user = config.check_secure_val(str(email_user)) # HMAC email_user validate
        result = config.model.get_usuario(int(email_user)) # search for the email_user
        result.email_user = config.make_secure_val(str(result.email_user)) # apply HMAC for email_user
        return config.render.edit(result, message) # render usuario edit.html

    def POST(self, email_user, **k):
        form = config.web.input()  # get form data
        form['email_user'] = config.check_secure_val(str(form['email_user'])) # HMAC email_user validate
        # edit user with new data
        result = config.model.edit_usuario(
            form['email_user'],form['nombre_user'],
        )
        if result == None: # Error on udpate data
            email_user = config.check_secure_val(str(email_user)) # validate HMAC email_user
            result = config.model.get_usuario(int(email_user)) # search for email_user data
            result.email_user = config.make_secure_val(str(result.email_user)) # apply HMAC to email_user
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/usuario') # render usuario index.html
