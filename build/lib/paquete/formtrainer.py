import sqlite3 as dbapi

import gi

import paquete.inicio
import paquete.baselog

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FichasGym(Gtk.Window):
    def __init__(self):
        """Ventana de entrenador, esta ventana solo mostrará los objetivos del cliente, también podrá
        en su caso consultar datos personales del cliente, este necesita la autorización del administrador o
        jefe del gym. Este metodo es el que crea la ventana con sus botones, texto y sus posiciones."""
        Gtk.Window.__init__(self, title="GYM - pargibay 6150")
        self.set_border_width(10)
        self.set_default_size(200, 150)

        cajaGeneral = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaGeneral)

        lbltitulo = Gtk.Label(xalign=0)
        lbltitulo.set_markup("<b>Fichas de Clientes</b>")
        cajaGeneral.add(lbltitulo)

        frameFichas = Gtk.Frame(label="Fichas Clientes")
        cajaInvisibleV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameFichas.add(cajaInvisibleV1)

        frameOpciones = Gtk.Frame(label="")
        cajaInvisibleV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameOpciones.add(cajaInvisibleV2)

        cajaInvisibleH1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        btnConsUs = Gtk.Button(label="Concultar Clientes")
        btnConsUs.connect("clicked", self.on_btn_consulta)

        self.lblDatosNb = Gtk.Label(xalign=0)
        self.lblDatosAp = Gtk.Label(xalign=0)
        self.lblDatosDp = Gtk.Label(xalign=0)
        self.lblDatosOb = Gtk.Label(xalign=0)
        self.lblDatosFs = Gtk.Label(xalign=0)
        self.lblDatosPt = Gtk.Label(xalign=0)
        self.lblDatosSn = Gtk.Label(xalign=0)

        btnCons = Gtk.Button(label="Concultar Ficha")
        btnCons.connect("clicked", self.on_btn_cons)
        self.Cons = Gtk.Label(xalign=0)
        self.txtCons = Gtk.Entry()

        btnExit = Gtk.Button(label="Cerrar Sesion")
        btnExit.connect("clicked", self.on_btn_close)
        self.Exit = Gtk.Label(xalign=0)

        cajaInvisibleV2.pack_start(btnConsUs, True, False, 0)
        cajaInvisibleV1.pack_start(self.txtCons, True, False, 0)
        cajaInvisibleV1.pack_start(self.lblDatosNb, True, False, 0)
        cajaInvisibleV1.pack_start(self.lblDatosAp, True, False, 0)
        cajaInvisibleV1.pack_start(self.lblDatosDp, True, False, 0)
        cajaInvisibleV1.pack_start(self.lblDatosOb, True, False, 0)
        cajaInvisibleV1.pack_start(self.lblDatosFs, True, False, 0)
        cajaInvisibleV1.pack_start(self.lblDatosPt, True, False, 0)
        cajaInvisibleV1.pack_start(self.lblDatosSn, True, False, 0)

        cajaInvisibleV1.pack_start(btnCons, True, False, 0)
        cajaInvisibleV2.pack_start(btnExit, True, False, 0)

        cajaInvisibleV1.add(cajaInvisibleH1)
        cajaInvisibleV2.add(cajaInvisibleH2)

        cajaGeneral.add(frameFichas)
        cajaGeneral.add(frameOpciones)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_consulta(self, boton):
        """Este metodo se comunica con la clase baselog y le inidicará que necesita unos permisos
        necesarios par acceder a información más detallada de los clientes."""
        try:
            paquete.baselog.DataBase()
            self.destroy()
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_cons(self, boton):
        """Metodo que devuelve los datos de los clientes que el entrendor necesita saber para
        desenvolver su trabajo."""
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
            cursor = base.cursor()
            reg = (self.txtCons.get_text())
            cursor.execute("SELECT * FROM clientes WHERE dni='%s'" % reg)
            print("Opening Data Base")
            for i in cursor:
                self.lblDatosNb.set_text(i[0])
                self.lblDatosAp.set_text(i[1])
                self.lblDatosDp.set_text(i[8])
                self.lblDatosOb.set_text(i[9])
                self.lblDatosFs.set_text(i[10])
                self.lblDatosPt.set_text(i[11])
                self.lblDatosSn.set_text(i[12])
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_close(self, widget):
        """Metodo para el boton de cerrar, nos cierra esta ventana y nos lleva a la anterior que estaba abierta"""
        try:
            self.destroy()
            paquete.inicio.VentanaInicio()
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

if __name__ == "__main__":
    fiestra = FichasGym()
    Gtk.main()


