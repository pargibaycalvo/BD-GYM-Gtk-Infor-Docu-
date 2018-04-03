import sqlite3 as dbapi

import paquete.formtrainer
import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class DataBaseRecep(Gtk.Window):
    def __init__(self):
        """Esta clase es la encargada de devolver a los usuarios los datos completos de los clientes.
         Se crea la ventana, con su consulta a la base de datos y se le añaden a la tabla todos los datos
         que se van a mostrar.
         #Si no le decimos que van a ser cada dato nos dara un problema al mostrarlo."""

        Gtk.Window.__init__(self,title="Base de Datos Clientes-GYM")
        self.set_default_size(250,150)
        self.set_border_width(10)

        columnas=["Nombre","Apellido","Telefono",
                  "CP","DNI","Direccion",
                  "Poblacion","Provincia","Deportes",
                  "Objetivo","Fisio","Trainer",
                  "Sauna"]

        modelo = Gtk.ListStore(str, str, int, int, int, str, str, str, str, str, str, str, str)

        base = dbapi.connect("/home/ped90/Documentos/Pycharm/BaseDatosGYM-Pedro Argibay/Base_Datos/paquete/gym.db")
        cursor = base.cursor()
        cursor.execute("SELECT * FROM clientes")

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
        """Este metodo es la funcion del boton, cuando lo pulsamos se destruye esta ventana (se cierra)
        y se nos abre la ventana en la que estabamos."""
        paquete.form.FormularioGym()
        self.destroy()

if __name__ == "__main__":
    DataBaseRecep()
    Gtk.main()
