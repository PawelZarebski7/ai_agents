from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
import requests

load_dotenv()

# ========================================
# NARZĘDZIE 1: CENA KRYPTOWALUTY
# ========================================
@function_tool
def crypto_price(coin: str) -> str:
    """
    Gets current price of cryptocurrency from CoinGecko API.
    Use for bitcoin, ethereum, dogecoin, etc.
    Example: crypto_price('bitcoin')
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        if coin in data:
            price = data[coin]["usd"]
            return f"Current price of {coin}: ${price:,.2f} USD"
        else:
            return f"Coin '{coin}' not found. Try: bitcoin, ethereum, dogecoin"
    except:
        return "Error fetching crypto price"

# ========================================
# NARZĘDZIE 2: KALKULATOR
# ========================================
@function_tool
def calculator(expression: str) -> str:
    """
    Performs math calculations.
    Use for operations like addition, subtraction, multiplication, division.
    Example: calculator('100*5') or calculator('1000+1000')
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Error in calculation"

# ========================================
# NARZĘDZIE 3: PORÓWNANIE WALUT
# ========================================
@function_tool
def compare_crypto(coin1: str, coin2: str) -> str:
    """
    Compares prices of two cryptocurrencies.
    Returns prices and ratio between them.
    Example: compare_crypto('bitcoin', 'ethereum')
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin1},{coin2}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price1 = data[coin1]["usd"]
        price2 = data[coin2]["usd"]
        ratio = price1 / price2
        return f"{coin1}: ${price1:,.2f}, {coin2}: ${price2:,.2f}. Ratio: 1 {coin1} = {ratio:.2f} {coin2}"
    except:
        return "Error comparing cryptocurrencies"

# ========================================
# AGENT: CRYPTO ANALYST
# ========================================
analyst = Agent(
    name="Crypto Market Analyst",
    instructions="""You are a senior crypto analyst with 5 years experience.
    You use real-time data to make recommendations.
    You always check current prices before giving advice.
    You calculate potential returns and risks.
    Use the available tools to get crypto prices and do calculations.""",
    tools=[crypto_price, calculator, compare_crypto]
)

# ========================================
# ZADANIE: ANALIZA RYNKU
# ========================================
task = """Perform a crypto market analysis:
1. Get current price of bitcoin
2. Get current price of ethereum
3. Compare bitcoin vs ethereum
4. If someone invests $1000 in each, calculate total investment
5. Provide brief market insight"""

# ========================================
# URUCHOMIENIE
# ========================================
print("=" * 50)
print("CRYPTO ANALYSIS STARTING")
print("=" * 50)

result = Runner.run_sync(analyst, task)

print("\n" + "=" * 50)
print("FINAL REPORT")
print("=" * 50)
print(result.final_output)