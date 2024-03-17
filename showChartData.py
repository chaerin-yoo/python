import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일에서 데이터 읽어오기
df = pd.read_csv('kakaobank_data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')


# 그래프 그리기
plt.figure(figsize=(10,5))
plt.plot(df['Close'])
plt.title('Kakao Bank Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')
plt.show()