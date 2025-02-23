class PatternRecognizer:
    """
    Basic class for the pattern recognizer component.
    """
    def __init__(self, config):
        """
        Initializes the PatternRecognizer.
        """
        self.config = config
        print("PatternRecognizer initialized")

    def recognize_patterns(self, chart_data):
        """
        Recognizes chart patterns in the given chart data.
        """
        patterns = {}
        patterns['doji'] = self._is_doji(chart_data)
        patterns['bullish_engulfing'] = self._is_bullish_engulfing(chart_data)
        patterns['bearish_engulfing'] = self._is_bearish_engulfing(chart_data) # Add Bearish Engulfing
        patterns['morning_star'] = self._is_morning_star(chart_data) # Add Morning Star
        print(f"Bullish Engulfing pattern? {'Yes' if patterns.get('bullish_engulfing') else 'No'}")
        print(f"Bearish Engulfing pattern? {'Yes' if patterns.get('bearish_engulfing') else 'No'}")
        print(f"Morning Star pattern? {'Yes' if patterns.get('morning_star') else 'No'}")
        return patterns

    def _is_doji(self, chart_data):
        """
        Detects Doji candlestick pattern.
        A Doji is when the open and close prices are virtually equal.
        """
        if not chart_data or len(chart_data) < 1:
            return False

        # OHLCV data is a list of lists: [timestamp, open, high, low, close, volume]
        candle = chart_data[-1] # Get the latest candle
        open_price = candle[1] # Index 1 is the open price
        close_price = candle[4] # Index 4 is the close price
        
        # Define a threshold for considering open and close prices equal
        threshold = 0.001 * open_price  # e.g., 0.1% of the open price
        return abs(close_price - open_price) < threshold

    def _is_bullish_engulfing(self, chart_data):
        """
        Detects Bullish Engulfing candlestick pattern.
        """
        if not chart_data or len(chart_data) < 2:
            return False

        # Get the last two candles
        first_candle = chart_data[-2]
        second_candle = chart_data[-1]

        first_open = first_candle[1]
        first_close = first_candle[4]
        second_open = second_candle[1]
        second_close = second_candle[4]

        # Condition 1: Downtrend (simplified - check if first candle is bearish)
        is_downtrend = first_close < first_open

        # Condition 2: Second candle bullish and engulfs first candle's body
        is_bullish_candle = second_close > second_open
        # Check if the second candle's body completely engulfs the first candle's body
        body_engulfs = second_open < first_open and second_close > first_close

        # Consider the size of the candles - second candle should be reasonably sized
        candle_size_threshold = 0.0005 * second_open # e.g., 0.05% of the open price
        is_significant_size = (second_close - second_open) > candle_size_threshold

        if is_downtrend and is_bullish_candle and body_engulfs and is_significant_size:
            return True
        return False

    def _is_bearish_engulfing(self, chart_data): # Bearish Engulfing detection logic
        """
        Detects Bearish Engulfing candlestick pattern.
        """
        if not chart_data or len(chart_data) < 2:
            return False

        # Get the last two candles
        first_candle = chart_data[-2]
        second_candle = chart_data[-1]

        first_open = first_candle[1]
        first_close = first_candle[4]
        second_open = second_candle[1]
        second_close = second_candle[4]

        # Condition 1: Uptrend (simplified - check if first candle is bullish)
        is_uptrend = first_close > first_open

        # Condition 2: Second candle bearish and engulfs first candle's body
        is_bearish_candle = second_close < second_open
        # Check if the second candle's body completely engulfs the first candle's body
        body_engulfs = second_open > first_open and second_close < first_close

        # Consider the size of the candles - second candle should be reasonably sized
        candle_size_threshold = 0.0005 * second_open # e.g., 0.05% of the open price
        is_significant_size = (second_open - second_close) > candle_size_threshold

        if is_uptrend and is_bearish_candle and body_engulfs and is_significant_size:
            return True
        return False

    def _is_morning_star(self, chart_data): # Placeholder for Morning Star
        """
        Detects Morning Star candlestick pattern.
        """
        if not chart_data or len(chart_data) < 3:
            return False

        first_candle = chart_data[-3]
        second_candle = chart_data[-2]
        third_candle = chart_data[-1]

        first_open = first_candle[1]
        first_close = first_candle[4]
        second_open = second_candle[1]
        second_close = second_candle[4]
        third_open = third_candle[1]
        third_close = third_candle[4]

        # Condition 1: Downtrend (simplified - check if first candle is bearish)
        is_downtrend = first_close < first_open
        # Condition 2: First candle is bearish
        is_first_bearish = first_close < first_open
        # Condition 3: Second candle is a Doji or small-bodied candle
        is_second_small_body = abs(second_close - second_open) <= abs(first_close - first_open) * 0.5
        # Condition 4: Third candle is bullish and closes above midpoint of first candle
        is_third_bullish = third_close > third_open
        closes_above_midpoint = third_close > (first_open + first_close) / 2

        if is_downtrend and is_first_bearish and is_second_small_body and is_third_bullish and closes_above_midpoint:
            return True
        return False