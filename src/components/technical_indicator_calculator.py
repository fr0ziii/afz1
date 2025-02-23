import pandas as pd
import logging # Import logging

class TechnicalIndicatorCalculator:
    """
    Component for calculating technical indicators from chart data.
    """

    def __init__(self, config):
        self.config = config
        self.indicators_config = self.config.get("indicators", []) # List of indicators to calculate
        self.logger = logging.getLogger(__name__) # Initialize logger

    def calculate_indicators(self, ohlcv_data: list) -> pd.DataFrame:
        """
        Calculates the technical indicators based on OHLCV data.

        Args:
            ohlcv_data (list): OHLCV data as a list of lists.

        Returns:
            pd.DataFrame: DataFrame containing OHLCV data and calculated indicators.
        """
        df = pd.DataFrame(ohlcv_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)

        if not self.indicators_config:
            return df # Return исходный DataFrame если indicators_config пуст

        for indicator_name in self.indicators_config:
            if indicator_name == "SMA":
                df = self._calculate_sma(df)
            elif indicator_name == "EMA":
                df = self._calculate_ema(df)
            elif indicator_name == "RSI":
                df = self._calculate_rsi(df)
            elif indicator_name == "MACD":
                df = self._calculate_macd(df)
            # Add other indicators here
        return df

    def _calculate_sma(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates Simple Moving Average (SMA).
        """
        periods = self.config.get("indicator_periods", {}).get("SMA", [20]) # Default SMA period is 20
        for period in periods:
            df[f'SMA_{period}'] = df['close'].rolling(window=period).mean()
        return df

    def _calculate_ema(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates Exponential Moving Average (EMA).
        """
        periods = self.config.get("indicator_periods", {}).get("EMA", [20]) # Default EMA period is 20
        for period in periods:
            df[f'EMA_{period}'] = df['close'].ewm(span=period, adjust=False).mean()
        return df


    def _calculate_rsi(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates Relative Strength Index (RSI).
        """
        rsi_period_config = self.config.get("indicator_periods", {}).get("RSI", 14) # Get RSI period config
        print(f"RSI period config value: {rsi_period_config}, type: {type(rsi_period_config)}") # Print period config value and type
        period = int(rsi_period_config) # Default RSI period is 14, cast to int, corrected syntax again and again
        print(f"RSI period value after int conversion: {period}, type: {type(period)}") # Print period value and type AFTER conversion

        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).fillna(0)
        loss = (-delta.where(delta < 0, 0)).fillna(0)

        avg_gain = gain.rolling(window=period, min_periods=period).mean() # Cast period to int here as well
        avg_loss = loss.rolling(window=period, min_periods=period).mean() # Cast period to int here as well

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        df[f'RSI_{period}'] = rsi
        return df

    def _calculate_macd(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates Moving Average Convergence Divergence (MACD).
        """
        macd_config = self.config.get("indicator_periods", {}).get("MACD", {"fast_period": 12, "slow_period": 26, "signal_period": 9})
        fast_period = macd_config.get("fast_period", 12)
        slow_period = macd_config.get("slow_period", 26)
        signal_period = macd_config.get("signal_period", 9)

        ema_fast = df['close'].ewm(span=fast_period, adjust=False).mean()
        ema_slow = df['close'].ewm(span=slow_period, adjust=False).mean()
        macd = ema_fast - ema_slow
        signal = macd.ewm(span=signal_period, adjust=False).mean()
        histogram = macd - signal

        df['MACD'] = macd
        df['MACD_Signal'] = signal
        df['MACD_Histogram'] = histogram
        return df

    # Add more indicator calculation methods here (e.g., Bollinger Bands, Fibonacci Retracement)