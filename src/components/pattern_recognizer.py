import logging

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
        self.logger = logging.getLogger(__name__) # Initialize logger

    def recognize_patterns(self, chart_data):
        """
        Recognizes chart patterns in the given chart data.
        """
        patterns = {}
        self.logger.debug("Checking for Doji pattern...")
        patterns['doji'] = self._is_doji(chart_data)
        self.logger.debug("Checking for Bullish Engulfing pattern...")
        patterns['bullish_engulfing'] = self._is_bullish_engulfing(chart_data)
        self.logger.debug("Checking for Bearish Engulfing pattern...")
        patterns['bearish_engulfing'] = self._is_bearish_engulfing(chart_data)
        self.logger.debug("Checking for Morning Star pattern...")
        patterns['morning_star'] = self._is_morning_star(chart_data)
        self.logger.debug("Checking for Evening Star pattern...")
        patterns['evening_star'] = self._is_evening_star(chart_data) # Add Evening Star
        self.logger.debug("Checking for Advance Block pattern...")
        patterns['advance_block'] = self._is_advance_block(chart_data) # Add Advance Block
        self.logger.debug("Checking for Three White Soldiers pattern...")
        patterns['three_white_soldiers'] = self._is_three_white_soldiers(chart_data) # Add Three White Soldiers

        detected_patterns = []
        for pattern, detected in patterns.items():
            if detected:
                detected_patterns.append(pattern)
                self.logger.info(f"Detected pattern: {pattern}")
            else:
                self.logger.debug(f"Pattern not detected: {pattern}") # Changed to debug level

        if not detected_patterns:
            self.logger.info("No candlestick patterns detected.")
        else:
            self.logger.info(f"Detected patterns summary: {', '.join(detected_patterns)}")


        return {'patterns': [{'pattern_name': pattern} for pattern in detected_patterns]}

    def _is_doji(self, chart_data):
        """
        Detects Doji candlestick pattern.
        A Doji is when the open and close prices are virtually equal.
        """
        if not chart_data or len(chart_data) < 1:
            return False

        candle = chart_data[-1]
        open_price = candle[1]
        close_price = candle[4]
        threshold = 0.001 * open_price
        is_doji = abs(close_price - open_price) < threshold
        return is_doji

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
        candle_size_threshold = 0.0005 * second_open
        is_significant_size = (second_close - second_open) > candle_size_threshold

        return is_downtrend and is_bullish_candle and body_engulfs and is_significant_size

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
        candle_size_threshold = 0.0005 * second_open
        is_significant_size = (second_open - second_close) > candle_size_threshold

        return is_uptrend and is_bearish_candle and body_engulfs and is_significant_size

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

        return is_downtrend and is_first_bearish and is_second_small_body and is_third_bullish and closes_above_midpoint

    def _is_evening_star(self, chart_data):
        """Detects Evening Star candlestick pattern."""
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

        is_uptrend = first_candle[4] > first_candle[1]
        is_first_bullish = first_close > first_open
        is_second_small_body = abs(second_close - second_open) <= abs(first_close - first_open) * 0.5
        is_third_bearish = third_close < third_open
        closes_below_midpoint = third_close < (first_open + first_close) / 2

        return is_uptrend and is_first_bullish and is_second_small_body and is_third_bearish and closes_below_midpoint


    def _is_advance_block(self, chart_data):
        """Detects Advance Block candlestick pattern."""
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

        # Condition 1: Uptrend
        is_uptrend = first_close > first_open and second_close > second_open and third_close > third_open and \
                     second_close > first_close and third_close > second_close

        # Condition 2: Decreasing real bodies
        is_decreasing_bodies = (abs(second_close - second_open) < abs(first_close - first_open)) and \
                               (abs(third_close - third_open) < abs(second_close - second_open))

        # Condition 3: Growing upper shadows (wicks)
        first_upper_shadow = first_candle[2] - max(first_open, first_close)
        second_upper_shadow = second_candle[2] - max(second_open, second_close)
        third_upper_shadow = third_candle[2] - max(third_open, third_close)
        is_growing_upper_shadows = second_upper_shadow > first_upper_shadow and third_upper_shadow > second_upper_shadow

    def _is_three_white_soldiers(self, chart_data):
        """
        Detects Three White Soldiers candlestick pattern.
        This pattern is characterized by three consecutive long bullish candles,
        each opening within or near the previous candle's real body and closing progressively higher.
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

        # Condition 1: Three consecutive bullish candles
        is_three_bullish_candles = (first_close > first_open) and (second_close > second_open) and (third_close > third_open)

        # Condition 2: Each candle opens within or near the previous candle's real body
        is_open_within_body = (second_open >= first_open and second_open <= first_close) and \
                               (third_open >= second_open and third_open <= second_close)

        # Condition 3: Candles close progressively higher
        is_closing_higher = second_close > first_close and third_close > second_close

        # Condition 4: Long bodies (configurable threshold - e.g., at least average body size of recent candles)
        avg_body_size = sum([abs(candle[4] - candle[1]) for candle in chart_data[-10:]]) / 10 # Average of last 10 candles
        is_long_bodies = (abs(first_close - first_open) > avg_body_size * 0.8) and \
                         (abs(second_close - second_open) > avg_body_size * 0.8) and \
                         (abs(third_close - third_open) > avg_body_size * 0.8)


        return is_three_bullish_candles and is_open_within_body and is_closing_higher and is_long_bodies

# Test comment insertion

        return is_decreasing_bodies and is_growing_upper_shadows