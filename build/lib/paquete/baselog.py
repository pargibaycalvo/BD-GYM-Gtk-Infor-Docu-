import gi

import paquete.winbase2

gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gio


class DataBase(Gtk.Window):
    def __init__(self):
        """Ventana para que el entrenador si quiere acceder a consultar datos de un cliente
        necesite el permiso del administrador o jefe. Contiene un boton de información.
        Como se ve, inicialmente creamos la ventana, con sus botones necesarios tanto de ayuda
        como de logeo."""
        Gtk.Window.__init__(self,title="Logear como Admin")
        self.set_default_size(350,100)
        self.set_border_width(10)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(cajaH)

        cabeceira = Gtk.HeaderBar(title="Credeciales de Admin")
        cabeceira.set_subtitle("Clave Superusuario")
        cabeceira.props.show_close_button = True
        self.set_titlebar(cabeceira)

        btn = Gtk.Button()
        btn.connect("clicked", self.on_btn_help)
        icono = Gio.ThemedIcon(name="help")
        imaxe = Gtk.Image.new_from_gicon(icono, Gtk.IconSize.BUTTON)
        btn.add(imaxe)
        cabeceira.pack_end(btn)

        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caixa.get_style_context(), "linked")

        frameLoginAdmin = Gtk.Frame()
        cajaInvisibleV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frameLoginAdmin.add(cajaInvisibleV)

        lblPass = Gtk.Label(label="Password", xalign=0)
        self.txtPass = Gtk.Entry()
        self.txtPass.set_visibility(False)
        btnLogear = Gtk.Button(label="Entry")
        btnLogear.connect("clicked", self.on_btn_ClickAdmin)
        self.lblCorInc = Gtk.Label(xalign=0)
        self.lblHelp = Gtk.Label(xalign=0)

        cajaInvisibleV.pack_start(lblPass, True, False, 0)
        cajaInvisibleV.pack_start(self.txtPass, True, False, 0)
        cajaInvisibleV.pack_start(btnLogear, True, False, 0)
        cajaInvisibleV.pack_start(self.lblCorInc, True, False, 0)
        cajaH.add(self.lblHelp)
        cajaH.add(frameLoginAdmin)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def on_btn_ClickAdmin(self,boton):
        """Los metodos son necesarios ya que necesitamos que las credenciales sean las correctas
        y no que se introduzca una clave cualquiera y entre un desconocido, para ello le añadimos una
        clave por defecto y sin esta clave no podrá entrar nadie.
        El mensaje que se muestra es de ayuda en este caso, se muestra en un boton superior de color azul"""
        password = self.txtPass.get_text()
        if (password == "abc123."):
            self.lblCorInc.set_text(str("Login Correcto"))
            paquete.winbase2.DataBaseTrainer()
            self.destroy()
        else:
            self.lblCorInc.set_text(str("Credenciales incorrectas"))

    def on_btn_help(self, boton):
        """Este es el metodo que indica la ayuda que necesitarías"""
        self.lblHelp.set_text("Necesitas credenciales de Admin")



if __name__ == "__main__":
    DataBase()
    Gtk.main()