import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO

def fetch_and_visualize(symbol):
    # Download 6 months of daily close data
    data = yf.download(symbol, period="6mo", interval="1d")

    # Handle empty DataFrame or missing 'Close' column
    if data.empty or 'Close' not in data.columns or data['Close'].empty:
        raise ValueError(f"No closing price data found for symbol '{symbol}'. Please check the symbol and try again.")
    
    # Prepare the plot for the closing price trend
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(data['Close'], label="Close Price", color='tab:blue')
    ax.set_title(f"{symbol.upper()} Closing Prices - Last 6 Months")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.grid(True)
    ax.legend()

    # Save figure to memory buffer
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    # Add source note for display
    source_note = "Data fetched from Yahoo Finance via yfinance"

    return data, buf, source_note
