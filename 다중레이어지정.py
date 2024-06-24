## 레이어 이름 조회
QgsProject.instance().mapLayers().values()


## 레이어 지정

layer11 = QgsProject.instance().mapLayersByName('arc_result_20_encoding')
layer1=layer11[0]