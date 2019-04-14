import web
import config

db = config.db


def get_all_usuario():
    try:
        return db.select('usuario')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_usuario(email_user):
    try:
        return db.select('usuario', where='email_user=$email_user', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_usuario(email_user):
    try:
        return db.delete('usuario', where='email_user=$email_user', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_usuario(email_user, nombre_user):
    try:
        return db.insert('usuario',email_user=email_user,
        nombre_user=nombre_user)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_usuario(email_user,nombre_user):
    try:
        return db.update('usuario',email_user=email_user,
            nombre_user=nombre_user,
                  where='email_user=$email_user',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
