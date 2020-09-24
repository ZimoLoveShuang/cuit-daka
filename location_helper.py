import requests

# 高德地图Web服务的key，官方地址，https://console.amap.com/dev/key/app
key = ''
# 百度地图浏览器端的ak，官方地址，http://lbsyun.baidu.com/apiconsole/key#/home
ak = ''

# 首先用百度地图的ip定位获取到经纬度，为什么要用百度的ip定位呢，因为高德的ip定位不传ip获取不到经纬度信息
res = requests.get(url='http://api.map.baidu.com/location/ip?ak={ak}&ip=&coor=bd09ll'.format(ak=ak))
point = res.json()['content']['point']
location = '%.6f,%.6f' % (float(point['x']), float(point['y']))

# 然后使用高德地图的逆地理编码，获得格式化后的位置，为什么要用高德地图呢，因为学校的app就是用的高德地图定位
res = requests.get(
    url='https://restapi.amap.com/v3/geocode/regeo?output=json&location={location}&key={key}&radius=1000&extensions=all'.format(
        location=location, key=key))
regeocode = res.json()['regeocode']

# 下面这些是需要的信息
print('location：', regeocode['formatted_address'])
print('locationProvince：', regeocode['addressComponent']['province'])
print('locationCity：', regeocode['addressComponent']['city'])
print('locationCountry：', regeocode['addressComponent']['district'])
