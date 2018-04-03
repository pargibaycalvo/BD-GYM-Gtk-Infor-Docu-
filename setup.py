#!/usr/bin/env python
from distutils.core import setup

#ficheiros= ["Cousas/*"]
setup(name = "AdministracionGYM",
      version="0.01",
      description="Aplicacion de exemplo de distribucion",
      long_description="""Descripcion en mais dunha liña
      extensa da aplicacion""",
      author="Pedro Argibay",
      author_email="pargibaycalvo@danielcastelao.org",
      url="www.urldoproxecto.es",
      keywords="Proba, distribuicion, exemplo",
      platforms="linux, mac",
      packages=['paquete'],
      #packages= find_packages(),
      #package_data={'Paquete': ficheiros},
      scripts=["lanzador"], requires=['reportlab']
      #py_modulos= ["moduloProbraModulo"]
      #install_requires= ["paquete_requerido >= 1.0 < 2.2"]

      )
#setup_requires
#test_requires