import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_user) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_user, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_user) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_user, **k):

    @staticmethod
    def POST_DELETE(id_user, **k):
    '''

    def GET(self, id_user, **k):
        message = None # Error message
        id_user = config.check_secure_val(str(id_user)) # HMAC id_user validate
        result = config.model.get_usuario(int(id_user)) # search  id_user
        result.id_user = config.make_secure_val(str(result.id_user)) # apply HMAC for id_user
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_user, **k):
        form = config.web.input() # get form data
        form['id_user'] = config.check_secure_val(str(form['id_user'])) # HMAC id_user validate
        result = config.model.delete_usuario(form['id_user']) # get usuario data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_user = config.check_secure_val(str(id_user))  # HMAC user validate
            id_user = config.check_secure_val(str(id_user))  # HMAC user validate
            result = config.model.get_usuario(int(id_user)) # get id_user data
            result.id_user = config.make_secure_val(str(result.id_user)) # apply HMAC to id_user
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/usuario') # render usuario delete.html 
