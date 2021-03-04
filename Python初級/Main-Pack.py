#建立資料夾放程式碼 !!需新增_init_.py檔(新版可不加)
#主程式
import geometry.point
resile=geometry.point.distance(3,4)
print(resile)

import geometry.line as s
resile=s.len(1,1,3,3)
print(resile)

import geometry.line as line
resile=line.slope(1,1,3,3)
print(resile)