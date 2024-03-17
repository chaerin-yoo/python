import dart_fss as dart

# Open DART API KEY 설정
crtfc_key = '97e1792c560676d2a4e8d575327b3c68964c771b'
dart.set_api_key(api_key=crtfc_key)

# DART 에 공시된 회사 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자 검색
samsung = corp_list.find_by_corp_name('삼성전자', exactly=True)[0]

# 연간 연결재무제표 불러오기
fs = samsung.extract_fs(bgn_de='20190101', fs_tp=('bs','is','cf'))

print(fs)

# 엑셀파일로 저장