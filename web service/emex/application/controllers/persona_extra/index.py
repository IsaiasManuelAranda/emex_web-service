import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    '''
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
    '''

    
    def GET(self):
        result = config.model.get_all_persona_extra().list() # get persona_extra table list
        for row in result:
            row.id_persona = config.make_secure_val(str(row.id_persona)) # apply HMAC to id_persona (primary key)
        return config.render.index(result) # render persona_extra index.html
