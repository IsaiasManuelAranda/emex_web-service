import web
import config

db = config.db


def get_all_persona_extra():
    try:
        return db.select('persona_extra')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_persona_extra(id_persona):
    try:
        return db.select('persona_extra', where='id_persona=$id_persona', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_persona_extra(id_persona):
    try:
        return db.delete('persona_extra', where='id_persona=$id_persona', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_persona_extra(nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user):
    try:
        return db.insert('persona_extra',nombre_persona=nombre_persona,
ape_pat_persona=ape_pat_persona,
ape_mat_persona=ape_mat_persona,
edad=edad,
fecha_extravio=fecha_extravio,
curp_persona=curp_persona,
sexo=sexo,
email_user=email_user)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_persona_extra(id_persona,nombre_persona,ape_pat_persona,ape_mat_persona,edad,fecha_extravio,curp_persona,sexo,email_user):
    try:
        return db.update('persona_extra',id_persona=id_persona,
nombre_persona=nombre_persona,
ape_pat_persona=ape_pat_persona,
ape_mat_persona=ape_mat_persona,
edad=edad,
fecha_extravio=fecha_extravio,
curp_persona=curp_persona,
sexo=sexo,
email_user=email_user,
                  where='id_persona=$id_persona',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
