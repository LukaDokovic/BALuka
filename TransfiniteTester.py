import gmsh



Spandau = gmsh.model.occ
gmsh.initialize()

lc = -1

Spandau.addPoint(0,0,0,lc,1)
Spandau.addPoint(1,0,0,lc,2)
Spandau.addPoint(1,1,0,lc,3)
Spandau.addPoint(0,1,0,lc,4)

Spandau.addBSpline([1,2], degree=3, tag=1) #OriginalKringel
Spandau.addBSpline([2,3], degree=3, tag=2) #OriginalKringel
Spandau.addBSpline([3,4], degree=3, tag=3) #OriginalKringel
Spandau.addBSpline([4,1], degree=3, tag=4) #OriginalKringel

Spandau.addCurveLoop([1,2,3,4], tag = 1)
Spandau.addPlaneSurface([1])

Spandau.synchronize()

gmsh.model.mesh.setTransfiniteCurve(1, 20)
gmsh.model.mesh.setTransfiniteCurve(2, 10)
gmsh.model.mesh.setTransfiniteCurve(3, 20)
gmsh.model.mesh.setTransfiniteCurve(4, 10)


gmsh.model.mesh.setTransfiniteSurface(1)


gmsh.model.mesh.generate(2)
gmsh.write("Tester.msh")
gmsh.fltk.run()
gmsh.clear()
gmsh.finalize()
