
import SofaRuntime

# to add elements like Node or objects
import Sofa.Core
import os
path = os.path.dirname(os.path.abspath(__file__))+'/design/'

def createScene(rootNode):

	rootNode.addObject('RequiredPlugin', name="CGALPlugin") # Needed to use components [MeshGenerationFromPolyhedron]
	rootNode.addObject('RequiredPlugin', name='Sofa.Component.IO.Mesh') # Needed to use components [MeshSTLLoader,VTKExporter]
	rootNode.addObject('RequiredPlugin', name='Sofa.Component.StateContainer') # Needed to use components [MechanicalObject]
	rootNode.addObject('RequiredPlugin', name='Sofa.Component.Topology.Container.Constant') # Needed to use components [MeshTopology]
	rootNode.addObject('RequiredPlugin', name='Sofa.Component.Visual') # Needed to use components [VisualStyle]
	rootNode.addObject('RequiredPlugin', name='Sofa.GL.Component.Rendering3D') # Needed to use components [OglModel]

	rootNode.addObject('VisualStyle',displayFlags="hideVisual")

	rootNode.addObject('MeshSTLLoader', name="loader", filename="mesh/cylinder5296.stl")

	rootNode.addObject('MechanicalObject', name="dofs", position="@loader.position")


	rootNode.addObject('MeshGenerationFromPolyhedron', name="gen", inputPoints="@loader.position", inputTriangles="@loader.triangles",facetSize="0.2",facetApproximation="1",cellRatio="0.2", cellSize="0.25", drawTetras = 1)
	rootNode.addObject('MeshTopology', name ='topo', position='@gen.outputPoints', tetrahedra='@gen.outputTetras')
	rootNode.addObject('VTKExporter', filename='finger',src = '@topo', edges='0', exportAtBegin='1')
	rootNode.addObject('OglModel', color=[0.3, 0.2, 0.2, 0.6])
	return rootNode
