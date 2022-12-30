## << Urban Cluster 102 >>
'''
레이어 : 인구격자 레이어에서 원하는 지역만 뽑은 레이어
실행 : urban cluster셀 찾기

++
수정해줘야 할 부분 : 필드 명, 필드 위치, 파일 경로

< 필드 설명 >
tot: 격자의 tot
id: 격자의 공간 인덱스
neighbors: 격자에 인접한 이웃격자들의 공간 인덱스
flag: 1=통합됨, 0=통합되지 않은 기준격자
tot_sum: 클러스터의 tot의 합
land: 클러스터의 번호
is_cluster: 102=UCluster
'''

# (시간 측정 위함) 코드의 제일 앞 부분
import time
import datetime
start = time.time()

from qgis.utils import iface
from PyQt5.QtCore import QVariant

# Names of the fields
_TOT_FIELD = 'TOT'
_ID_FIELD = 'id'
_NEIGHBORS_FIELD = 'neighbors_'
_FLAG_FIELD = 'flag'
_TOT_SUM_FIELD = 'TOT_SUM'
_LAND_FIELD = 'land'
_IS_CLUSTER_FIELD = 'is_cluster'

# location of field
_WHERE_TOT_FIELD = 5
_WHERE_NEIGHBORS_FIELD = 6
_WHERE_ID_FIELD = 7
_WHERE_FLAG_FIELD = 8
_WHERE_TOT_SUM_FIELD = 9
_WHERE_LAND_FIELD = 10
_WHERE_IS_CLUSTER_FIELD = 11

#UCluster 묶음이 있는 리스트
my_list102= []


## Create new field and initialization / 새로운 필드 추가와 초기화
def create_new_field_and_initialization(name,type,value):
    ##<<  Create new field and initialization  >>
    layer_provider = layer.dataProvider()
    layer_provider.addAttributes([QgsField(name, type)])
    layer.updateFields()

    visited_index = layer.fields().indexFromName(name)
    attr_map = {}
    new_value = value

    for line in layer.getFeatures():
        attr_map[line.id()] = {visited_index: new_value}
    layer.dataProvider().changeAttributeValues(attr_map)
    print('Processing complete. _create_new_field_and_initialization')


##<< Find the adjacent grid >> / 한 격자에 인접한 격자 찾기
def find_adjacent_grid():
    layer = iface.activeLayer()
    layer.startEditing()

    # create new fields / 새로운 필드 생성
    layer_provider = layer.dataProvider()
    layer_provider.addAttributes([QgsField(_NEIGHBORS_FIELD, QVariant.String),
                                  QgsField(_ID_FIELD, QVariant.Int)])
    layer.updateFields()

    # Create a dictionary of all features / 모든 피쳐에 대한 딕셔너리 생성
    feature_dict = {f.id(): f for f in layer.getFeatures()}

    # Build a spatial index / 공간 인덱스 생성
    index = QgsSpatialIndex()
    for f in feature_dict.values():
        index.insertFeature(f)

    # Loop through all features and find features that touch each feature / 모든 피쳐를 돌면서 인접한 격자 찾기
    for f in feature_dict.values():
        geom = f.geometry()
        # TOT above 300
        if (f.attributes()[_WHERE_TOT_FIELD] >= 300 ):
            # Find all features that intersect the bounding box of the current feature.
            intersecting_ids = index.intersects(geom.boundingBox())

            # Initalize neighbors list and sum / neighbors : 인접한 격자의 리스트
            neighbors = []
            # 한 격자의 인접한 격자들을 돌면서
            for intersecting_id in intersecting_ids:

                # Look up the feature from the dictionary / 자신의 공간 인덱스를 변수에 담아주고
                intersecting_f = feature_dict[intersecting_id]

                # add id in _ID_FIELD / 테이블과 매칭
                if (f == intersecting_f):
                    f[_ID_FIELD] = intersecting_id

                # 인접한 격자라면
                if (not intersecting_f.geometry().disjoint(geom) ):
                    # Add to neighbors when all neighbors satisfy tot>=300 / 테이블 돌면서 tot가 300 넘는건 인접한 이웃격자로 추가해줌
                    for b in feature_dict.values():
                        if (b.attributes()[_WHERE_ID_FIELD]==intersecting_id):
                            if (b.attributes()[_WHERE_TOT_FIELD] >= 300 ):
                                neighbors.append(intersecting_id)

            # 인접한 격자들의 공간인덱스를 neighbors 필드에 넣어줌
            f[_NEIGHBORS_FIELD] = ','.join(map(str, neighbors))

            # Update the layer with new attribute values.
            layer.updateFeature(f)

    layer.commitChanges()
    print('Processing complete. _find_adjacent_grid')



