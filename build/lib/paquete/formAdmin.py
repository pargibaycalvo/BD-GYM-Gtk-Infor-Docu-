import sqlite3 as dbapi

import paquete.baselog
import paquete.form
import paquete.inicio
import paquete.winAdmin
import paquete.winRecep
import paquete.winbaseadmin
import gi

import paquete.winTrain

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class FormularioGym(Gtk.Window):
    """Ventana del administrador o jefe del gym, tendrá privilegios mayores sobre el programa,
    podrá consultar datos de clientes y empleados así como modificar sus datos.  Todo este metodo largo es para la creación
    de la ventana, botones, textos y en las posiciones que queremos que esten los objectos"""
    def __init__(self):
        Gtk.Window.__init__(self, title="GYM - pargibay 6150")
        self.set_border_width(10)
        self.set_default_size(200, 150)

        cajaGeneral = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaGeneral)

        lbltitulo = Gtk.Label(xalign=0)
        lbltitulo.set_markup("<b>ADMINISTRADOR</b>")
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
        frameAdmins = Gtk.Frame(label="Opciones Administrador")
        cajaInvisibleV9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameAdmins.add(cajaInvisibleV9)
        frameAdmins1 = Gtk.Frame(label="Opciones Administrador")
        cajaInvisibleV10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameAdmins1.add(cajaInvisibleV10)

        cajaInvisibleH1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaInvisibleH7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleH12 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

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

        btnConsAdmin = Gtk.Button(label="Consulta Admins")
        btnConsAdmin.connect("clicked", self.on_btn_consultAdmins)
        self.ConsAdmin = Gtk.Label(xalign=0)

        btnConsTrainer = Gtk.Button(label="Consulta Trainers")
        btnConsTrainer.connect("clicked", self.on_btn_consultTrainers)
        self.ConsTrainer = Gtk.Label(xalign=0)

        btnConsRecep = Gtk.Button(label="Consulta Recepcion")
        btnConsRecep.connect("clicked", self.on_btn_consultRecepcion)
        self.ConsRecep = Gtk.Label(xalign=0)

        btnNewAdmin = Gtk.Button(label="Nuevo Admin")
        btnNewAdmin.connect("clicked", self.on_btn_newAdmin)
        self.NewAdmin = Gtk.Label(xalign=0)

        btnNewTrain = Gtk.Button(label="Nuevo Trainer")
        btnNewTrain.connect("clicked", self.on_btn_newTrain)
        self.NewTrain = Gtk.Label(xalign=0)

        btnNewRecep = Gtk.Button(label="Nuevo Recepcion")
        btnNewRecep.connect("clicked", self.on_btn_newRecep)
        self.NewRecep = Gtk.Label(xalign=0)

        lblUser = Gtk.Label(label="User", xalign=0)
        self.txtUser = Gtk.Entry()
        lblPass = Gtk.Label(label="Password", xalign=0)
        self.txtPass = Gtk.Entry()


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
        cajaInvisibleH10.pack_start(btnDeleUs, True, False, 0)
        cajaInvisibleH10.pack_start(self.txtDeleUs, True, False, 0)
        cajaInvisibleH11.pack_start(btnConsAdmin, True, False, 0)
        cajaInvisibleH11.pack_start(btnConsRecep, True, False, 0)
        cajaInvisibleH11.pack_start(btnConsTrainer, True, False, 0)
        cajaInvisibleH12.pack_start(btnNewAdmin, True, False, 0)
        cajaInvisibleH12.pack_start(btnNewRecep, True, False, 0)
        cajaInvisibleH12.pack_start(btnNewTrain, True, False, 0)
        cajaInvisibleH12.pack_start(lblUser, True, False, 0)
        cajaInvisibleH12.pack_start(self.txtUser, True, False, 0)
        cajaInvisibleH12.pack_start(lblPass, True, False, 0)
        cajaInvisibleH12.pack_start(self.txtPass, True, False, 0)


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
        cajaInvisibleV9.add(cajaInvisibleH11)
        cajaInvisibleV10.add(cajaInvisibleH12)


        cajaGeneral.add(frameDatos)
        cajaGeneral.add(frameObjetivos)
        cajaGeneral.add(frameExtras)
        cajaGeneral.add(framePrecio)
        cajaGeneral.add(frameConsultar)
        cajaGeneral.add(frameBorrar)
        cajaGeneral.add(frameOpciones)
        cajaGeneral.add(frameAdmins)
        cajaGeneral.add(frameAdmins1)


        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def conectarBase(self, boton):
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
            cursor = base.cursor()
            print("Cambios realizados con éxito")
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
        """Metodo que nos devuleve la base de datos de clientes"""
        paquete.winbaseadmin.DataBaseAdmin()
        self.destroy()


    def on_btn_consulta(self, boton):
        """Metodo que nos devulve mediante el dni solicitado los datos del cliente"""
        base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/gym.db")
        cursor = base.cursor()
        reg=(self.txtConsUs.get_text())
        cursor.execute("SELECT * FROM clientes WHERE dni='%s'" %reg)
        self.txtConsUs.set_text("")
        print("Cliente")
        print("---")
        for i in cursor:
            print("Nombre=", i[0])
            print("Apellidos=", i[1])
            print("Telefono=", i[2])
            print("CP=", i[3])
            print("DNI=", i[4])
            print("Direccion=", i[5])
            print("Poblacion=", i[6])
            print("Provincia=", i[7])
            print("Deporte=", i[8])
            print("Objetivos=", i[9])
            print("Fisioterapeuta=", i[10])
            print("Personal Trainer=", i[11])
            print("Sauna=", i[12])
            print("---")

    def on_btn_delete(self, boton):
        FormularioGym.on_btn_delete()

    def on_btn_newAdmin(self, boton):
        """Metodo para añadir un nuevo administrador en la base de datos"""
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/user.db")
            cursor = base.cursor()
            print("Cambios realizados con éxito")
            reg=(self.txtUser.get_text(),
                 self.txtPass.get_text())
            cursor.execute('INSERT INTO gym VALUES (?,?)', reg)
            base.commit()
            cursor.close()
            base.close()
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_newTrain(self, boton):
        """Metodo para añadir un nuevo entreandor a la base de datos"""
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/usertrainers.db")
            cursor = base.cursor()
            print("Cambios realizados con éxito")
            reg=(self.txtUser.get_text(),
                 self.txtPass.get_text())
            cursor.execute('INSERT INTO gym VALUES (?,?)', reg)
            base.commit()
            cursor.close()
            base.close()
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_newRecep(self, boton):
        """Metodo para añadir un nuevo recepcionista a la base de datos"""
        try:
            base = dbapi.connect("/home/pedro/Documentos/PycharmProjects/Base_Datos/userrecep.db")
            cursor = base.cursor()
            print("Cambios realizados con éxito")
            reg=(self.txtUser.get_text(),
                 self.txtPass.get_text())
            cursor.execute('INSERT INTO gym VALUES (?,?)', reg)
            base.commit()
            cursor.close()
            base.close()
        except dbapi.OperationalError:
            print("Error al conectar a la base (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la base de datos")

    def on_btn_consultAdmins(self, boton):
        """Consultar en la base de datos los administradores, la ventana anterior se cierra para
        dejar paso a la nueva"""
        paquete.winAdmin.DataBase()
        self.destroy()

    def on_btn_consultTrainers(self, boton):
        """Consultar en la base de datos los entrenadores, la ventana anterior se cierra para
        dejar paso a la nueva"""
        paquete.winTrain.DataBase()
        self.destroy()

    def on_btn_consultRecepcion(self, boton):
        """Consultar en la base de datos los recepcionistas, la ventana anterior se cierra para
        dejar paso a la nueva"""
        paquete.winRecep.DataBase()
        self.destroy()

    def on_btn_close(self, widget):
        """Boton para cerrar la ventana y abrir la que anteriormente estaba abierta"""
        self.destroy()
        paquete.inicio.VentanaInicio()

    def on_btn_cdatabase(self, base):
        """Boton para conectarse a la base de datos"""
        self.conectarBase(base)




if __name__ == "__main__":
    fiestra = FormularioGym()
    Gtk.main()





