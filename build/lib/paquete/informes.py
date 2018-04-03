from reportlab.platypus import Table
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A3,A4
from reportlab.lib import colors
from sqlite3 import connect
from sqlite3 import DatabaseError
import os

guion=[]

cabeceira=[["Nombre","Apellido","Telefono",
                  "CP","DNI","Direccion",
                  "Poblacion","Provincia","Deportes",
                  "Objetivo","Fisio","Trainer",
                  "Sauna"]]
cabeceiraTrainer=[["User","Password"]]

def generainformeclientes():
    """Esta clase, devuelve un informe con todos los clientes registrados en el
    gym, le mandamos todos los campos que queremos mostrar en el informe, asi como
    la consulta necesaria que ejecutaremos para que muestre todos los datos que necesitemos.
    Luego anhadiremos la tabla para que se muestren las celdas con un borde y un fondo de color,
    mas la imagen de la empresa (logo)"""
    try:
        bbdd=connect("/home/ped90/Documentos/Pycharm/BaseDatosGYM-Pedro Argibay/Base_Datos/paquete/gym.db")
        cursor=bbdd.cursor()
        cursor.execute("select * from clientes")

        taboa=Table(cabeceira+cursor.fetchall())

    except DatabaseError as e:
        print("Error al exportar el informe")

    taboa.setStyle((['BOX',(0,0),(-1,-1),0.25,colors.black],
                    ['BACKGROUND',(0,0),(-1,-1),colors.slategrey],
                    ['INNERGRID',(0,0),(-1,-1),0.25,colors.black]))

    guion.append(taboa)
    imaxe = Image(os.path.realpath('/home/ped90/Documentos/Pycharm/BaseDatosGYM-Pedro Argibay/Base_Datos/images/sun2.jpg'))
    guion.append(imaxe)
    doc=SimpleDocTemplate("InformesGYMClientes.pdf", pagesize=A3)
    doc.build(guion)

def generainformetrainers():
    """Este metodo es igual que el anterior solo que devolveria otro informe solo para
    verificar que personal de entrenadores estaria en el gimnasio"""
    try:
        bbdd=connect("/Users/pargibaycalvo/PycharmProjects/Base_Datos/paquete/usertrainers.db")
        cursor=bbdd.cursor()
        cursor.execute("select * from gym")

        taboa1=Table(cabeceiraTrainer+cursor.fetchall())

    except DatabaseError as e:
        print("Error al exportar el informe")

    taboa1.setStyle((['BOX',(0,0),(-1,-1),0.25,colors.black],
                    ['BACKGROUND',(0,0),(-1,-1),colors.slategrey],
                    ['INNERGRID',(0,0),(-1,-1),0.25,colors.black]))

    guion.append(taboa1)
    imaxe = Image(os.path.realpath('/home/ped90/Documentos/Pycharm/BaseDatosGYM-Pedro Argibay/Base_Datos/images/sun2.jpg'))
    guion.append(imaxe)
    doc=SimpleDocTemplate("InformesGYMEntrenadores.pdf", pagesize=A4)
    doc.build(guion)

def generainformeadmins():
    """Este metodo es igual que el anterior solo que devolveria otro informe solo para
    verificar que personal de administradores del programa"""
    try:
        bbdd = connect("/Users/pargibaycalvo/PycharmProjects/Base_Datos/paquete/user.db")
        cursor = bbdd.cursor()
        cursor.execute("select * from gym")

        taboa1 = Table(cabeceiraTrainer + cursor.fetchall())

    except DatabaseError as e:
        print("Error al exportar el informe")

    taboa1.setStyle((['BOX', (0, 0), (-1, -1), 0.25, colors.black],
                     ['BACKGROUND', (0, 0), (-1, -1), colors.slategrey],
                     ['INNERGRID', (0, 0), (-1, -1), 0.25, colors.black]))

    guion.append(taboa1)
    imaxe = Image(os.path.realpath('/Users/pargibaycalvo/PycharmProjects/Base_Datos/images/sun2.jpg'))
    guion.append(imaxe)
    doc = SimpleDocTemplate("InformesGYMAdmins.pdf", pagesize=A4)
    doc.build(guion)

def generainformerecep():
    """Este metodo es igual que el anterior solo que devolveria otro informe solo para
    verificar que personal de recepcion estaria en el gimnasio"""
    try:
        bbdd = connect("/Users/pargibaycalvo/PycharmProjects/Base_Datos/paquete/userrecep.db")
        cursor = bbdd.cursor()
        cursor.execute("select * from gym")

        taboa1 = Table(cabeceiraTrainer + cursor.fetchall())

    except DatabaseError as e:
        print("Error al exportar el informe")

    taboa1.setStyle((['BOX', (0, 0), (-1, -1), 0.25, colors.black],
                     ['BACKGROUND', (0, 0), (-1, -1), colors.slategrey],
                     ['INNERGRID', (0, 0), (-1, -1), 0.25, colors.black]))

    guion.append(taboa1)
    imaxe = Image(os.path.realpath('/Users/pargibaycalvo/PycharmProjects/Base_Datos/images/sun2.jpg'))
    guion.append(imaxe)
    doc = SimpleDocTemplate("InformesGYMRecepcion.pdf", pagesize=A4)
    doc.build(guion)