##<< Integrate neighbors >> / 클러스터 찾기 (묶음)
def integration_neighbors():
    layer = iface.activeLayer()
    layer.startEditing()

    # Create a dictionary of all features
    feature_dict = {f.id(): f for f in layer.getFeatures()}

    # my_list_a : a의 인접한 tot>=300 인 이웃
    # my_list_b : b의 인접한 tot>=300 인 이웃
    # my_list : a와 b의 이웃
    my_list_a = []
    my_list_b = []
    my_list = []

    # Make two pointers / 포인터 두개를 생성
    for a in feature_dict.values():
        # TOT above 300 / 그 격자의 tot가 300 이상이 넘고
        if (a.attributes()[_WHERE_TOT_FIELD] >=300):
            # 비교하는 격자의 포인터
            for b in feature_dict.values():
                # TOT above 300 / 비교하는 격자도 tot가 300이 넘는다면
                if (b.attributes()[_WHERE_TOT_FIELD] >=300):
                    # Initalize neighbors list / 인접한 이웃 리스트를 재생성 해주고
                    neighbors = []

                    ## not the one to compare itself and unmodified grid / 비교 대상이 자신이 아니고
                    if (a[_ID_FIELD] != b[_ID_FIELD]):  ##not the one to compare itself
                        if (a.attributes()[_WHERE_FLAG_FIELD] == 0 and b.attributes()[_WHERE_FLAG_FIELD] == 0):  ##unmodified grid / 통합되지 않은 셀이라면
                            # my_list_a에 a의 이웃들을 넣어
                            my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD])
                            my_list_a = my_list_a.split(',')

                            # Check the a_neighbor one by one / a의 이웃들을 모두 돌면서
                            for i in range(len(my_list_a)):  ##check a's neighbors_
                                number = my_list_a[i]  ##a's 'i'th neighbors_ / a의 i번째 이웃을 변수에 담아
                                # my_list_b에 b의 이웃을 넣어
                                my_list_b = str(b.attributes()[_WHERE_NEIGHBORS_FIELD])
                                my_list_b = my_list_b.split(',')

                                # Check elements of a_neighbor is in b_neighbors and both of them are unmodified
                                # / a와 b가 모두 통합되지 않았고 b의 이웃중에 a의 이웃이 있으면
                                if ((number in my_list_b) and (a[_FLAG_FIELD] == 0) and (
                                        b[_FLAG_FIELD] == 0)):

                                    # Combine a_neighbors and b_neighbors / a의 이웃과 b의 이웃을 합해
                                    my_list = my_list_a + my_list_b

                                    # Remove duplicate elements / 중복된 원소 제거
                                    new_list = []
                                    new_list.append(b.attributes()[_WHERE_ID_FIELD])
                                    for v in my_list:
                                        if v not in new_list:
                                            new_list.append(v)

                                    my_list102.append(new_list)

                                    a[_FLAG_FIELD] = 1

                                    b[_NEIGHBORS_FIELD] = ','.join(map(str, new_list))
                                    layer.updateFeature(a)
                                    layer.updateFeature(b)

    layer.commitChanges()
    print('Processing complete. _integration_neighbors')


##<< Calculate the sum of the tot in the cluster >> / 클러스터의 tot의 총합 구하기
def tot_sum():
    layer = iface.activeLayer()

    # Create new field and initialization
    layer_provider = layer.dataProvider()
    layer_provider.addAttributes([QgsField('TOT_SUM', QVariant.Int), QgsField('land', QVariant.Int)])
    layer.updateFields()
    layer.startEditing()

    # Names of the new fields to be added to the layer
    _TOT_SUM_FIELD = 'TOT_SUM'
    _LAND_FIELD = 'land'

    # Create a dictionary of all features
    feature_dict = {f.id(): f for f in layer.getFeatures()}

    land = 100

    # 결측치 제거 _TOT_FIELD
    for a in feature_dict.values():
        if (a.attributes()[_WHERE_TOT_FIELD] == NULL):
            a[_TOT_FIELD] = 0
            layer.updateFeature(a)

    # Make one pointer _table / 모든 피쳐를 돌면서
    for a in feature_dict.values():
        sum = 0
        my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD])
        my_list_a = my_list_a.split(',')

        # flag==0 and have neighors_ / give an id_field to variable / 통합되지 않은 기준격자이고 단독격자가 아니라면
        if (a.attributes()[_WHERE_FLAG_FIELD] == 0 and len(my_list_a) > 1):
            number = a.attributes()[_WHERE_ID_FIELD]

            # check array / 리스트 체크 (리스트와 테이블을 맞추는 작업)
            for i in range(len(my_list102)):
                # put id in number2 _array
                number2 = my_list102[i][0]
                number2 = int(number2)
                # match table's id (a) and array's id
                if (number2 == number):
                    # check i's neighbors _array
                    for j in range(1, len(my_list102[i])):
                        # check table
                        for b in feature_dict.values():
                            # Get the id from the array and the TOT of the id from the table
                            id = int(my_list102[i][j])
                            if (id == b.attributes()[_WHERE_ID_FIELD]):
                                TOT = b.attributes()[_WHERE_TOT_FIELD]
                                sum += TOT

                                b[_LAND_FIELD] = land
                                layer.updateFeature(b)

            land += 1
            if (sum >= 5000):
                a[_TOT_SUM_FIELD] = sum
                layer.updateFeature(a)

    layer.commitChanges()
    print('Processing complete. _tot_sum')


