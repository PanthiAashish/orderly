from openai import OpenAI
from app.core.config import settings
import json

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class TradeParseError(Exception):
    pass

def parse_trade_instruction(text: str) -> dict:
    system_prompt = (
        "You are a trading assistant. "
        "Given a natural language instruction, extract the structured trading command "
        "strictly as a JSON object with these fields:\n"
        "- action (string: 'buy' or 'sell')\n"
        "- ticker (string: stock symbol in ALL CAPS, like 'AAPL', 'TSLA')\n"
        "- amount (number: amount of money to invest in USD)\n"
        "- condition (string: written in machine-readable format, like 'price < 100' or 'price > 200')\n\n"
        "Rules:\n"
        "- Do NOT include company names like 'apple', use only tickers like 'AAPL'.\n"
        "- Always use double quotes (\") in your JSON.\n"
        "- Only return JSON. No extra words or explanation."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        )

        parsed_text = response.choices[0].message.content
        parsed_data = json.loads(parsed_text)
        return parsed_data

    except Exception as e:
        raise TradeParseError(f"Error parsing trade instruction: {str(e)}")