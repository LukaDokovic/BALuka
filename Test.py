
import gmsh
import os
import sys



gmsh.initialize()

gmsh.merge('./Analogieprüfstand_Spanraum.STEP')

gmsh.model.geo.synchronize()


gmsh.fltk.run()

gmsh.finalize()
