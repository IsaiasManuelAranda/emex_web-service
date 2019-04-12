import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, email_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(email_user) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, email_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(email_user) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(email_user, **k):

    @staticmethod
    def POST_DELETE(email_user, **k):
    '''

    def GET(self, email_user, **k):
        message = None # Error message
        email_user = config.check_secure_val(str(email_user)) # HMAC email_user validate
        result = config.model.get_usuario(int(email_user)) # search  email_user
        result.email_user = config.make_secure_val(str(result.email_user)) # apply HMAC for email_user
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, email_user, **k):
        form = config.web.input() # get form data
        form['email_user'] = config.check_secure_val(str(form['email_user'])) # HMAC email_user validate
        result = config.model.delete_usuario(form['email_user']) # get usuario data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            email_user = config.check_secure_val(str(email_user))  # HMAC user validate
            email_user = config.check_secure_val(str(email_user))  # HMAC user validate
            result = config.model.get_usuario(int(email_user)) # get email_user data
            result.email_user = config.make_secure_val(str(result.email_user)) # apply HMAC to email_user
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/usuario') # render usuario delete.html 
