#載入內建sys模組並取得資訊
# import sys as s

# print(s.platform)
# print(s.maxsize)


#建立geometry模組，載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)

# result=geometry.slope(1,2,5,6)
# print(result)


#調整搜尋模組路徑
import sys
sys.path.append("BackUp")#搜尋資料夾 模駔路徑
#print(sys.path)#印出路印

import geometry
print(geometry.distance(1,1,5,5))