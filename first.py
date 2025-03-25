import os
from dotenv import load_dotenv
load_dotenv()

#1. 업비트 차트 데이터 가져오기(예시. 일봉 30개)

import pyupbit
df = pyupbit.get_ohlcv("KRW-BTC", count = 30, interval = "day")


#2. AI에게 데이터 제공하고 판단받기
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are an expert in Bitcoin investing. Tell me whether to buy, sell, or hold at the moment based on the chart data provided. response in json format.\n\nResponse Example :\n{\"decision\" : \"hold\", \"reason\" : \"some technical reason\"}\n{\"decision\" : \"buy\", \"reason\" : \"some technical reason\"}\n{\"decision\" : \"sell\", \"reason\" : \"some technical reason\"}"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": df.to_json()
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"decision\": \"sell\",\n  \"reason\": \"The chart data shows a general downtrend in Bitcoin prices with no signs of reversal. The recent trend indicates decreasing highs and lows, reflecting bearish market sentiment. Additionally, there's a significant increase in selling volume without corresponding upward price movement, suggesting strong selling pressure.\"\n}"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"decision\": \"sell\",\n  \"reason\": \"The chart data shows a general downtrend in Bitcoin prices with no signs of reversal. The recent trend indicates decreasing highs and lows, reflecting bearish market sentiment. Additionally, there's a significant increase in selling volume without corresponding upward price movement, suggesting strong selling pressure.\"\n}"
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)