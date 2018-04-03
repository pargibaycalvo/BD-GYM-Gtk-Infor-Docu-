import sqlite3 as dbapi

import gi

import paquete.formAdmin

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class DataBase(Gtk.Window):
    def __init__(self):
        """Esta clase se comunica con la ventana de formulario para el administrador y le
        indica la base de datos de los recepcionistas agregados en el programa que pueden
        iniciar sesion y la creacion de la ventana"""
        Gtk.Window.__init__(self,title="Base de Datos Recepcion-GYM")
        self.set_default_size(250,150)
        self.set_border_width(10)

        columnas = ["Users", "Password"]

        modelo = Gtk.ListStore(str, str)

        base = dbapi.connect("userrecep.db")
        cursor = base.cursor()
        cursor.execute("SELECT * FROM gym")

        for i in cursor:
            modelo.append(i)

        vista = Gtk.TreeView(model=modelo)
        for i in range(len(columnas)):
            celda = Gtk.CellRendererText()
            celda.set_property("editable", False)
            columna = Gtk.TreeViewColumn(columnas[i], celda, text=i)

            vista.append_column(columna)

        btnReturn = Gtk.Button(label="Atrás")
        btnReturn.connect("clicked", self.on_btn_return)
        self.Conndb = Gtk.Label(xalign=0)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        cajaH.pack_start(vista, False, False, 0)
        cajaH.pack_start(btnReturn,True, False, 0)
        self.add(cajaH)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_return(self, boton):
        """Metodo para cerrar la ventana y devolverte a la ventana anteriormente abierta"""
        paquete.formAdmin.FormularioGym()
        self.destroy()


if __name__ == "__main__":
    DataBase()
    Gtk.main()
