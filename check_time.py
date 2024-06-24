## 시간 측정 위해 맨 앞과 뒤에 추가해주는 코드 _ 시,분,초 단위로 출력


# 코드의 제일 앞 부분
import time
import datetime
start = time.time()

# 코드의 제일 뒷 부분
sec = time.time()-start
times=str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)