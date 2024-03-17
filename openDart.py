import requests 
import pandas as pd 
import io 
import zipfile
import xml.etree.ElementTree as et 
import json


crtfc_key = '97e1792c560676d2a4e8d575327b3c68964c771b'


######################################
# OpenDART 기업 고유번호 받아오기
######################################
def get_corpcode(crtfc_key): 
    params = {'crtfc_key':crtfc_key} 
    items = ["corp_code","corp_name","stock_code","modify_date"] 
    item_names = ["고유번호","회사명","종목코드","수정일"] 
    url = "https://opendart.fss.or.kr/api/corpCode.xml" #요청 url
    res = requests.get(url,params=params) #url 불러오기
    zfile = zipfile.ZipFile(io.BytesIO(res.content))  #zip file 받기
    fin = zfile.open(zfile.namelist()[0])  #zip file 열고
    root = et.fromstring(fin.read().decode('utf-8'))  #utf-8 디코딩
    data = [] 
    for child in root: 
        if len(child.find('stock_code').text.strip()) > 1: # 종목코드가 있는 경우 
            data.append([]) #data에 append하라 
            for item in items: 
                data[-1].append(child.find(item).text) 
    df = pd.DataFrame(data, columns=item_names) 
    return df


stock_comp = get_corpcode(crtfc_key)

print(stock_comp)





def Frame(url, items, item_names, params): 
    """
    url : json형태로 요청하는 주소
    items : 반환되는 데이터들의 key를 가진 리스트
    item_names :  데이터프레임을 만들때 컬럼명 리스트
    params : url 요청시 필수값으로 들어가는 인자들을 가진 딕셔너리
    """
    res = requests.get(url, params)
    json_data = res.json()
    json_dict = json.loads(res.text) 
    data = [] 
    if json_dict['status'] == "000":  # 오류 없이 정상적으로 데이터가 있다면 
        for line in json_dict['list']: 
            data.append([])
            for itm in items: 
                if itm in line.keys(): 
                    data[-1].append(line[itm]) 
                else: 
                    data[-1].append('')
    df = pd.DataFrame(data, columns=item_names)
    return df