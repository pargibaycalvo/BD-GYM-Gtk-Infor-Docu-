import sys

import paquete.log
import paquete.logTrainer
import paquete.informes
import paquete.logRecep
import gi



gi.require_version('Gtk','3.0')
from gi.repository import Gtk



class VentanaInicio(Gtk.Window):
    def __init__(self):
        """Ventana de inicio del programa, mostrara como quieres logearte recepcion,
        entrenador o administrador las contrasenhas estan guardadas en ficheros sql que solo
        el administrador o jefe podra modificar o anhadir si esa cuenta no existe  el programa
        no se inicia indicando un mensaje de credenciales incorrectas"""
        Gtk.Window.__init__(self,title="")
        self.set_default_size(350,100)
        self.set_border_width(10)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(cajaH)

        cabeceira = Gtk.HeaderBar(title="Bienvenido al GYMpargibay")
        cabeceira.set_subtitle("Inicie sesion")
        cabeceira.props.show_close_button = True
        self.set_titlebar(cabeceira)

        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caixa.get_style_context(), "linked")

        frameLoginAdmin = Gtk.Frame()
        cajaInvisibleV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameLoginAdmin.add(cajaInvisibleV)

        btnAdmin = Gtk.Button(label="Administrador")
        btnAdmin.connect("clicked", self.on_btn_Admin)
        btnTrainer = Gtk.Button(label="Entrenadores")
        btnTrainer.connect("clicked", self.on_btn_Trainer)
        btnRecep = Gtk.Button(label="Recepcion")
        btnRecep.connect("clicked", self.on_btn_Recep)
        btnExit = Gtk.Button(label="Salir")
        btnExit.connect("clicked", self.on_btn_Exit)
        btnInforme = Gtk.Button(label="Informes")
        btnInforme.connect("clicked", self.on_btn_Informes)
        image = Gtk.Image()
        image.set_from_file('/home/ped90/Documentos/pycharm/diproyecto/Base_Datos/images/sun.png')

        cajaInvisibleV.pack_start(btnRecep, True, False, 0)
        cajaInvisibleV.pack_start(btnTrainer, True, False, 0)
        cajaInvisibleV.pack_start(btnAdmin, True, False, 20)
        cajaInvisibleV.pack_start(btnExit, True, False, 0)
        cajaInvisibleV.pack_start(image, True, False, 0)
        cajaInvisibleV.pack_start(btnInforme, True, False, 0)

        cajaH.add(frameLoginAdmin)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btn_Admin(self, boton):
        """Metodo para logearse como administrador"""
        paquete.log.VentanaLogin()
        self.destroy()

    def on_btn_Trainer(self, boton):
        """Metodo para logearse como entrenador"""
        paquete.logTrainer.VentanaLogin()
        self.destroy()

    def on_btn_Recep(self, boton):
        """Metodo para logearse como recepcionista"""
        paquete.logRecep.VentanaLogin()
        self.destroy()

    def on_btn_Exit(self, boton):
        """Metodo para salir del programa y cerrar proceso abierto"""
        sys.exit()

    def on_btn_Informes(self, boton):
        """Metodo para sacar informes de todos los entrenadores y clientes del gimnasio
        esto se puede realizar una vez inicies el programa"""
        paquete.informes.generainformeclientes()
        paquete.informes.generainformetrainers()
        paquete.informes.generainformerecep()
        paquete.informes.generainformeadmins()

if __name__ == "__main__":
    fiestra = VentanaInicio()
    Gtk.main()