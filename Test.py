import numpy as np
from scipy.special import fresnel
import gmsh
import sys
import math
import os

gmsh.initialize()
gmsh.open('./Stroemungsgebiet_mit_Spalt.STEP')
gmsh.model.occ.synchronize()
gmsh.model.mesh.generate(1)
gmsh.write("Kringel.msh")
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
