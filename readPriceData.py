##################################################################################################################################
# 1. 주식, 환율, 암호화폐, 종목 리스팅 등 다양한 금융 데이터를 수집할 수 있는 라이브러리 설치
# $ pip install -U finance-datareader
# $ pip install plotly (의존성)
#
# 2. HTML 및 XML 문서를 파싱하기위한 Python 라이브러리로 FinanceDataReader에서 내부적으로 사용하기 위함
# $ pip install beautifulsoup4
#
# 3. Python에서 데이터를 차트나 플롯으로 사막화하는 라이브러리
# $ matplotlib
##################################################################################################################################

import FinanceDataReader as fdr

# 한국 주식 코드 목록 가져오기
krx = fdr.StockListing('KRX')

code = krx[krx['Name'] == '카카오뱅크']['Code'].values[0]
print(code)


# 주식 코드값으로 주식 데이터 가져오기 (최근 5개)
# 카카오뱅크 주식코드 : 323410
# df = fdr.DataReader('323410')
# print(df.head())


# 특정 기간의 주식 데이터 수집하기
df = fdr.DataReader('323410', '2023-01-01', '2023-12-31')

df['Open']   = df['Open'].apply(lambda x: f'{x:,}원')
df['High']   = df['High'].apply(lambda x: f'{x:,}원')
df['Low']    = df['Low'].apply(lambda x: f'{x:,}원')
df['Close']  = df['Close'].apply(lambda x: f'{x:,}원')
df['Volume'] = df['Volume'].apply(lambda x: f'{x:,}건')
df['Change'] = df['Change'].apply(lambda x: f'{x:.2%}')

df = df.rename(columns={'Date':'날짜', 'Open':'시가', 'High':'고가', 'Low':'저가', 'Close':'종가', 'Volume':'거래량', 'Change':'변동률'})

print(df.tail())

# csv 파일로 저장
df.to_csv('kakaobank_data.csv')