##<< Find cluster with more than 5000 tot_sum >> / tot의 총합이 5000이 넘는 클러스터 찾기
def find_5000above_clusters():
    layer = iface.activeLayer()
    layer.startEditing()

    # Create a dictionary of all features
    feature_dict = {f.id(): f for f in layer.getFeatures()}

    land_list = []

    # tot_sum이 5000이 넘는 클러스터의 land를 land_list에 추가
    for a in feature_dict.values():
        my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD])
        my_list_a = my_list_a.split(',')
        if (a.attributes()[_WHERE_TOT_SUM_FIELD] >= 5000 ):
            land_list.append(a.attributes()[_WHERE_LAND_FIELD])

    # 전체 피쳐를 돌면서 land_list속에 있는 land값을 가진 피쳐들의 is_cluster 필드에 102부여
    for a in feature_dict.values():
        my_list_a = str(a.attributes()[_WHERE_NEIGHBORS_FIELD])
        my_list_a = my_list_a.split(',')
        for b in range(len(land_list)):
            if (land_list[b] == a.attributes()[_WHERE_LAND_FIELD]):
                a[_IS_CLUSTER_FIELD] = 102
                layer.updateFeature(a)

    layer.commitChanges()
    print('Processing complete. _find 5000 above_clusters')

## Select by Expression / 표현식으로 피쳐 선택하기
def select_by_Expression(exp):
    layer.selectByExpression(exp, QgsVectorLayer.SetSelection)

## Fill value / 필드에 값 채우기
def fill_value(name,value):
    visited_index = layer.fields().indexFromName(name)
    attr_map = {}
    new_value = value

    for line in layer.getFeatures():
        attr_map[line.id()] = {visited_index: new_value}
    layer.dataProvider().changeAttributeValues(attr_map)
    print('Processing complete. _fill_value')





######################################### start
'''
여기부터 시작, 실행 하고싶은 함수만 골라서 실행하면 됨
'''

##<< import layer >> / 레이어 추가
fn = 'C:/Users/User/Desktop/지역분류체계/총정리/1_지역분류/1216test_new인구격자사용/인구격자00_부울경인근.shp'
layer = iface.addVectorLayer(fn, '', 'ogr')

# 레이어 지정 - 클릭된 레이어
layer= iface.activeLayer()

##<< Save layer as UCluster > /  UCluster로 레이어 저장
path = 'C:/Users/User/Desktop/지역분류체계/총정리/1_지역분류/1216test_new인구격자사용/인구격자00_부울경인근_UCluster102.shp'
_writer = QgsVectorFileWriter.writeAsVectorFormat(layer,path,'utf-8',driverName='ESRI Shapefile')

##<< import UCluster layer >> / UCenter 레이어 추가
layer = iface.addVectorLayer(path, '', 'ogr')

# 레이어 지정 - 클릭된 레이어
layer= iface.activeLayer()

##<< Find the adjacent grid>> / 인접한 이웃격자 찾기
find_adjacent_grid()

##<< Create new field and initialization >> / flag 필드 생성 후 0으로 초기화
create_new_field_and_initialization("flag",QVariant.Int,0)

##<< Integrate neighbors >> / 클러스터 찾기
integration_neighbors()

##<< Get TOT_SUM >> / 클러스터의 tot_sum 구하기
tot_sum()

##<< Add is_cluster field >> / is_cluster 필드 추가 후 0으로 초기화
create_new_field_and_initialization("is_cluster",QVariant.Int,0)


##<< Find cluster with more than 5000 tot_sum >> / tot_sum이 5000이 넘는 클러스터 찾기
find_5000above_clusters()


##<< Select by expression _"is_cluster=102" >> / UCluster인 것만 골라서 선택
select_by_Expression('"is_cluster"=102')


##<< Neighbors initialization >> Need to initialize because field length is not saved as exceeded / neighbors 필드를 0으로 초기화
fill_value(_NEIGHBORS_FIELD,0)


##<< Save selected part to vector layer >> / 선택된 레이어만 저장
_writer = QgsVectorFileWriter.writeAsVectorFormat(layer,
                                                  'C:/Users/User/Desktop/지역분류체계/총정리/1_지역분류/1216test_new인구격자사용/00_is_cluster_102.shp',
                                                  "EUC-KR", layer.crs(), "ESRI Shapefile", onlySelected=True)


##<< dissolve >>  - for Visualization / 시각화 위해 디졸브
layer = iface.activeLayer()

import processing

infn = 'C:/Users/User/Desktop/지역분류체계/총정리/1_지역분류/1216test_new인구격자사용/00_is_cluster_102.shp'
outfn2 = "C:/Users/User/Desktop/지역분류체계/총정리/1_지역분류/1216test_new인구격자사용/인구격자00_부울경인근_UCluster102_dissolve.shp"


processing.run("native:dissolve", {'INPUT': infn, 'FIELD': [_WHERE_LAND_FIELD], 'OUTPUT': outfn2})


##<< get dissolved file >> / 디졸브 한 레이어 추가
layer3 = iface.addVectorLayer(outfn2, '','ogr')

print('Processing complete._UrbanCluster 102')

# (시간 측정 위함) 코드의 제일 뒷 부분
sec = time.time()-start
times=str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)