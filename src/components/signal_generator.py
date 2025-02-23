import logging

logger = logging.getLogger(__name__)

class SignalGenerator:
    """
    Basic class for the signal generator component.
    """
    def __init__(self, config):
        """
        Initializes the SignalGenerator.
        """
        self.config = config
        logger.info("SignalGenerator initialized")

    def generate_signals(self, indicator_data, pattern_data):
        """
        Generates trading signals based on indicator data and patterns.
        """
        signals = {}
        signal_weights = {} # Weights for each signal type to calculate confidence

        # 1. Momentum Indicators (EMA and RSI)
        ema_20 = indicator_data[f'EMA_20'].iloc[-1] if f'EMA_20' in indicator_data.columns else None
        ema_50 = indicator_data[f'EMA_50'].iloc[-1] if f'EMA_50' in indicator_data.columns else None
        rsi_14 = indicator_data[f'RSI_14'].iloc[-1] if f'RSI_14' in indicator_data.columns else None

        momentum_signal = "Neutral"
        momentum_strength = 0.5 # Default neutral strength
        if ema_20 is not None and ema_50 is not None and rsi_14 is not None:
            ema_diff_percentage = ((ema_20 - ema_50) / ema_50) * 100
            if ema_20 > ema_50 and rsi_14 > 70: # RSI overbought, strong bullish
                momentum_signal = "Overbought Bullish"
                momentum_strength = 0.9  # Very strong signal weight
            elif ema_20 < ema_50 and rsi_14 < 30: # RSI oversold, strong bearish
                momentum_signal = "Oversold Bearish"
                momentum_strength = 0.9  # Very strong signal weight
            elif ema_20 > ema_50 and ema_diff_percentage > 0.5 and rsi_14 > 50: # EMA crossover and RSI bullish
                momentum_signal = "Bullish"
                momentum_strength = 0.8
            elif ema_20 < ema_50 and ema_diff_percentage < -0.5 and rsi_14 < 50: # EMA crossover and RSI bearish
                momentum_signal = "Bearish"
                momentum_strength = 0.8
            elif (ema_20 > ema_50 and rsi_14 < 50) or (ema_20 < ema_50 and rsi_14 > 50): # Mixed signals
                momentum_signal = "Mixed"
                momentum_strength = 0.4  # Moderate signal weight
            else:
                momentum_signal = "Neutral"
                momentum_strength = 0.5  # Neutral signal weight
        signals['momentum'] = momentum_signal
        signal_weights['momentum'] = momentum_strength
        logger.info(f"Momentum Signal: {momentum_signal} with strength {momentum_strength}")


        # 2. Volume Analysis
        current_volume = indicator_data['volume'].iloc[-1] if 'volume' in indicator_data.columns else None
        volume_signal = "Neutral"
        volume_strength = 0.3  # Lower weight for volume
        if current_volume is not None:
            volume_ma_7 = indicator_data['volume'].rolling(window=7).mean().iloc[-1] if 'volume' in indicator_data.columns else None
            volume_ma_30 = indicator_data['volume'].rolling(window=30).mean().iloc[-1] if 'volume' in indicator_data.columns else None
            if volume_ma_7 is not None and volume_ma_30 is not None:
                if current_volume > 1.5 * volume_ma_30: # Significant volume spike
                    volume_signal = "Spike"
                    volume_strength = 0.7 # High volume spike indicates strong interest
                elif current_volume < 0.7 * volume_ma_7: # Very low volume
                    volume_signal = "Very Weak"
                    volume_strength = 0.1 # Very weak volume, low interest
                elif current_volume < 0.9 * volume_ma_7:  # Below 90% of 7-bar MA
                    volume_signal = "Weak"
                    volume_strength = 0.3  # Weaker signal weight
                elif current_volume > 1.2 * volume_ma_7:  # Above 120% of 7-bar MA
                    volume_signal = "Strong"
                    volume_strength = 0.5  # Stronger signal weight
                else:
                    volume_signal = "Neutral"
                    volume_strength = 0.3 # Neutral signal weight
        signals['volume'] = volume_signal
        signal_weights['volume'] = volume_strength
        logger.info(f"Volume Signal: {volume_signal} with strength {volume_strength}")

        # 3. Candlestick Pattern (Basic - replaced by PatternRecognizer)
        candlestick_signal = "Neutral" # Placeholder - Candlestick signal now from PatternRecognizer
        candlestick_strength = 0.1  # Reduced weight as PatternRecognizer is used
        last_candle_close = indicator_data['close'].iloc[-1] if 'close' in indicator_data.columns else None
        last_candle_open = indicator_data['open'].iloc[-1] if 'open' in indicator_data.columns else None
        if last_candle_close is not None and last_candle_open is not None:
            if last_candle_close < last_candle_open:  # Red candle (bearish) - still include basic candle direction
                candlestick_signal = "Bearish Candle" # Basic bearish candle
            elif last_candle_close > last_candle_open:  # Green candle (bullish) - still include basic candle direction
                candlestick_signal = "Bullish Candle" # Basic bullish candle
        signals['candlestick_direction'] = candlestick_signal # Renamed to candlestick_direction
        signal_weights['candlestick_direction'] = candlestick_strength # Lower weight
        logger.info(f"Candlestick Direction Signal (Basic): {candlestick_signal} with strength {candlestick_strength}")

        # 4. Enhanced Candlestick Pattern Recognition from PatternRecognizer
        pattern_signal = "Neutral"
        pattern_strength = 0.6 # Default weight
        detected_patterns = pattern_data.get('patterns', []) # Get detected patterns from pattern_data
        if detected_patterns:
            pattern_names = [pattern['pattern_name'] for pattern in detected_patterns]
            if 'BullishEngulfing' in pattern_names:
                pattern_signal = "Bullish Engulfing"
            elif 'BearishEngulfing' in pattern_names:
                pattern_signal = "Bearish Engulfing"
            elif 'Doji' in pattern_names:
                pattern_signal = "Doji"
            elif 'MorningStar' in pattern_names:
                pattern_signal = "Morning Star"
            elif 'EveningStar' in pattern_names:
                pattern_signal = "Evening Star"
            # Add more patterns here as needed
            pattern_strength = 0.8 # Stronger signal if specific patterns are detected
            pattern_list_str = ', '.join(pattern_names)
        else:
            pattern_list_str = "No pattern detected"
        signals['chart_patterns'] = pattern_signal # Renamed to candlestick_pattern (enhanced)
        signal_weights['chart_patterns'] = pattern_strength # Higher weight
        logger.info(f"Candlestick Pattern Signal (Enhanced): {pattern_signal} with strength {pattern_strength}, Patterns: {pattern_list_str}")

        # 5. Bollinger Bands
        bb_lower = indicator_data['BB_Lower'].iloc[-1] if 'BB_Lower' in indicator_data.columns else None
        bb_upper = indicator_data['BB_Upper'].iloc[-1] if 'BB_Upper' in indicator_data.columns else None
        bb_mid = indicator_data['BB_Mid'].iloc[-1] if 'BB_Mid' in indicator_data.columns else None # Middle band (SMA)
        price = indicator_data['close'].iloc[-1] if 'close' in indicator_data.columns else None
        bollinger_signal = "Neutral"
        bollinger_strength = 0.5
        if bb_lower is not None and bb_upper is not None and price is not None and bb_mid is not None:
            if price < bb_lower:
                bollinger_signal = "Buy"  # Buy signal if price is below lower band
                bollinger_strength = 0.7
            elif price > bb_upper:
                bollinger_signal = "Sell"  # Sell signal if price is above upper band
                bollinger_strength = 0.7
            elif bb_lower < price < bb_mid: # Price between lower band and middle band
                bollinger_signal = "Weak Buy" # Weak buy signal - potential bounce
                bollinger_strength = 0.4
            elif bb_upper > price > bb_mid: # Price between upper band and middle band
                bollinger_signal = "Weak Sell" # Weak sell signal - potential pullback
                bollinger_strength = 0.4
            else:
                bollinger_signal = "Neutral"
                bollinger_strength = 0.5

        signals['bollinger_bands'] = bollinger_signal
        signal_weights['bollinger_bands'] = bollinger_strength
        logger.info(f"Bollinger Bands Signal: {bollinger_signal} with strength {bollinger_strength}")

        # 6. MACD Crossovers
        macd_signal_val = indicator_data['MACD_Signal'].iloc[-1] if 'MACD_Signal' in indicator_data.columns else None
        macd_val = indicator_data['MACD'].iloc[-1] if 'MACD' in indicator_data.columns else None
        prev_macd_signal_val = indicator_data['MACD_Signal'].iloc[-2] if 'MACD_Signal' in indicator_data.columns and len(indicator_data) > 1 else None
        prev_macd_val = indicator_data['MACD'].iloc[-2] if 'MACD' in indicator_data.columns and len(indicator_data) > 1 else None
        macd_signal = "Neutral"
        macd_strength = 0.5
        if macd_val is not None and macd_signal_val is not None and prev_macd_val is not None and prev_macd_signal_val is not None:
            if prev_macd_val < prev_macd_signal_val and macd_val > macd_signal_val:
                macd_signal = "Bullish Crossover"  # MACD bullish crossover
                macd_strength = 0.7
            elif prev_macd_val > prev_macd_signal_val and macd_val < macd_signal_val:
                macd_signal = "Bearish Crossover"  # MACD bearish crossover
                macd_strength = 0.7
        signals['macd_crossover'] = macd_signal
        signal_weights['macd_crossover'] = macd_strength
        logger.info(f"MACD Crossover Signal: {macd_signal} with strength {macd_strength}")

        # 7. Consolidated Signal and Confidence (Weighted Sum with Configurable Weights)
        # Define weights for each signal type (configurable in __init__)
        weights = {
            'momentum': self.config.get('momentum_weight', 0.4),
            'volume': self.config.get('volume_weight', 0.1),
            'candlestick_direction': self.config.get('candlestick_direction_weight', 0.05),
            'chart_patterns': self.config.get('chart_patterns_weight', 0.3),
            'bollinger_bands': self.config.get('bollinger_bands_weight', 0.1),
            'macd_crossover': self.config.get('macd_crossover_weight', 0.15),
        }

        weighted_sum_strength = sum(signal_weights[signal_type] * weights[signal_type] for signal_type in signal_weights)
        total_weight = sum(weights.values())
        average_weighted_strength = weighted_sum_strength / total_weight if total_weight > 0 else 0.5

        confidence = int(average_weighted_strength * 100)
        if confidence >= 70: # Increased threshold for BUY
            overall_signal = "BUY"
        elif confidence <= 30: # Decreased threshold for SELL
            overall_signal = "SELL"
        elif 40 <= confidence < 60: # Narrowed HOLD range, added SLIGHT_BUY/SLIGHT_SELL
            overall_signal = "HOLD"
        elif 60 <= confidence < 70:
            overall_signal = "SLIGHT_BUY"
        elif 30 < confidence < 40:
            overall_signal = "SLIGHT_SELL"
        else:
            overall_signal = "NEUTRAL" # Default to NEUTRAL if none of the conditions are met

        signals['overall_signal'] = overall_signal
        signals['confidence'] = f"{confidence}%"
        logger.info(f"Overall Signal: {overall_signal} with confidence {confidence}%")

        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        trading_pair = self.config.get('trading_pair', 'N/A')
        timeframe = self.config.get('timeframe', 'N/A')

        print(f"[{timestamp}] Generating signals for {trading_pair} - {timeframe}...")

        print(f"[{timestamp}] --- Indicator Analysis ---")
        print(f"[{timestamp}]   Momentum: EMA(20)={ema_20:.2f}, EMA(50)={ema_50:.2f}, RSI(14)={rsi_14:.2f} - {momentum_signal}")
        print(f"[{timestamp}]   Volume: Last Volume={current_volume:.2f}, 7-MA Volume={volume_ma_7:.2f}, 30-MA Volume={volume_ma_30:.2f} - {volume_signal}")
        print(f"[{timestamp}]   Candlestick: Last Candle - {candlestick_signal}")
        print(f"[{timestamp}]   Chart Patterns: {pattern_list_str} - {pattern_signal}") # Added chart patterns to output
        print(f"[{timestamp}]   Bollinger Bands: Close={price:.2f}, Lower Band={bb_lower:.2f}, Upper Band={bb_upper:.2f} - {bollinger_signal}")
        print(f"[{timestamp}]   MACD Crossover: MACD={macd_val:.4f}, Signal={macd_signal_val:.4f} - {macd_signal}")

        print(f"[{timestamp}] --- Generated Signals ---")
        print(f"[{timestamp}]   Overall Signal: {overall_signal}")
        print(f"[{timestamp}]   Confidence: {confidence}%")

        return signals