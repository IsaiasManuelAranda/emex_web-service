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


def get_usuario(id_user):
    try:
        return db.select('usuario', where='id_user=$id_user', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_usuario(id_user):
    try:
        return db.delete('usuario', where='id_user=$id_user', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_usuario(nombre_user,ape_pat_user,ape_mat_user,telefono_user,email_user,passwd):
    try:
        return db.insert('usuario',nombre_user=nombre_user,
ape_pat_user=ape_pat_user,
ape_mat_user=ape_mat_user,
telefono_user=telefono_user,
email_user=email_user,
passwd=passwd)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_usuario(id_user,nombre_user,ape_pat_user,ape_mat_user,telefono_user,email_user,passwd):
    try:
        return db.update('usuario',id_user=id_user,
nombre_user=nombre_user,
ape_pat_user=ape_pat_user,
ape_mat_user=ape_mat_user,
telefono_user=telefono_user,
email_user=email_user,
passwd=passwd,
                  where='id_user=$id_user',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
