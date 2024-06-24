#TOT 격자 수 구하기

layer=iface.activeLayer()
print(layer)

layer.selectByExpression('"TOT">=0 and "TOT"<=299',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("0 ~ 299 : %d" %features_count)

layer.selectByExpression('"TOT">=300 and "TOT"<=499',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("300 ~ 499 : %d" %features_count)

layer.selectByExpression('"TOT">=500 and "TOT"<=999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("500 ~ 999 : %d" %features_count)

layer.selectByExpression('"TOT">=1000 and "TOT"<=1999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("1000 ~ 1999 : %d" %features_count)

layer.selectByExpression('"TOT">=2000 and "TOT"<=2999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("2000- : %d" %features_count)

layer.selectByExpression('"TOT">=3000 and "TOT"<=3999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("3000- : %d" %features_count)

layer.selectByExpression('"TOT">=4000 and "TOT"<=4999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("4000- : %d" %features_count)

layer.selectByExpression('"TOT">=5000 and "TOT"<=5999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("5000- : %d" %features_count)

layer.selectByExpression('"TOT">=6000 and "TOT"<=6999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("6000- : %d" %features_count)

layer.selectByExpression('"TOT">=7000 and "TOT"<=7999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("7000- : %d" %features_count)

layer.selectByExpression('"TOT">=8000 and "TOT"<=8999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("8000- : %d" %features_count)

layer.selectByExpression('"TOT">=9000 and "TOT"<=9999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("9000- : %d" %features_count)

layer.selectByExpression('"TOT">=10000 and "TOT"<=10999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("10000- : %d" %features_count)

layer.selectByExpression('"TOT">=11000 and "TOT"<=11999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("11000- : %d" %features_count)

layer.selectByExpression('"TOT">=12000 and "TOT"<=12999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("12000- : %d" %features_count)

layer.selectByExpression('"TOT">=13000 and "TOT"<=13999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("13000- : %d" %features_count)

layer.selectByExpression('"TOT">=14000 and "TOT"<=14999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("14000- : %d" %features_count)

layer.selectByExpression('"TOT">=15000 and "TOT"<=15999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("15000- : %d" %features_count)

layer.selectByExpression('"TOT">=16000 and "TOT"<=16999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("16000- : %d" %features_count)

layer.selectByExpression('"TOT">=17000 and "TOT"<=17999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("17000- : %d" %features_count)

layer.selectByExpression('"TOT">=18000 and "TOT"<=18999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("18000- : %d" %features_count)

layer.selectByExpression('"TOT">=19000 and "TOT"<=19999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("19000- : %d" %features_count)

layer.selectByExpression('"TOT">=20000 and "TOT"<=24999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("20000- : %d" %features_count)

layer.selectByExpression('"TOT">=25000 and "TOT"<=29999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("25000- : %d" %features_count)

layer.selectByExpression('"TOT">=30000 and "TOT"<=34999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("30000- : %d" %features_count)

layer.selectByExpression('"TOT">=35000 and "TOT"<=39999',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("35000- : %d" %features_count)

layer.selectByExpression('"TOT">=40000',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("40000- : %d" %features_count)

layer.selectByExpression('"TOT" is null',QgsVectorLayer.SetSelection)
features_count = layer.selectedFeatureCount()
print("null : %d" %features_count)

print(layer.featureCount())
##for i in range(1000,19000,1000):
  ##  j=i+999
    ##layer.selectByExpression('"TOT">=i and "TOT"<=j',QgsVectorLayer.SetSelection)
    ##features_count = layer.selectedFeatureCount()
    ##print("%d ~ %d : %d" %(i,j,features_count))