class SignalGenerator:
    """
    Basic class for the signal generator component.
    """
    def __init__(self, config):
        """
        Initializes the SignalGenerator.
        """
        self.config = config
        print("SignalGenerator initialized")

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
            if ema_20 > ema_50 and rsi_14 > 50:
                momentum_signal = "Strong Bullish"
                momentum_strength = 0.7  # Stronger signal weight
            elif ema_20 < ema_50 and rsi_14 < 50:
                momentum_signal = "Strong Bearish"
                momentum_strength = 0.7  # Stronger signal weight
            elif (ema_20 > ema_50 and rsi_14 < 50) or (ema_20 < ema_50 and rsi_14 > 50):
                momentum_signal = "Mixed"
                momentum_strength = 0.4  # Moderate signal weight
            else:
                momentum_signal = "Neutral"
                momentum_strength = 0.5  # Neutral signal weight
        signals['momentum'] = momentum_signal
        signal_weights['momentum'] = momentum_strength

        # 2. Volume Analysis
        current_volume = indicator_data['volume'].iloc[-1] if 'volume' in indicator_data.columns else None
        volume_signal = "Neutral"
        volume_strength = 0.3  # Lower weight for volume
        if current_volume is not None:
            volume_ma_7 = indicator_data['volume'].rolling(window=7).mean().iloc[-1] if 'volume' in indicator_data.columns else None
            volume_ma_30 = indicator_data['volume'].rolling(window=30).mean().iloc[-1] if 'volume' in indicator_data.columns else None
            if volume_ma_7 is not None and volume_ma_30 is not None:
                if current_volume < 0.9 * volume_ma_7:  # Below 90% of 7-bar MA
                    volume_signal = "Weak"
                    volume_strength = 0.2  # Weaker signal weight
                elif current_volume > 1.2 * volume_ma_7:  # Above 120% of 7-bar MA
                    volume_signal = "Strong"
                    volume_strength = 0.5  # Stronger signal weight
        signals['volume'] = volume_signal
        signal_weights['volume'] = volume_strength

        # 3. Candlestick Pattern
        candlestick_signal = "Neutral"
        candlestick_strength = 0.4  # Slightly lower weight
        last_candle_close = indicator_data['close'].iloc[-1] if 'close' in indicator_data.columns else None
        last_candle_open = indicator_data['open'].iloc[-1] if 'open' in indicator_data.columns else None
        if last_candle_close is not None and last_candle_open is not None:
            if last_candle_close < last_candle_open:  # Red candle (bearish)
                candlestick_signal = "Bearish"
                candlestick_strength = 0.4
            elif last_candle_close > last_candle_open:  # Green candle (bullish)
                candlestick_signal = "Bullish"
                candlestick_strength = 0.4
        signals['candlestick_pattern'] = candlestick_signal
        signal_weights['candlestick_pattern'] = candlestick_strength

        # 4. Bollinger Bands
        bb_lower = indicator_data['BB_Lower'].iloc[-1] if 'BB_Lower' in indicator_data.columns else None
        bb_upper = indicator_data['BB_Upper'].iloc[-1] if 'BB_Upper' in indicator_data.columns else None
        price = indicator_data['close'].iloc[-1] if 'close' in indicator_data.columns else None
        bollinger_signal = "Neutral"
        bollinger_strength = 0.5
        if bb_lower is not None and bb_upper is not None and price is not None:
            if price < bb_lower:
                bollinger_signal = "Buy"  # Buy signal if price is below lower band
                bollinger_strength = 0.6
            elif price > bb_upper:
                bollinger_signal = "Sell"  # Sell signal if price is above upper band
                bollinger_strength = 0.6
        signals['bollinger_bands'] = bollinger_signal
        signal_weights['bollinger_bands'] = bollinger_strength

        # 5. MACD Crossovers
        macd_signal_val = indicator_data['MACD_Signal'].iloc[-1] if 'MACD_Signal' in indicator_data.columns else None
        macd_val = indicator_data['MACD'].iloc[-1] if 'MACD' in indicator_data.columns else None
        prev_macd_signal_val = indicator_data['MACD_Signal'].iloc[-2] if 'MACD_Signal' in indicator_data.columns and len(indicator_data) > 1 else None
        prev_macd_val = indicator_data['MACD'].iloc[-2] if 'MACD' in indicator_data.columns and len(indicator_data) > 1 else None
        macd_signal = "Neutral"
        macd_strength = 0.5
        if macd_val is not None and macd_signal_val is not None and prev_macd_val is not None and prev_macd_signal_val is not None:
            if prev_macd_val < prev_macd_signal_val and macd_val > macd_signal_val:
                macd_signal = "Bullish Crossover"  # MACD bullish crossover
                macd_strength = 0.6
            elif prev_macd_val > prev_macd_signal_val and macd_val < macd_signal_val:
                macd_signal = "Bearish Crossover"  # MACD bearish crossover
                macd_strength = 0.6
        signals['macd_crossover'] = macd_signal
        signal_weights['macd_crossover'] = macd_strength

        # 6. Consolidated Signal and Confidence (Weighted Averaging)
        total_weighted_strength = sum(signal_weights.values())
        num_signals = len(signal_weights)
        average_weighted_strength = total_weighted_strength / num_signals if num_signals > 0 else 0.5

        confidence = int(average_weighted_strength * 100)
        if confidence >= 60:
            overall_signal = "BUY"
        elif confidence <= 40:
            overall_signal = "SELL"
        else:
            overall_signal = "HOLD"
        signals['overall_signal'] = overall_signal
        signals['confidence'] = f"{confidence}%"

        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        trading_pair = self.config.get('trading_pair', 'N/A')
        timeframe = self.config.get('timeframe', 'N/A')

        print(f"[{timestamp}] Generating signals for {trading_pair} - {timeframe}...")

        print(f"[{timestamp}] --- Indicator Analysis ---")
        print(f"[{timestamp}]   Momentum: EMA(20)={ema_20:.2f}, EMA(50)={ema_50:.2f}, RSI(14)={rsi_14:.2f} - {momentum_signal}")
        print(f"[{timestamp}]   Volume: Last Volume={current_volume:.2f}, 7-MA Volume={volume_ma_7:.2f}, 30-MA Volume={volume_ma_30:.2f} - {volume_signal}")
        print(f"[{timestamp}]   Candlestick: Last Candle - {candlestick_signal}")
        print(f"[{timestamp}]   Bollinger Bands: Close={price:.2f}, Lower Band={bb_lower:.2f}, Upper Band={bb_upper:.2f} - {bollinger_signal}")
        print(f"[{timestamp}]   MACD Crossover: MACD={macd_val:.4f}, Signal={macd_signal_val:.4f} - {macd_signal}")

        print(f"[{timestamp}] --- Generated Signals ---")
        print(f"[{timestamp}]   Overall Signal: {overall_signal}")
        print(f"[{timestamp}]   Confidence: {confidence}%")

        return signals