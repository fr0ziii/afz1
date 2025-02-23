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
        Generates trading signals based on indicator data and recognized patterns.
        """
        signals = {}
        rsi = indicator_data['RSI'][-1] if 'RSI' in indicator_data and not indicator_data['RSI'].empty else None
        doji_pattern = pattern_data.get('doji')

        if doji_pattern:
            signals['candlestick_pattern'] = 'HOLD' # Neutral signal for Doji
        elif rsi:
            if rsi < 30:
                signals['rsi_signal'] = 'BUY' # Buy signal for oversold RSI
            elif rsi > 70:
                signals['rsi_signal'] = 'SELL' # Sell signal for overbought RSI
            else:
                signals['rsi_signal'] = 'NEUTRAL' # Neutral signal for RSI
        else:
            signals['signal'] = 'NEUTRAL' # Default neutral signal

        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        trading_pair = self.config.get('trading_pair', 'N/A')
        timeframe = self.config.get('timeframe', 'N/A')

        print(f"[{timestamp}] Generating signals for {trading_pair} - {timeframe}...")
        print(f"[{timestamp}] --- Recognized Patterns ---")
        for pattern, detected in pattern_data.items():
            print(f"[{timestamp}]   {pattern}: {'Yes' if detected else 'No'}")
        print(f"[{timestamp}] --- Indicator Data ---")
        print(f"[{timestamp}]   RSI: {rsi}")
        print(f"[{timestamp}] --- Generated Signals ---")
        for signal_type, signal_value in signals.items():
            print(f"[{timestamp}]   {signal_type}: {signal_value}")
        return signals