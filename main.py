import requests
import googlemaps
from datetime import datetime
import dotenv
import configparser

def distancexx(mylocation):
    info = dotenv.dotenv_values('.env')
    api_key = info.get('GOOGLE_PLACES_API_KEY')
    gmaps_client=googlemaps.Client(key=api_key)
    now=datetime.now()
    headers = {'Accept': 'application/json'}
    data=['國賓大戲院','台北獅子林新光影城','樂聲影城 LUX CINEMA','今日秀泰影城','喜滿客影城 絕色店','台北in89豪華影城',
    '真善美劇院','光點台北(台北之家)','光點華山電影館','臺北京站威秀影城','百老匯影城','東南亞秀泰影城','湳山戲院','梅花數位影院','新民生戲院',
    '欣欣秀泰影城','總督數位影城','台北天母新光影城','台北長春國賓影城','華威天母影城','美麗新大直皇家影城','微風影城','美麗華大直影城','哈拉影城',
    '佳佳來來戲院','台北信義威秀影城','誠品電影院','喜樂時代影城 南港店','台北松仁威秀影城 MUVIE CINEMAS','天台影城','板橋秀泰影城','板橋大遠百威秀影城',
    '鴻金寶麻吉影城','中和環球威秀影城','林口昕境國賓影城','新莊晶冠國賓影城','林口MITSUI OUTLET PARK威秀影城','樹林秀泰影城','土城秀泰影城',
    '美麗新淡海影城','美麗新宏匯影城','淡水禮萊國賓影城','喜樂時代影城 永和店','全球影城','台中日日新影城','豐源國際影城','臺中大遠百威秀影城',
    '台中中港新光影城','台中大魯閣新時代威秀影城','親親戲院','台中TIGER CITY威秀影城','時代影城2館','秀泰影城二館','台中站前秀泰影城','台中文心秀泰影城',
    '台中麗寶秀泰影城','台中in89豪華影城','台南仁德秀泰影城','全美戲院','今日戲院','台南大遠百威秀影城','台南西門新光影城','台南國賓影城','南台影城',
    '麻豆戲院','台南南紡威秀影城','台南FOCUS威秀影城','台南真善美劇院','夢時代秀泰影城','高雄台鋁秀泰影城','高雄大遠百威秀影城','環球影城',
    '岡山秀泰影城','高雄義大國賓影城','in89駁二電影院','國賓影城','高雄大立in89豪華影城','喜樂時代影城 高雄總圖店','基隆秀泰影城',
    '桃園青埔新光影城','喜樂時代影城 桃園A19店','美麗新台茂影城','桃園in89統領影城','星橋國際影城','威尼斯影城','八德置地國賓影城','桃園統領威秀影城',
    '星際國際影城本館','星際國際影城中興館','新竹大遠百威秀影城','新竹巨城威秀影城','新復珍戲院','新竹市影像博物館 或者光盒子','Broadway cinemas 百老匯影城竹北店',
    '頭份尚順威秀影城','台灣大戲院','員林影城','埔里山明戲院','南投戲院','雲林北港秀泰影城','白宮影城','環球中華影城','嘉義in89豪華影城','嘉年華影城',
    '嘉義秀泰影城','中影股份有限公司屏東光華分公司','屏東環球國賓影城','友愛影城','日新戲院','羅東日新戲院統一廳（原統一戲院）','新月豪華影城','花蓮秀泰影城',
    '花蓮新天堂樂園威秀影城','台東秀泰影城','金獅影城','國賓影城 @金門昇恆昌金湖廣場','澎湖in89豪華影城']
    get_movie=[]
    my_params={'location':mylocation,
                'radius':1500,
                'keyword':'影城||戲院',
                'language':'zh-TW',
                'key':api_key
                }
    rurl=requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?',params=my_params)
    r = requests.get(rurl.url,headers=headers)
    
    dic1=r.json()
    results_list=[]
    for i in dic1['results']:
        if i['name'] in data :
            dest = '{},{}'.format(i['geometry']['location']['lat'], i['geometry']['location']['lng'])
            d_result=gmaps_client.directions(mylocation,dest,mode="driving",avoid='ferris',departure_time=now,language='zh-tw',transit_mode='best_guess')
            # directions(我的位置,計算距離位置,mode="預計行使模式",avoid='避開什麼路段',departure_time=起程時間,language=語言',transit_mode='best_guess(官方推薦)')
            place=i['name']
            rating=i['rating']
            distance=d_result[0]['legs'][0]['distance']['value']
            time=d_result[0]['legs'][0]['duration']['text']
            results_list.append({'place': place, 'rating': rating, 'distance': distance, 'time': time})
    
    results_list = sorted(results_list, key=lambda x: x['distance'])
    
    count = 0
    for result in results_list:
        movie = f"地點: {result['place']}, 評分: {result['rating']}, 距離: {result['distance']} 公尺, 預計時間: {result['time']}"
        get_movie.append(movie)
        count += 1
        if count == 3:
            break
    return '\n'.join(get_movie)
    
print(distancexx('25.0452169, 121.506424'))
