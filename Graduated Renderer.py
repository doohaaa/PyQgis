# Graduated Symbol Renderer

from PyQt5 import QtGui
layer=iface.activeLayer()
myVectorLayer = layer
myTargetField = 'TOT'
myRangeList = []
myOpacity = 0.6
# Make our first symbol and range...
myMin = 1500
myMax = 5000
myLabel = 'Group 1'
myColour = QtGui.QColor('yellow')
mySymbol1 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol1.setColor(myColour)
mySymbol1.setOpacity(myOpacity)
myRange1 = QgsRendererRange(myMin, myMax, mySymbol1, myLabel)
myRangeList.append(myRange1)
# now make another symbol and range...
myMin = 5000
myMax = 10000
myOpacity = 0.25
myLabel = 'Group 2'
myColour = QtGui.QColor('red')
mySymbol2 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol2.setColor(myColour)
mySymbol2.setOpacity(myOpacity)
myRange2 = QgsRendererRange(myMin, myMax, mySymbol2, myLabel)
myRangeList.append(myRange2)

myMin = 10000
myMax = 20000
myOpacity = 0.5
myLabel = 'Group 3'
myColour = QtGui.QColor('red')
mySymbol3 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol3.setColor(myColour)
mySymbol3.setOpacity(myOpacity)
myRange3 = QgsRendererRange(myMin, myMax, mySymbol3, myLabel)
myRangeList.append(myRange3)

myMin = 20000
myMax = 30000
myOpacity = 0.75
myLabel = 'Group 4'
myColour = QtGui.QColor('red')
mySymbol4 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol4.setColor(myColour)
mySymbol4.setOpacity(myOpacity)
myRange4 = QgsRendererRange(myMin, myMax, mySymbol4, myLabel)
myRangeList.append(myRange4)

myMin = 30000
myMax = 999999999
myOpacity = 0.5
myLabel = 'Group 5'
myColour = QtGui.QColor('black')
mySymbol5 = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
mySymbol5.setColor(myColour)
mySymbol5.setOpacity(myOpacity)
myRange5 = QgsRendererRange(myMin, myMax, mySymbol5, myLabel)
myRangeList.append(myRange5)



myRenderer = QgsGraduatedSymbolRenderer('', myRangeList)
myRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
myRenderer.setClassAttribute(myTargetField)

myVectorLayer.setRenderer(myRenderer)
QgsProject.instance().addMapLayer(myVectorLayer)
