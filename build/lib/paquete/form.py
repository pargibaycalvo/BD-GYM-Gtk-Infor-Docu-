import sqlite3 as dbapi

import paquete.baselog
import paquete.inicio
import gi

import paquete.winbase

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FormularioGym(Gtk.Window):
    def __init__(self):
        """Ventana para el ingreso de un nuevos cliente. Esta ventana será para el/la secretario
        del gym, podrá añadir, borrar y consultar datos del cliente.
        Todo este metodo largo es para la creación de la ventana, botones, textos y en las posiciones
        que queremos que esten los objectos"""
        Gtk.Window.__init__(self, title="GYM - pargibay 6150")
        self.set_border_width(10)
        self.set_default_size(200, 150)

        cajaGeneral = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaGeneral)

        lbltitulo = Gtk.Label(xalign=0)
        lbltitulo.set_markup("<b>Formulario De Inscripción</b>")
        cajaGeneral.add(lbltitulo)

        frameDatos = Gtk.Frame(label="Datos Cliente")
        cajaInvisibleV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameDatos.add(cajaInvisibleV1)
        frameObservacion = Gtk.Frame(label="Observaciones")
        cajaInvisibleV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameObservacion.add(cajaInvisibleV2)
        frameObjetivos = Gtk.Frame(label="Objetivos")
        cajaInvisibleV3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameObjetivos.add(cajaInvisibleV3)
        frameExtras = Gtk.Frame(label="Extras")
        cajaInvisibleV4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameExtras.add(cajaInvisibleV4)
        framePrecio = Gtk.Frame(label="Precio")
        cajaInvisibleV5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        framePrecio.add(cajaInvisibleV5)
        frameOpciones = Gtk.Frame(label="")
        cajaInvisibleV6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameOpciones.add(cajaInvisibleV6)
        frameConsultar = Gtk.Frame(label="Consultar Cliente")
        cajaInvisibleV7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameConsultar.add(cajaInvisibleV7)
        frameBorrar = Gtk.Frame(label="Borrar Cliente")
        cajaInvisibleV8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameBorrar.add(cajaInvisibleV8)

        cajaInvisibleH1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaInvisibleH7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaInvisibleH10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        lblNombre = Gtk.Label(label="Nombre", xalign=0)
        self.txtNombre = Gtk.Entry()
        lblApellidos = Gtk.Label(label="Apellidos", xalign=0)
        self.txtApellidos = Gtk.Entry()
        lblDireccion = Gtk.Label(label="Dirección", xalign=0)
        self.txtDireccion = Gtk.Entry()
        lblPoblacion = Gtk.Label(label="Población", xalign=0)
        self.txtPoblacion = Gtk.Entry()

        lblCP = Gtk.Label(label="C.P.", xalign=0)
        self.txtCP = Gtk.Entry()
        lblDni = Gtk.Label(label="Dni", xalign=0)
        self.txtDni = Gtk.Entry()
        lblTelf = Gtk.Label(label="Teléfono Fijo", xalign=0)
        self.txtTelf = Gtk.Entry()
        lblProvincia = Gtk.Label(label="Provincia", xalign=0)
        self.txtprovincia = Gtk.Entry()

        scroll = Gtk.ScrolledWindow()
        scroll.set_size_request(500, 100)
        scroll.set_margin_left(10)
        scroll.set_margin_right(20)
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        txtObservaciones = Gtk.TextView()
        scroll.add(txtObservaciones)

        lblObjetivo = Gtk.Label("Objetivo", xalign=0)
        self.boxObjetivo = Gtk.ComboBoxText()
        self.boxObjetivo.insert(0, "0", "Adelgazar")
        self.boxObjetivo.insert(1, "1", "Aumentar MM")
        self.boxObjetivo.insert(2, "2", "Mantenimiento")
        self.boxObjetivo.insert(3, "3", "Salud")

        lblDeportes = Gtk.Label("Deportes", xalign=0)
        self.boxDeportes = Gtk.ComboBoxText()
        self.boxDeportes.insert(0, "0", "Sala")
        self.boxDeportes.insert(1, "1", "Piscina")
        self.boxDeportes.insert(2, "2", "CrossFit")
        self.boxDeportes.insert(3, "3", "Zumba")
        self.boxDeportes.insert(4, "4", "Boxeo")

        lblPrecio = Gtk.Label()
        self.lblPrecioT = Gtk.Label("Deportes - 25€/mes \n Extras - 20€/mes")

        self.btnTick1 = Gtk.CheckButton(label="Fisioterapeuta")
        self.btnTick2 = Gtk.CheckButton(label="Personal Trainer")
        self.btnTick3 = Gtk.CheckButton(label="Sauna")

        btnConndb = Gtk.Button(label="NuevoDB")
        btnConndb.connect("clicked", self.on_btn_cdatabase)
        self.Conndb = Gtk.Label(xalign=0)

        btnConsUs = Gtk.Button(label="Concultar Cliente")
        btnConsUs.connect("clicked", self.on_btn_consulta)
        self.ConsUs = Gtk.Label(xalign=0)
        self.txtConsUs = Gtk.Entry()

        btnDeleUs = Gtk.Button(label="Borrar Cliente")
        btnDeleUs.connect("clicked", self.on_btn_delete)
        self.DeleUs = Gtk.Label(xalign=0)
        self.txtDeleUs = Gtk.Entry()

        btnExit = Gtk.Button(label="Cerrar Sesion")
        btnExit.connect("clicked", self.on_btn_close)
        self.Exit = Gtk.Label(xalign=0)

        btnConsdb = Gtk.Button(label="ConsultaDB")
        btnConsdb.connect("clicked", self.on_btn_consult)
        self.Consdb = Gtk.Label(xalign=0)

        self.lblDatosNb = Gtk.Label(xalign=0)
        self.lblDatosAp = Gtk.Label(xalign=0)
        self.lblDatosTf = Gtk.Label(xalign=0)
        self.lblDatosCp = Gtk.Label(xalign=0)
        self.lblDatosDn = Gtk.Label(xalign=0)
        self.lblDatosDr = Gtk.Label(xalign=0)
        self.lblDatosPo = Gtk.Label(xalign=0)
        self.lblDatosPv = Gtk.Label(xalign=0)
        self.lblDatosDp = Gtk.Label(xalign=0)
        self.lblDatosOb = Gtk.Label(xalign=0)
        self.lblDatosFs = Gtk.Label(xalign=0)
        self.lblDatosPt = Gtk.Label(xalign=0)
        self.lblDatosSn = Gtk.Label(xalign=0)

        self.lblInsertUs = Gtk.Label(xalign=0)


        cajaInvisibleH1.pack_start(lblNombre, True, False, 0)
        cajaInvisibleH1.pack_start(self.txtNombre, True, False, 0)
        cajaInvisibleH1.pack_start(lblCP, True, False, 0)
        cajaInvisibleH1.pack_start(self.txtCP, True, False, 0)
        cajaInvisibleH2.pack_start(lblApellidos, True, False, 0)
        cajaInvisibleH2.pack_start(self.txtApellidos, True, False, 0)
        cajaInvisibleH2.pack_start(lblDni, True, False, 0)
        cajaInvisibleH2.pack_start(self.txtDni, True, False, 0)
        cajaInvisibleH3.pack_start(lblDireccion, True, False, 0)
        cajaInvisibleH3.pack_start(self.txtDireccion, True, False, 0)
        cajaInvisibleH3.pack_start(lblTelf, True, False, 0)
        cajaInvisibleH3.pack_start(self.txtTelf, True, False, 0)
        cajaInvisibleH4.pack_start(lblPoblacion, True, False, 0)
        cajaInvisibleH4.pack_start(self.txtPoblacion, True, False, 0)
        cajaInvisibleH4.pack_start(lblProvincia, True, False, 0)
        cajaInvisibleH4.pack_start(self.txtprovincia, True, False, 0)
        cajaInvisibleH5.pack_start(lblObjetivo, False, False, 0)
        cajaInvisibleH5.pack_start(self.boxObjetivo, False, False, 0)
        cajaInvisibleH5.pack_start(lblDeportes, False, False, 0)
        cajaInvisibleH5.pack_start(self.boxDeportes, False, False, 0)
        cajaInvisibleH6.pack_start(self.btnTick1, False, False, 0)
        cajaInvisibleH6.pack_start(self.btnTick2, False, False, 0)
        cajaInvisibleH6.pack_start(self.btnTick3, False, False, 0)
        cajaInvisibleH7.pack_start(lblPrecio, False, False, 0)
        cajaInvisibleH7.pack_start(self.lblPrecioT, False, False, 0)
        cajaInvisibleH8.pack_start(btnExit, True, False, 0)
        cajaInvisibleH8.pack_start(btnConndb, True, False, 0)
        cajaInvisibleH8.pack_start(btnConsdb, True, False, 0)
        cajaInvisibleH9.pack_start(btnConsUs, True, False, 0)
        cajaInvisibleH9.pack_start(self.txtConsUs, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosNb, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosAp, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosTf, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosCp, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosDn, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosDr, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosPo, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosPv, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosDp, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosOb, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosFs, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosPt, True, False, 0)
        cajaInvisibleH9.pack_start(self.lblDatosSn, True, False, 0)
        cajaInvisibleH10.pack_start(btnDeleUs, True, False, 0)
        cajaInvisibleH10.pack_start(self.txtDeleUs, True, False, 0)
        cajaInvisibleH10.pack_start(self.lblInsertUs, True, False, 0)

        cajaInvisibleV1.add(cajaInvisibleH1)
        cajaInvisibleV1.add(cajaInvisibleH2)
        cajaInvisibleV1.add(cajaInvisibleH3)
        cajaInvisibleV1.add(cajaInvisibleH4)
        cajaInvisibleV3.add(cajaInvisibleH5)
        cajaInvisibleV4.add(cajaInvisibleH6)
        cajaInvisibleV5.add(cajaInvisibleH7)
        cajaInvisibleV6.add(cajaInvisibleH8)
        cajaInvisibleV7.add(cajaInvisibleH9)
        cajaInvisibleV8.add(cajaInvisibleH10)


        cajaGeneral.add(frameDatos)
        cajaGeneral.add(frameObjetivos)
        cajaGeneral.add(frameExtras)
        cajaGeneral.add(framePrecio)
        cajaGeneral.add(frameConsultar)
        cajaGeneral.add(frameBorrar)
        cajaGeneral.add(frameOpciones)


        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def conectarBase(self, boton):
        """Este metodo sirve para añadir usuarios nuevos en la base de datos, cuando se termine de rellenar y se pulse
        el boton, todos los campos del formulario se vacian, así, se podrá añadir otro nuevamente sin tener que borrar a mano"""
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
            cursor = base.cursor()
            print("Insert Data Base")
            reg=(self.txtNombre.get_text(),
                 self.txtApellidos.get_text(),
                 self.txtTelf.get_text(),
                 self.txtCP.get_text(),
                 self.txtDni.get_text(),
                 self.txtDireccion.get_text(),
                 self.txtPoblacion.get_text(),
                 self.txtprovincia.get_text(),
                 self.boxDeportes.get_active_text(),
                 self.boxObjetivo.get_active_text(),
                 self.btnTick1.get_active(),
                 self.btnTick2.get_active(),
                 self.btnTick3.get_active())
            cursor.execute('INSERT INTO clientes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', reg)
            self.lblInsertUs.set_text("Cliente añadido")
            base.commit()

            self.txtNombre.set_text("")
            self.txtApellidos.set_text("")
            self.txtTelf.set_text("")
            self.txtCP.set_text("")
            self.txtDni.set_text("")
            self.txtDireccion.set_text("")
            self.txtPoblacion.set_text("")
            self.txtprovincia.set_text("")
            cursor.close()
            base.close()

        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_consult(self, boton):
        """Boton de consulta que te devuelve hacia el terminal todos los datos de los clientes"""
        try:
            paquete.winbase.DataBaseRecep()
            self.destroy()
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
            cursor = base.cursor()
            cursor.execute("SELECT * FROM clientes")
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")


    def on_btn_consulta(self, boton):
        """Insertando el dni del cliente nos muestra todos los datos relacionados de ese cliente"""
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
            cursor = base.cursor()
            reg=(self.txtConsUs.get_text())
            cursor.execute("SELECT * FROM clientes WHERE dni='%s'" %reg)
            self.txtConsUs.set_text("")
            print("Opening Data Base")
            for i in cursor:
                self.lblDatosNb.set_text(i[0])
                self.lblDatosAp.set_text(i[1])
                self.lblDatosTf.set_text(str(i[2]))
                self.lblDatosCp.set_text(str(i[3]))
                self.lblDatosDn.set_text(str(i[4]))
                self.lblDatosDr.set_text(i[5])
                self.lblDatosPo.set_text(i[6])
                self.lblDatosPv.set_text(i[7])
                self.lblDatosDp.set_text(i[8])
                self.lblDatosOb.set_text(i[9])
                self.lblDatosFs.set_text(i[10])
                self.lblDatosPt.set_text(i[11])
                self.lblDatosSn.set_text(i[12])
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_delete(self, boton):
        """Insertando en dni nos borra ese cliente deseado"""
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
            cursor = base.cursor()
            reg=(self.txtDeleUs.get_text())
            cursor.execute("DELETE FROM clientes WHERE dni='%s'" %reg)
            self.txtDeleUs.set_text("")
            self.lblInsertUs.set_text("Cliente Borrado")
            print("Delete User")
            base.commit()
            cursor.close()
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_close(self, widget):
        """Boton que al pulsarlo, se cierra la ventana y no redirige a la ventana de incio"""
        try:
            self.destroy()
            paquete.inicio.VentanaInicio()
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_cdatabase(self, base):
        """Boton que nos permitirá conectarnos a la base de datos"""
        try:
            self.conectarBase(base)
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")




if __name__ == "__main__":
    fiestra = FormularioGym()
    Gtk.main()





