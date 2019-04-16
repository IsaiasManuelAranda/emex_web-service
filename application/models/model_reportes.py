import web
import config

db = config.db


def get_all_reportes():
    try:
        return db.select('reportes')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_reportes(id_reporte):
    try:
        return db.select('reportes', where='id_reporte=$id_reporte', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_reportes(id_reporte):
    try:
        return db.delete('reportes', where='id_reporte=$id_reporte', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_reportes(nombre,edad,latitud,longitud):
    try:
        return db.insert('reportes',nombre=nombre,
edad=edad,
latitud=latitud,
longitud=longitud)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_reportes(id_reporte,nombre,edad,latitud,longitud):
    try:
        return db.update('reportes',id_reporte=id_reporte,
nombre=nombre,
edad=edad,
latitud=latitud,
longitud=longitud,
                  where='id_reporte=$id_reporte',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
