import dart_fss as dart
import pandas as pd

corp_name='삼성전자'

# Open DART API KEY 설정
crtfc_key = '97e1792c560676d2a4e8d575327b3c68964c771b'
dart.set_api_key(api_key=crtfc_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 회사 검색
corp = corp_list.find_by_corp_name(corp_name, exactly=True)[0]
corp_code = str(corp)[1:9]

# 재무 정보
# 1분기보고서 : 11013, 반기보고서 : 110123, 분기보고서 : 11014, 사업보고서 : 11011
data = dart.api.finance.fnltt_singl_acnt(corp_code, '2014', '11011')

dataFrame = pd.DataFrame(data['list'])

# dataFrame = dataFrame[['bsns_year', '']]
# dataFrame.columns = ['연도', '']

dataFrame = dataFrame.loc[(dataFrame['fs_nm'] == '연결재무제표') & (dataFrame['account_nm'] == '자본금')]

print(dataFrame)

dataFrame.to_excel('삼성전자.xlsx')
