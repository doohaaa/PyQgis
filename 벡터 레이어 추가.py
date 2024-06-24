#벡터 레이어 추가
#Add Vector Layer

fn="C:/Users/User/Desktop/지역분류체계/urban_emd_20/인구격자읍면동_20_부산/original"
layer = iface.addVectorLayer(fn, '', 'ogr')

## encoding
layer.setProviderEncoding(u'UTF-8')
layer.dataProvider().setEncoding(u'UTF-8')
