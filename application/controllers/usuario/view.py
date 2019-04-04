import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_user):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_user) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_user):
    '''

    def GET(self, id_user):
        id_user = config.check_secure_val(str(id_user)) # HMAC id_user validate
        result = config.model.get_usuario(id_user) # search for the id_user data
        return config.render.view(result) # render view.html with id_user data
