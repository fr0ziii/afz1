Directory structure:
└── ccxt-ccxt/
    ├── README.md
    ├── CHANGELOG.md
    ├── CODEOWNERS
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── ISSUE_TEMPLATE.md
    ├── LICENSE.txt
    ├── build-go.sh
    ├── build.sh
    ├── ccxt.php
    ├── ci-requirements.txt
    ├── cleanup.sh
    ├── coin-ws.js
    ├── composer-install.sh
    ├── composer.json
    ├── composer.lock
    ├── docker-compose.yml
    ├── examples2md.js
    ├── exchanges.cfg
    ├── gource.sh
    ├── index.html
    ├── jsdoc2md.js
    ├── keys.json
    ├── package.json
    ├── phpunit.xml.dist
    ├── postinstall.js
    ├── pyproject.toml
    ├── rollup.config.js
    ├── run-tests-simul.sh
    ├── run-tests.js
    ├── setup.cfg
    ├── skip-tests.json
    ├── tests-manager.sh
    ├── tsconfig.json
    ├── webpack.config.js
    ├── .dockerignore
    ├── .eslintignore
    ├── .npmignore
    ├── .travis.yml
    ├── cs/
    │   ├── ccxt.sln
    │   ├── deploy.sh
    │   ├── .editorconfig
    │   ├── .gitignore
    │   ├── ccxt/
    │   │   ├── ccxt.csproj
    │   │   ├── api/
    │   │   │   ├── ace.cs
    │   │   │   ├── alpaca.cs
    │   │   │   ├── ascendex.cs
    │   │   │   ├── bequant.cs
    │   │   │   ├── bigone.cs
    │   │   │   ├── binance.cs
    │   │   │   ├── binancecoinm.cs
    │   │   │   ├── binanceus.cs
    │   │   │   ├── binanceusdm.cs
    │   │   │   ├── bingx.cs
    │   │   │   ├── bit2c.cs
    │   │   │   ├── bitbank.cs
    │   │   │   ├── bitbns.cs
    │   │   │   ├── bitcoincom.cs
    │   │   │   ├── bitfinex.cs
    │   │   │   ├── bitfinex1.cs
    │   │   │   ├── bitflyer.cs
    │   │   │   ├── bitget.cs
    │   │   │   ├── bithumb.cs
    │   │   │   ├── bitmart.cs
    │   │   │   ├── bitmex.cs
    │   │   │   ├── bitopro.cs
    │   │   │   ├── bitpanda.cs
    │   │   │   ├── bitrue.cs
    │   │   │   ├── bitso.cs
    │   │   │   ├── bitstamp.cs
    │   │   │   ├── bitteam.cs
    │   │   │   ├── bitvavo.cs
    │   │   │   ├── bl3p.cs
    │   │   │   ├── blockchaincom.cs
    │   │   │   ├── blofin.cs
    │   │   │   ├── btcalpha.cs
    │   │   │   ├── btcbox.cs
    │   │   │   ├── btcmarkets.cs
    │   │   │   ├── btcturk.cs
    │   │   │   ├── bybit.cs
    │   │   │   ├── cex.cs
    │   │   │   ├── coinbase.cs
    │   │   │   ├── coinbaseadvanced.cs
    │   │   │   ├── coinbaseexchange.cs
    │   │   │   ├── coinbaseinternational.cs
    │   │   │   ├── coincatch.cs
    │   │   │   ├── coincheck.cs
    │   │   │   ├── coinex.cs
    │   │   │   ├── coinlist.cs
    │   │   │   ├── coinmate.cs
    │   │   │   ├── coinmetro.cs
    │   │   │   ├── coinone.cs
    │   │   │   ├── coinsph.cs
    │   │   │   ├── coinspot.cs
    │   │   │   ├── cryptocom.cs
    │   │   │   ├── currencycom.cs
    │   │   │   ├── defx.cs
    │   │   │   ├── delta.cs
    │   │   │   ├── deribit.cs
    │   │   │   ├── digifinex.cs
    │   │   │   ├── ellipx.cs
    │   │   │   ├── exmo.cs
    │   │   │   ├── fmfwio.cs
    │   │   │   ├── gate.cs
    │   │   │   ├── gateio.cs
    │   │   │   ├── gemini.cs
    │   │   │   ├── hashkey.cs
    │   │   │   ├── hitbtc.cs
    │   │   │   ├── hollaex.cs
    │   │   │   ├── htx.cs
    │   │   │   ├── huobi.cs
    │   │   │   ├── huobijp.cs
    │   │   │   ├── hyperliquid.cs
    │   │   │   ├── idex.cs
    │   │   │   ├── independentreserve.cs
    │   │   │   ├── indodax.cs
    │   │   │   ├── kraken.cs
    │   │   │   ├── krakenfutures.cs
    │   │   │   ├── kucoin.cs
    │   │   │   ├── kucoinfutures.cs
    │   │   │   ├── kuna.cs
    │   │   │   ├── latoken.cs
    │   │   │   ├── lbank.cs
    │   │   │   ├── luno.cs
    │   │   │   ├── mercado.cs
    │   │   │   ├── mexc.cs
    │   │   │   ├── myokx.cs
    │   │   │   ├── ndax.cs
    │   │   │   ├── novadax.cs
    │   │   │   ├── oceanex.cs
    │   │   │   ├── okcoin.cs
    │   │   │   ├── okx.cs
    │   │   │   ├── onetrading.cs
    │   │   │   ├── oxfun.cs
    │   │   │   ├── p2b.cs
    │   │   │   ├── paradex.cs
    │   │   │   ├── paymium.cs
    │   │   │   ├── phemex.cs
    │   │   │   ├── poloniex.cs
    │   │   │   ├── poloniexfutures.cs
    │   │   │   ├── probit.cs
    │   │   │   ├── timex.cs
    │   │   │   ├── tokocrypto.cs
    │   │   │   ├── tradeogre.cs
    │   │   │   ├── upbit.cs
    │   │   │   ├── vertex.cs
    │   │   │   ├── wavesexchange.cs
    │   │   │   ├── wazirx.cs
    │   │   │   ├── whitebit.cs
    │   │   │   ├── woo.cs
    │   │   │   ├── woofipro.cs
    │   │   │   ├── xt.cs
    │   │   │   ├── yobit.cs
    │   │   │   ├── zaif.cs
    │   │   │   └── zonda.cs
    │   │   ├── base/
    │   │   │   ├── Exchange.BaseMethods.cs
    │   │   │   ├── Exchange.Crypto.cs
    │   │   │   ├── Exchange.ETH.cs
    │   │   │   ├── Exchange.Encode.cs
    │   │   │   ├── Exchange.Errors.cs
    │   │   │   ├── Exchange.Functions.cs
    │   │   │   ├── Exchange.Generic.cs
    │   │   │   ├── Exchange.Instantiate.cs
    │   │   │   ├── Exchange.JSONHelper.cs
    │   │   │   ├── Exchange.MetaData.cs
    │   │   │   ├── Exchange.Misc.cs
    │   │   │   ├── Exchange.Number.cs
    │   │   │   ├── Exchange.Options.cs
    │   │   │   ├── Exchange.Precise.cs
    │   │   │   ├── Exchange.SafeMethods.cs
    │   │   │   ├── Exchange.String.cs
    │   │   │   ├── Exchange.Time.cs
    │   │   │   ├── Exchange.TranspileHelpers.cs
    │   │   │   ├── Exchange.Types.cs
    │   │   │   ├── Exchange.Wrappers.cs
    │   │   │   ├── Exchange.cs
    │   │   │   ├── Polyfills.cs
    │   │   │   └── Throttler.cs
    │   │   ├── exchanges/
    │   │   │   ├── ace.cs
    │   │   │   ├── alpaca.cs
    │   │   │   ├── ascendex.cs
    │   │   │   ├── bequant.cs
    │   │   │   ├── bigone.cs
    │   │   │   ├── binance.cs
    │   │   │   ├── binancecoinm.cs
    │   │   │   ├── binanceus.cs
    │   │   │   ├── binanceusdm.cs
    │   │   │   ├── bingx.cs
    │   │   │   ├── bit2c.cs
    │   │   │   ├── bitbank.cs
    │   │   │   ├── bitbns.cs
    │   │   │   ├── bitcoincom.cs
    │   │   │   ├── bitfinex.cs
    │   │   │   ├── bitfinex1.cs
    │   │   │   ├── bitflyer.cs
    │   │   │   ├── bitget.cs
    │   │   │   ├── bithumb.cs
    │   │   │   ├── bitmart.cs
    │   │   │   ├── bitmex.cs
    │   │   │   ├── bitopro.cs
    │   │   │   ├── bitpanda.cs
    │   │   │   ├── bitrue.cs
    │   │   │   ├── bitso.cs
    │   │   │   ├── bitstamp.cs
    │   │   │   ├── bitteam.cs
    │   │   │   ├── bitvavo.cs
    │   │   │   ├── bl3p.cs
    │   │   │   ├── blockchaincom.cs
    │   │   │   ├── blofin.cs
    │   │   │   ├── btcalpha.cs
    │   │   │   ├── btcbox.cs
    │   │   │   ├── btcmarkets.cs
    │   │   │   ├── btcturk.cs
    │   │   │   ├── bybit.cs
    │   │   │   ├── cex.cs
    │   │   │   ├── coinbase.cs
    │   │   │   ├── coinbaseadvanced.cs
    │   │   │   ├── coinbaseexchange.cs
    │   │   │   ├── coinbaseinternational.cs
    │   │   │   ├── coincatch.cs
    │   │   │   ├── coincheck.cs
    │   │   │   ├── coinex.cs
    │   │   │   ├── coinlist.cs
    │   │   │   ├── coinmate.cs
    │   │   │   ├── coinmetro.cs
    │   │   │   ├── coinone.cs
    │   │   │   ├── coinsph.cs
    │   │   │   ├── coinspot.cs
    │   │   │   ├── cryptocom.cs
    │   │   │   ├── currencycom.cs
    │   │   │   ├── defx.cs
    │   │   │   ├── delta.cs
    │   │   │   ├── deribit.cs
    │   │   │   ├── digifinex.cs
    │   │   │   ├── ellipx.cs
    │   │   │   ├── exmo.cs
    │   │   │   ├── fmfwio.cs
    │   │   │   ├── gate.cs
    │   │   │   ├── gateio.cs
    │   │   │   ├── gemini.cs
    │   │   │   ├── hashkey.cs
    │   │   │   ├── hitbtc.cs
    │   │   │   ├── hollaex.cs
    │   │   │   ├── htx.cs
    │   │   │   ├── huobi.cs
    │   │   │   ├── huobijp.cs
    │   │   │   ├── hyperliquid.cs
    │   │   │   ├── idex.cs
    │   │   │   ├── independentreserve.cs
    │   │   │   ├── indodax.cs
    │   │   │   ├── kraken.cs
    │   │   │   ├── krakenfutures.cs
    │   │   │   ├── kucoin.cs
    │   │   │   ├── kucoinfutures.cs
    │   │   │   ├── kuna.cs
    │   │   │   ├── latoken.cs
    │   │   │   ├── lbank.cs
    │   │   │   ├── luno.cs
    │   │   │   ├── mercado.cs
    │   │   │   ├── mexc.cs
    │   │   │   ├── myokx.cs
    │   │   │   ├── ndax.cs
    │   │   │   ├── novadax.cs
    │   │   │   ├── oceanex.cs
    │   │   │   ├── okcoin.cs
    │   │   │   ├── okx.cs
    │   │   │   ├── onetrading.cs
    │   │   │   ├── oxfun.cs
    │   │   │   ├── p2b.cs
    │   │   │   ├── paradex.cs
    │   │   │   ├── paymium.cs
    │   │   │   ├── phemex.cs
    │   │   │   ├── poloniex.cs
    │   │   │   ├── poloniexfutures.cs
    │   │   │   ├── probit.cs
    │   │   │   ├── timex.cs
    │   │   │   ├── tokocrypto.cs
    │   │   │   ├── tradeogre.cs
    │   │   │   ├── upbit.cs
    │   │   │   ├── vertex.cs
    │   │   │   ├── wavesexchange.cs
    │   │   │   ├── wazirx.cs
    │   │   │   ├── whitebit.cs
    │   │   │   ├── woo.cs
    │   │   │   ├── woofipro.cs
    │   │   │   ├── xt.cs
    │   │   │   ├── yobit.cs
    │   │   │   ├── zaif.cs
    │   │   │   ├── zonda.cs
    │   │   │   └── pro/
    │   │   │       ├── alpaca.cs
    │   │   │       ├── ascendex.cs
    │   │   │       ├── bequant.cs
    │   │   │       ├── binance.cs
    │   │   │       ├── binancecoinm.cs
    │   │   │       ├── binanceus.cs
    │   │   │       ├── binanceusdm.cs
    │   │   │       ├── bingx.cs
    │   │   │       ├── bitcoincom.cs
    │   │   │       ├── bitfinex.cs
    │   │   │       ├── bitfinex1.cs
    │   │   │       ├── bitget.cs
    │   │   │       ├── bithumb.cs
    │   │   │       ├── bitmart.cs
    │   │   │       ├── bitmex.cs
    │   │   │       ├── bitopro.cs
    │   │   │       ├── bitpanda.cs
    │   │   │       ├── bitrue.cs
    │   │   │       ├── bitstamp.cs
    │   │   │       ├── bitvavo.cs
    │   │   │       ├── blockchaincom.cs
    │   │   │       ├── blofin.cs
    │   │   │       ├── bybit.cs
    │   │   │       ├── cex.cs
    │   │   │       ├── coinbase.cs
    │   │   │       ├── coinbaseadvanced.cs
    │   │   │       ├── coinbaseexchange.cs
    │   │   │       ├── coinbaseinternational.cs
    │   │   │       ├── coincatch.cs
    │   │   │       ├── coincheck.cs
    │   │   │       ├── coinex.cs
    │   │   │       ├── coinone.cs
    │   │   │       ├── cryptocom.cs
    │   │   │       ├── currencycom.cs
    │   │   │       ├── defx.cs
    │   │   │       ├── deribit.cs
    │   │   │       ├── exmo.cs
    │   │   │       ├── gate.cs
    │   │   │       ├── gateio.cs
    │   │   │       ├── gemini.cs
    │   │   │       ├── hashkey.cs
    │   │   │       ├── hitbtc.cs
    │   │   │       ├── hollaex.cs
    │   │   │       ├── htx.cs
    │   │   │       ├── huobi.cs
    │   │   │       ├── huobijp.cs
    │   │   │       ├── hyperliquid.cs
    │   │   │       ├── idex.cs
    │   │   │       ├── independentreserve.cs
    │   │   │       ├── kraken.cs
    │   │   │       ├── krakenfutures.cs
    │   │   │       ├── kucoin.cs
    │   │   │       ├── kucoinfutures.cs
    │   │   │       ├── lbank.cs
    │   │   │       ├── luno.cs
    │   │   │       ├── mexc.cs
    │   │   │       ├── myokx.cs
    │   │   │       ├── ndax.cs
    │   │   │       ├── okcoin.cs
    │   │   │       ├── okx.cs
    │   │   │       ├── onetrading.cs
    │   │   │       ├── oxfun.cs
    │   │   │       ├── p2b.cs
    │   │   │       ├── paradex.cs
    │   │   │       ├── phemex.cs
    │   │   │       ├── poloniex.cs
    │   │   │       ├── poloniexfutures.cs
    │   │   │       ├── probit.cs
    │   │   │       ├── upbit.cs
    │   │   │       ├── vertex.cs
    │   │   │       ├── wazirx.cs
    │   │   │       ├── whitebit.cs
    │   │   │       ├── woo.cs
    │   │   │       ├── woofipro.cs
    │   │   │       ├── xt.cs
    │   │   │       └── wrappers/
    │   │   │           ├── alpaca.cs
    │   │   │           ├── ascendex.cs
    │   │   │           ├── bequant.cs
    │   │   │           ├── binance.cs
    │   │   │           ├── binancecoinm.cs
    │   │   │           ├── binanceus.cs
    │   │   │           ├── binanceusdm.cs
    │   │   │           ├── bingx.cs
    │   │   │           ├── bitcoincom.cs
    │   │   │           ├── bitfinex.cs
    │   │   │           ├── bitfinex1.cs
    │   │   │           ├── bitget.cs
    │   │   │           ├── bithumb.cs
    │   │   │           ├── bitmart.cs
    │   │   │           ├── bitmex.cs
    │   │   │           ├── bitopro.cs
    │   │   │           ├── bitpanda.cs
    │   │   │           ├── bitrue.cs
    │   │   │           ├── bitstamp.cs
    │   │   │           ├── bitvavo.cs
    │   │   │           ├── blockchaincom.cs
    │   │   │           ├── blofin.cs
    │   │   │           ├── bybit.cs
    │   │   │           ├── cex.cs
    │   │   │           ├── coinbase.cs
    │   │   │           ├── coinbaseadvanced.cs
    │   │   │           ├── coinbaseexchange.cs
    │   │   │           ├── coinbaseinternational.cs
    │   │   │           ├── coincatch.cs
    │   │   │           ├── coincheck.cs
    │   │   │           ├── coinex.cs
    │   │   │           ├── coinone.cs
    │   │   │           ├── cryptocom.cs
    │   │   │           ├── currencycom.cs
    │   │   │           ├── defx.cs
    │   │   │           ├── deribit.cs
    │   │   │           ├── exmo.cs
    │   │   │           ├── gate.cs
    │   │   │           ├── gateio.cs
    │   │   │           ├── gemini.cs
    │   │   │           ├── hashkey.cs
    │   │   │           ├── hitbtc.cs
    │   │   │           ├── hollaex.cs
    │   │   │           ├── htx.cs
    │   │   │           ├── huobi.cs
    │   │   │           ├── huobijp.cs
    │   │   │           ├── hyperliquid.cs
    │   │   │           ├── idex.cs
    │   │   │           ├── independentreserve.cs
    │   │   │           ├── kraken.cs
    │   │   │           ├── krakenfutures.cs
    │   │   │           ├── kucoin.cs
    │   │   │           ├── kucoinfutures.cs
    │   │   │           ├── lbank.cs
    │   │   │           ├── luno.cs
    │   │   │           ├── mexc.cs
    │   │   │           ├── myokx.cs
    │   │   │           ├── ndax.cs
    │   │   │           ├── okcoin.cs
    │   │   │           ├── okx.cs
    │   │   │           ├── onetrading.cs
    │   │   │           ├── oxfun.cs
    │   │   │           ├── p2b.cs
    │   │   │           ├── paradex.cs
    │   │   │           ├── phemex.cs
    │   │   │           ├── poloniex.cs
    │   │   │           ├── poloniexfutures.cs
    │   │   │           ├── probit.cs
    │   │   │           ├── upbit.cs
    │   │   │           ├── vertex.cs
    │   │   │           ├── wazirx.cs
    │   │   │           ├── whitebit.cs
    │   │   │           ├── woo.cs
    │   │   │           ├── woofipro.cs
    │   │   │           └── xt.cs
    │   │   ├── img/
    │   │   ├── static/
    │   │   │   ├── Cryptography.ECDSA/
    │   │   │   │   ├── Base58.cs
    │   │   │   │   ├── Callback.cs
    │   │   │   │   ├── Cryptography.ECDSA.csproj
    │   │   │   │   ├── Hex.cs
    │   │   │   │   ├── Ripemd160Manager.cs
    │   │   │   │   ├── Secp256k1Manager.cs
    │   │   │   │   ├── Sha256Manager.cs
    │   │   │   │   └── Internal/
    │   │   │   │       ├── Secp256K1/
    │   │   │   │       │   ├── Const.cs
    │   │   │   │       │   ├── Context.cs
    │   │   │   │       │   ├── ContextStruct.cs
    │   │   │   │       │   ├── ECKey.cs
    │   │   │   │       │   ├── ECMult.cs
    │   │   │   │       │   ├── ECMultGen.cs
    │   │   │   │       │   ├── EcMultGenContext.cs
    │   │   │   │       │   ├── EcdsaRecoverableSignature.cs
    │   │   │   │       │   ├── EcmultContext.cs
    │   │   │   │       │   ├── Fe.cs
    │   │   │   │       │   ├── FeStorage.cs
    │   │   │   │       │   ├── Field.cs
    │   │   │   │       │   ├── Field_10x26.cs
    │   │   │   │       │   ├── Ge.cs
    │   │   │   │       │   ├── GeJ.cs
    │   │   │   │       │   ├── GeStorage.cs
    │   │   │   │       │   ├── Group.cs
    │   │   │   │       │   ├── NonceFunction.cs
    │   │   │   │       │   ├── Options.cs
    │   │   │   │       │   ├── PubKey.cs
    │   │   │   │       │   ├── Scalar.cs
    │   │   │   │       │   ├── Secp256K1T.cs
    │   │   │   │       │   └── Util.cs
    │   │   │   │       └── Sha256/
    │   │   │   │           ├── Hash.cs
    │   │   │   │           ├── HmacSha256T.cs
    │   │   │   │           ├── Rfc6979HmacSha256T.cs
    │   │   │   │           └── Sha256T.cs
    │   │   │   ├── MiniMessagePack/
    │   │   │   │   ├── README.md
    │   │   │   │   ├── MiniMessagePack.sln
    │   │   │   │   └── MiniMessagePack/
    │   │   │   │       ├── MiniMessagePack.csproj
    │   │   │   │       ├── MiniMessagePacker.cs
    │   │   │   │       └── Properties/
    │   │   │   │           └── AssemblyInfo.cs
    │   │   │   ├── Nethereum/
    │   │   │   │   ├── Nethereum.ABI/
    │   │   │   │   │   ├── ABIEncode.cs
    │   │   │   │   │   ├── ABIType.cs
    │   │   │   │   │   ├── ABIValue.cs
    │   │   │   │   │   ├── AddressType.cs
    │   │   │   │   │   ├── ArrayType.cs
    │   │   │   │   │   ├── BoolType.cs
    │   │   │   │   │   ├── ByteCodeConstants.cs
    │   │   │   │   │   ├── Bytes32Type.cs
    │   │   │   │   │   ├── BytesElementaryType.cs
    │   │   │   │   │   ├── BytesType.cs
    │   │   │   │   │   ├── DynamicArrayType.cs
    │   │   │   │   │   ├── EncoderDecoderHelpers.cs
    │   │   │   │   │   ├── IntType.cs
    │   │   │   │   │   ├── Nethereum.ABI.csprojRm
    │   │   │   │   │   ├── StaticArrayType.cs
    │   │   │   │   │   ├── StringType.cs
    │   │   │   │   │   ├── TupleType.cs
    │   │   │   │   │   ├── ABIDeserialisation/
    │   │   │   │   │   │   ├── ABIDeserialiserFactory.cs
    │   │   │   │   │   │   ├── ABIJsonDeserialiser.cs
    │   │   │   │   │   │   ├── ABIStringSignatureDeserialiser.cs
    │   │   │   │   │   │   └── ExpandoConvertor.cs
    │   │   │   │   │   ├── ABIRepository/
    │   │   │   │   │   │   ├── ABIInfo.cs
    │   │   │   │   │   │   ├── ABIInfoInMemoryStorage.cs
    │   │   │   │   │   │   └── IABIInfoStorage.cs
    │   │   │   │   │   ├── ByteArrayConvertors/
    │   │   │   │   │   │   ├── AbiStructEncoderByteConvertor.cs
    │   │   │   │   │   │   ├── AbiStructEncoderPackedByteConvertor.cs
    │   │   │   │   │   │   └── AbiStructSha3KeccackHashByteArrayConvertor.cs
    │   │   │   │   │   ├── CompilationMetadata/
    │   │   │   │   │   │   └── CompilationMetadata.cs
    │   │   │   │   │   ├── Decoders/
    │   │   │   │   │   │   ├── AddressTypeDecoder.cs
    │   │   │   │   │   │   ├── ArrayTypeDecoder.cs
    │   │   │   │   │   │   ├── BoolTypeDecoder.cs
    │   │   │   │   │   │   ├── ByteUtilExtensions.cs
    │   │   │   │   │   │   ├── Bytes32TypeDecoder.cs
    │   │   │   │   │   │   ├── BytesElementaryTypeDecoder .cs
    │   │   │   │   │   │   ├── BytesTypeDecoder.cs
    │   │   │   │   │   │   ├── DynamicArrayTypeDecoder.cs
    │   │   │   │   │   │   ├── IRawDecoder.cs
    │   │   │   │   │   │   ├── ITypeDecoder.cs
    │   │   │   │   │   │   ├── IntTypeDecoder.cs
    │   │   │   │   │   │   ├── StringBytes32Decoder.cs
    │   │   │   │   │   │   ├── StringTypeDecoder.cs
    │   │   │   │   │   │   ├── TupleTypeDecoder.cs
    │   │   │   │   │   │   └── TypeDecoder.cs
    │   │   │   │   │   ├── EIP712/
    │   │   │   │   │   │   ├── Domain.cs
    │   │   │   │   │   │   ├── Eip712TypedDataEncoder.cs
    │   │   │   │   │   │   ├── MemberDescription.cs
    │   │   │   │   │   │   ├── MemberDescriptionFactory.cs
    │   │   │   │   │   │   ├── MemberValue.cs
    │   │   │   │   │   │   ├── MemberValueFactory.cs
    │   │   │   │   │   │   ├── TypedData.cs
    │   │   │   │   │   │   ├── TypedDataRaw.cs
    │   │   │   │   │   │   ├── TypedDataRawJsonConversion.cs
    │   │   │   │   │   │   └── EIP2612/
    │   │   │   │   │   │       ├── EIP2612TypeFactory.cs
    │   │   │   │   │   │       └── Permit.cs
    │   │   │   │   │   ├── Encoders/
    │   │   │   │   │   │   ├── AddressTypeEncoder.cs
    │   │   │   │   │   │   ├── ArrayTypeEncoder.cs
    │   │   │   │   │   │   ├── BoolTypeEncoder.cs
    │   │   │   │   │   │   ├── Bytes32TypeEncoder.cs
    │   │   │   │   │   │   ├── BytesElementaryTypeEncoder.cs
    │   │   │   │   │   │   ├── BytesTypeEncoder.cs
    │   │   │   │   │   │   ├── DynamicArrayTypeEncoder.cs
    │   │   │   │   │   │   ├── ITypeEncoder.cs
    │   │   │   │   │   │   ├── IntTypeEncoder.cs
    │   │   │   │   │   │   ├── StaticArrayTypeEncoder.cs
    │   │   │   │   │   │   ├── StringTypeEncoder.cs
    │   │   │   │   │   │   └── TupleTypeEncoder.cs
    │   │   │   │   │   ├── FunctionEncoding/
    │   │   │   │   │   │   ├── AbiEncodingException.cs
    │   │   │   │   │   │   ├── ByteCodeLibrary.cs
    │   │   │   │   │   │   ├── ByteCodeLibraryLinker.cs
    │   │   │   │   │   │   ├── ByteCodeSwarmExtractor.cs
    │   │   │   │   │   │   ├── ConstructorCallDecoder.cs
    │   │   │   │   │   │   ├── ConstructorCallEncoder.cs
    │   │   │   │   │   │   ├── DecodedValue.cs
    │   │   │   │   │   │   ├── ErrorFunction.cs
    │   │   │   │   │   │   ├── EventTopicDecoder.cs
    │   │   │   │   │   │   ├── FunctionCallDecoder.cs
    │   │   │   │   │   │   ├── FunctionCallEncoder.cs
    │   │   │   │   │   │   ├── JsonParameterObjectConvertor.cs
    │   │   │   │   │   │   ├── ParameterDecoder.cs
    │   │   │   │   │   │   ├── ParameterExtensions.cs
    │   │   │   │   │   │   ├── ParameterOutput.cs
    │   │   │   │   │   │   ├── ParameterOutputExtensions.cs
    │   │   │   │   │   │   ├── ParametersEncoder.cs
    │   │   │   │   │   │   ├── PropertyInfoExtensions.cs
    │   │   │   │   │   │   ├── SerpentSignatureEncoder.cs
    │   │   │   │   │   │   ├── SignatureEncoder.cs
    │   │   │   │   │   │   ├── SmartContractRevertException.cs
    │   │   │   │   │   │   ├── AttributeEncoding/
    │   │   │   │   │   │   │   ├── ParameterAttributeValue.cs
    │   │   │   │   │   │   │   └── ParameterOutputProperty.cs
    │   │   │   │   │   │   └── Attributes/
    │   │   │   │   │   │       ├── AttributesToABIExtractor.cs
    │   │   │   │   │   │       ├── ErrorAttribute.cs
    │   │   │   │   │   │       ├── EventAttribute.cs
    │   │   │   │   │   │       ├── FunctionAttribute.cs
    │   │   │   │   │   │       ├── FunctionOutputAttribute.cs
    │   │   │   │   │   │       ├── IErrorDTO.cs
    │   │   │   │   │   │       ├── IEventDTO.cs
    │   │   │   │   │   │       ├── IFunctionOutputDTO.cs
    │   │   │   │   │   │       ├── ParameterAttribute.cs
    │   │   │   │   │   │       ├── ParameterAttributeIndexedTopics.cs
    │   │   │   │   │   │       ├── ParameterIndexedTopicExtractor.cs
    │   │   │   │   │   │       ├── PropertiesExtractor.cs
    │   │   │   │   │   │       └── StructAttribute.cs
    │   │   │   │   │   ├── Model/
    │   │   │   │   │   │   ├── ConstructorABI.cs
    │   │   │   │   │   │   ├── ContractABI.cs
    │   │   │   │   │   │   ├── ErrorABI.cs
    │   │   │   │   │   │   ├── EventABI.cs
    │   │   │   │   │   │   ├── FunctionABI.cs
    │   │   │   │   │   │   ├── IGetErrorAbi.cs
    │   │   │   │   │   │   ├── IGetEventAbi.cs
    │   │   │   │   │   │   ├── IGetFunctionAbi.cs
    │   │   │   │   │   │   ├── IGetParametersAbi.cs
    │   │   │   │   │   │   ├── ModelExtensions.cs
    │   │   │   │   │   │   └── Parameter.cs
    │   │   │   │   │   ├── Properties/
    │   │   │   │   │   │   └── AssemblyInfo.cs
    │   │   │   │   │   ├── Util/
    │   │   │   │   │   │   ├── ByteUtil.cs
    │   │   │   │   │   │   └── NumberUtilExtensions.cs
    │   │   │   │   │   └── net35/
    │   │   │   │   │       └── IntrospectionExtensions.cs
    │   │   │   │   ├── Nethereum.Hex/
    │   │   │   │   │   ├── Nethereum.Hex.csprojMe
    │   │   │   │   │   ├── NethereumKey.snk
    │   │   │   │   │   ├── HexConvertors/
    │   │   │   │   │   │   ├── HexBigIntegerBigEndianConvertor.cs
    │   │   │   │   │   │   ├── HexUTF8StringConvertor.cs
    │   │   │   │   │   │   ├── IHexConvertor.cs
    │   │   │   │   │   │   └── Extensions/
    │   │   │   │   │   │       ├── HexBigIntegerConvertorExtensions.cs
    │   │   │   │   │   │       ├── HexByteConvertorExtensions.cs
    │   │   │   │   │   │       └── HexStringUTF8ConvertorExtensions.cs
    │   │   │   │   │   ├── HexTypes/
    │   │   │   │   │   │   ├── HexBigInteger.cs
    │   │   │   │   │   │   ├── HexBigIntegerNumberExtensions.cs
    │   │   │   │   │   │   ├── HexType.cs
    │   │   │   │   │   │   ├── HexTypeFactory.cs
    │   │   │   │   │   │   ├── HexTypeJsonConverter.cs
    │   │   │   │   │   │   └── HexUTF8String.cs
    │   │   │   │   │   └── Properties/
    │   │   │   │   │       └── AssemblyInfo.cs
    │   │   │   │   ├── Nethereum.Signer.EIP712/
    │   │   │   │   │   ├── Eip712TypedDataSigner.cs
    │   │   │   │   │   └── Nethereum.Signer.EIP712.csproj
    │   │   │   │   └── Nethereum.Util/
    │   │   │   │       ├── AddressExtensions.cs
    │   │   │   │       ├── AddressUtil.cs
    │   │   │   │       ├── BigDecimal.Formatter.cs
    │   │   │   │       ├── BigDecimal.cs
    │   │   │   │       ├── BigIntegerExtensions.cs
    │   │   │   │       ├── ByteUtil.cs
    │   │   │   │       ├── ContractUtils.cs
    │   │   │   │       ├── EnumerableExtensions.cs
    │   │   │   │       ├── FormattingExtensions.cs
    │   │   │   │       ├── IWaitStrategy.cs
    │   │   │   │       ├── Nethereum.Util.csprojRem
    │   │   │   │       ├── NumberFormatting.cs
    │   │   │   │       ├── PredicateBuilder.cs
    │   │   │   │       ├── Sha3Keccack.cs
    │   │   │   │       ├── TaskExtensions.cs
    │   │   │   │       ├── TransactionUtils.cs
    │   │   │   │       ├── UnitConversion.cs
    │   │   │   │       ├── WaitStrategy.cs
    │   │   │   │       ├── ByteArrayConvertors/
    │   │   │   │       │   ├── ChartByteArrayConvertor.cs
    │   │   │   │       │   ├── HexToByteArrayConvertor.cs
    │   │   │   │       │   ├── IByteArrayConvertor.cs
    │   │   │   │       │   └── StringByteArrayConvertor.cs
    │   │   │   │       ├── HashProviders/
    │   │   │   │       │   ├── IHashProvider.cs
    │   │   │   │       │   └── Sha3KeccackHashProvider.cs
    │   │   │   │       ├── Keccak/
    │   │   │   │       │   └── KeccakDigest.cs
    │   │   │   │       └── Properties/
    │   │   │   │           └── AssemblyInfo.cs
    │   │   │   ├── Portable.BouncyCastle/
    │   │   │   │   ├── AssemblyInfo.cs
    │   │   │   │   ├── BouncyCastle.Crypto.csproj
    │   │   │   │   ├── asn1/
    │   │   │   │   │   ├── ASN1Generator.cs
    │   │   │   │   │   ├── ASN1OctetStringParser.cs
    │   │   │   │   │   ├── ASN1SequenceParser.cs
    │   │   │   │   │   ├── ASN1SetParser.cs
    │   │   │   │   │   ├── ASN1StreamParser.cs
    │   │   │   │   │   ├── ASN1TaggedObjectParser.cs
    │   │   │   │   │   ├── Asn1BitStringParser.cs
    │   │   │   │   │   ├── Asn1Encodable.cs
    │   │   │   │   │   ├── Asn1EncodableVector.cs
    │   │   │   │   │   ├── Asn1Exception.cs
    │   │   │   │   │   ├── Asn1InputStream.cs
    │   │   │   │   │   ├── Asn1Null.cs
    │   │   │   │   │   ├── Asn1Object.cs
    │   │   │   │   │   ├── Asn1ObjectDescriptor.cs
    │   │   │   │   │   ├── Asn1OctetString.cs
    │   │   │   │   │   ├── Asn1OutputStream.cs
    │   │   │   │   │   ├── Asn1ParsingException.cs
    │   │   │   │   │   ├── Asn1RelativeOid.cs
    │   │   │   │   │   ├── Asn1Sequence.cs
    │   │   │   │   │   ├── Asn1Set.cs
    │   │   │   │   │   ├── Asn1Tag.cs
    │   │   │   │   │   ├── Asn1TaggedObject.cs
    │   │   │   │   │   ├── Asn1Tags.cs
    │   │   │   │   │   ├── Asn1Type.cs
    │   │   │   │   │   ├── Asn1UniversalType.cs
    │   │   │   │   │   ├── Asn1UniversalTypes.cs
    │   │   │   │   │   ├── Asn1Utilities.cs
    │   │   │   │   │   ├── BERBitString.cs
    │   │   │   │   │   ├── BERGenerator.cs
    │   │   │   │   │   ├── BEROctetStringGenerator.cs
    │   │   │   │   │   ├── BEROctetStringParser.cs
    │   │   │   │   │   ├── BERSequenceGenerator.cs
    │   │   │   │   │   ├── BERSequenceParser.cs
    │   │   │   │   │   ├── BERSetGenerator.cs
    │   │   │   │   │   ├── BERSetParser.cs
    │   │   │   │   │   ├── BERTaggedObjectParser.cs
    │   │   │   │   │   ├── BerBitStringParser.cs
    │   │   │   │   │   ├── BerOctetString.cs
    │   │   │   │   │   ├── BerSequence.cs
    │   │   │   │   │   ├── BerSet.cs
    │   │   │   │   │   ├── BerTaggedObject.cs
    │   │   │   │   │   ├── ConstructedBitStream.cs
    │   │   │   │   │   ├── ConstructedDLEncoding.cs
    │   │   │   │   │   ├── ConstructedILEncoding.cs
    │   │   │   │   │   ├── ConstructedLazyDLEncoding.cs
    │   │   │   │   │   ├── ConstructedOctetStream.cs
    │   │   │   │   │   ├── DERExternal.cs
    │   │   │   │   │   ├── DERExternalParser.cs
    │   │   │   │   │   ├── DERGenerator.cs
    │   │   │   │   │   ├── DEROctetStringParser.cs
    │   │   │   │   │   ├── DERSequenceGenerator.cs
    │   │   │   │   │   ├── DERSequenceParser.cs
    │   │   │   │   │   ├── DERSetGenerator.cs
    │   │   │   │   │   ├── DERSetParser.cs
    │   │   │   │   │   ├── DLBitString.cs
    │   │   │   │   │   ├── DLBitStringParser.cs
    │   │   │   │   │   ├── DLSequence.cs
    │   │   │   │   │   ├── DLSet.cs
    │   │   │   │   │   ├── DLTaggedObject.cs
    │   │   │   │   │   ├── DLTaggedObjectParser.cs
    │   │   │   │   │   ├── DefiniteLengthInputStream.cs
    │   │   │   │   │   ├── DerBMPString.cs
    │   │   │   │   │   ├── DerBitString.cs
    │   │   │   │   │   ├── DerBoolean.cs
    │   │   │   │   │   ├── DerEnumerated.cs
    │   │   │   │   │   ├── DerGeneralString.cs
    │   │   │   │   │   ├── DerGeneralizedTime.cs
    │   │   │   │   │   ├── DerGraphicString.cs
    │   │   │   │   │   ├── DerIA5String.cs
    │   │   │   │   │   ├── DerInteger.cs
    │   │   │   │   │   ├── DerNull.cs
    │   │   │   │   │   ├── DerNumericString.cs
    │   │   │   │   │   ├── DerObjectIdentifier.cs
    │   │   │   │   │   ├── DerOctetString.cs
    │   │   │   │   │   ├── DerOutputStream.cs
    │   │   │   │   │   ├── DerPrintableString.cs
    │   │   │   │   │   ├── DerSequence.cs
    │   │   │   │   │   ├── DerSet.cs
    │   │   │   │   │   ├── DerStringBase.cs
    │   │   │   │   │   ├── DerT61String.cs
    │   │   │   │   │   ├── DerTaggedObject.cs
    │   │   │   │   │   ├── DerUTCTime.cs
    │   │   │   │   │   ├── DerUTF8String.cs
    │   │   │   │   │   ├── DerUniversalString.cs
    │   │   │   │   │   ├── DerVideotexString.cs
    │   │   │   │   │   ├── DerVisibleString.cs
    │   │   │   │   │   ├── IAsn1Choice.cs
    │   │   │   │   │   ├── IAsn1Convertible.cs
    │   │   │   │   │   ├── IAsn1Encoding.cs
    │   │   │   │   │   ├── IAsn1String.cs
    │   │   │   │   │   ├── IndefiniteLengthInputStream.cs
    │   │   │   │   │   ├── LazyASN1InputStream.cs
    │   │   │   │   │   ├── LazyDLEnumerator.cs
    │   │   │   │   │   ├── LazyDLSequence.cs
    │   │   │   │   │   ├── LazyDLSet.cs
    │   │   │   │   │   ├── LimitedInputStream.cs
    │   │   │   │   │   ├── OidTokenizer.cs
    │   │   │   │   │   ├── PrimitiveEncoding.cs
    │   │   │   │   │   ├── PrimitiveEncodingSuffixed.cs
    │   │   │   │   │   ├── anssi/
    │   │   │   │   │   │   ├── ANSSINamedCurves.cs
    │   │   │   │   │   │   └── ANSSIObjectIdentifiers.cs
    │   │   │   │   │   ├── bsi/
    │   │   │   │   │   │   └── BsiObjectIdentifiers.cs
    │   │   │   │   │   ├── cryptopro/
    │   │   │   │   │   │   └── CryptoProObjectIdentifiers.cs
    │   │   │   │   │   ├── eac/
    │   │   │   │   │   │   └── EACObjectIdentifiers.cs
    │   │   │   │   │   ├── edec/
    │   │   │   │   │   │   └── EdECObjectIdentifiers.cs
    │   │   │   │   │   ├── nist/
    │   │   │   │   │   │   ├── KMACwithSHAKE128_params.cs
    │   │   │   │   │   │   ├── KMACwithSHAKE256_params.cs
    │   │   │   │   │   │   ├── NISTNamedCurves.cs
    │   │   │   │   │   │   └── NISTObjectIdentifiers.cs
    │   │   │   │   │   ├── pkcs/
    │   │   │   │   │   │   ├── Attribute.cs
    │   │   │   │   │   │   ├── AuthenticatedSafe.cs
    │   │   │   │   │   │   ├── CertBag.cs
    │   │   │   │   │   │   ├── ContentInfo.cs
    │   │   │   │   │   │   ├── DHParameter.cs
    │   │   │   │   │   │   ├── PBEParameter.cs
    │   │   │   │   │   │   ├── PKCS12PBEParams.cs
    │   │   │   │   │   │   ├── PKCSObjectIdentifiers.cs
    │   │   │   │   │   │   ├── PrivateKeyInfo.cs
    │   │   │   │   │   │   └── SafeBag.cs
    │   │   │   │   │   ├── sec/
    │   │   │   │   │   │   ├── ECPrivateKeyStructure.cs
    │   │   │   │   │   │   ├── SECNamedCurves.cs
    │   │   │   │   │   │   └── SECObjectIdentifiers.cs
    │   │   │   │   │   ├── util/
    │   │   │   │   │   │   └── Asn1Dump.cs
    │   │   │   │   │   ├── x509/
    │   │   │   │   │   │   ├── AccessDescription.cs
    │   │   │   │   │   │   ├── AlgorithmIdentifier.cs
    │   │   │   │   │   │   ├── AttCertIssuer.cs
    │   │   │   │   │   │   ├── AttCertValidityPeriod.cs
    │   │   │   │   │   │   ├── Attribute.cs
    │   │   │   │   │   │   ├── AttributeCertificate.cs
    │   │   │   │   │   │   ├── AttributeCertificateInfo.cs
    │   │   │   │   │   │   ├── AttributeTable.cs
    │   │   │   │   │   │   ├── AuthorityInformationAccess.cs
    │   │   │   │   │   │   ├── BasicConstraints.cs
    │   │   │   │   │   │   ├── CRLDistPoint.cs
    │   │   │   │   │   │   ├── CRLReason.cs
    │   │   │   │   │   │   ├── CertPolicyId.cs
    │   │   │   │   │   │   ├── CertificateList.cs
    │   │   │   │   │   │   ├── CertificatePair.cs
    │   │   │   │   │   │   ├── CertificatePolicies.cs
    │   │   │   │   │   │   ├── DSAParameter.cs
    │   │   │   │   │   │   ├── DigestInfo.cs
    │   │   │   │   │   │   ├── DisplayText.cs
    │   │   │   │   │   │   ├── DistributionPoint.cs
    │   │   │   │   │   │   ├── DistributionPointName.cs
    │   │   │   │   │   │   ├── ExtendedKeyUsage.cs
    │   │   │   │   │   │   ├── GeneralName.cs
    │   │   │   │   │   │   ├── GeneralNames.cs
    │   │   │   │   │   │   ├── GeneralSubtree.cs
    │   │   │   │   │   │   ├── Holder.cs
    │   │   │   │   │   │   ├── IetfAttrSyntax.cs
    │   │   │   │   │   │   ├── IssuerSerial.cs
    │   │   │   │   │   │   ├── IssuingDistributionPoint.cs
    │   │   │   │   │   │   ├── KeyPurposeId.cs
    │   │   │   │   │   │   ├── KeyUsage.cs
    │   │   │   │   │   │   ├── NameConstraints.cs
    │   │   │   │   │   │   ├── NoticeReference.cs
    │   │   │   │   │   │   ├── ObjectDigestInfo.cs
    │   │   │   │   │   │   ├── OtherName.cs
    │   │   │   │   │   │   ├── PolicyInformation.cs
    │   │   │   │   │   │   ├── PolicyMappings.cs
    │   │   │   │   │   │   ├── PolicyQualifierId.cs
    │   │   │   │   │   │   ├── PolicyQualifierInfo.cs
    │   │   │   │   │   │   ├── PrivateKeyUsagePeriod.cs
    │   │   │   │   │   │   ├── RSAPublicKeyStructure.cs
    │   │   │   │   │   │   ├── ReasonFlags.cs
    │   │   │   │   │   │   ├── RoleSyntax.cs
    │   │   │   │   │   │   ├── SubjectDirectoryAttributes.cs
    │   │   │   │   │   │   ├── SubjectPublicKeyInfo.cs
    │   │   │   │   │   │   ├── TBSCertList.cs
    │   │   │   │   │   │   ├── TBSCertificateStructure.cs
    │   │   │   │   │   │   ├── Target.cs
    │   │   │   │   │   │   ├── TargetInformation.cs
    │   │   │   │   │   │   ├── Targets.cs
    │   │   │   │   │   │   ├── Time.cs
    │   │   │   │   │   │   ├── UserNotice.cs
    │   │   │   │   │   │   ├── V1TBSCertificateGenerator.cs
    │   │   │   │   │   │   ├── V2AttributeCertificateInfoGenerator.cs
    │   │   │   │   │   │   ├── V2Form.cs
    │   │   │   │   │   │   ├── V2TBSCertListGenerator.cs
    │   │   │   │   │   │   ├── V3TBSCertificateGenerator.cs
    │   │   │   │   │   │   ├── X509Attributes.cs
    │   │   │   │   │   │   ├── X509CertificateStructure.cs
    │   │   │   │   │   │   ├── X509DefaultEntryConverter.cs
    │   │   │   │   │   │   ├── X509Extension.cs
    │   │   │   │   │   │   ├── X509Extensions.cs
    │   │   │   │   │   │   ├── X509ExtensionsGenerator.cs
    │   │   │   │   │   │   ├── X509Name.cs
    │   │   │   │   │   │   ├── X509NameEntryConverter.cs
    │   │   │   │   │   │   ├── X509NameTokenizer.cs
    │   │   │   │   │   │   └── X509ObjectIdentifiers.cs
    │   │   │   │   │   └── x9/
    │   │   │   │   │       ├── DHDomainParameters.cs
    │   │   │   │   │       ├── DHPublicKey.cs
    │   │   │   │   │       ├── DHValidationParms.cs
    │   │   │   │   │       ├── ECNamedCurveTable.cs
    │   │   │   │   │       ├── KeySpecificInfo.cs
    │   │   │   │   │       ├── OtherInfo.cs
    │   │   │   │   │       ├── X962NamedCurves.cs
    │   │   │   │   │       ├── X962Parameters.cs
    │   │   │   │   │       ├── X9Curve.cs
    │   │   │   │   │       ├── X9ECParameters.cs
    │   │   │   │   │       ├── X9ECParametersHolder.cs
    │   │   │   │   │       ├── X9ECPoint.cs
    │   │   │   │   │       ├── X9FieldElement.cs
    │   │   │   │   │       ├── X9FieldID.cs
    │   │   │   │   │       ├── X9IntegerConverter.cs
    │   │   │   │   │       └── X9ObjectIdentifiers.cs
    │   │   │   │   ├── crypto/
    │   │   │   │   │   ├── AsymmetricCipherKeyPair.cs
    │   │   │   │   │   ├── AsymmetricKeyParameter.cs
    │   │   │   │   │   ├── Check.cs
    │   │   │   │   │   ├── CipherKeyGenerator.cs
    │   │   │   │   │   ├── CryptoException.cs
    │   │   │   │   │   ├── DataLengthException.cs
    │   │   │   │   │   ├── IAlphabetMapper.cs
    │   │   │   │   │   ├── IAsymmetricBlockCipher.cs
    │   │   │   │   │   ├── IAsymmetricCipherKeyPairGenerator.cs
    │   │   │   │   │   ├── IBasicAgreement.cs
    │   │   │   │   │   ├── IBlockCipher.cs
    │   │   │   │   │   ├── IBlockResult.cs
    │   │   │   │   │   ├── IBufferedCipher.cs
    │   │   │   │   │   ├── ICipher.cs
    │   │   │   │   │   ├── ICipherBuilder.cs
    │   │   │   │   │   ├── ICipherBuilderWithKey.cs
    │   │   │   │   │   ├── ICipherParameters.cs
    │   │   │   │   │   ├── IDSA.cs
    │   │   │   │   │   ├── IDecryptorBuilderProvider.cs
    │   │   │   │   │   ├── IDerivationFunction.cs
    │   │   │   │   │   ├── IDerivationParameters.cs
    │   │   │   │   │   ├── IDigest.cs
    │   │   │   │   │   ├── IDigestFactory.cs
    │   │   │   │   │   ├── IEncapsulatedSecretExtractor.cs
    │   │   │   │   │   ├── IEncapsulatedSecretGenerator.cs
    │   │   │   │   │   ├── IEntropySource.cs
    │   │   │   │   │   ├── IEntropySourceProvider.cs
    │   │   │   │   │   ├── IKeyUnwrapper.cs
    │   │   │   │   │   ├── IKeyWrapper.cs
    │   │   │   │   │   ├── IMac.cs
    │   │   │   │   │   ├── IMacDerivationFunction.cs
    │   │   │   │   │   ├── IMacFactory.cs
    │   │   │   │   │   ├── IRawAgreement.cs
    │   │   │   │   │   ├── IRsa.cs
    │   │   │   │   │   ├── ISecretWithEncapsulation.cs
    │   │   │   │   │   ├── ISignatureFactory.cs
    │   │   │   │   │   ├── ISigner.cs
    │   │   │   │   │   ├── ISignerWithRecovery.cs
    │   │   │   │   │   ├── IStreamCalculator.cs
    │   │   │   │   │   ├── IStreamCipher.cs
    │   │   │   │   │   ├── IVerifier.cs
    │   │   │   │   │   ├── IVerifierFactory.cs
    │   │   │   │   │   ├── IVerifierFactoryProvider.cs
    │   │   │   │   │   ├── IWrapper.cs
    │   │   │   │   │   ├── IXof.cs
    │   │   │   │   │   ├── InvalidCipherTextException.cs
    │   │   │   │   │   ├── KeyGenerationParameters.cs
    │   │   │   │   │   ├── MaxBytesExceededException.cs
    │   │   │   │   │   ├── OutputLengthException.cs
    │   │   │   │   │   ├── PbeParametersGenerator.cs
    │   │   │   │   │   ├── Security.cs
    │   │   │   │   │   ├── SimpleBlockResult.cs
    │   │   │   │   │   ├── digests/
    │   │   │   │   │   │   ├── CSHAKEDigest.cs
    │   │   │   │   │   │   ├── GeneralDigest.cs
    │   │   │   │   │   │   ├── KeccakDigest.cs
    │   │   │   │   │   │   ├── LongDigest.cs
    │   │   │   │   │   │   ├── MD5Digest.cs
    │   │   │   │   │   │   ├── Sha256Digest.cs
    │   │   │   │   │   │   ├── Sha512Digest.cs
    │   │   │   │   │   │   ├── ShakeDigest.cs
    │   │   │   │   │   │   └── XofUtils.cs
    │   │   │   │   │   ├── ec/
    │   │   │   │   │   │   └── CustomNamedCurves.cs
    │   │   │   │   │   ├── encodings/
    │   │   │   │   │   │   └── Pkcs1Encoding.cs
    │   │   │   │   │   ├── generators/
    │   │   │   │   │   │   ├── BCrypt.cs
    │   │   │   │   │   │   ├── ECKeyPairGenerator.cs
    │   │   │   │   │   │   ├── Ed25519KeyPairGenerator.cs
    │   │   │   │   │   │   └── OpenSSLPBEParametersGenerator.cs
    │   │   │   │   │   ├── io/
    │   │   │   │   │   │   ├── DigestSink.cs
    │   │   │   │   │   │   └── SignerSink.cs
    │   │   │   │   │   ├── macs/
    │   │   │   │   │   │   ├── GMac.cs
    │   │   │   │   │   │   ├── GOST28147Mac.cs
    │   │   │   │   │   │   ├── HMac.cs
    │   │   │   │   │   │   └── VMPCMac.cs
    │   │   │   │   │   ├── modes/
    │   │   │   │   │   │   └── gcm/
    │   │   │   │   │   │       ├── BasicGcmExponentiator.cs
    │   │   │   │   │   │       ├── BasicGcmMultiplier.cs
    │   │   │   │   │   │       ├── GcmUtilities.cs
    │   │   │   │   │   │       ├── IGcmExponentiator.cs
    │   │   │   │   │   │       ├── IGcmMultiplier.cs
    │   │   │   │   │   │       ├── Tables1kGcmExponentiator.cs
    │   │   │   │   │   │       ├── Tables4kGcmMultiplier.cs
    │   │   │   │   │   │       ├── Tables64kGcmMultiplier.cs
    │   │   │   │   │   │       └── Tables8kGcmMultiplier.cs
    │   │   │   │   │   ├── operators/
    │   │   │   │   │   │   ├── DefaultSignatureCalculator.cs
    │   │   │   │   │   │   ├── DefaultSignatureResult.cs
    │   │   │   │   │   │   ├── DefaultVerifierCalculator.cs
    │   │   │   │   │   │   └── DefaultVerifierResult.cs
    │   │   │   │   │   ├── paddings/
    │   │   │   │   │   │   ├── IBlockCipherPadding.cs
    │   │   │   │   │   │   ├── Pkcs7Padding.cs
    │   │   │   │   │   │   └── ZeroBytePadding.cs
    │   │   │   │   │   ├── parameters/
    │   │   │   │   │   │   ├── DSAParameterGenerationParameters.cs
    │   │   │   │   │   │   ├── DsaKeyGenerationParameters.cs
    │   │   │   │   │   │   ├── DsaKeyParameters.cs
    │   │   │   │   │   │   ├── DsaParameters.cs
    │   │   │   │   │   │   ├── DsaPrivateKeyParameters.cs
    │   │   │   │   │   │   ├── DsaPublicKeyParameters.cs
    │   │   │   │   │   │   ├── DsaValidationParameters.cs
    │   │   │   │   │   │   ├── ECDomainParameters.cs
    │   │   │   │   │   │   ├── ECKeyGenerationParameters.cs
    │   │   │   │   │   │   ├── ECKeyParameters.cs
    │   │   │   │   │   │   ├── ECNamedDomainParameters.cs
    │   │   │   │   │   │   ├── ECPrivateKeyParameters.cs
    │   │   │   │   │   │   ├── ECPublicKeyParameters.cs
    │   │   │   │   │   │   ├── Ed25519KeyGenerationParameters.cs
    │   │   │   │   │   │   ├── Ed25519PrivateKeyParameters.cs
    │   │   │   │   │   │   ├── Ed25519PublicKeyParameters.cs
    │   │   │   │   │   │   ├── IesParameters.cs
    │   │   │   │   │   │   ├── IesWithCipherParameters.cs
    │   │   │   │   │   │   ├── KeyParameter.cs
    │   │   │   │   │   │   ├── ParametersWithID.cs
    │   │   │   │   │   │   ├── ParametersWithIV.cs
    │   │   │   │   │   │   ├── ParametersWithRandom.cs
    │   │   │   │   │   │   ├── ParametersWithSBox.cs
    │   │   │   │   │   │   └── ParametersWithSalt.cs
    │   │   │   │   │   ├── prng/
    │   │   │   │   │   │   ├── BasicEntropySourceProvider.cs
    │   │   │   │   │   │   ├── CryptoApiEntropySourceProvider.cs
    │   │   │   │   │   │   ├── CryptoApiRandomGenerator.cs
    │   │   │   │   │   │   ├── DigestRandomGenerator.cs
    │   │   │   │   │   │   ├── EntropyUtilities.cs
    │   │   │   │   │   │   ├── IDrbgProvider.cs
    │   │   │   │   │   │   ├── IRandomGenerator.cs
    │   │   │   │   │   │   ├── SP800SecureRandom.cs
    │   │   │   │   │   │   ├── SP800SecureRandomBuilder.cs
    │   │   │   │   │   │   ├── VMPCRandomGenerator.cs
    │   │   │   │   │   │   ├── X931Rng.cs
    │   │   │   │   │   │   ├── X931SecureRandom.cs
    │   │   │   │   │   │   ├── X931SecureRandomBuilder.cs
    │   │   │   │   │   │   └── drbg/
    │   │   │   │   │   │       ├── CtrSP800Drbg.cs
    │   │   │   │   │   │       ├── DrbgUtilities.cs
    │   │   │   │   │   │       ├── HMacSP800Drbg.cs
    │   │   │   │   │   │       ├── HashSP800Drbg.cs
    │   │   │   │   │   │       └── ISP80090Drbg.cs
    │   │   │   │   │   ├── signers/
    │   │   │   │   │   │   ├── DsaDigestSigner.cs
    │   │   │   │   │   │   ├── ECDsaSigner.cs
    │   │   │   │   │   │   ├── ECGOST3410Signer.cs
    │   │   │   │   │   │   ├── ECNRSigner.cs
    │   │   │   │   │   │   ├── Ed25519Signer.cs
    │   │   │   │   │   │   ├── Ed25519ctxSigner.cs
    │   │   │   │   │   │   ├── Ed25519phSigner.cs
    │   │   │   │   │   │   ├── GenericSigner.cs
    │   │   │   │   │   │   ├── HMacDsaKCalculator.cs
    │   │   │   │   │   │   ├── IDsaEncoding.cs
    │   │   │   │   │   │   ├── IDsaKCalculator.cs
    │   │   │   │   │   │   ├── IsoTrailers.cs
    │   │   │   │   │   │   ├── PlainDsaEncoding.cs
    │   │   │   │   │   │   ├── RandomDsaKCalculator.cs
    │   │   │   │   │   │   └── StandardDsaEncoding.cs
    │   │   │   │   │   └── util/
    │   │   │   │   │       ├── AlgorithmIdentifierFactory.cs
    │   │   │   │   │       ├── BasicAlphabetMapper.cs
    │   │   │   │   │       └── Pack.cs
    │   │   │   │   ├── math/
    │   │   │   │   │   ├── BigInteger.cs
    │   │   │   │   │   ├── Primes.cs
    │   │   │   │   │   ├── ec/
    │   │   │   │   │   │   ├── AbstractECLookupTable.cs
    │   │   │   │   │   │   ├── ECAlgorithms.cs
    │   │   │   │   │   │   ├── ECCurve.cs
    │   │   │   │   │   │   ├── ECFieldElement.cs
    │   │   │   │   │   │   ├── ECLookupTable.cs
    │   │   │   │   │   │   ├── ECPoint.cs
    │   │   │   │   │   │   ├── ECPointMap.cs
    │   │   │   │   │   │   ├── LongArray.cs
    │   │   │   │   │   │   ├── ScaleXNegateYPointMap.cs
    │   │   │   │   │   │   ├── ScaleXPointMap.cs
    │   │   │   │   │   │   ├── ScaleYNegateXPointMap.cs
    │   │   │   │   │   │   ├── ScaleYPointMap.cs
    │   │   │   │   │   │   ├── SimpleLookupTable.cs
    │   │   │   │   │   │   ├── abc/
    │   │   │   │   │   │   │   ├── SimpleBigDecimal.cs
    │   │   │   │   │   │   │   ├── Tnaf.cs
    │   │   │   │   │   │   │   └── ZTauElement.cs
    │   │   │   │   │   │   ├── custom/
    │   │   │   │   │   │   │   ├── gm/
    │   │   │   │   │   │   │   │   ├── SM2P256V1Curve.cs
    │   │   │   │   │   │   │   │   ├── SM2P256V1Field.cs
    │   │   │   │   │   │   │   │   ├── SM2P256V1FieldElement.cs
    │   │   │   │   │   │   │   │   └── SM2P256V1Point.cs
    │   │   │   │   │   │   │   └── sec/
    │   │   │   │   │   │   │       ├── SecP256K1Curve.cs
    │   │   │   │   │   │   │       ├── SecP256K1Field.cs
    │   │   │   │   │   │   │       ├── SecP256K1FieldElement.cs
    │   │   │   │   │   │   │       ├── SecP256K1Point.cs
    │   │   │   │   │   │   │       ├── SecP256R1Curve.cs
    │   │   │   │   │   │   │       ├── SecP256R1Field.cs
    │   │   │   │   │   │   │       ├── SecP256R1FieldElement.cs
    │   │   │   │   │   │   │       └── SecP256R1Point.cs
    │   │   │   │   │   │   ├── endo/
    │   │   │   │   │   │   │   ├── ECEndomorphism.cs
    │   │   │   │   │   │   │   ├── EndoPreCompInfo.cs
    │   │   │   │   │   │   │   ├── EndoUtilities.cs
    │   │   │   │   │   │   │   ├── GlvEndomorphism.cs
    │   │   │   │   │   │   │   ├── GlvTypeAEndomorphism.cs
    │   │   │   │   │   │   │   ├── GlvTypeAParameters.cs
    │   │   │   │   │   │   │   ├── GlvTypeBEndomorphism.cs
    │   │   │   │   │   │   │   ├── GlvTypeBParameters.cs
    │   │   │   │   │   │   │   └── ScalarSplitParameters.cs
    │   │   │   │   │   │   ├── multiplier/
    │   │   │   │   │   │   │   ├── AbstractECMultiplier.cs
    │   │   │   │   │   │   │   ├── ECMultiplier.cs
    │   │   │   │   │   │   │   ├── FixedPointCombMultiplier.cs
    │   │   │   │   │   │   │   ├── FixedPointPreCompInfo.cs
    │   │   │   │   │   │   │   ├── FixedPointUtilities.cs
    │   │   │   │   │   │   │   ├── GlvMultiplier.cs
    │   │   │   │   │   │   │   ├── IPreCompCallback.cs
    │   │   │   │   │   │   │   ├── PreCompInfo.cs
    │   │   │   │   │   │   │   ├── ValidityPreCompInfo.cs
    │   │   │   │   │   │   │   ├── WNafL2RMultiplier.cs
    │   │   │   │   │   │   │   ├── WNafPreCompInfo.cs
    │   │   │   │   │   │   │   ├── WNafUtilities.cs
    │   │   │   │   │   │   │   ├── WTauNafMultiplier.cs
    │   │   │   │   │   │   │   └── WTauNafPreCompInfo.cs
    │   │   │   │   │   │   ├── rfc7748/
    │   │   │   │   │   │   │   ├── X25519.cs
    │   │   │   │   │   │   │   ├── X25519Field.cs
    │   │   │   │   │   │   │   ├── X448.cs
    │   │   │   │   │   │   │   └── X448Field.cs
    │   │   │   │   │   │   └── rfc8032/
    │   │   │   │   │   │       ├── Ed25519.cs
    │   │   │   │   │   │       └── Ed448.cs
    │   │   │   │   │   ├── field/
    │   │   │   │   │   │   ├── FiniteFields.cs
    │   │   │   │   │   │   ├── GF2Polynomial.cs
    │   │   │   │   │   │   ├── GenericPolynomialExtensionField.cs
    │   │   │   │   │   │   ├── IExtensionField.cs
    │   │   │   │   │   │   ├── IFiniteField.cs
    │   │   │   │   │   │   ├── IPolynomial.cs
    │   │   │   │   │   │   ├── IPolynomialExtensionField.cs
    │   │   │   │   │   │   └── PrimeField.cs
    │   │   │   │   │   └── raw/
    │   │   │   │   │       ├── Bits.cs
    │   │   │   │   │       ├── Interleave.cs
    │   │   │   │   │       ├── Mod.cs
    │   │   │   │   │       ├── Nat.cs
    │   │   │   │   │       ├── Nat128.cs
    │   │   │   │   │       ├── Nat160.cs
    │   │   │   │   │       ├── Nat192.cs
    │   │   │   │   │       ├── Nat224.cs
    │   │   │   │   │       ├── Nat256.cs
    │   │   │   │   │       ├── Nat320.cs
    │   │   │   │   │       ├── Nat384.cs
    │   │   │   │   │       ├── Nat448.cs
    │   │   │   │   │       ├── Nat512.cs
    │   │   │   │   │       └── Nat576.cs
    │   │   │   │   ├── openssl/
    │   │   │   │   │   ├── EncryptionException.cs
    │   │   │   │   │   ├── IPasswordFinder.cs
    │   │   │   │   │   ├── MiscPemGenerator.cs
    │   │   │   │   │   ├── PEMException.cs
    │   │   │   │   │   ├── PEMReader.cs
    │   │   │   │   │   ├── PEMUtilities.cs
    │   │   │   │   │   ├── PEMWriter.cs
    │   │   │   │   │   ├── PasswordException.cs
    │   │   │   │   │   └── Pkcs8Generator.cs
    │   │   │   │   ├── pkcs/
    │   │   │   │   │   ├── AsymmetricKeyEntry.cs
    │   │   │   │   │   ├── PkcsException.cs
    │   │   │   │   │   ├── PkcsIOException.cs
    │   │   │   │   │   └── PrivateKeyInfoFactory.cs
    │   │   │   │   ├── security/
    │   │   │   │   │   ├── DigestUtilities.cs
    │   │   │   │   │   ├── DotNetUtilities.cs
    │   │   │   │   │   ├── GeneralSecurityException.cs
    │   │   │   │   │   ├── GeneratorUtilities.cs
    │   │   │   │   │   ├── InvalidKeyException.cs
    │   │   │   │   │   ├── InvalidParameterException.cs
    │   │   │   │   │   ├── KeyException.cs
    │   │   │   │   │   ├── MacUtilities.cs
    │   │   │   │   │   ├── ParameterUtilities.cs
    │   │   │   │   │   ├── PrivateKeyFactory.cs
    │   │   │   │   │   ├── PublicKeyFactory.cs
    │   │   │   │   │   ├── SecureRandom.cs
    │   │   │   │   │   ├── SecurityUtilityException.cs
    │   │   │   │   │   └── WrapperUtilities.cs
    │   │   │   │   └── util/
    │   │   │   │       ├── Arrays.cs
    │   │   │   │       ├── BigIntegers.cs
    │   │   │   │       ├── Bytes.cs
    │   │   │   │       ├── Enums.cs
    │   │   │   │       ├── IEncodable.cs
    │   │   │   │       ├── IMemoable.cs
    │   │   │   │       ├── Integers.cs
    │   │   │   │       ├── Longs.cs
    │   │   │   │       ├── MemoableResetException.cs
    │   │   │   │       ├── Objects.cs
    │   │   │   │       ├── Platform.cs
    │   │   │   │       ├── Spans.cs
    │   │   │   │       ├── Strings.cs
    │   │   │   │       ├── Times.cs
    │   │   │   │       ├── collections/
    │   │   │   │       │   ├── CollectionUtilities.cs
    │   │   │   │       │   ├── EnumerableProxy.cs
    │   │   │   │       │   ├── ISelector.cs
    │   │   │   │       │   ├── IStore.cs
    │   │   │   │       │   ├── ReadOnlyCollection.cs
    │   │   │   │       │   ├── ReadOnlyDictionary.cs
    │   │   │   │       │   ├── ReadOnlyList.cs
    │   │   │   │       │   ├── ReadOnlySet.cs
    │   │   │   │       │   └── StoreImpl.cs
    │   │   │   │       ├── date/
    │   │   │   │       │   ├── DateTimeObject.cs
    │   │   │   │       │   └── DateTimeUtilities.cs
    │   │   │   │       ├── encoders/
    │   │   │   │       │   ├── Base64.cs
    │   │   │   │       │   ├── Base64Encoder.cs
    │   │   │   │       │   ├── BufferedDecoder.cs
    │   │   │   │       │   ├── BufferedEncoder.cs
    │   │   │   │       │   ├── Hex.cs
    │   │   │   │       │   ├── HexEncoder.cs
    │   │   │   │       │   ├── HexTranslator.cs
    │   │   │   │       │   ├── IEncoder.cs
    │   │   │   │       │   ├── Translator.cs
    │   │   │   │       │   ├── UrlBase64.cs
    │   │   │   │       │   └── UrlBase64Encoder.cs
    │   │   │   │       ├── io/
    │   │   │   │       │   ├── BaseInputStream.cs
    │   │   │   │       │   ├── BaseOutputStream.cs
    │   │   │   │       │   ├── FilterStream.cs
    │   │   │   │       │   ├── MemoryInputStream.cs
    │   │   │   │       │   ├── MemoryOutputStream.cs
    │   │   │   │       │   ├── PushbackStream.cs
    │   │   │   │       │   ├── StreamOverflowException.cs
    │   │   │   │       │   ├── Streams.cs
    │   │   │   │       │   ├── TeeInputStream.cs
    │   │   │   │       │   ├── TeeOutputStream.cs
    │   │   │   │       │   └── pem/
    │   │   │   │       │       ├── PemGenerationException.cs
    │   │   │   │       │       ├── PemHeader.cs
    │   │   │   │       │       ├── PemObject.cs
    │   │   │   │       │       ├── PemObjectGenerator.cs
    │   │   │   │       │       ├── PemObjectParser.cs
    │   │   │   │       │       ├── PemReader.cs
    │   │   │   │       │       └── PemWriter.cs
    │   │   │   │       └── net/
    │   │   │   │           └── IPAddress.cs
    │   │   │   └── StarkSharp/
    │   │   │       ├── StarkSharp.Account/
    │   │   │       │   └── Account.cs
    │   │   │       ├── StarkSharp.Base/
    │   │   │       │   ├── StarkSharp.ABI/
    │   │   │       │   │   └── V1/
    │   │   │       │   │       ├── abi.cs
    │   │   │       │   │       ├── parser.cs
    │   │   │       │   │       ├── schemas.cs
    │   │   │       │   │       └── shape.cs
    │   │   │       │   ├── StarkSharp.Cairo/
    │   │   │       │   │   ├── CairoContract.cs
    │   │   │       │   │   ├── SierraCairoContract.cs
    │   │   │       │   │   └── Type.cs
    │   │   │       │   ├── StarkSharp.Hash/
    │   │   │       │   │   ├── Address.cs
    │   │   │       │   │   ├── MemberDescription.cs
    │   │   │       │   │   ├── MemberDescriptionFactory.cs
    │   │   │       │   │   ├── MemberValue.cs
    │   │   │       │   │   ├── MemberValueFactory.cs
    │   │   │       │   │   ├── TypedData.cs
    │   │   │       │   │   └── TypedDataRaw.cs
    │   │   │       │   └── StarkSharp.Provider/
    │   │   │       │       └── StarkProvider.cs
    │   │   │       ├── StarkSharp.Platform/
    │   │   │       │   └── Platform.cs
    │   │   │       ├── StarkSharp.Resources/
    │   │   │       │   ├── Image/
    │   │   │       │   └── Settings/
    │   │   │       │       └── Settings.cs
    │   │   │       ├── StarkSharp.Rpc/
    │   │   │       │   └── Utils/
    │   │   │       │       ├── HexUtilities/
    │   │   │       │       │   └── NumericOps.cs
    │   │   │       │       └── StarknetUtilities/
    │   │   │       │           └── StarknetOps.cs
    │   │   │       ├── StarkSharp.Signer/
    │   │   │       │   └── StarkCurveSigner/
    │   │   │       │       ├── Extensions.cs
    │   │   │       │       ├── Signature.cs
    │   │   │       │       ├── pedersen_params.json
    │   │   │       │       └── Utils/
    │   │   │       │           ├── Errors.cs
    │   │   │       │           └── Math.cs
    │   │   │       └── StarkSharp.Tools/
    │   │   │           └── Sharp.Update/
    │   │   │               └── SharpUpdate.cs
    │   │   ├── wrappers/
    │   │   │   ├── ace.cs
    │   │   │   ├── alpaca.cs
    │   │   │   ├── ascendex.cs
    │   │   │   ├── bequant.cs
    │   │   │   ├── bigone.cs
    │   │   │   ├── binance.cs
    │   │   │   ├── binancecoinm.cs
    │   │   │   ├── binanceus.cs
    │   │   │   ├── binanceusdm.cs
    │   │   │   ├── bingx.cs
    │   │   │   ├── bit2c.cs
    │   │   │   ├── bitbank.cs
    │   │   │   ├── bitbns.cs
    │   │   │   ├── bitcoincom.cs
    │   │   │   ├── bitfinex.cs
    │   │   │   ├── bitfinex1.cs
    │   │   │   ├── bitflyer.cs
    │   │   │   ├── bitget.cs
    │   │   │   ├── bithumb.cs
    │   │   │   ├── bitmart.cs
    │   │   │   ├── bitmex.cs
    │   │   │   ├── bitopro.cs
    │   │   │   ├── bitpanda.cs
    │   │   │   ├── bitrue.cs
    │   │   │   ├── bitso.cs
    │   │   │   ├── bitstamp.cs
    │   │   │   ├── bitteam.cs
    │   │   │   ├── bitvavo.cs
    │   │   │   ├── bl3p.cs
    │   │   │   ├── blockchaincom.cs
    │   │   │   ├── blofin.cs
    │   │   │   ├── btcalpha.cs
    │   │   │   ├── btcbox.cs
    │   │   │   ├── btcmarkets.cs
    │   │   │   ├── btcturk.cs
    │   │   │   ├── bybit.cs
    │   │   │   ├── cex.cs
    │   │   │   ├── coinbase.cs
    │   │   │   ├── coinbaseadvanced.cs
    │   │   │   ├── coinbaseexchange.cs
    │   │   │   ├── coinbaseinternational.cs
    │   │   │   ├── coincatch.cs
    │   │   │   ├── coincheck.cs
    │   │   │   ├── coinex.cs
    │   │   │   ├── coinlist.cs
    │   │   │   ├── coinmate.cs
    │   │   │   ├── coinmetro.cs
    │   │   │   ├── coinone.cs
    │   │   │   ├── coinsph.cs
    │   │   │   ├── coinspot.cs
    │   │   │   ├── cryptocom.cs
    │   │   │   ├── currencycom.cs
    │   │   │   ├── defx.cs
    │   │   │   ├── delta.cs
    │   │   │   ├── deribit.cs
    │   │   │   ├── digifinex.cs
    │   │   │   ├── ellipx.cs
    │   │   │   ├── exmo.cs
    │   │   │   ├── fmfwio.cs
    │   │   │   ├── gate.cs
    │   │   │   ├── gateio.cs
    │   │   │   ├── gemini.cs
    │   │   │   ├── hashkey.cs
    │   │   │   ├── hitbtc.cs
    │   │   │   ├── hollaex.cs
    │   │   │   ├── htx.cs
    │   │   │   ├── huobi.cs
    │   │   │   ├── huobijp.cs
    │   │   │   ├── hyperliquid.cs
    │   │   │   ├── idex.cs
    │   │   │   ├── independentreserve.cs
    │   │   │   ├── indodax.cs
    │   │   │   ├── kraken.cs
    │   │   │   ├── krakenfutures.cs
    │   │   │   ├── kucoin.cs
    │   │   │   ├── kucoinfutures.cs
    │   │   │   ├── kuna.cs
    │   │   │   ├── latoken.cs
    │   │   │   ├── lbank.cs
    │   │   │   ├── luno.cs
    │   │   │   ├── mercado.cs
    │   │   │   ├── mexc.cs
    │   │   │   ├── myokx.cs
    │   │   │   ├── ndax.cs
    │   │   │   ├── novadax.cs
    │   │   │   ├── oceanex.cs
    │   │   │   ├── okcoin.cs
    │   │   │   ├── okx.cs
    │   │   │   ├── onetrading.cs
    │   │   │   ├── oxfun.cs
    │   │   │   ├── p2b.cs
    │   │   │   ├── paradex.cs
    │   │   │   ├── paymium.cs
    │   │   │   ├── phemex.cs
    │   │   │   ├── poloniex.cs
    │   │   │   ├── poloniexfutures.cs
    │   │   │   ├── probit.cs
    │   │   │   ├── timex.cs
    │   │   │   ├── tokocrypto.cs
    │   │   │   ├── tradeogre.cs
    │   │   │   ├── upbit.cs
    │   │   │   ├── vertex.cs
    │   │   │   ├── wavesexchange.cs
    │   │   │   ├── wazirx.cs
    │   │   │   ├── whitebit.cs
    │   │   │   ├── woo.cs
    │   │   │   ├── woofipro.cs
    │   │   │   ├── xt.cs
    │   │   │   ├── yobit.cs
    │   │   │   ├── zaif.cs
    │   │   │   └── zonda.cs
    │   │   └── ws/
    │   │       ├── ArrayCache.cs
    │   │       ├── Client.cs
    │   │       ├── CustomConcurrentDictionary.cs
    │   │       ├── Exchange.Ws.cs
    │   │       ├── Exchange.WsBridge.cs
    │   │       ├── Future.cs
    │   │       ├── OrderBook.cs
    │   │       ├── OrderBookSide.cs
    │   │       └── SlimConcurrentList.cs
    │   ├── cli/
    │   │   ├── Helper.cs
    │   │   ├── Program.cs
    │   │   └── cli.csproj
    │   └── tests/
    │       ├── BaseTest.Bridge.cs
    │       ├── BaseTest.Helpers.cs
    │       ├── Program.cs
    │       ├── RaceTest.cs
    │       ├── tests.csproj
    │       └── Generated/
    │           ├── TestMethods.cs
    │           ├── Base/
    │           │   ├── test.afterConstructor.cs
    │           │   ├── test.cryptography.cs
    │           │   ├── test.datetime.cs
    │           │   ├── test.deepExtend.cs
    │           │   ├── test.extend.cs
    │           │   ├── test.filterBy.cs
    │           │   ├── test.groupBy.cs
    │           │   ├── test.json.cs
    │           │   ├── test.number.cs
    │           │   ├── test.omit.cs
    │           │   ├── test.safeMethods.cs
    │           │   ├── test.sortBy.cs
    │           │   ├── test.sum.cs
    │           │   ├── tests.init.cs
    │           │   └── Ws/
    │           │       ├── test.cache.cs
    │           │       └── test.orderBook.cs
    │           └── Exchange/
    │               ├── test.createOrder.cs
    │               ├── test.features.cs
    │               ├── test.fetchAccounts.cs
    │               ├── test.fetchBalance.cs
    │               ├── test.fetchBorrowInterest.cs
    │               ├── test.fetchClosedOrders.cs
    │               ├── test.fetchCurrencies.cs
    │               ├── test.fetchDepositWithdrawals.cs
    │               ├── test.fetchDeposits.cs
    │               ├── test.fetchFundingRateHistory.cs
    │               ├── test.fetchL2OrderBook.cs
    │               ├── test.fetchLastPrices.cs
    │               ├── test.fetchLedger.cs
    │               ├── test.fetchLedgerEntry.cs
    │               ├── test.fetchLeverageTiers.cs
    │               ├── test.fetchLiquidations.cs
    │               ├── test.fetchMarginMode.cs
    │               ├── test.fetchMarginModes.cs
    │               ├── test.fetchMarketLeverageTiers.cs
    │               ├── test.fetchMarkets.cs
    │               ├── test.fetchMyLiquidations.cs
    │               ├── test.fetchMyTrades.cs
    │               ├── test.fetchOHLCV.cs
    │               ├── test.fetchOpenInterestHistory.cs
    │               ├── test.fetchOpenOrders.cs
    │               ├── test.fetchOrderBook.cs
    │               ├── test.fetchOrderBooks.cs
    │               ├── test.fetchOrders.cs
    │               ├── test.fetchPositions.cs
    │               ├── test.fetchStatus.cs
    │               ├── test.fetchTicker.cs
    │               ├── test.fetchTickers.cs
    │               ├── test.fetchTrades.cs
    │               ├── test.fetchTradingFee.cs
    │               ├── test.fetchTradingFees.cs
    │               ├── test.fetchTransactionFees.cs
    │               ├── test.fetchWithdrawals.cs
    │               ├── test.loadMarkets.cs
    │               ├── test.proxies.cs
    │               ├── test.signIn.cs
    │               ├── Base/
    │               │   ├── test.account.cs
    │               │   ├── test.balance.cs
    │               │   ├── test.borrowInterest.cs
    │               │   ├── test.borrowRate.cs
    │               │   ├── test.currency.cs
    │               │   ├── test.depositWithdrawal.cs
    │               │   ├── test.fundingRateHistory.cs
    │               │   ├── test.lastPrice.cs
    │               │   ├── test.ledgerEntry.cs
    │               │   ├── test.leverageTier.cs
    │               │   ├── test.liquidation.cs
    │               │   ├── test.marginMode.cs
    │               │   ├── test.marginModification.cs
    │               │   ├── test.market.cs
    │               │   ├── test.ohlcv.cs
    │               │   ├── test.openInterest.cs
    │               │   ├── test.order.cs
    │               │   ├── test.orderBook.cs
    │               │   ├── test.position.cs
    │               │   ├── test.sharedMethods.cs
    │               │   ├── test.status.cs
    │               │   ├── test.ticker.cs
    │               │   ├── test.trade.cs
    │               │   └── test.tradingFee.cs
    │               └── Ws/
    │                   ├── test.watchBalance.cs
    │                   ├── test.watchBidsAsks.cs
    │                   ├── test.watchLiquidations.cs
    │                   ├── test.watchLiquidationsForSymbols.cs
    │                   ├── test.watchMyTrades.cs
    │                   ├── test.watchOHLCV.cs
    │                   ├── test.watchOHLCVForSymbols.cs
    │                   ├── test.watchOrderBook.cs
    │                   ├── test.watchOrderBookForSymbols.cs
    │                   ├── test.watchOrders.cs
    │                   ├── test.watchPosition.cs
    │                   ├── test.watchPositions.cs
    │                   ├── test.watchTicker.cs
    │                   ├── test.watchTickers.cs
    │                   ├── test.watchTrades.cs
    │                   └── test.watchTradesForSymbols.cs
    ├── doc/
    │   ├── FAQ.rst
    │   ├── Makefile
    │   ├── ccxt.pro.install.rst
    │   ├── ccxt.pro.manual.rst
    │   ├── conf.py
    │   ├── exchange-markets-by-country.rst
    │   ├── exchange-markets.rst
    │   ├── index.rst
    │   ├── install.rst
    │   ├── make.bat
    │   ├── manual.rst
    │   ├── readme.rst
    │   ├── requirements.txt
    │   ├── .gitignore
    │   └── _static/
    │       ├── css/
    │       │   ├── dark.css
    │       │   └── index.css
    │       └── javascript/
    │           └── index.js
    ├── examples/
    │   ├── README.md
    │   ├── tsconfig.json
    │   ├── .gitignore
    │   ├── bots/
    │   │   └── py/
    │   │       ├── bitfinex-lending-bot.py
    │   │       └── spot-arbitrage-bot.py
    │   ├── ccxt.pro/
    │   │   ├── html/
    │   │   │   └── watchTicker.html
    │   │   ├── js/
    │   │   │   ├── binance-fetch-balance-snapshot-watch-balance-updates.js
    │   │   │   ├── binance-https-proxy.js
    │   │   │   ├── binance-watch-ohlcv-many-symbols-continuously.js
    │   │   │   ├── binance-watch-ohlcv-many-symbols.js
    │   │   │   ├── binance-watch-ticker-many-symbols.js
    │   │   │   ├── build-ohlcv-many-symbols.js
    │   │   │   ├── calculate-ohlcvs-from-trades-warmup.js
    │   │   │   ├── calculate-ohlcvs-from-trades.js
    │   │   │   ├── exchange-capabitities.js
    │   │   │   ├── exchange-close.js
    │   │   │   ├── gateio-swap-watch-many-orderbooks.js
    │   │   │   ├── gateio-watch-balance.js
    │   │   │   ├── gateio-watch-order-book.js
    │   │   │   ├── graceful-shutdown.js
    │   │   │   ├── many-exchanges-many-streams.js
    │   │   │   ├── okex-create-futures-order.js
    │   │   │   ├── okex-watch-balance-and-create-order.js
    │   │   │   ├── okx-watch-tickers.js
    │   │   │   ├── one-exchange-many-different-streams.js
    │   │   │   ├── one-exchange-many-streams-2.js
    │   │   │   ├── one-exchange-many-streams.js
    │   │   │   ├── socks-binance-watch-orderbook.js
    │   │   │   ├── watch-fetch-many-exchanges-many-ordersbooks.js
    │   │   │   ├── watch-many-exchanges-many-ordersbooks.js
    │   │   │   ├── watch-many-exchanges-many-symbols.js
    │   │   │   ├── watch-many-orderbooks.js
    │   │   │   ├── watch-new-trades-only.js
    │   │   │   ├── watch-new-trades.js
    │   │   │   ├── watch-trades-many-symbols.js
    │   │   │   └── watch-vs-fetch.js
    │   │   ├── php/
    │   │   │   ├── many-exchanges-many-accounts.php
    │   │   │   ├── many-exchanges-synchronously.php
    │   │   │   ├── one-exchange-many-streams.php
    │   │   │   └── watch-multiple-methods-multiple-exchanges.php
    │   │   └── py/
    │   │       ├── binance-create-order-cancel-order.py
    │   │       ├── binance-fetch-balance-snapshot-watch-balance-updates.py
    │   │       ├── binance-futures-watch-balance.py
    │   │       ├── binance-futures-watch-order-book.py
    │   │       ├── binance-futures.py
    │   │       ├── binance-reload-markets.py
    │   │       ├── binance-spot-and-futures.py
    │   │       ├── binance-watch-many-orderbooks.py
    │   │       ├── binance-watch-margin-balance.py
    │   │       ├── binance-watch-ohlcv.py
    │   │       ├── binance-watch-order-book-individual-updates.py
    │   │       ├── binance-watch-orderbook-watch-balance.py
    │   │       ├── binance-watch-orders-being-placed.py
    │   │       ├── binance-watch-spot-futures-balances-continuously.py
    │   │       ├── bitmex_watch_ohlcv.py
    │   │       ├── bitmex_watch_ticker_and_ohlcv.py
    │   │       ├── bitvavo-watch-order-book.py
    │   │       ├── build-ohlcv-many-symbols.py
    │   │       ├── coinbase-watch-all-trades.py
    │   │       ├── coinbase-watch-trades.py
    │   │       ├── consume-all-trades.py
    │   │       ├── gateio-watch-trades.py
    │   │       ├── intercept-original-ohlcv-updates.py
    │   │       ├── kucoin-watch-multiple-orderbooks.py
    │   │       ├── many-exchanges-many-different-streams.py
    │   │       ├── many-exchanges-many-orderbooks-synchronized.py
    │   │       ├── many-exchanges-many-orderbooks-throttled.py
    │   │       ├── many-exchanges-many-streams-with-keys.py
    │   │       ├── many-exchanges-many-streams.py
    │   │       ├── many-exchanges-many-symbols-watch-trades.py
    │   │       ├── many-exchanges.py
    │   │       ├── multiple-exchanges-watch-orderbook-continuously.py
    │   │       ├── okex-create-swap-order.py
    │   │       ├── okex-watch-margin-balance-with-params.py
    │   │       ├── okex-watch-margin-balance.py
    │   │       ├── okx-bbo-tbt.py
    │   │       ├── on-connected-user-hook.py
    │   │       ├── one-exchange-different-streams.py
    │   │       ├── one-exchange-many-streams.py
    │   │       ├── phemex-cancel-all-orders.py
    │   │       ├── spot-vs-future-arbitrage-bitmart.py
    │   │       ├── watch-all-symbols.py
    │   │       ├── watch-custom-exchange-specific-streams.py
    │   │       ├── watch-many-exchanges-many-tickers.py
    │   │       └── watch-ticker-to-csv.py
    │   ├── cs/
    │   │   ├── Examples.sln
    │   │   ├── c#.csproj
    │   │   └── examples/
    │   │       ├── CreateExchangesDynamically.cs
    │   │       ├── CreateOrder.cs
    │   │       ├── Examples.Bridge.cs
    │   │       ├── FetchBalanceWithParams.cs
    │   │       ├── FetchFundingRateHistory.cs
    │   │       ├── FetchMarkets.cs
    │   │       ├── FetchMultipleTrades.cs
    │   │       ├── FetchOrderBook.cs
    │   │       ├── FetchPosition.cs
    │   │       ├── FetchTrades.cs
    │   │       ├── MarketAndCurrency.cs
    │   │       ├── Program.cs
    │   │       ├── compare-two-exchanges-capabilities.cs
    │   │       ├── create-order-position-with-takeprofit-stoploss.cs
    │   │       ├── create-order-ws-example.cs
    │   │       ├── create-orders-example.cs
    │   │       ├── create-trailing-amount-order.cs
    │   │       ├── create-trailing-percent-order.cs
    │   │       ├── fetch-ohlcv-many-exchanges-continuosly.cs
    │   │       ├── fetch-ohlcv.cs
    │   │       ├── get-active-markets.cs
    │   │       ├── kraken-create-and-close-position.cs
    │   │       ├── phemex-create-order-position-with-takeprofit-stoploss.cs
    │   │       ├── proxy-usage.cs
    │   │       ├── watch-OHLCV-For-Symbols.cs
    │   │       ├── watch-OrderBook-For-Symbols.cs
    │   │       ├── watch-Trades-For-Symbols.cs
    │   │       ├── watch-tickers.cs
    │   │       ├── watchPositions-many-exchanges-continuosly.cs
    │   │       ├── watchPositions.cs
    │   │       └── watchPositionsForSymbols.cs
    │   ├── go/
    │   │   ├── createOrderWithParams.go
    │   │   ├── errorHandlingExample.go
    │   │   ├── fetchOHLCV.go
    │   │   ├── fetchTrades.go
    │   │   ├── getMarketInformation.go
    │   │   └── spotPerpMarkets.go
    │   ├── html/
    │   │   ├── basic-cors-proxy.html
    │   │   ├── basic-inheritance.html
    │   │   ├── basic-poller.html
    │   │   ├── basic-rate-limiting.html
    │   │   ├── basic.html
    │   │   ├── binance-cors-proxy.html
    │   │   ├── bitmex-browser-cors-proxy.js
    │   │   ├── bitmex-cors.html
    │   │   ├── tradingview-charts.html
    │   │   └── webworker/
    │   │       ├── index.html
    │   │       └── worker.js
    │   ├── js/
    │   │   ├── README.md
    │   │   ├── advanced-error-handling.js
    │   │   ├── aggregate-orderbook.js
    │   │   ├── arbitrage-pairs.js
    │   │   ├── basic-chart.js
    │   │   ├── basic-orderbook-polling.js
    │   │   ├── bcc-vs-bch.js
    │   │   ├── benchmark.js
    │   │   ├── binance-fetch-all-deposits.js
    │   │   ├── binance-fetch-ohlcv-many-symbols-async-await.js
    │   │   ├── binance-fetch-ohlcv-many-symbols-promise-then-callbacks.js
    │   │   ├── binance-fetchTicker-delivery-vs-future.js
    │   │   ├── binance-futures-transfer-from-sub-account-to-master.js
    │   │   ├── binance-margin-stop-order.js
    │   │   ├── binance-server-time.js
    │   │   ├── binance-universal-transfer.js
    │   │   ├── bitfinex-fetch-trades.js
    │   │   ├── bitfinex2-fetch-trades.js
    │   │   ├── bitmex-browser-cors-proxy.js
    │   │   ├── bitpanda-fetchMyTrades-reduce.js
    │   │   ├── bitrue-fetch-balance.js
    │   │   ├── bitstamp-private-api.js
    │   │   ├── bitstamp-public-api.js
    │   │   ├── bittrex-balance.js
    │   │   ├── bittrex-fetch-closed-orders-history.js
    │   │   ├── blockchaincom-withdrawal.js
    │   │   ├── build-ohlcv-bars.js
    │   │   ├── builtin-rate-limiting-rest-poller.js
    │   │   ├── bybit-trailing.js
    │   │   ├── bybit-updated.cjs
    │   │   ├── cli.js
    │   │   ├── coinbase-fetch-all-balances.js
    │   │   ├── coinex-fetch-all-deposit-addresses-using-fetchDepositAddress.js
    │   │   ├── coinex-futures.js
    │   │   ├── coinone-fetch-tickers.js
    │   │   ├── coinone-markets.js
    │   │   ├── compare-two-exchanges-capabilities.js
    │   │   ├── cors-proxy.js
    │   │   ├── create-order-handle-errors.js
    │   │   ├── create-order-position-with-takeprofit-stoploss.js
    │   │   ├── create-order-with-retry.js
    │   │   ├── create-order-ws-example.js
    │   │   ├── create-orders-example.js
    │   │   ├── create-trailing-amount-order.js
    │   │   ├── create-trailing-percent-order.js
    │   │   ├── credentials.json
    │   │   ├── custom-proxy-agent-for-js.js
    │   │   ├── custom-proxy-url.js
    │   │   ├── delta-maintenance-margin-rate-max-leverage.js
    │   │   ├── env-variables.js
    │   │   ├── error-handling.js
    │   │   ├── exchange-capabilities.js
    │   │   ├── exchanges-by-volume.js
    │   │   ├── exchanges.js
    │   │   ├── fetch-all-balances.js
    │   │   ├── fetch-all-tickers-to-files-2.js
    │   │   ├── fetch-all-tickers-to-files.js
    │   │   ├── fetch-balance.js
    │   │   ├── fetch-create-deposit-address.js
    │   │   ├── fetch-from-many-exchanges-simultaneously.js
    │   │   ├── fetch-funding-rate-history.js
    │   │   ├── fetch-ohlcv-from-to-mark-index-premium.js
    │   │   ├── fetch-ohlcv-many-exchanges-continuosly.js
    │   │   ├── fetch-ohlcv.js
    │   │   ├── fetch-okex-futures.js
    │   │   ├── fetch-orders.js
    │   │   ├── fetch-ticker-from-multiple-exchanges.js
    │   │   ├── fetch-ticker-where-available.js
    │   │   ├── gateio-create-batch-order.js
    │   │   ├── gateio-futures.js
    │   │   ├── gateio-open-close-contract.js
    │   │   ├── gateio-swaps.js
    │   │   ├── gdax-fetch-trades-pagination.js
    │   │   ├── hitbtc2-withdraw.js
    │   │   ├── how-to-import-one-exchange-esm.js
    │   │   ├── huobi-futures.js
    │   │   ├── huobi-open-close-contract.js
    │   │   ├── huobi-swaps.js
    │   │   ├── huobipro-market-buy-sell-fetch-trading-limits.js
    │   │   ├── hybridCJSExample.cjs
    │   │   ├── hybridESMExample.js
    │   │   ├── idex-fetch-balance.js
    │   │   ├── instantiate-all-at-once.js
    │   │   ├── instantiate-all-from-json.js
    │   │   ├── kraken-create-and-close-position.js
    │   │   ├── kraken-fetch-order-trades.js
    │   │   ├── kraken-margin-trading.js
    │   │   ├── kucoin-rate-limit.js
    │   │   ├── latoken-example.js
    │   │   ├── live-orderbook.js
    │   │   ├── live-ticker.js
    │   │   ├── live-tickers.js
    │   │   ├── load-all-contracts.js
    │   │   ├── load-all-symbols-at-once.js
    │   │   ├── load-all-tickers-at-once.js
    │   │   ├── load-markets-to-files.js
    │   │   ├── looping-over-all-symbols-of-specific-exchanges.js
    │   │   ├── looping-over-specific-symbols-of-all-exchanges.js
    │   │   ├── margin-loan-borrow-buy-sell-repay.js
    │   │   ├── market-status-and-currency-status.js
    │   │   ├── ohlcv-console-chart.js
    │   │   ├── okex-fetch-closed-orders-archive.js
    │   │   ├── okex-transfer.js
    │   │   ├── okx-poll-fetch-my-trades.js
    │   │   ├── okx-poll-rate-limit.js
    │   │   ├── order-book-extra-level-depth-param.js
    │   │   ├── phemex-create-order-position-with-takeprofit-stoploss.js
    │   │   ├── poll-ohlcv.js
    │   │   ├── poloniex-fetch-order-books.js
    │   │   ├── poloniex-limits-amount-min.js
    │   │   ├── proxy-round-robin.js
    │   │   ├── proxy-usage.js
    │   │   ├── sample-local-proxy-server-with-cors.js
    │   │   ├── search-all-exchanges.js
    │   │   ├── shared-load-markets.js
    │   │   ├── sort-swap-markets-by-hourly-price-change.js
    │   │   ├── symbols.js
    │   │   ├── theocean.js
    │   │   ├── tickers.js
    │   │   ├── validate-paginated-data.js
    │   │   ├── watch-OHLCV-For-Symbols.js
    │   │   ├── watch-OHLCV.js
    │   │   ├── watch-OrderBook-For-Symbols.js
    │   │   ├── watch-Trades-For-Symbols.js
    │   │   ├── watch-tickers.js
    │   │   ├── watchOHLCVForSymbols.js
    │   │   ├── watchOrderBookForSymbols.js
    │   │   ├── watchPositions-many-exchanges-continuosly.d.ts
    │   │   ├── watchPositions-many-exchanges-continuosly.js
    │   │   ├── watchPositions.d.ts
    │   │   ├── watchPositions.js
    │   │   ├── watchPositionsForSymbols.d.ts
    │   │   ├── watchPositionsForSymbols.js
    │   │   ├── watchTradesForSymbols.js
    │   │   ├── withdraw-from-one-exchange-to-another.js
    │   │   ├── fetch-futures/
    │   │   │   ├── prettier.config.js
    │   │   │   └── src/
    │   │   │       └── index.js
    │   │   └── fetch-tickers/
    │   │       ├── prettier.config.js
    │   │       ├── build/
    │   │       │   └── index.js
    │   │       └── src/
    │   │           └── index.js
    │   ├── php/
    │   │   ├── README.md
    │   │   ├── arbitrage-pairs.php
    │   │   ├── async-await-fetch-multiple.php
    │   │   ├── async-await-fetch.php
    │   │   ├── basic-error-handling.php
    │   │   ├── basic-order.php
    │   │   ├── binance-create-order-stop-loss-take-profit.php
    │   │   ├── binance-fetch-all-trades-for-all-traded-symbols.php
    │   │   ├── binance-oco-order.php
    │   │   ├── binance-set-futures-leverage.php
    │   │   ├── binance-spot-trailing.php
    │   │   ├── bitfinex2-fetch-ohlcv-since-limit.php
    │   │   ├── bitfinex2-fetch-ohlcv.php
    │   │   ├── bitfinex2-fetch-trades-since.php
    │   │   ├── bitmex-create-order.php
    │   │   ├── build-ohlcv-bars.php
    │   │   ├── built-in-rate-limiting-poller.php
    │   │   ├── bybit-updated.php
    │   │   ├── bytetrade-create-order.php
    │   │   ├── cache-exchange-instance-reuse.php
    │   │   ├── cancel-order.php
    │   │   ├── cli.php
    │   │   ├── coinbase-fetch-all-balances.php
    │   │   ├── coinbasepro-cursor-pagination.php
    │   │   ├── coinone-markets.php
    │   │   ├── compare-two-exchanges-capabilities.php
    │   │   ├── create-order-position-with-takeprofit-stoploss.php
    │   │   ├── create-order-ws-example.php
    │   │   ├── create-orders-example.php
    │   │   ├── create-trailing-amount-order.php
    │   │   ├── create-trailing-percent-order.php
    │   │   ├── error-handling-message.php
    │   │   ├── exchange-properties.php
    │   │   ├── fetch-balance.php
    │   │   ├── fetch-ohlcv-many-exchanges-continuosly.php
    │   │   ├── fetch-ohlcv.php
    │   │   ├── fetch-order.php
    │   │   ├── fetch-ticker.php
    │   │   ├── fetch-tickers.php
    │   │   ├── gateio-futures.php
    │   │   ├── gateio-swaps.php
    │   │   ├── huobi-fetch-balance.php
    │   │   ├── huobi-futures.php
    │   │   ├── huobi-swaps.php
    │   │   ├── indodax-fetch-balance-create-order-cancel-order.php
    │   │   ├── kraken-create-and-close-position.php
    │   │   ├── kraken-query-ledgers.php
    │   │   ├── kucoin-fetch-all-deposit-addresses.php
    │   │   ├── kucoin-implicit-inner-transfer-v1.php
    │   │   ├── latoken-example.php
    │   │   ├── load-all-at-once-async.php
    │   │   ├── load-all-at-once.php
    │   │   ├── margin-loan-borrow-buy-sell-repay.php
    │   │   ├── method-overload-override.php
    │   │   ├── nonce-override.php
    │   │   ├── order-book-level-depth-extra-param.php
    │   │   ├── phemex-create-order-position-with-takeprofit-stoploss.php
    │   │   ├── proxy-usage.php
    │   │   ├── react-eventloop-with-rate-limiting.php
    │   │   ├── sample-local-proxy-server-with-cors.php
    │   │   ├── shared-markets.php
    │   │   ├── symbols.php
    │   │   ├── trading-view.php
    │   │   ├── watch-OHLCV-For-Symbols.php
    │   │   ├── watch-OHLCV.php
    │   │   ├── watch-OrderBook-For-Symbols.php
    │   │   ├── watch-Trades-For-Symbols.php
    │   │   ├── watch-tickers.php
    │   │   ├── watchOHLCVForSymbols.php
    │   │   ├── watchOrderBookForSymbols.php
    │   │   ├── watchPositions-many-exchanges-continuosly.php
    │   │   ├── watchPositions.php
    │   │   ├── watchPositionsForSymbols.php
    │   │   └── watchTradesForSymbols.php
    │   ├── py/
    │   │   ├── README.md
    │   │   ├── all-exchanges.py
    │   │   ├── arbitrage-pairs.py
    │   │   ├── asciichart.py
    │   │   ├── async-analyse-augur-v1-vs-v2-exchanges.py
    │   │   ├── async-balance-coinbasepro.py
    │   │   ├── async-balance-gdax.py
    │   │   ├── async-balance.py
    │   │   ├── async-balances.py
    │   │   ├── async-basic-callchain.py
    │   │   ├── async-basic-orderbook.py
    │   │   ├── async-basic-rate-limiter.py
    │   │   ├── async-basic.py
    │   │   ├── async-binance-cancel-option-order.py
    │   │   ├── async-binance-create-margin-order.py
    │   │   ├── async-binance-create-option-order.py
    │   │   ├── async-binance-create-trailing-percent-order.py
    │   │   ├── async-binance-fetch-margin-balance-with-options.py
    │   │   ├── async-binance-fetch-margin-balance-with-params.py
    │   │   ├── async-binance-fetch-option-OHLCV.py
    │   │   ├── async-binance-fetch-option-details.py
    │   │   ├── async-binance-fetch-option-order.py
    │   │   ├── async-binance-fetch-option-orderbook.py
    │   │   ├── async-binance-fetch-option-position.py
    │   │   ├── async-binance-fetch-option-ticker.py
    │   │   ├── async-binance-fetch-ticker-continuously.py
    │   │   ├── async-binance-futures-vs-spot.py
    │   │   ├── async-binance-margin-borrow.py
    │   │   ├── async-binance-margin-repay.py
    │   │   ├── async-binance-usdm-fetch-continuous-klines-ohlcv.py
    │   │   ├── async-bitfinex-public-get-symbols.py
    │   │   ├── async-bitget-perpetual-futures-swaps.py
    │   │   ├── async-bitstamp-create-limit-buy-order.py
    │   │   ├── async-bitstamp-create-order-cancel-order.py
    │   │   ├── async-bittrex-orderbook.py
    │   │   ├── async-bybit-transfer.py
    │   │   ├── async-fetch-balance.py
    │   │   ├── async-fetch-many-orderbooks-continuously.py
    │   │   ├── async-fetch-ohlcv-indicators-discord-webhook.py
    │   │   ├── async-fetch-ohlcv-multiple-symbols-continuously.py
    │   │   ├── async-fetch-order-book-from-many-exchanges.py
    │   │   ├── async-fetch-ticker.py
    │   │   ├── async-gather-concurrency.py
    │   │   ├── async-gdax-fetch-order-book-continuously.py
    │   │   ├── async-generator-basic.py
    │   │   ├── async-generator-multiple-tickers.py
    │   │   ├── async-generator-ticker-poller.py
    │   │   ├── async-hollaex-sandbox.py
    │   │   ├── async-instantiate-all-at-once.py
    │   │   ├── async-kucoin-rate-limit.py
    │   │   ├── async-macd.py
    │   │   ├── async-market-making-symbols.py
    │   │   ├── async-multiple-accounts.py
    │   │   ├── async-multiple-parallel-calls.py
    │   │   ├── async-okx-create-margin-order.py
    │   │   ├── async-okx-margin-borrow.py
    │   │   ├── async-okx-margin-repay.py
    │   │   ├── async-okx-positional-orders.py
    │   │   ├── async-orderbooks-from-multiple-exchanges-at-once.py
    │   │   ├── async-orderbooks.py
    │   │   ├── async-rtt.py
    │   │   ├── async-theocean-orderbook.py
    │   │   ├── async-theocean-tickers.py
    │   │   ├── async-ticker.py
    │   │   ├── async-tickers-from-many-exchanges-at-once.py
    │   │   ├── async-tickers.py
    │   │   ├── async-with-threads.py
    │   │   ├── async.py
    │   │   ├── balance-coinbasepro.py
    │   │   ├── balance-gdax.py
    │   │   ├── balance-kraken.py
    │   │   ├── balances.py
    │   │   ├── basic-chart.py
    │   │   ├── basic-rate-limiting.py
    │   │   ├── binance-batch-orders.py
    │   │   ├── binance-coin-margined-take-profit.py
    │   │   ├── binance-conditional-orders.py
    │   │   ├── binance-create-oco-order-with-implicit-methods.py
    │   │   ├── binance-ema.py
    │   │   ├── binance-fetch-all-my-trades-paginate-by-id.py
    │   │   ├── binance-fetch-all-my-trades.py
    │   │   ├── binance-fetch-all-trades.py
    │   │   ├── binance-fetch-ohlcv-closing-time-1.py
    │   │   ├── binance-fetch-ohlcv-closing-time-2.py
    │   │   ├── binance-fetch-ohlcv-pagination.py
    │   │   ├── binance-fetch-ohlcv-quote-volume.py
    │   │   ├── binance-fetch-ohlcv-to-csv.py
    │   │   ├── binance-fetch-ohlcv.py
    │   │   ├── binance-fiat.py
    │   │   ├── binance-futures-margin.py
    │   │   ├── binance-futures-positions.py
    │   │   ├── binance-futures-set-leverage-implicit-api.py
    │   │   ├── binance-futures-set-leverage.py
    │   │   ├── binance-market-order-quote-usdt.py
    │   │   ├── binance-poll-balance.py
    │   │   ├── binance-poll-positions.py
    │   │   ├── binance-savings-endpoints.py
    │   │   ├── binance-spot-trailing.py
    │   │   ├── binance-stop-loss-take-profit.py
    │   │   ├── binance-test-order.py
    │   │   ├── binance-universal-transfer.py
    │   │   ├── binance-usdm-fetch-continuous-klines-ohlcv.py
    │   │   ├── bitfinex-rate-limiting.py
    │   │   ├── bitget-perpetual-futures-swaps.py
    │   │   ├── bitmex-cancel-orders.py
    │   │   ├── bitmex-create-order.py
    │   │   ├── bitmex-fetch-ohlcv-with-extra-params.py
    │   │   ├── bitmex-ohlcv-convert-5m-to-15m.py
    │   │   ├── bitmex-order-value.py
    │   │   ├── bittrex-fetch-closed-orders-history.py
    │   │   ├── build-ohlcv-bars.py
    │   │   ├── builtin-rate-limiting-long-poller.py
    │   │   ├── bybit-USDC-create-option-order.py
    │   │   ├── bybit-conditional-orders.py
    │   │   ├── bybit-positions.py
    │   │   ├── bybit-trailling.py
    │   │   ├── bybit-updated.py
    │   │   ├── cli.py
    │   │   ├── coinbase-cancel-order.py
    │   │   ├── coinbase-create-order.py
    │   │   ├── coinbase-fetch-OHLCV.py
    │   │   ├── coinbase-fetch-order.py
    │   │   ├── coinbase-fetch-ticker.py
    │   │   ├── coinbase-fetch-trades.py
    │   │   ├── coinbasepro-fetch-my-trades-pagination.py
    │   │   ├── coinex-futures.py
    │   │   ├── coinone-fetch-tickers.py
    │   │   ├── coinone-markets.py
    │   │   ├── compare-two-exchanges-capabilities.py
    │   │   ├── create-order-position-with-takeprofit-stoploss.py
    │   │   ├── create-order-ws-example.py
    │   │   ├── create-orders-example.py
    │   │   ├── create-trailing-amount-order.py
    │   │   ├── create-trailing-percent-order.py
    │   │   ├── exchange-save-load-markets-cache.py
    │   │   ├── exchanges-by-country.py
    │   │   ├── exchanges.py
    │   │   ├── fetch-all-okex-ohclv.py
    │   │   ├── fetch-all-tickers.py
    │   │   ├── fetch-balance-asset-valuation.py
    │   │   ├── fetch-bitfinex-ohlcv-history.py
    │   │   ├── fetch-coinbasepro-ohlcv-sequentially.py
    │   │   ├── fetch-create-deposit-address.py
    │   │   ├── fetch-gdax-ohlcv-sequentially.py
    │   │   ├── fetch-ohlcv-cex.py
    │   │   ├── fetch-ohlcv-kraken.py
    │   │   ├── fetch-ohlcv-many-exchanges-continuosly.py
    │   │   ├── fetch-ohlcv-mark-index-price.py
    │   │   ├── fetch-ohlcv-on-new-candle.py
    │   │   ├── fetch-ohlcv-sequentially.py
    │   │   ├── fetch-ohlcv.py
    │   │   ├── fetch-okex-futures.py
    │   │   ├── fetch-open-orders.py
    │   │   ├── fetch-order-book-rtt.py
    │   │   ├── fetch-orders.py
    │   │   ├── fetch-ticker-many-exchanges-many-symbols.py
    │   │   ├── fetch_longer_ohlcv_through_multiple_calls_and_save_to_csv.py
    │   │   ├── gateio-fetch-ohlcv-pagination.py
    │   │   ├── gateio-futures.py
    │   │   ├── gateio-open-close-contract.py
    │   │   ├── gateio-swaps.py
    │   │   ├── gdax-fetch-my-trades-pagination.py
    │   │   ├── hitbtc-withdraw.py
    │   │   ├── huobi-futures.py
    │   │   ├── huobi-open-close-contract.py
    │   │   ├── huobi-open-close-position-bbo.py
    │   │   ├── huobi-spot.py
    │   │   ├── huobi-swaps.py
    │   │   ├── instantiate-all-at-once.py
    │   │   ├── kraken-conditional-close-order.py
    │   │   ├── kraken-create-and-close-position.py
    │   │   ├── kraken-fetch-my-trades-pagination.py
    │   │   ├── krakenfutures-basic.py
    │   │   ├── kucoin-fetch-all-deposit-addresses-by-network.py
    │   │   ├── kucoin-fetch-all-deposit-addresses.py
    │   │   ├── kucoin-fetch-closed-orders-pagination.py
    │   │   ├── kucoin-rate-limit.py
    │   │   ├── kucoin-withdraw-chain.py
    │   │   ├── kucoinfutures-create-stop-order.py
    │   │   ├── latoken-create-order.py
    │   │   ├── latoken-example.py
    │   │   ├── manual-rate-limiting-long-poller.py
    │   │   ├── margin-leverage-order-kraken.py
    │   │   ├── margin-loan-borrow-buy-sell-repay.py
    │   │   ├── measure-latency.py
    │   │   ├── minimal-2-lines.py
    │   │   ├── multiple-subscriptions-watchXForSymbols.py
    │   │   ├── normalize-sparse-candle-timestamps.py
    │   │   ├── okx-fetch-all-my-trades.py
    │   │   ├── okx-fetch-closed-orders-pagenumber-pagination.py
    │   │   ├── okx-position-takeprofit-stoploss.py
    │   │   ├── okx-transfer.py
    │   │   ├── order-book-extra-level-depth-param.py
    │   │   ├── phemex-create-order-position-with-takeprofit-stoploss.py
    │   │   ├── phemex-create-stop-order.py
    │   │   ├── phemex-leverage-orders.py
    │   │   ├── phemex-open-cancel-close-positions.py
    │   │   ├── phemex-perpetual-balance.py
    │   │   ├── phemex-positions.py
    │   │   ├── phemex-transfer.py
    │   │   ├── playing_with_ccxt_example.ipynb
    │   │   ├── poloniex-fetch-ohlcv-continuously.py
    │   │   ├── poloniex-fetch-ohlcv-with-pagination.py
    │   │   ├── poloniex-fetch-order-books.py
    │   │   ├── poloniex-fetch-trades-continuously.py
    │   │   ├── poloniex-fetch-trades-with-pagination-to-csv.py
    │   │   ├── poloniex-python2-memleak-test.py
    │   │   ├── poloniex-python3-memleak-test.py
    │   │   ├── proxies-for-synchronous-python.py
    │   │   ├── proxy-asyncio-aiohttp-python-3.py
    │   │   ├── proxy-asyncio-aiohttp-socks.py
    │   │   ├── proxy-sync-python-requests-2-and-3.py
    │   │   ├── proxy-usage.py
    │   │   ├── rsi.py
    │   │   ├── rtt.py
    │   │   ├── sample-local-proxy-server-with-cors.py
    │   │   ├── sign-in.py
    │   │   ├── sort-swap-markets-by-hourly-price-change.py
    │   │   ├── source-ip-address.py
    │   │   ├── symbols.py
    │   │   ├── test-server.py
    │   │   ├── theocean.py
    │   │   ├── tickers.py
    │   │   ├── watch-OHLCV-For-Symbols.py
    │   │   ├── watch-OHLCV.py
    │   │   ├── watch-OrderBook-For-Symbols.py
    │   │   ├── watch-Trades-For-Symbols.py
    │   │   ├── watch-tickers.py
    │   │   ├── watchOHLCVForSymbols.py
    │   │   ├── watchOrderBookForSymbols.py
    │   │   ├── watchPositions-many-exchanges-continuosly.py
    │   │   ├── watchPositions.py
    │   │   ├── watchPositionsForSymbols.py
    │   │   ├── watchTradesForSymbols.py
    │   │   ├── wazirx-create-cancel-orders.py
    │   │   └── withdraw-from-one-exchange-to-another.py
    │   └── ts/
    │       ├── benchmark.ts
    │       ├── build-ohlcv-bars.ts
    │       ├── cli.ts
    │       ├── compare-two-exchanges-capabilities.ts
    │       ├── create-order-position-with-takeprofit-stoploss.ts
    │       ├── create-order-ws-example.ts
    │       ├── create-orders-example.ts
    │       ├── create-trailing-amount-order.ts
    │       ├── create-trailing-percent-order.ts
    │       ├── custom-proxy-agent-for-js.ts
    │       ├── fetch-ohlcv-many-exchanges-continuosly.ts
    │       ├── fetch-ohlcv.ts
    │       ├── how-to-import-one-exchange-esm.ts
    │       ├── kraken-create-and-close-position.ts
    │       ├── margin-loan-borrow-buy-sell-repay.ts
    │       ├── phemex-create-order-position-with-takeprofit-stoploss.ts
    │       ├── proxy-usage.ts
    │       ├── sample-local-proxy-server-with-cors.ts
    │       ├── watch-OHLCV-For-Symbols.ts
    │       ├── watch-OHLCV.ts
    │       ├── watch-OrderBook-For-Symbols.ts
    │       ├── watch-Trades-For-Symbols.ts
    │       ├── watch-tickers.ts
    │       ├── watchPositions-many-exchanges-continuosly.ts
    │       ├── watchPositions.ts
    │       ├── watchPositionsForSymbols.ts
    │       ├── .eslintrc
    │       ├── fetch-futures/
    │       │   ├── package-lock.json
    │       │   ├── package.json
    │       │   ├── prettier.config.js
    │       │   ├── tsconfig.json
    │       │   ├── .gitignore
    │       │   └── src/
    │       │       └── index.ts
    │       ├── fetch-tickers/
    │       │   ├── package-lock.json
    │       │   ├── package.json
    │       │   ├── prettier.config.js
    │       │   ├── tsconfig.json
    │       │   ├── .gitignore
    │       │   └── src/
    │       │       └── index.ts
    │       └── nextjs-page-router/
    │           ├── README.md
    │           ├── next.config.js
    │           ├── package-lock.json
    │           ├── package.json
    │           ├── postcss.config.js
    │           ├── tailwind.config.ts
    │           ├── tsconfig.json
    │           ├── .eslintrc.json
    │           ├── .gitignore
    │           ├── public/
    │           └── src/
    │               ├── pages/
    │               │   ├── _app.tsx
    │               │   ├── _document.tsx
    │               │   ├── balance.tsx
    │               │   ├── index.tsx
    │               │   └── tickers.tsx
    │               └── styles/
    │                   └── globals.css
    ├── go/
    │   ├── go.work
    │   ├── go.work.sum
    │   ├── cli/
    │   │   ├── go.mod
    │   │   ├── go.sum
    │   │   ├── main.go
    │   │   └── bench/
    │   │       ├── markets.json
    │   │       ├── ohlcv.json
    │   │       ├── orderbook.json
    │   │       ├── tickers.json
    │   │       └── trades.json
    │   ├── tests/
    │   │   ├── go.mod
    │   │   ├── main.go
    │   │   ├── out.txt
    │   │   ├── output.txt
    │   │   ├── base/
    │   │   │   ├── go.mod
    │   │   │   ├── helpers.go
    │   │   │   ├── test.account.go
    │   │   │   ├── test.afterConstructor.go
    │   │   │   ├── test.balance.go
    │   │   │   ├── test.borrowInterest.go
    │   │   │   ├── test.borrowRate.go
    │   │   │   ├── test.cryptography.go
    │   │   │   ├── test.currency.go
    │   │   │   ├── test.datetime.go
    │   │   │   ├── test.deepExtend.go
    │   │   │   ├── test.depositWithdrawal.go
    │   │   │   ├── test.extend.go
    │   │   │   ├── test.features.go
    │   │   │   ├── test.fetchAccounts.go
    │   │   │   ├── test.fetchBalance.go
    │   │   │   ├── test.fetchBorrowInterest.go
    │   │   │   ├── test.fetchClosedOrders.go
    │   │   │   ├── test.fetchCurrencies.go
    │   │   │   ├── test.fetchDepositWithdrawals.go
    │   │   │   ├── test.fetchDeposits.go
    │   │   │   ├── test.fetchFundingRateHistory.go
    │   │   │   ├── test.fetchL2OrderBook.go
    │   │   │   ├── test.fetchLedger.go
    │   │   │   ├── test.fetchLedgerEntry.go
    │   │   │   ├── test.fetchLeverageTiers.go
    │   │   │   ├── test.fetchLiquidations.go
    │   │   │   ├── test.fetchMarginMode.go
    │   │   │   ├── test.fetchMarginModes.go
    │   │   │   ├── test.fetchMarketLeverageTiers.go
    │   │   │   ├── test.fetchMarkets.go
    │   │   │   ├── test.fetchMyLiquidations.go
    │   │   │   ├── test.fetchMyTrades.go
    │   │   │   ├── test.fetchOHLCV.go
    │   │   │   ├── test.fetchOpenInterestHistory.go
    │   │   │   ├── test.fetchOpenOrders.go
    │   │   │   ├── test.fetchOrderBook.go
    │   │   │   ├── test.fetchOrderBooks.go
    │   │   │   ├── test.fetchOrders.go
    │   │   │   ├── test.fetchPositions.go
    │   │   │   ├── test.fetchStatus.go
    │   │   │   ├── test.fetchTicker.go
    │   │   │   ├── test.fetchTickers.go
    │   │   │   ├── test.fetchTrades.go
    │   │   │   ├── test.fetchTradingFee.go
    │   │   │   ├── test.fetchTradingFees.go
    │   │   │   ├── test.fetchTransactionFees.go
    │   │   │   ├── test.fetchWithdrawals.go
    │   │   │   ├── test.filterBy.go
    │   │   │   ├── test.functions.go
    │   │   │   ├── test.fundingRateHistory.go
    │   │   │   ├── test.groupBy.go
    │   │   │   ├── test.helpers.go
    │   │   │   ├── test.json.go
    │   │   │   ├── test.languageSpecific.go
    │   │   │   ├── test.lastPrice.go
    │   │   │   ├── test.ledgerEntry.go
    │   │   │   ├── test.leverageTier.go
    │   │   │   ├── test.liquidation.go
    │   │   │   ├── test.loadMarkets.go
    │   │   │   ├── test.marginMode.go
    │   │   │   ├── test.marginModification.go
    │   │   │   ├── test.market.go
    │   │   │   ├── test.number.go
    │   │   │   ├── test.ohlcv.go
    │   │   │   ├── test.omit.go
    │   │   │   ├── test.openInterest.go
    │   │   │   ├── test.order.go
    │   │   │   ├── test.orderBook.go
    │   │   │   ├── test.position.go
    │   │   │   ├── test.safeMethods.go
    │   │   │   ├── test.sharedMethods.go
    │   │   │   ├── test.signIn.go
    │   │   │   ├── test.sortBy.go
    │   │   │   ├── test.status.go
    │   │   │   ├── test.sum.go
    │   │   │   ├── test.ticker.go
    │   │   │   ├── test.trade.go
    │   │   │   ├── test.tradingFee.go
    │   │   │   ├── tests.go
    │   │   │   ├── tests.init.go
    │   │   │   └── utils.go
    │   │   ├── profile/
    │   │   │   ├── README
    │   │   │   ├── go.mod
    │   │   │   ├── go.sum
    │   │   │   └── profile.go
    │   │   └── types/
    │   │       ├── go.mod
    │   │       ├── go.sum
    │   │       ├── types.go
    │   │       └── static/
    │   │           ├── balance.json
    │   │           ├── ohlcv.json
    │   │           ├── orderbook.json
    │   │           ├── orders.json
    │   │           ├── positions.json
    │   │           ├── tickers.json
    │   │           └── trades.json
    │   └── v4/
    │       ├── LICENSE
    │       ├── ace.go
    │       ├── ace_api.go
    │       ├── ace_wrapper.go
    │       ├── alpaca.go
    │       ├── alpaca_api.go
    │       ├── alpaca_wrapper.go
    │       ├── ascendex.go
    │       ├── ascendex_api.go
    │       ├── ascendex_wrapper.go
    │       ├── bequant.go
    │       ├── bequant_api.go
    │       ├── bequant_wrapper.go
    │       ├── bigone.go
    │       ├── bigone_api.go
    │       ├── bigone_wrapper.go
    │       ├── binance.go
    │       ├── binance_api.go
    │       ├── binance_wrapper.go
    │       ├── binancecoinm.go
    │       ├── binancecoinm_api.go
    │       ├── binancecoinm_wrapper.go
    │       ├── binanceus.go
    │       ├── binanceus_api.go
    │       ├── binanceus_wrapper.go
    │       ├── binanceusdm.go
    │       ├── binanceusdm_api.go
    │       ├── binanceusdm_wrapper.go
    │       ├── bingx.go
    │       ├── bingx_api.go
    │       ├── bingx_wrapper.go
    │       ├── bit2c.go
    │       ├── bit2c_api.go
    │       ├── bit2c_wrapper.go
    │       ├── bitbank.go
    │       ├── bitbank_api.go
    │       ├── bitbank_wrapper.go
    │       ├── bitbns.go
    │       ├── bitbns_api.go
    │       ├── bitbns_wrapper.go
    │       ├── bitcoincom.go
    │       ├── bitcoincom_api.go
    │       ├── bitcoincom_wrapper.go
    │       ├── bitfinex.go
    │       ├── bitfinex1.go
    │       ├── bitfinex1_api.go
    │       ├── bitfinex1_wrapper.go
    │       ├── bitfinex_api.go
    │       ├── bitfinex_wrapper.go
    │       ├── bitflyer.go
    │       ├── bitflyer_api.go
    │       ├── bitflyer_wrapper.go
    │       ├── bitget.go
    │       ├── bitget_api.go
    │       ├── bitget_wrapper.go
    │       ├── bithumb.go
    │       ├── bithumb_api.go
    │       ├── bithumb_wrapper.go
    │       ├── bitmart.go
    │       ├── bitmart_api.go
    │       ├── bitmart_wrapper.go
    │       ├── bitmex.go
    │       ├── bitmex_api.go
    │       ├── bitmex_wrapper.go
    │       ├── bitopro.go
    │       ├── bitopro_api.go
    │       ├── bitopro_wrapper.go
    │       ├── bitpanda.go
    │       ├── bitpanda_api.go
    │       ├── bitpanda_wrapper.go
    │       ├── bitrue.go
    │       ├── bitrue_api.go
    │       ├── bitrue_wrapper.go
    │       ├── bitso.go
    │       ├── bitso_api.go
    │       ├── bitso_wrapper.go
    │       ├── bitstamp.go
    │       ├── bitstamp_api.go
    │       ├── bitstamp_wrapper.go
    │       ├── bitteam.go
    │       ├── bitteam_api.go
    │       ├── bitteam_wrapper.go
    │       ├── bitvavo.go
    │       ├── bitvavo_api.go
    │       ├── bitvavo_wrapper.go
    │       ├── bl3p.go
    │       ├── bl3p_api.go
    │       ├── bl3p_wrapper.go
    │       ├── blockchaincom.go
    │       ├── blockchaincom_api.go
    │       ├── blockchaincom_wrapper.go
    │       ├── blofin.go
    │       ├── blofin_api.go
    │       ├── blofin_wrapper.go
    │       ├── btcalpha.go
    │       ├── btcalpha_api.go
    │       ├── btcalpha_wrapper.go
    │       ├── btcbox.go
    │       ├── btcbox_api.go
    │       ├── btcbox_wrapper.go
    │       ├── btcmarkets.go
    │       ├── btcmarkets_api.go
    │       ├── btcmarkets_wrapper.go
    │       ├── btcturk.go
    │       ├── btcturk_api.go
    │       ├── btcturk_wrapper.go
    │       ├── bybit.go
    │       ├── bybit_api.go
    │       ├── bybit_wrapper.go
    │       ├── cex.go
    │       ├── cex_api.go
    │       ├── cex_wrapper.go
    │       ├── coinbase.go
    │       ├── coinbase_api.go
    │       ├── coinbase_wrapper.go
    │       ├── coinbaseadvanced.go
    │       ├── coinbaseadvanced_api.go
    │       ├── coinbaseadvanced_wrapper.go
    │       ├── coinbaseexchange.go
    │       ├── coinbaseexchange_api.go
    │       ├── coinbaseexchange_wrapper.go
    │       ├── coinbaseinternational.go
    │       ├── coinbaseinternational_api.go
    │       ├── coinbaseinternational_wrapper.go
    │       ├── coincatch.go
    │       ├── coincatch_api.go
    │       ├── coincatch_wrapper.go
    │       ├── coincheck.go
    │       ├── coincheck_api.go
    │       ├── coincheck_wrapper.go
    │       ├── coinex.go
    │       ├── coinex_api.go
    │       ├── coinex_wrapper.go
    │       ├── coinlist.go
    │       ├── coinlist_api.go
    │       ├── coinlist_wrapper.go
    │       ├── coinmate.go
    │       ├── coinmate_api.go
    │       ├── coinmate_wrapper.go
    │       ├── coinmetro.go
    │       ├── coinmetro_api.go
    │       ├── coinmetro_wrapper.go
    │       ├── coinone.go
    │       ├── coinone_api.go
    │       ├── coinone_wrapper.go
    │       ├── coinsph.go
    │       ├── coinsph_api.go
    │       ├── coinsph_wrapper.go
    │       ├── coinspot.go
    │       ├── coinspot_api.go
    │       ├── coinspot_wrapper.go
    │       ├── cryptocom.go
    │       ├── cryptocom_api.go
    │       ├── cryptocom_wrapper.go
    │       ├── currencycom.go
    │       ├── currencycom_api.go
    │       ├── currencycom_wrapper.go
    │       ├── defx.go
    │       ├── defx_api.go
    │       ├── defx_wrapper.go
    │       ├── delta.go
    │       ├── delta_api.go
    │       ├── delta_wrapper.go
    │       ├── deribit.go
    │       ├── deribit_api.go
    │       ├── deribit_wrapper.go
    │       ├── digifinex.go
    │       ├── digifinex_api.go
    │       ├── digifinex_wrapper.go
    │       ├── ellipx.go
    │       ├── ellipx_api.go
    │       ├── ellipx_wrapper.go
    │       ├── exchange.go
    │       ├── exchange_client.go
    │       ├── exchange_crypto.go
    │       ├── exchange_crypto_256k1.go
    │       ├── exchange_dynamic.go
    │       ├── exchange_encode.go
    │       ├── exchange_errors.go
    │       ├── exchange_eth.go
    │       ├── exchange_functions.go
    │       ├── exchange_generated.go
    │       ├── exchange_generic.go
    │       ├── exchange_helpers.go
    │       ├── exchange_interface.go
    │       ├── exchange_metadata.go
    │       ├── exchange_misc.go
    │       ├── exchange_number.go
    │       ├── exchange_options.go
    │       ├── exchange_orderbookside.go
    │       ├── exchange_precise.go
    │       ├── exchange_queue.go
    │       ├── exchange_req.go
    │       ├── exchange_safe.go
    │       ├── exchange_set.go
    │       ├── exchange_string.go
    │       ├── exchange_throttler.go
    │       ├── exchange_time.go
    │       ├── exchange_types.go
    │       ├── exchange_wrapper_options.go
    │       ├── exchange_wrapper_structs.go
    │       ├── exmo.go
    │       ├── exmo_api.go
    │       ├── exmo_wrapper.go
    │       ├── fmfwio.go
    │       ├── fmfwio_api.go
    │       ├── fmfwio_wrapper.go
    │       ├── gate.go
    │       ├── gate_api.go
    │       ├── gate_wrapper.go
    │       ├── gateio.go
    │       ├── gateio_api.go
    │       ├── gateio_wrapper.go
    │       ├── gemini.go
    │       ├── gemini_api.go
    │       ├── gemini_wrapper.go
    │       ├── go.mod
    │       ├── go.sum
    │       ├── go.work
    │       ├── go.work.sum
    │       ├── hashkey.go
    │       ├── hashkey_api.go
    │       ├── hashkey_wrapper.go
    │       ├── hitbtc.go
    │       ├── hitbtc_api.go
    │       ├── hitbtc_wrapper.go
    │       ├── hollaex.go
    │       ├── hollaex_api.go
    │       ├── hollaex_wrapper.go
    │       ├── htx.go
    │       ├── htx_api.go
    │       ├── htx_wrapper.go
    │       ├── huobi.go
    │       ├── huobi_api.go
    │       ├── huobi_wrapper.go
    │       ├── huobijp.go
    │       ├── huobijp_api.go
    │       ├── huobijp_wrapper.go
    │       ├── hyperliquid.go
    │       ├── hyperliquid_api.go
    │       ├── hyperliquid_wrapper.go
    │       ├── idex.go
    │       ├── idex_api.go
    │       ├── idex_wrapper.go
    │       ├── independentreserve.go
    │       ├── independentreserve_api.go
    │       ├── independentreserve_wrapper.go
    │       ├── indodax.go
    │       ├── indodax_api.go
    │       ├── indodax_wrapper.go
    │       ├── kraken.go
    │       ├── kraken_api.go
    │       ├── kraken_wrapper.go
    │       ├── krakenfutures.go
    │       ├── krakenfutures_api.go
    │       ├── krakenfutures_wrapper.go
    │       ├── kucoin.go
    │       ├── kucoin_api.go
    │       ├── kucoin_wrapper.go
    │       ├── kucoinfutures.go
    │       ├── kucoinfutures_api.go
    │       ├── kucoinfutures_wrapper.go
    │       ├── kuna.go
    │       ├── kuna_api.go
    │       ├── kuna_wrapper.go
    │       ├── latoken.go
    │       ├── latoken_api.go
    │       ├── latoken_wrapper.go
    │       ├── lbank.go
    │       ├── lbank_api.go
    │       ├── lbank_wrapper.go
    │       ├── luno.go
    │       ├── luno_api.go
    │       ├── luno_wrapper.go
    │       ├── mercado.go
    │       ├── mercado_api.go
    │       ├── mercado_wrapper.go
    │       ├── mexc.go
    │       ├── mexc_api.go
    │       ├── mexc_wrapper.go
    │       ├── myokx.go
    │       ├── myokx_api.go
    │       ├── myokx_wrapper.go
    │       ├── ndax.go
    │       ├── ndax_api.go
    │       ├── ndax_wrapper.go
    │       ├── novadax.go
    │       ├── novadax_api.go
    │       ├── novadax_wrapper.go
    │       ├── oceanex.go
    │       ├── oceanex_api.go
    │       ├── oceanex_wrapper.go
    │       ├── okcoin.go
    │       ├── okcoin_api.go
    │       ├── okcoin_wrapper.go
    │       ├── okx.go
    │       ├── okx_api.go
    │       ├── okx_wrapper.go
    │       ├── onetrading.go
    │       ├── onetrading_api.go
    │       ├── onetrading_wrapper.go
    │       ├── oxfun.go
    │       ├── oxfun_api.go
    │       ├── oxfun_wrapper.go
    │       ├── p2b.go
    │       ├── p2b_api.go
    │       ├── p2b_wrapper.go
    │       ├── paradex.go
    │       ├── paradex_api.go
    │       ├── paradex_wrapper.go
    │       ├── paymium.go
    │       ├── paymium_api.go
    │       ├── paymium_wrapper.go
    │       ├── phemex.go
    │       ├── phemex_api.go
    │       ├── phemex_wrapper.go
    │       ├── poloniex.go
    │       ├── poloniex_api.go
    │       ├── poloniex_wrapper.go
    │       ├── poloniexfutures.go
    │       ├── poloniexfutures_api.go
    │       ├── poloniexfutures_wrapper.go
    │       ├── probit.go
    │       ├── probit_api.go
    │       ├── probit_wrapper.go
    │       ├── timex.go
    │       ├── timex_api.go
    │       ├── timex_wrapper.go
    │       ├── tokocrypto.go
    │       ├── tokocrypto_api.go
    │       ├── tokocrypto_wrapper.go
    │       ├── tradeogre.go
    │       ├── tradeogre_api.go
    │       ├── tradeogre_wrapper.go
    │       ├── upbit.go
    │       ├── upbit_api.go
    │       ├── upbit_wrapper.go
    │       ├── vertex.go
    │       ├── vertex_api.go
    │       ├── vertex_wrapper.go
    │       ├── wavesexchange.go
    │       ├── wavesexchange_api.go
    │       ├── wavesexchange_wrapper.go
    │       ├── wazirx.go
    │       ├── wazirx_api.go
    │       ├── wazirx_wrapper.go
    │       ├── whitebit.go
    │       ├── whitebit_api.go
    │       ├── whitebit_wrapper.go
    │       ├── woo.go
    │       ├── woo_api.go
    │       ├── woo_wrapper.go
    │       ├── woofipro.go
    │       ├── woofipro_api.go
    │       ├── woofipro_wrapper.go
    │       ├── xt.go
    │       ├── xt_api.go
    │       ├── xt_wrapper.go
    │       ├── yobit.go
    │       ├── yobit_api.go
    │       ├── yobit_wrapper.go
    │       ├── zaif.go
    │       ├── zaif_api.go
    │       ├── zaif_wrapper.go
    │       ├── zonda.go
    │       ├── zonda_api.go
    │       └── zonda_wrapper.go
    ├── js/
    │   ├── ccxt.d.ts
    │   ├── ccxt.js
    │   └── src/
    │       ├── ace.d.ts
    │       ├── ace.js
    │       ├── alpaca.d.ts
    │       ├── alpaca.js
    │       ├── ascendex.d.ts
    │       ├── ascendex.js
    │       ├── bequant.d.ts
    │       ├── bequant.js
    │       ├── bigone.d.ts
    │       ├── bigone.js
    │       ├── binance.d.ts
    │       ├── binance.js
    │       ├── binancecoinm.d.ts
    │       ├── binancecoinm.js
    │       ├── binanceus.d.ts
    │       ├── binanceus.js
    │       ├── binanceusdm.d.ts
    │       ├── binanceusdm.js
    │       ├── bingx.d.ts
    │       ├── bingx.js
    │       ├── bit2c.d.ts
    │       ├── bit2c.js
    │       ├── bitbank.d.ts
    │       ├── bitbank.js
    │       ├── bitbns.d.ts
    │       ├── bitbns.js
    │       ├── bitcoincom.d.ts
    │       ├── bitcoincom.js
    │       ├── bitfinex.d.ts
    │       ├── bitfinex.js
    │       ├── bitfinex1.d.ts
    │       ├── bitfinex1.js
    │       ├── bitflyer.d.ts
    │       ├── bitflyer.js
    │       ├── bitget.d.ts
    │       ├── bitget.js
    │       ├── bithumb.d.ts
    │       ├── bithumb.js
    │       ├── bitmart.d.ts
    │       ├── bitmart.js
    │       ├── bitmex.d.ts
    │       ├── bitmex.js
    │       ├── bitopro.d.ts
    │       ├── bitopro.js
    │       ├── bitpanda.d.ts
    │       ├── bitpanda.js
    │       ├── bitrue.d.ts
    │       ├── bitrue.js
    │       ├── bitso.d.ts
    │       ├── bitso.js
    │       ├── bitstamp.d.ts
    │       ├── bitstamp.js
    │       ├── bitteam.d.ts
    │       ├── bitteam.js
    │       ├── bitvavo.d.ts
    │       ├── bitvavo.js
    │       ├── bl3p.d.ts
    │       ├── bl3p.js
    │       ├── blockchaincom.d.ts
    │       ├── blockchaincom.js
    │       ├── blofin.d.ts
    │       ├── blofin.js
    │       ├── btcalpha.d.ts
    │       ├── btcalpha.js
    │       ├── btcbox.d.ts
    │       ├── btcbox.js
    │       ├── btcmarkets.d.ts
    │       ├── btcmarkets.js
    │       ├── btcturk.d.ts
    │       ├── btcturk.js
    │       ├── bybit.d.ts
    │       ├── bybit.js
    │       ├── cex.d.ts
    │       ├── cex.js
    │       ├── coinbase.d.ts
    │       ├── coinbase.js
    │       ├── coinbaseadvanced.d.ts
    │       ├── coinbaseadvanced.js
    │       ├── coinbaseexchange.d.ts
    │       ├── coinbaseexchange.js
    │       ├── coinbaseinternational.d.ts
    │       ├── coinbaseinternational.js
    │       ├── coincatch.d.ts
    │       ├── coincatch.js
    │       ├── coincheck.d.ts
    │       ├── coincheck.js
    │       ├── coinex.d.ts
    │       ├── coinex.js
    │       ├── coinlist.d.ts
    │       ├── coinlist.js
    │       ├── coinmate.d.ts
    │       ├── coinmate.js
    │       ├── coinmetro.d.ts
    │       ├── coinmetro.js
    │       ├── coinone.d.ts
    │       ├── coinone.js
    │       ├── coinsph.d.ts
    │       ├── coinsph.js
    │       ├── coinspot.d.ts
    │       ├── coinspot.js
    │       ├── cryptocom.d.ts
    │       ├── cryptocom.js
    │       ├── currencycom.d.ts
    │       ├── currencycom.js
    │       ├── defx.d.ts
    │       ├── defx.js
    │       ├── delta.d.ts
    │       ├── delta.js
    │       ├── deribit.d.ts
    │       ├── deribit.js
    │       ├── digifinex.d.ts
    │       ├── digifinex.js
    │       ├── ellipx.d.ts
    │       ├── ellipx.js
    │       ├── exmo.d.ts
    │       ├── exmo.js
    │       ├── fmfwio.d.ts
    │       ├── fmfwio.js
    │       ├── gate.d.ts
    │       ├── gate.js
    │       ├── gateio.d.ts
    │       ├── gateio.js
    │       ├── gemini.d.ts
    │       ├── gemini.js
    │       ├── hashkey.d.ts
    │       ├── hashkey.js
    │       ├── hitbtc.d.ts
    │       ├── hitbtc.js
    │       ├── hollaex.d.ts
    │       ├── hollaex.js
    │       ├── htx.d.ts
    │       ├── htx.js
    │       ├── huobi.d.ts
    │       ├── huobi.js
    │       ├── huobijp.d.ts
    │       ├── huobijp.js
    │       ├── hyperliquid.d.ts
    │       ├── hyperliquid.js
    │       ├── idex.d.ts
    │       ├── idex.js
    │       ├── independentreserve.d.ts
    │       ├── independentreserve.js
    │       ├── indodax.d.ts
    │       ├── indodax.js
    │       ├── kraken.d.ts
    │       ├── kraken.js
    │       ├── krakenfutures.d.ts
    │       ├── krakenfutures.js
    │       ├── kucoin.d.ts
    │       ├── kucoin.js
    │       ├── kucoinfutures.d.ts
    │       ├── kucoinfutures.js
    │       ├── kuna.d.ts
    │       ├── kuna.js
    │       ├── latoken.d.ts
    │       ├── latoken.js
    │       ├── lbank.d.ts
    │       ├── lbank.js
    │       ├── luno.d.ts
    │       ├── luno.js
    │       ├── mercado.d.ts
    │       ├── mercado.js
    │       ├── mexc.d.ts
    │       ├── mexc.js
    │       ├── myokx.d.ts
    │       ├── myokx.js
    │       ├── ndax.d.ts
    │       ├── ndax.js
    │       ├── novadax.d.ts
    │       ├── novadax.js
    │       ├── oceanex.d.ts
    │       ├── oceanex.js
    │       ├── okcoin.d.ts
    │       ├── okcoin.js
    │       ├── okx.d.ts
    │       ├── okx.js
    │       ├── onetrading.d.ts
    │       ├── onetrading.js
    │       ├── oxfun.d.ts
    │       ├── oxfun.js
    │       ├── p2b.d.ts
    │       ├── p2b.js
    │       ├── paradex.d.ts
    │       ├── paradex.js
    │       ├── paymium.d.ts
    │       ├── paymium.js
    │       ├── phemex.d.ts
    │       ├── phemex.js
    │       ├── poloniex.d.ts
    │       ├── poloniex.js
    │       ├── poloniexfutures.d.ts
    │       ├── poloniexfutures.js
    │       ├── probit.d.ts
    │       ├── probit.js
    │       ├── timex.d.ts
    │       ├── timex.js
    │       ├── tokocrypto.d.ts
    │       ├── tokocrypto.js
    │       ├── tradeogre.d.ts
    │       ├── tradeogre.js
    │       ├── upbit.d.ts
    │       ├── upbit.js
    │       ├── vertex.d.ts
    │       ├── vertex.js
    │       ├── wavesexchange.d.ts
    │       ├── wavesexchange.js
    │       ├── whitebit.d.ts
    │       ├── whitebit.js
    │       ├── woo.d.ts
    │       ├── woo.js
    │       ├── woofipro.d.ts
    │       ├── woofipro.js
    │       ├── xt.d.ts
    │       ├── xt.js
    │       ├── yobit.d.ts
    │       ├── yobit.js
    │       ├── zaif.d.ts
    │       ├── zaif.js
    │       ├── zonda.d.ts
    │       ├── zonda.js
    │       ├── abstract/
    │       │   ├── ace.d.ts
    │       │   ├── ace.js
    │       │   ├── alpaca.d.ts
    │       │   ├── alpaca.js
    │       │   ├── ascendex.d.ts
    │       │   ├── ascendex.js
    │       │   ├── bequant.d.ts
    │       │   ├── bequant.js
    │       │   ├── bigone.d.ts
    │       │   ├── bigone.js
    │       │   ├── binance.d.ts
    │       │   ├── binance.js
    │       │   ├── binancecoinm.d.ts
    │       │   ├── binancecoinm.js
    │       │   ├── binanceus.d.ts
    │       │   ├── binanceus.js
    │       │   ├── binanceusdm.d.ts
    │       │   ├── binanceusdm.js
    │       │   ├── bingx.d.ts
    │       │   ├── bingx.js
    │       │   ├── bit2c.d.ts
    │       │   ├── bit2c.js
    │       │   ├── bitbank.d.ts
    │       │   ├── bitbank.js
    │       │   ├── bitbns.d.ts
    │       │   ├── bitbns.js
    │       │   ├── bitcoincom.d.ts
    │       │   ├── bitcoincom.js
    │       │   ├── bitfinex.d.ts
    │       │   ├── bitfinex.js
    │       │   ├── bitfinex1.d.ts
    │       │   ├── bitfinex1.js
    │       │   ├── bitflyer.d.ts
    │       │   ├── bitflyer.js
    │       │   ├── bitget.d.ts
    │       │   ├── bitget.js
    │       │   ├── bithumb.d.ts
    │       │   ├── bithumb.js
    │       │   ├── bitmart.d.ts
    │       │   ├── bitmart.js
    │       │   ├── bitmex.d.ts
    │       │   ├── bitmex.js
    │       │   ├── bitopro.d.ts
    │       │   ├── bitopro.js
    │       │   ├── bitpanda.d.ts
    │       │   ├── bitpanda.js
    │       │   ├── bitrue.d.ts
    │       │   ├── bitrue.js
    │       │   ├── bitso.d.ts
    │       │   ├── bitso.js
    │       │   ├── bitstamp.d.ts
    │       │   ├── bitstamp.js
    │       │   ├── bitteam.d.ts
    │       │   ├── bitteam.js
    │       │   ├── bitvavo.d.ts
    │       │   ├── bitvavo.js
    │       │   ├── bl3p.d.ts
    │       │   ├── bl3p.js
    │       │   ├── blockchaincom.d.ts
    │       │   ├── blockchaincom.js
    │       │   ├── blofin.d.ts
    │       │   ├── blofin.js
    │       │   ├── btcalpha.d.ts
    │       │   ├── btcalpha.js
    │       │   ├── btcbox.d.ts
    │       │   ├── btcbox.js
    │       │   ├── btcmarkets.d.ts
    │       │   ├── btcmarkets.js
    │       │   ├── btcturk.d.ts
    │       │   ├── btcturk.js
    │       │   ├── bybit.d.ts
    │       │   ├── bybit.js
    │       │   ├── cex.d.ts
    │       │   ├── cex.js
    │       │   ├── coinbase.d.ts
    │       │   ├── coinbase.js
    │       │   ├── coinbaseadvanced.d.ts
    │       │   ├── coinbaseadvanced.js
    │       │   ├── coinbaseexchange.d.ts
    │       │   ├── coinbaseexchange.js
    │       │   ├── coinbaseinternational.d.ts
    │       │   ├── coinbaseinternational.js
    │       │   ├── coincatch.d.ts
    │       │   ├── coincatch.js
    │       │   ├── coincheck.d.ts
    │       │   ├── coincheck.js
    │       │   ├── coinex.d.ts
    │       │   ├── coinex.js
    │       │   ├── coinlist.d.ts
    │       │   ├── coinlist.js
    │       │   ├── coinmate.d.ts
    │       │   ├── coinmate.js
    │       │   ├── coinmetro.d.ts
    │       │   ├── coinmetro.js
    │       │   ├── coinone.d.ts
    │       │   ├── coinone.js
    │       │   ├── coinsph.d.ts
    │       │   ├── coinsph.js
    │       │   ├── coinspot.d.ts
    │       │   ├── coinspot.js
    │       │   ├── cryptocom.d.ts
    │       │   ├── cryptocom.js
    │       │   ├── currencycom.d.ts
    │       │   ├── currencycom.js
    │       │   ├── defx.d.ts
    │       │   ├── defx.js
    │       │   ├── delta.d.ts
    │       │   ├── delta.js
    │       │   ├── deribit.d.ts
    │       │   ├── deribit.js
    │       │   ├── digifinex.d.ts
    │       │   ├── digifinex.js
    │       │   ├── ellipx.d.ts
    │       │   ├── ellipx.js
    │       │   ├── exmo.d.ts
    │       │   ├── exmo.js
    │       │   ├── fmfwio.d.ts
    │       │   ├── fmfwio.js
    │       │   ├── gate.d.ts
    │       │   ├── gate.js
    │       │   ├── gateio.d.ts
    │       │   ├── gateio.js
    │       │   ├── gemini.d.ts
    │       │   ├── gemini.js
    │       │   ├── hashkey.d.ts
    │       │   ├── hashkey.js
    │       │   ├── hitbtc.d.ts
    │       │   ├── hitbtc.js
    │       │   ├── hollaex.d.ts
    │       │   ├── hollaex.js
    │       │   ├── htx.d.ts
    │       │   ├── htx.js
    │       │   ├── huobi.d.ts
    │       │   ├── huobi.js
    │       │   ├── huobijp.d.ts
    │       │   ├── huobijp.js
    │       │   ├── hyperliquid.d.ts
    │       │   ├── hyperliquid.js
    │       │   ├── idex.d.ts
    │       │   ├── idex.js
    │       │   ├── independentreserve.d.ts
    │       │   ├── independentreserve.js
    │       │   ├── indodax.d.ts
    │       │   ├── indodax.js
    │       │   ├── kraken.d.ts
    │       │   ├── kraken.js
    │       │   ├── krakenfutures.d.ts
    │       │   ├── krakenfutures.js
    │       │   ├── kucoin.d.ts
    │       │   ├── kucoin.js
    │       │   ├── kucoinfutures.d.ts
    │       │   ├── kucoinfutures.js
    │       │   ├── kuna.d.ts
    │       │   ├── kuna.js
    │       │   ├── latoken.d.ts
    │       │   ├── latoken.js
    │       │   ├── lbank.d.ts
    │       │   ├── lbank.js
    │       │   ├── luno.d.ts
    │       │   ├── luno.js
    │       │   ├── mercado.d.ts
    │       │   ├── mercado.js
    │       │   ├── mexc.d.ts
    │       │   ├── mexc.js
    │       │   ├── myokx.d.ts
    │       │   ├── myokx.js
    │       │   ├── ndax.d.ts
    │       │   ├── ndax.js
    │       │   ├── novadax.d.ts
    │       │   ├── novadax.js
    │       │   ├── oceanex.d.ts
    │       │   ├── oceanex.js
    │       │   ├── okcoin.d.ts
    │       │   ├── okcoin.js
    │       │   ├── okx.d.ts
    │       │   ├── okx.js
    │       │   ├── onetrading.d.ts
    │       │   ├── onetrading.js
    │       │   ├── oxfun.d.ts
    │       │   ├── oxfun.js
    │       │   ├── p2b.d.ts
    │       │   ├── p2b.js
    │       │   ├── paradex.d.ts
    │       │   ├── paradex.js
    │       │   ├── paymium.d.ts
    │       │   ├── paymium.js
    │       │   ├── phemex.d.ts
    │       │   ├── phemex.js
    │       │   ├── poloniex.d.ts
    │       │   ├── poloniex.js
    │       │   ├── poloniexfutures.d.ts
    │       │   ├── poloniexfutures.js
    │       │   ├── probit.d.ts
    │       │   ├── probit.js
    │       │   ├── timex.d.ts
    │       │   ├── timex.js
    │       │   ├── tokocrypto.d.ts
    │       │   ├── tokocrypto.js
    │       │   ├── tradeogre.d.ts
    │       │   ├── tradeogre.js
    │       │   ├── upbit.d.ts
    │       │   ├── upbit.js
    │       │   ├── vertex.d.ts
    │       │   ├── vertex.js
    │       │   ├── wavesexchange.d.ts
    │       │   ├── wavesexchange.js
    │       │   ├── wazirx.d.ts
    │       │   ├── wazirx.js
    │       │   ├── whitebit.d.ts
    │       │   ├── whitebit.js
    │       │   ├── woo.d.ts
    │       │   ├── woo.js
    │       │   ├── woofipro.d.ts
    │       │   ├── woofipro.js
    │       │   ├── xt.d.ts
    │       │   ├── xt.js
    │       │   ├── yobit.d.ts
    │       │   ├── yobit.js
    │       │   ├── zaif.d.ts
    │       │   ├── zaif.js
    │       │   ├── zonda.d.ts
    │       │   └── zonda.js
    │       ├── base/
    │       │   ├── Exchange.d.ts
    │       │   ├── Exchange.js
    │       │   ├── Precise.d.ts
    │       │   ├── Precise.js
    │       │   ├── errorHierarchy.d.ts
    │       │   ├── errorHierarchy.js
    │       │   ├── errors.d.ts
    │       │   ├── errors.js
    │       │   ├── functions.d.ts
    │       │   ├── functions.js
    │       │   ├── types.d.ts
    │       │   ├── types.js
    │       │   ├── functions/
    │       │   │   ├── crypto.d.ts
    │       │   │   ├── crypto.js
    │       │   │   ├── encode.d.ts
    │       │   │   ├── encode.js
    │       │   │   ├── generic.d.ts
    │       │   │   ├── generic.js
    │       │   │   ├── misc.d.ts
    │       │   │   ├── misc.js
    │       │   │   ├── number.d.ts
    │       │   │   ├── number.js
    │       │   │   ├── platform.d.ts
    │       │   │   ├── platform.js
    │       │   │   ├── rsa.d.ts
    │       │   │   ├── rsa.js
    │       │   │   ├── string.d.ts
    │       │   │   ├── string.js
    │       │   │   ├── throttle.d.ts
    │       │   │   ├── throttle.js
    │       │   │   ├── time.d.ts
    │       │   │   ├── time.js
    │       │   │   ├── totp.d.ts
    │       │   │   ├── totp.js
    │       │   │   ├── type.d.ts
    │       │   │   └── type.js
    │       │   └── ws/
    │       │       ├── Cache.d.ts
    │       │       ├── Cache.js
    │       │       ├── Client.d.ts
    │       │       ├── Client.js
    │       │       ├── Future.d.ts
    │       │       ├── Future.js
    │       │       ├── OrderBook.d.ts
    │       │       ├── OrderBook.js
    │       │       ├── OrderBookSide.d.ts
    │       │       ├── OrderBookSide.js
    │       │       ├── WsClient.d.ts
    │       │       ├── WsClient.js
    │       │       ├── functions.d.ts
    │       │       └── functions.js
    │       ├── pro/
    │       │   ├── alpaca.d.ts
    │       │   ├── alpaca.js
    │       │   ├── ascendex.d.ts
    │       │   ├── ascendex.js
    │       │   ├── bequant.d.ts
    │       │   ├── bequant.js
    │       │   ├── binance.d.ts
    │       │   ├── binance.js
    │       │   ├── binancecoinm.d.ts
    │       │   ├── binancecoinm.js
    │       │   ├── binanceus.d.ts
    │       │   ├── binanceus.js
    │       │   ├── binanceusdm.d.ts
    │       │   ├── binanceusdm.js
    │       │   ├── bingx.d.ts
    │       │   ├── bingx.js
    │       │   ├── bitcoincom.d.ts
    │       │   ├── bitcoincom.js
    │       │   ├── bitfinex.d.ts
    │       │   ├── bitfinex.js
    │       │   ├── bitfinex1.d.ts
    │       │   ├── bitfinex1.js
    │       │   ├── bitfinex2.d.ts
    │       │   ├── bitfinex2.js
    │       │   ├── bitget.d.ts
    │       │   ├── bitget.js
    │       │   ├── bithumb.d.ts
    │       │   ├── bithumb.js
    │       │   ├── bitmart.d.ts
    │       │   ├── bitmart.js
    │       │   ├── bitmex.d.ts
    │       │   ├── bitmex.js
    │       │   ├── bitopro.d.ts
    │       │   ├── bitopro.js
    │       │   ├── bitpanda.d.ts
    │       │   ├── bitpanda.js
    │       │   ├── bitrue.d.ts
    │       │   ├── bitrue.js
    │       │   ├── bitstamp.d.ts
    │       │   ├── bitstamp.js
    │       │   ├── bitvavo.d.ts
    │       │   ├── bitvavo.js
    │       │   ├── blockchaincom.d.ts
    │       │   ├── blockchaincom.js
    │       │   ├── blofin.d.ts
    │       │   ├── blofin.js
    │       │   ├── bybit.d.ts
    │       │   ├── bybit.js
    │       │   ├── cex.d.ts
    │       │   ├── cex.js
    │       │   ├── coinbase.d.ts
    │       │   ├── coinbase.js
    │       │   ├── coinbaseadvanced.d.ts
    │       │   ├── coinbaseadvanced.js
    │       │   ├── coinbaseexchange.d.ts
    │       │   ├── coinbaseexchange.js
    │       │   ├── coinbaseinternational.d.ts
    │       │   ├── coinbaseinternational.js
    │       │   ├── coincatch.d.ts
    │       │   ├── coincatch.js
    │       │   ├── coincheck.d.ts
    │       │   ├── coincheck.js
    │       │   ├── coinex.d.ts
    │       │   ├── coinex.js
    │       │   ├── coinone.d.ts
    │       │   ├── coinone.js
    │       │   ├── cryptocom.d.ts
    │       │   ├── cryptocom.js
    │       │   ├── currencycom.d.ts
    │       │   ├── currencycom.js
    │       │   ├── defx.d.ts
    │       │   ├── defx.js
    │       │   ├── deribit.d.ts
    │       │   ├── deribit.js
    │       │   ├── exmo.d.ts
    │       │   ├── exmo.js
    │       │   ├── gate.d.ts
    │       │   ├── gate.js
    │       │   ├── gateio.d.ts
    │       │   ├── gateio.js
    │       │   ├── gemini.d.ts
    │       │   ├── gemini.js
    │       │   ├── hashkey.d.ts
    │       │   ├── hashkey.js
    │       │   ├── hitbtc.d.ts
    │       │   ├── hitbtc.js
    │       │   ├── hollaex.d.ts
    │       │   ├── hollaex.js
    │       │   ├── htx.d.ts
    │       │   ├── htx.js
    │       │   ├── huobi.d.ts
    │       │   ├── huobi.js
    │       │   ├── huobijp.d.ts
    │       │   ├── huobijp.js
    │       │   ├── hyperliquid.d.ts
    │       │   ├── hyperliquid.js
    │       │   ├── idex.d.ts
    │       │   ├── idex.js
    │       │   ├── independentreserve.d.ts
    │       │   ├── independentreserve.js
    │       │   ├── kraken.d.ts
    │       │   ├── kraken.js
    │       │   ├── krakenfutures.d.ts
    │       │   ├── krakenfutures.js
    │       │   ├── kucoin.d.ts
    │       │   ├── kucoin.js
    │       │   ├── kucoinfutures.d.ts
    │       │   ├── kucoinfutures.js
    │       │   ├── lbank.d.ts
    │       │   ├── lbank.js
    │       │   ├── luno.d.ts
    │       │   ├── luno.js
    │       │   ├── mexc.d.ts
    │       │   ├── mexc.js
    │       │   ├── myokx.d.ts
    │       │   ├── myokx.js
    │       │   ├── ndax.d.ts
    │       │   ├── ndax.js
    │       │   ├── okcoin.d.ts
    │       │   ├── okcoin.js
    │       │   ├── okx.d.ts
    │       │   ├── okx.js
    │       │   ├── onetrading.d.ts
    │       │   ├── onetrading.js
    │       │   ├── oxfun.d.ts
    │       │   ├── oxfun.js
    │       │   ├── p2b.d.ts
    │       │   ├── p2b.js
    │       │   ├── paradex.d.ts
    │       │   ├── paradex.js
    │       │   ├── phemex.d.ts
    │       │   ├── phemex.js
    │       │   ├── poloniex.d.ts
    │       │   ├── poloniex.js
    │       │   ├── poloniexfutures.d.ts
    │       │   ├── poloniexfutures.js
    │       │   ├── probit.d.ts
    │       │   ├── probit.js
    │       │   ├── upbit.d.ts
    │       │   ├── upbit.js
    │       │   ├── vertex.d.ts
    │       │   ├── vertex.js
    │       │   ├── wazirx.d.ts
    │       │   ├── wazirx.js
    │       │   ├── whitebit.d.ts
    │       │   ├── whitebit.js
    │       │   ├── woo.d.ts
    │       │   ├── woo.js
    │       │   ├── woofipro.d.ts
    │       │   ├── woofipro.js
    │       │   ├── xt.d.ts
    │       │   ├── xt.js
    │       │   └── test/
    │       │       ├── Exchange/
    │       │       │   ├── test.watchBalance.d.ts
    │       │       │   ├── test.watchBalance.js
    │       │       │   ├── test.watchBidsAsks.d.ts
    │       │       │   ├── test.watchBidsAsks.js
    │       │       │   ├── test.watchLiquidations.d.ts
    │       │       │   ├── test.watchLiquidations.js
    │       │       │   ├── test.watchLiquidationsForSymbols.d.ts
    │       │       │   ├── test.watchLiquidationsForSymbols.js
    │       │       │   ├── test.watchMyTrades.d.ts
    │       │       │   ├── test.watchMyTrades.js
    │       │       │   ├── test.watchOHLCV.d.ts
    │       │       │   ├── test.watchOHLCV.js
    │       │       │   ├── test.watchOHLCVForSymbols.d.ts
    │       │       │   ├── test.watchOHLCVForSymbols.js
    │       │       │   ├── test.watchOrderBook.d.ts
    │       │       │   ├── test.watchOrderBook.js
    │       │       │   ├── test.watchOrderBookForSymbols.d.ts
    │       │       │   ├── test.watchOrderBookForSymbols.js
    │       │       │   ├── test.watchOrders.d.ts
    │       │       │   ├── test.watchOrders.js
    │       │       │   ├── test.watchPosition.d.ts
    │       │       │   ├── test.watchPosition.js
    │       │       │   ├── test.watchPositions.d.ts
    │       │       │   ├── test.watchPositions.js
    │       │       │   ├── test.watchTicker.d.ts
    │       │       │   ├── test.watchTicker.js
    │       │       │   ├── test.watchTickers.d.ts
    │       │       │   ├── test.watchTickers.js
    │       │       │   ├── test.watchTrades.d.ts
    │       │       │   ├── test.watchTrades.js
    │       │       │   ├── test.watchTradesForSymbols.d.ts
    │       │       │   └── test.watchTradesForSymbols.js
    │       │       ├── base/
    │       │       │   ├── test.Cache.d.ts
    │       │       │   ├── test.Cache.js
    │       │       │   ├── test.OrderBook.d.ts
    │       │       │   ├── test.OrderBook.js
    │       │       │   ├── test.cache.d.ts
    │       │       │   ├── test.cache.js
    │       │       │   ├── test.client.resolve.d.ts
    │       │       │   ├── test.client.resolve.js
    │       │       │   ├── test.close.d.ts
    │       │       │   ├── test.close.js
    │       │       │   ├── test.orderBook.d.ts
    │       │       │   ├── test.orderBook.js
    │       │       │   ├── test.watchWithDelay.d.ts
    │       │       │   ├── test.watchWithDelay.js
    │       │       │   ├── tests.init.d.ts
    │       │       │   └── tests.init.js
    │       │       └── custom/
    │       │           ├── fastMessageServer.d.ts
    │       │           ├── fastMessageServer.js
    │       │           ├── server.d.ts
    │       │           └── server.js
    │       ├── static_dependencies/
    │       │   ├── ethers/
    │       │   │   ├── abi-coder.d.ts
    │       │   │   ├── abi-coder.js
    │       │   │   ├── bytes32.d.ts
    │       │   │   ├── bytes32.js
    │       │   │   ├── fragments.d.ts
    │       │   │   ├── fragments.js
    │       │   │   ├── index.d.ts
    │       │   │   ├── index.js
    │       │   │   ├── interface.d.ts
    │       │   │   ├── interface.js
    │       │   │   ├── typed.d.ts
    │       │   │   ├── typed.js
    │       │   │   ├── address/
    │       │   │   │   ├── address.d.ts
    │       │   │   │   ├── address.js
    │       │   │   │   ├── checks.d.ts
    │       │   │   │   ├── checks.js
    │       │   │   │   ├── contract-address.d.ts
    │       │   │   │   ├── contract-address.js
    │       │   │   │   ├── index.d.ts
    │       │   │   │   └── index.js
    │       │   │   ├── coders/
    │       │   │   │   ├── abstract-coder.d.ts
    │       │   │   │   ├── abstract-coder.js
    │       │   │   │   ├── address.d.ts
    │       │   │   │   ├── address.js
    │       │   │   │   ├── anonymous.d.ts
    │       │   │   │   ├── anonymous.js
    │       │   │   │   ├── array.d.ts
    │       │   │   │   ├── array.js
    │       │   │   │   ├── boolean.d.ts
    │       │   │   │   ├── boolean.js
    │       │   │   │   ├── bytes.d.ts
    │       │   │   │   ├── bytes.js
    │       │   │   │   ├── fixed-bytes.d.ts
    │       │   │   │   ├── fixed-bytes.js
    │       │   │   │   ├── null.d.ts
    │       │   │   │   ├── null.js
    │       │   │   │   ├── number.d.ts
    │       │   │   │   ├── number.js
    │       │   │   │   ├── string.d.ts
    │       │   │   │   ├── string.js
    │       │   │   │   ├── tuple.d.ts
    │       │   │   │   └── tuple.js
    │       │   │   ├── hash/
    │       │   │   │   ├── index.d.ts
    │       │   │   │   ├── index.js
    │       │   │   │   ├── solidity.d.ts
    │       │   │   │   ├── solidity.js
    │       │   │   │   ├── typed-data.d.ts
    │       │   │   │   └── typed-data.js
    │       │   │   └── utils/
    │       │   │       ├── base58.d.ts
    │       │   │       ├── base58.js
    │       │   │       ├── base64-browser.d.ts
    │       │   │       ├── base64-browser.js
    │       │   │       ├── base64.d.ts
    │       │   │       ├── base64.js
    │       │   │       ├── data.d.ts
    │       │   │       ├── data.js
    │       │   │       ├── errors.d.ts
    │       │   │       ├── errors.js
    │       │   │       ├── events.d.ts
    │       │   │       ├── events.js
    │       │   │       ├── fixednumber.d.ts
    │       │   │       ├── fixednumber.js
    │       │   │       ├── index.d.ts
    │       │   │       ├── index.js
    │       │   │       ├── maths.d.ts
    │       │   │       ├── maths.js
    │       │   │       ├── properties.d.ts
    │       │   │       ├── properties.js
    │       │   │       ├── rlp-decode.d.ts
    │       │   │       ├── rlp-decode.js
    │       │   │       ├── rlp-encode.d.ts
    │       │   │       ├── rlp-encode.js
    │       │   │       ├── rlp.d.ts
    │       │   │       ├── rlp.js
    │       │   │       ├── units.d.ts
    │       │   │       ├── units.js
    │       │   │       ├── utf8.d.ts
    │       │   │       ├── utf8.js
    │       │   │       ├── uuid.d.ts
    │       │   │       └── uuid.js
    │       │   ├── fflake/
    │       │   │   ├── browser.d.ts
    │       │   │   └── browser.js
    │       │   ├── jsencrypt/
    │       │   │   ├── JSEncrypt.d.ts
    │       │   │   ├── JSEncrypt.js
    │       │   │   ├── JSEncryptRSAKey.d.ts
    │       │   │   ├── JSEncryptRSAKey.js
    │       │   │   ├── index.d.ts
    │       │   │   ├── index.js
    │       │   │   └── lib/
    │       │   │       ├── asn1js/
    │       │   │       │   ├── asn1.d.ts
    │       │   │       │   ├── asn1.js
    │       │   │       │   ├── base64.d.ts
    │       │   │       │   ├── base64.js
    │       │   │       │   ├── hex.d.ts
    │       │   │       │   ├── hex.js
    │       │   │       │   ├── int10.d.ts
    │       │   │       │   ├── int10.js
    │       │   │       │   ├── oids.d.ts
    │       │   │       │   └── oids.js
    │       │   │       ├── jsbn/
    │       │   │       │   ├── base64.d.ts
    │       │   │       │   ├── base64.js
    │       │   │       │   ├── jsbn.d.ts
    │       │   │       │   ├── jsbn.js
    │       │   │       │   ├── prng4.d.ts
    │       │   │       │   ├── prng4.js
    │       │   │       │   ├── rng.d.ts
    │       │   │       │   ├── rng.js
    │       │   │       │   ├── rsa.d.ts
    │       │   │       │   ├── rsa.js
    │       │   │       │   ├── util.d.ts
    │       │   │       │   └── util.js
    │       │   │       └── jsrsasign/
    │       │   │           ├── asn1-1.0.d.ts
    │       │   │           ├── asn1-1.0.js
    │       │   │           ├── yahoo.d.ts
    │       │   │           └── yahoo.js
    │       │   ├── messagepack/
    │       │   │   ├── msgpack.d.ts
    │       │   │   └── msgpack.js
    │       │   ├── noble-curves/
    │       │   │   ├── _shortw_utils.d.ts
    │       │   │   ├── _shortw_utils.js
    │       │   │   ├── bn.d.ts
    │       │   │   ├── bn.js
    │       │   │   ├── ed25519.d.ts
    │       │   │   ├── ed25519.js
    │       │   │   ├── ed448.d.ts
    │       │   │   ├── ed448.js
    │       │   │   ├── index.d.ts
    │       │   │   ├── index.js
    │       │   │   ├── jubjub.d.ts
    │       │   │   ├── jubjub.js
    │       │   │   ├── p256.d.ts
    │       │   │   ├── p256.js
    │       │   │   ├── p384.d.ts
    │       │   │   ├── p384.js
    │       │   │   ├── p521.d.ts
    │       │   │   ├── p521.js
    │       │   │   ├── pasta.d.ts
    │       │   │   ├── pasta.js
    │       │   │   ├── secp256k1.d.ts
    │       │   │   ├── secp256k1.js
    │       │   │   └── abstract/
    │       │   │       ├── curve.d.ts
    │       │   │       ├── curve.js
    │       │   │       ├── edwards.d.ts
    │       │   │       ├── edwards.js
    │       │   │       ├── hash-to-curve.d.ts
    │       │   │       ├── hash-to-curve.js
    │       │   │       ├── modular.d.ts
    │       │   │       ├── modular.js
    │       │   │       ├── montgomery.d.ts
    │       │   │       ├── montgomery.js
    │       │   │       ├── poseidon.d.ts
    │       │   │       ├── poseidon.js
    │       │   │       ├── utils.d.ts
    │       │   │       ├── utils.js
    │       │   │       ├── weierstrass.d.ts
    │       │   │       └── weierstrass.js
    │       │   ├── noble-hashes/
    │       │   │   ├── _assert.d.ts
    │       │   │   ├── _assert.js
    │       │   │   ├── _blake2.d.ts
    │       │   │   ├── _blake2.js
    │       │   │   ├── _sha2.d.ts
    │       │   │   ├── _sha2.js
    │       │   │   ├── _u64.d.ts
    │       │   │   ├── _u64.js
    │       │   │   ├── argon2.d.ts
    │       │   │   ├── argon2.js
    │       │   │   ├── blake2b.d.ts
    │       │   │   ├── blake2b.js
    │       │   │   ├── blake2s.d.ts
    │       │   │   ├── blake2s.js
    │       │   │   ├── blake3.d.ts
    │       │   │   ├── blake3.js
    │       │   │   ├── crypto.d.ts
    │       │   │   ├── crypto.js
    │       │   │   ├── cryptoNode.d.ts
    │       │   │   ├── cryptoNode.js
    │       │   │   ├── eskdf.d.ts
    │       │   │   ├── eskdf.js
    │       │   │   ├── hkdf.d.ts
    │       │   │   ├── hkdf.js
    │       │   │   ├── hmac.d.ts
    │       │   │   ├── hmac.js
    │       │   │   ├── index.d.ts
    │       │   │   ├── index.js
    │       │   │   ├── md5.d.ts
    │       │   │   ├── md5.js
    │       │   │   ├── pbkdf2.d.ts
    │       │   │   ├── pbkdf2.js
    │       │   │   ├── ripemd160.d.ts
    │       │   │   ├── ripemd160.js
    │       │   │   ├── scrypt.d.ts
    │       │   │   ├── scrypt.js
    │       │   │   ├── sha1.d.ts
    │       │   │   ├── sha1.js
    │       │   │   ├── sha256.d.ts
    │       │   │   ├── sha256.js
    │       │   │   ├── sha3-addons.d.ts
    │       │   │   ├── sha3-addons.js
    │       │   │   ├── sha3.d.ts
    │       │   │   ├── sha3.js
    │       │   │   ├── sha512.d.ts
    │       │   │   ├── sha512.js
    │       │   │   ├── utils.d.ts
    │       │   │   └── utils.js
    │       │   ├── node-fetch/
    │       │   │   ├── body.d.ts
    │       │   │   ├── body.js
    │       │   │   ├── headers.d.ts
    │       │   │   ├── headers.js
    │       │   │   ├── index.d.ts
    │       │   │   ├── index.js
    │       │   │   ├── request.d.ts
    │       │   │   ├── request.js
    │       │   │   ├── response.d.ts
    │       │   │   ├── response.js
    │       │   │   ├── errors/
    │       │   │   │   ├── abort-error.d.ts
    │       │   │   │   ├── abort-error.js
    │       │   │   │   ├── base.d.ts
    │       │   │   │   ├── base.js
    │       │   │   │   ├── fetch-error.d.ts
    │       │   │   │   └── fetch-error.js
    │       │   │   └── utils/
    │       │   │       ├── get-search.d.ts
    │       │   │       ├── get-search.js
    │       │   │       ├── is-redirect.d.ts
    │       │   │       ├── is-redirect.js
    │       │   │       ├── is.d.ts
    │       │   │       ├── is.js
    │       │   │       ├── referrer.d.ts
    │       │   │       └── referrer.js
    │       │   ├── proxies/
    │       │   │   ├── agent-base/
    │       │   │   │   ├── helpers.d.ts
    │       │   │   │   ├── helpers.js
    │       │   │   │   ├── index.d.ts
    │       │   │   │   └── index.js
    │       │   │   ├── http-proxy-agent/
    │       │   │   │   ├── index.d.ts
    │       │   │   │   └── index.js
    │       │   │   └── https-proxy-agent/
    │       │   │       ├── index.d.ts
    │       │   │       ├── index.js
    │       │   │       ├── parse-proxy-response.d.ts
    │       │   │       └── parse-proxy-response.js
    │       │   ├── qs/
    │       │   │   ├── formats.cjs
    │       │   │   ├── formats.d.cts
    │       │   │   ├── index.cjs
    │       │   │   ├── index.d.cts
    │       │   │   ├── parse.cjs
    │       │   │   ├── parse.d.cts
    │       │   │   ├── stringify.cjs
    │       │   │   ├── stringify.d.cts
    │       │   │   ├── utils.cjs
    │       │   │   └── utils.d.cts
    │       │   ├── scure-base/
    │       │   │   ├── index.d.ts
    │       │   │   └── index.js
    │       │   ├── scure-starknet/
    │       │   │   ├── index.d.ts
    │       │   │   └── index.js
    │       │   ├── starknet/
    │       │   │   ├── constants.d.ts
    │       │   │   ├── constants.js
    │       │   │   ├── index.d.ts
    │       │   │   ├── index.js
    │       │   │   ├── types/
    │       │   │   │   ├── cairoEnum.d.ts
    │       │   │   │   ├── cairoEnum.js
    │       │   │   │   ├── calldata.d.ts
    │       │   │   │   ├── calldata.js
    │       │   │   │   ├── index.d.ts
    │       │   │   │   ├── index.js
    │       │   │   │   ├── typedData.d.ts
    │       │   │   │   ├── typedData.js
    │       │   │   │   └── lib/
    │       │   │   │       ├── index.d.ts
    │       │   │   │       ├── index.js
    │       │   │   │       └── contract/
    │       │   │   │           ├── abi.d.ts
    │       │   │   │           ├── abi.js
    │       │   │   │           ├── index.d.ts
    │       │   │   │           ├── index.js
    │       │   │   │           ├── legacy.d.ts
    │       │   │   │           ├── legacy.js
    │       │   │   │           ├── sierra.d.ts
    │       │   │   │           └── sierra.js
    │       │   │   └── utils/
    │       │   │       ├── address.d.ts
    │       │   │       ├── address.js
    │       │   │       ├── assert.d.ts
    │       │   │       ├── assert.js
    │       │   │       ├── encode.d.ts
    │       │   │       ├── encode.js
    │       │   │       ├── json.d.ts
    │       │   │       ├── json.js
    │       │   │       ├── merkle.d.ts
    │       │   │       ├── merkle.js
    │       │   │       ├── num.d.ts
    │       │   │       ├── num.js
    │       │   │       ├── selector.d.ts
    │       │   │       ├── selector.js
    │       │   │       ├── shortString.d.ts
    │       │   │       ├── shortString.js
    │       │   │       ├── starknetId.d.ts
    │       │   │       ├── starknetId.js
    │       │   │       ├── typedData.d.ts
    │       │   │       ├── typedData.js
    │       │   │       ├── uint256.d.ts
    │       │   │       ├── uint256.js
    │       │   │       ├── url.d.ts
    │       │   │       ├── url.js
    │       │   │       ├── cairoDataTypes/
    │       │   │       │   ├── felt.d.ts
    │       │   │       │   ├── felt.js
    │       │   │       │   ├── uint256.d.ts
    │       │   │       │   ├── uint256.js
    │       │   │       │   ├── uint512.d.ts
    │       │   │       │   └── uint512.js
    │       │   │       ├── calldata/
    │       │   │       │   ├── byteArray.d.ts
    │       │   │       │   ├── byteArray.js
    │       │   │       │   ├── cairo.d.ts
    │       │   │       │   ├── cairo.js
    │       │   │       │   ├── formatter.d.ts
    │       │   │       │   ├── formatter.js
    │       │   │       │   ├── index.d.ts
    │       │   │       │   ├── index.js
    │       │   │       │   ├── propertyOrder.d.ts
    │       │   │       │   ├── propertyOrder.js
    │       │   │       │   ├── requestParser.d.ts
    │       │   │       │   ├── requestParser.js
    │       │   │       │   ├── responseParser.d.ts
    │       │   │       │   ├── responseParser.js
    │       │   │       │   ├── tuple.d.ts
    │       │   │       │   ├── tuple.js
    │       │   │       │   ├── validate.d.ts
    │       │   │       │   ├── validate.js
    │       │   │       │   ├── enum/
    │       │   │       │   │   ├── CairoCustomEnum.d.ts
    │       │   │       │   │   ├── CairoCustomEnum.js
    │       │   │       │   │   ├── CairoOption.d.ts
    │       │   │       │   │   ├── CairoOption.js
    │       │   │       │   │   ├── CairoResult.d.ts
    │       │   │       │   │   ├── CairoResult.js
    │       │   │       │   │   ├── index.d.ts
    │       │   │       │   │   └── index.js
    │       │   │       │   └── parser/
    │       │   │       │       ├── index.d.ts
    │       │   │       │       ├── index.js
    │       │   │       │       ├── interface.d.ts
    │       │   │       │       ├── interface.js
    │       │   │       │       ├── parser-0-1.1.0.d.ts
    │       │   │       │       ├── parser-0-1.1.0.js
    │       │   │       │       ├── parser-2.0.0.d.ts
    │       │   │       │       └── parser-2.0.0.js
    │       │   │       └── hash/
    │       │   │           ├── classHash.d.ts
    │       │   │           ├── classHash.js
    │       │   │           ├── index.d.ts
    │       │   │           └── index.js
    │       │   └── watchable/
    │       │       └── src/
    │       │           ├── index.d.ts
    │       │           ├── index.js
    │       │           ├── types.d.ts
    │       │           ├── types.js
    │       │           ├── unpromise.d.ts
    │       │           └── unpromise.js
    │       └── test/
    │           ├── test.d.ts
    │           ├── test.js
    │           ├── tests.d.ts
    │           ├── tests.helpers.d.ts
    │           ├── tests.helpers.js
    │           ├── tests.init.d.ts
    │           ├── tests.init.js
    │           ├── tests.js
    │           ├── Exchange/
    │           │   ├── exportTests.d.ts
    │           │   ├── exportTests.js
    │           │   ├── test.account.d.ts
    │           │   ├── test.account.js
    │           │   ├── test.balance.d.ts
    │           │   ├── test.balance.js
    │           │   ├── test.borrowRate.d.ts
    │           │   ├── test.borrowRate.js
    │           │   ├── test.createOrder.d.ts
    │           │   ├── test.createOrder.js
    │           │   ├── test.currency.d.ts
    │           │   ├── test.currency.js
    │           │   ├── test.features.d.ts
    │           │   ├── test.features.js
    │           │   ├── test.fetchAccounts.d.ts
    │           │   ├── test.fetchAccounts.js
    │           │   ├── test.fetchBalance.d.ts
    │           │   ├── test.fetchBalance.js
    │           │   ├── test.fetchBorrowInterest.d.ts
    │           │   ├── test.fetchBorrowInterest.js
    │           │   ├── test.fetchBorrowRate.d.ts
    │           │   ├── test.fetchBorrowRate.js
    │           │   ├── test.fetchBorrowRates.d.ts
    │           │   ├── test.fetchBorrowRates.js
    │           │   ├── test.fetchClosedOrders.d.ts
    │           │   ├── test.fetchClosedOrders.js
    │           │   ├── test.fetchCurrencies.d.ts
    │           │   ├── test.fetchCurrencies.js
    │           │   ├── test.fetchDepositWithdrawals.d.ts
    │           │   ├── test.fetchDepositWithdrawals.js
    │           │   ├── test.fetchDeposits.d.ts
    │           │   ├── test.fetchDeposits.js
    │           │   ├── test.fetchFundingRateHistory.d.ts
    │           │   ├── test.fetchFundingRateHistory.js
    │           │   ├── test.fetchL2OrderBook.d.ts
    │           │   ├── test.fetchL2OrderBook.js
    │           │   ├── test.fetchLastPrices.d.ts
    │           │   ├── test.fetchLastPrices.js
    │           │   ├── test.fetchLedger.d.ts
    │           │   ├── test.fetchLedger.js
    │           │   ├── test.fetchLedgerEntry.d.ts
    │           │   ├── test.fetchLedgerEntry.js
    │           │   ├── test.fetchLeverageTiers.d.ts
    │           │   ├── test.fetchLeverageTiers.js
    │           │   ├── test.fetchLiquidations.d.ts
    │           │   ├── test.fetchLiquidations.js
    │           │   ├── test.fetchMarginMode.d.ts
    │           │   ├── test.fetchMarginMode.js
    │           │   ├── test.fetchMarginModes.d.ts
    │           │   ├── test.fetchMarginModes.js
    │           │   ├── test.fetchMarketLeverageTiers.d.ts
    │           │   ├── test.fetchMarketLeverageTiers.js
    │           │   ├── test.fetchMarkets.d.ts
    │           │   ├── test.fetchMarkets.js
    │           │   ├── test.fetchMyLiquidations.d.ts
    │           │   ├── test.fetchMyLiquidations.js
    │           │   ├── test.fetchMyTrades.d.ts
    │           │   ├── test.fetchMyTrades.js
    │           │   ├── test.fetchOHLCV.d.ts
    │           │   ├── test.fetchOHLCV.js
    │           │   ├── test.fetchOpenInterestHistory.d.ts
    │           │   ├── test.fetchOpenInterestHistory.js
    │           │   ├── test.fetchOpenOrders.d.ts
    │           │   ├── test.fetchOpenOrders.js
    │           │   ├── test.fetchOrderBook.d.ts
    │           │   ├── test.fetchOrderBook.js
    │           │   ├── test.fetchOrderBooks.d.ts
    │           │   ├── test.fetchOrderBooks.js
    │           │   ├── test.fetchOrders.d.ts
    │           │   ├── test.fetchOrders.js
    │           │   ├── test.fetchPositions.d.ts
    │           │   ├── test.fetchPositions.js
    │           │   ├── test.fetchStatus.d.ts
    │           │   ├── test.fetchStatus.js
    │           │   ├── test.fetchTicker.d.ts
    │           │   ├── test.fetchTicker.js
    │           │   ├── test.fetchTickers.d.ts
    │           │   ├── test.fetchTickers.js
    │           │   ├── test.fetchTrades.d.ts
    │           │   ├── test.fetchTrades.js
    │           │   ├── test.fetchTradingFee.d.ts
    │           │   ├── test.fetchTradingFee.js
    │           │   ├── test.fetchTradingFees.d.ts
    │           │   ├── test.fetchTradingFees.js
    │           │   ├── test.fetchTransactionFees.d.ts
    │           │   ├── test.fetchTransactionFees.js
    │           │   ├── test.fetchTransactions.d.ts
    │           │   ├── test.fetchTransactions.js
    │           │   ├── test.fetchWithdrawals.d.ts
    │           │   ├── test.fetchWithdrawals.js
    │           │   ├── test.ledgerItem.d.ts
    │           │   ├── test.ledgerItem.js
    │           │   ├── test.leverageTier.d.ts
    │           │   ├── test.leverageTier.js
    │           │   ├── test.loadMarkets.d.ts
    │           │   ├── test.loadMarkets.js
    │           │   ├── test.marginModification.d.ts
    │           │   ├── test.marginModification.js
    │           │   ├── test.market.d.ts
    │           │   ├── test.market.js
    │           │   ├── test.ohlcv.d.ts
    │           │   ├── test.ohlcv.js
    │           │   ├── test.openInterest.d.ts
    │           │   ├── test.openInterest.js
    │           │   ├── test.order.d.ts
    │           │   ├── test.order.js
    │           │   ├── test.orderbook.d.ts
    │           │   ├── test.orderbook.js
    │           │   ├── test.position.d.ts
    │           │   ├── test.position.js
    │           │   ├── test.proxies.d.ts
    │           │   ├── test.proxies.js
    │           │   ├── test.signIn.d.ts
    │           │   ├── test.signIn.js
    │           │   ├── test.throttle.d.ts
    │           │   ├── test.throttle.js
    │           │   ├── test.ticker.d.ts
    │           │   ├── test.ticker.js
    │           │   ├── test.trade.d.ts
    │           │   ├── test.trade.js
    │           │   ├── test.tradingFee.d.ts
    │           │   ├── test.tradingFee.js
    │           │   ├── test.transaction.d.ts
    │           │   ├── test.transaction.js
    │           │   └── base/
    │           │       ├── test.account.d.ts
    │           │       ├── test.account.js
    │           │       ├── test.balance.d.ts
    │           │       ├── test.balance.js
    │           │       ├── test.borrowInterest.d.ts
    │           │       ├── test.borrowInterest.js
    │           │       ├── test.borrowRate.d.ts
    │           │       ├── test.borrowRate.js
    │           │       ├── test.currency.d.ts
    │           │       ├── test.currency.js
    │           │       ├── test.depositWithdrawal.d.ts
    │           │       ├── test.depositWithdrawal.js
    │           │       ├── test.fundingRateHistory.d.ts
    │           │       ├── test.fundingRateHistory.js
    │           │       ├── test.lastPrice.d.ts
    │           │       ├── test.lastPrice.js
    │           │       ├── test.ledgerEntry.d.ts
    │           │       ├── test.ledgerEntry.js
    │           │       ├── test.ledgerItem.d.ts
    │           │       ├── test.ledgerItem.js
    │           │       ├── test.leverageTier.d.ts
    │           │       ├── test.leverageTier.js
    │           │       ├── test.liquidation.d.ts
    │           │       ├── test.liquidation.js
    │           │       ├── test.marginMode.d.ts
    │           │       ├── test.marginMode.js
    │           │       ├── test.marginModification.d.ts
    │           │       ├── test.marginModification.js
    │           │       ├── test.market.d.ts
    │           │       ├── test.market.js
    │           │       ├── test.ohlcv.d.ts
    │           │       ├── test.ohlcv.js
    │           │       ├── test.openInterest.d.ts
    │           │       ├── test.openInterest.js
    │           │       ├── test.order.d.ts
    │           │       ├── test.order.js
    │           │       ├── test.orderBook.d.ts
    │           │       ├── test.orderBook.js
    │           │       ├── test.position.d.ts
    │           │       ├── test.position.js
    │           │       ├── test.sharedMethods.d.ts
    │           │       ├── test.sharedMethods.js
    │           │       ├── test.status.d.ts
    │           │       ├── test.status.js
    │           │       ├── test.throttle.d.ts
    │           │       ├── test.throttle.js
    │           │       ├── test.ticker.d.ts
    │           │       ├── test.ticker.js
    │           │       ├── test.trade.d.ts
    │           │       ├── test.trade.js
    │           │       ├── test.tradingFee.d.ts
    │           │       └── test.tradingFee.js
    │           ├── base/
    │           │   ├── test.afterConstructor.d.ts
    │           │   ├── test.afterConstructor.js
    │           │   ├── test.aggregate.d.ts
    │           │   ├── test.aggregate.js
    │           │   ├── test.base.d.ts
    │           │   ├── test.base.js
    │           │   ├── test.calculateFee.d.ts
    │           │   ├── test.calculateFee.js
    │           │   ├── test.camelcase.d.ts
    │           │   ├── test.camelcase.js
    │           │   ├── test.config.d.ts
    │           │   ├── test.config.js
    │           │   ├── test.cryptography.d.ts
    │           │   ├── test.cryptography.js
    │           │   ├── test.datetime.d.ts
    │           │   ├── test.datetime.js
    │           │   ├── test.deepExtend.d.ts
    │           │   ├── test.deepExtend.js
    │           │   ├── test.extend.d.ts
    │           │   ├── test.extend.js
    │           │   ├── test.filterBy.d.ts
    │           │   ├── test.filterBy.js
    │           │   ├── test.generic.d.ts
    │           │   ├── test.generic.js
    │           │   ├── test.groupBy.d.ts
    │           │   ├── test.groupBy.js
    │           │   ├── test.json.d.ts
    │           │   ├── test.json.js
    │           │   ├── test.languageSpecific.d.ts
    │           │   ├── test.languageSpecific.js
    │           │   ├── test.legacyHas.d.ts
    │           │   ├── test.legacyHas.js
    │           │   ├── test.number.d.ts
    │           │   ├── test.number.js
    │           │   ├── test.omit.d.ts
    │           │   ├── test.omit.js
    │           │   ├── test.safeBalance.d.ts
    │           │   ├── test.safeBalance.js
    │           │   ├── test.safeMethods.d.ts
    │           │   ├── test.safeMethods.js
    │           │   ├── test.sortBy.d.ts
    │           │   ├── test.sortBy.js
    │           │   ├── test.sum.d.ts
    │           │   ├── test.sum.js
    │           │   ├── test.throttle.d.ts
    │           │   ├── test.throttle.js
    │           │   ├── test.time.d.ts
    │           │   ├── test.time.js
    │           │   ├── test.timeout_hang.d.ts
    │           │   ├── test.timeout_hang.js
    │           │   ├── test.type.d.ts
    │           │   ├── test.type.js
    │           │   ├── test.uncamelcase.d.ts
    │           │   ├── test.uncamelcase.js
    │           │   ├── tests.init.d.ts
    │           │   ├── tests.init.js
    │           │   ├── custom/
    │           │   │   ├── proxy-ws-test.d.ts
    │           │   │   └── proxy-ws-test.js
    │           │   ├── errors/
    │           │   │   ├── test.InsufficientFunds.d.ts
    │           │   │   ├── test.InsufficientFunds.js
    │           │   │   ├── test.InvalidNonce.d.ts
    │           │   │   ├── test.InvalidNonce.js
    │           │   │   ├── test.InvalidOrder.d.ts
    │           │   │   ├── test.InvalidOrder.js
    │           │   │   ├── test.OrderNotFound.d.ts
    │           │   │   └── test.OrderNotFound.js
    │           │   ├── functions/
    │           │   │   ├── test.binanceMarkets.d.ts
    │           │   │   ├── test.binanceMarkets.js
    │           │   │   ├── test.crypto.d.ts
    │           │   │   ├── test.crypto.js
    │           │   │   ├── test.datetime.d.ts
    │           │   │   ├── test.datetime.js
    │           │   │   ├── test.generic.d.ts
    │           │   │   ├── test.generic.js
    │           │   │   ├── test.number.d.ts
    │           │   │   ├── test.number.js
    │           │   │   ├── test.throttle.d.ts
    │           │   │   ├── test.throttle.js
    │           │   │   ├── test.time.d.ts
    │           │   │   ├── test.time.js
    │           │   │   ├── test.timeout_hang.d.ts
    │           │   │   ├── test.timeout_hang.js
    │           │   │   ├── test.type.d.ts
    │           │   │   └── test.type.js
    │           │   └── language_specific/
    │           │       ├── test.aggregate.d.ts
    │           │       ├── test.aggregate.js
    │           │       ├── test.calculateFee.d.ts
    │           │       ├── test.calculateFee.js
    │           │       ├── test.camelcase.d.ts
    │           │       ├── test.camelcase.js
    │           │       ├── test.config.d.ts
    │           │       ├── test.config.js
    │           │       ├── test.languageSpecific.d.ts
    │           │       ├── test.languageSpecific.js
    │           │       ├── test.legacyHas.d.ts
    │           │       ├── test.legacyHas.js
    │           │       ├── test.safeBalance.d.ts
    │           │       ├── test.safeBalance.js
    │           │       ├── test.throttle.d.ts
    │           │       ├── test.throttle.js
    │           │       ├── test.time.d.ts
    │           │       ├── test.time.js
    │           │       ├── test.timeout_hang.d.ts
    │           │       ├── test.timeout_hang.js
    │           │       ├── test.type.d.ts
    │           │       ├── test.type.js
    │           │       ├── test.uncamelcase.d.ts
    │           │       └── test.uncamelcase.js
    │           ├── errors/
    │           │   ├── test.InsufficientFunds.d.ts
    │           │   ├── test.InsufficientFunds.js
    │           │   ├── test.InvalidNonce.d.ts
    │           │   ├── test.InvalidNonce.js
    │           │   ├── test.InvalidOrder.d.ts
    │           │   ├── test.InvalidOrder.js
    │           │   ├── test.OrderNotFound.d.ts
    │           │   └── test.OrderNotFound.js
    │           └── static/
    │               ├── test.ids.d.ts
    │               └── test.ids.js
    ├── php/
    │   ├── AccountNotEnabled.php
    │   ├── AccountSuspended.php
    │   ├── AddressPending.php
    │   ├── ArgumentsRequired.php
    │   ├── AuthenticationError.php
    │   ├── BadRequest.php
    │   ├── BadResponse.php
    │   ├── BadSymbol.php
    │   ├── BaseError.php
    │   ├── CancelPending.php
    │   ├── ChecksumError.php
    │   ├── ContractUnavailable.php
    │   ├── DDoSProtection.php
    │   ├── DuplicateOrderId.php
    │   ├── Exchange.php
    │   ├── ExchangeClosedByUser.php
    │   ├── ExchangeError.php
    │   ├── ExchangeNotAvailable.php
    │   ├── InsufficientFunds.php
    │   ├── InvalidAddress.php
    │   ├── InvalidNonce.php
    │   ├── InvalidOperation.php
    │   ├── InvalidOrder.php
    │   ├── InvalidProxySettings.php
    │   ├── ManualInteractionNeeded.php
    │   ├── MarginModeAlreadySet.php
    │   ├── MarketClosed.php
    │   ├── NetworkError.php
    │   ├── NoChange.php
    │   ├── NotSupported.php
    │   ├── NullResponse.php
    │   ├── OnMaintenance.php
    │   ├── OperationFailed.php
    │   ├── OperationRejected.php
    │   ├── OrderImmediatelyFillable.php
    │   ├── OrderNotCached.php
    │   ├── OrderNotFillable.php
    │   ├── OrderNotFound.php
    │   ├── PermissionDenied.php
    │   ├── Precise.php
    │   ├── ProxyError.php
    │   ├── RateLimitExceeded.php
    │   ├── RequestTimeout.php
    │   ├── UnsubscribeError.php
    │   ├── ace.php
    │   ├── alpaca.php
    │   ├── ascendex.php
    │   ├── bequant.php
    │   ├── bigone.php
    │   ├── binance.php
    │   ├── binancecoinm.php
    │   ├── binanceus.php
    │   ├── binanceusdm.php
    │   ├── bingx.php
    │   ├── bit2c.php
    │   ├── bitbank.php
    │   ├── bitbns.php
    │   ├── bitcoincom.php
    │   ├── bitfinex.php
    │   ├── bitfinex1.php
    │   ├── bitflyer.php
    │   ├── bitget.php
    │   ├── bithumb.php
    │   ├── bitmart.php
    │   ├── bitmex.php
    │   ├── bitopro.php
    │   ├── bitpanda.php
    │   ├── bitrue.php
    │   ├── bitso.php
    │   ├── bitstamp.php
    │   ├── bitteam.php
    │   ├── bitvavo.php
    │   ├── bl3p.php
    │   ├── blockchaincom.php
    │   ├── blofin.php
    │   ├── btcalpha.php
    │   ├── btcbox.php
    │   ├── btcmarkets.php
    │   ├── btcturk.php
    │   ├── bybit.php
    │   ├── cex.php
    │   ├── coinbase.php
    │   ├── coinbaseadvanced.php
    │   ├── coinbaseexchange.php
    │   ├── coinbaseinternational.php
    │   ├── coincatch.php
    │   ├── coincheck.php
    │   ├── coinex.php
    │   ├── coinlist.php
    │   ├── coinmate.php
    │   ├── coinmetro.php
    │   ├── coinone.php
    │   ├── coinsph.php
    │   ├── coinspot.php
    │   ├── cryptocom.php
    │   ├── currencycom.php
    │   ├── defx.php
    │   ├── delta.php
    │   ├── deribit.php
    │   ├── digifinex.php
    │   ├── ellipx.php
    │   ├── exmo.php
    │   ├── fmfwio.php
    │   ├── gate.php
    │   ├── gateio.php
    │   ├── gemini.php
    │   ├── hashkey.php
    │   ├── hitbtc.php
    │   ├── hollaex.php
    │   ├── htx.php
    │   ├── huobi.php
    │   ├── huobijp.php
    │   ├── hyperliquid.php
    │   ├── idex.php
    │   ├── independentreserve.php
    │   ├── indodax.php
    │   ├── kraken.php
    │   ├── krakenfutures.php
    │   ├── kucoin.php
    │   ├── kucoinfutures.php
    │   ├── kuna.php
    │   ├── latoken.php
    │   ├── lbank.php
    │   ├── luno.php
    │   ├── mercado.php
    │   ├── mexc.php
    │   ├── myokx.php
    │   ├── ndax.php
    │   ├── novadax.php
    │   ├── oceanex.php
    │   ├── okcoin.php
    │   ├── okx.php
    │   ├── onetrading.php
    │   ├── oxfun.php
    │   ├── p2b.php
    │   ├── paradex.php
    │   ├── paymium.php
    │   ├── phemex.php
    │   ├── poloniex.php
    │   ├── poloniexfutures.php
    │   ├── probit.php
    │   ├── timex.php
    │   ├── tokocrypto.php
    │   ├── tradeogre.php
    │   ├── upbit.php
    │   ├── vertex.php
    │   ├── wavesexchange.php
    │   ├── whitebit.php
    │   ├── woo.php
    │   ├── woofipro.php
    │   ├── xt.php
    │   ├── yobit.php
    │   ├── zaif.php
    │   ├── zonda.php
    │   ├── abstract/
    │   │   ├── ace.php
    │   │   ├── alpaca.php
    │   │   ├── ascendex.php
    │   │   ├── bequant.php
    │   │   ├── bigone.php
    │   │   ├── binance.php
    │   │   ├── binancecoinm.php
    │   │   ├── binanceus.php
    │   │   ├── binanceusdm.php
    │   │   ├── bingx.php
    │   │   ├── bit2c.php
    │   │   ├── bitbank.php
    │   │   ├── bitbns.php
    │   │   ├── bitcoincom.php
    │   │   ├── bitfinex.php
    │   │   ├── bitfinex1.php
    │   │   ├── bitflyer.php
    │   │   ├── bitget.php
    │   │   ├── bithumb.php
    │   │   ├── bitmart.php
    │   │   ├── bitmex.php
    │   │   ├── bitopro.php
    │   │   ├── bitpanda.php
    │   │   ├── bitrue.php
    │   │   ├── bitso.php
    │   │   ├── bitstamp.php
    │   │   ├── bitteam.php
    │   │   ├── bitvavo.php
    │   │   ├── bl3p.php
    │   │   ├── blockchaincom.php
    │   │   ├── blofin.php
    │   │   ├── btcalpha.php
    │   │   ├── btcbox.php
    │   │   ├── btcmarkets.php
    │   │   ├── btcturk.php
    │   │   ├── bybit.php
    │   │   ├── cex.php
    │   │   ├── coinbase.php
    │   │   ├── coinbaseadvanced.php
    │   │   ├── coinbaseexchange.php
    │   │   ├── coinbaseinternational.php
    │   │   ├── coincatch.php
    │   │   ├── coincheck.php
    │   │   ├── coinex.php
    │   │   ├── coinlist.php
    │   │   ├── coinmate.php
    │   │   ├── coinmetro.php
    │   │   ├── coinone.php
    │   │   ├── coinsph.php
    │   │   ├── coinspot.php
    │   │   ├── cryptocom.php
    │   │   ├── currencycom.php
    │   │   ├── defx.php
    │   │   ├── delta.php
    │   │   ├── deribit.php
    │   │   ├── digifinex.php
    │   │   ├── ellipx.php
    │   │   ├── exmo.php
    │   │   ├── fmfwio.php
    │   │   ├── gate.php
    │   │   ├── gateio.php
    │   │   ├── gemini.php
    │   │   ├── hashkey.php
    │   │   ├── hitbtc.php
    │   │   ├── hollaex.php
    │   │   ├── htx.php
    │   │   ├── huobi.php
    │   │   ├── huobijp.php
    │   │   ├── hyperliquid.php
    │   │   ├── idex.php
    │   │   ├── independentreserve.php
    │   │   ├── indodax.php
    │   │   ├── kraken.php
    │   │   ├── krakenfutures.php
    │   │   ├── kucoin.php
    │   │   ├── kucoinfutures.php
    │   │   ├── kuna.php
    │   │   ├── latoken.php
    │   │   ├── lbank.php
    │   │   ├── luno.php
    │   │   ├── mercado.php
    │   │   ├── mexc.php
    │   │   ├── myokx.php
    │   │   ├── ndax.php
    │   │   ├── novadax.php
    │   │   ├── oceanex.php
    │   │   ├── okcoin.php
    │   │   ├── okx.php
    │   │   ├── onetrading.php
    │   │   ├── oxfun.php
    │   │   ├── p2b.php
    │   │   ├── paradex.php
    │   │   ├── paymium.php
    │   │   ├── phemex.php
    │   │   ├── poloniex.php
    │   │   ├── poloniexfutures.php
    │   │   ├── probit.php
    │   │   ├── timex.php
    │   │   ├── tokocrypto.php
    │   │   ├── tradeogre.php
    │   │   ├── upbit.php
    │   │   ├── vertex.php
    │   │   ├── wavesexchange.php
    │   │   ├── whitebit.php
    │   │   ├── woo.php
    │   │   ├── woofipro.php
    │   │   ├── xt.php
    │   │   ├── yobit.php
    │   │   ├── zaif.php
    │   │   └── zonda.php
    │   ├── async/
    │   │   ├── Exchange.php
    │   │   ├── Throttler.php
    │   │   ├── ace.php
    │   │   ├── alpaca.php
    │   │   ├── ascendex.php
    │   │   ├── bequant.php
    │   │   ├── bigone.php
    │   │   ├── binance.php
    │   │   ├── binancecoinm.php
    │   │   ├── binanceus.php
    │   │   ├── binanceusdm.php
    │   │   ├── bingx.php
    │   │   ├── bit2c.php
    │   │   ├── bitbank.php
    │   │   ├── bitbns.php
    │   │   ├── bitcoincom.php
    │   │   ├── bitfinex.php
    │   │   ├── bitfinex1.php
    │   │   ├── bitflyer.php
    │   │   ├── bitget.php
    │   │   ├── bithumb.php
    │   │   ├── bitmart.php
    │   │   ├── bitmex.php
    │   │   ├── bitopro.php
    │   │   ├── bitpanda.php
    │   │   ├── bitrue.php
    │   │   ├── bitso.php
    │   │   ├── bitstamp.php
    │   │   ├── bitteam.php
    │   │   ├── bitvavo.php
    │   │   ├── bl3p.php
    │   │   ├── blockchaincom.php
    │   │   ├── blofin.php
    │   │   ├── btcalpha.php
    │   │   ├── btcbox.php
    │   │   ├── btcmarkets.php
    │   │   ├── btcturk.php
    │   │   ├── bybit.php
    │   │   ├── cex.php
    │   │   ├── coinbase.php
    │   │   ├── coinbaseadvanced.php
    │   │   ├── coinbaseexchange.php
    │   │   ├── coinbaseinternational.php
    │   │   ├── coincatch.php
    │   │   ├── coincheck.php
    │   │   ├── coinex.php
    │   │   ├── coinlist.php
    │   │   ├── coinmate.php
    │   │   ├── coinmetro.php
    │   │   ├── coinone.php
    │   │   ├── coinsph.php
    │   │   ├── coinspot.php
    │   │   ├── cryptocom.php
    │   │   ├── currencycom.php
    │   │   ├── defx.php
    │   │   ├── delta.php
    │   │   ├── deribit.php
    │   │   ├── digifinex.php
    │   │   ├── ellipx.php
    │   │   ├── exmo.php
    │   │   ├── fmfwio.php
    │   │   ├── gate.php
    │   │   ├── gateio.php
    │   │   ├── gemini.php
    │   │   ├── hashkey.php
    │   │   ├── hitbtc.php
    │   │   ├── hollaex.php
    │   │   ├── htx.php
    │   │   ├── huobi.php
    │   │   ├── huobijp.php
    │   │   ├── hyperliquid.php
    │   │   ├── idex.php
    │   │   ├── independentreserve.php
    │   │   ├── indodax.php
    │   │   ├── kraken.php
    │   │   ├── krakenfutures.php
    │   │   ├── kucoin.php
    │   │   ├── kucoinfutures.php
    │   │   ├── kuna.php
    │   │   ├── latoken.php
    │   │   ├── lbank.php
    │   │   ├── luno.php
    │   │   ├── mercado.php
    │   │   ├── mexc.php
    │   │   ├── myokx.php
    │   │   ├── ndax.php
    │   │   ├── novadax.php
    │   │   ├── oceanex.php
    │   │   ├── okcoin.php
    │   │   ├── okx.php
    │   │   ├── onetrading.php
    │   │   ├── oxfun.php
    │   │   ├── p2b.php
    │   │   ├── paradex.php
    │   │   ├── paymium.php
    │   │   ├── phemex.php
    │   │   ├── poloniex.php
    │   │   ├── poloniexfutures.php
    │   │   ├── probit.php
    │   │   ├── timex.php
    │   │   ├── tokocrypto.php
    │   │   ├── tradeogre.php
    │   │   ├── upbit.php
    │   │   ├── vertex.php
    │   │   ├── wavesexchange.php
    │   │   ├── whitebit.php
    │   │   ├── woo.php
    │   │   ├── woofipro.php
    │   │   ├── xt.php
    │   │   ├── yobit.php
    │   │   ├── zaif.php
    │   │   ├── zonda.php
    │   │   └── abstract/
    │   │       ├── ace.php
    │   │       ├── alpaca.php
    │   │       ├── ascendex.php
    │   │       ├── bequant.php
    │   │       ├── bigone.php
    │   │       ├── binance.php
    │   │       ├── binancecoinm.php
    │   │       ├── binanceus.php
    │   │       ├── binanceusdm.php
    │   │       ├── bingx.php
    │   │       ├── bit2c.php
    │   │       ├── bitbank.php
    │   │       ├── bitbns.php
    │   │       ├── bitcoincom.php
    │   │       ├── bitfinex.php
    │   │       ├── bitfinex1.php
    │   │       ├── bitflyer.php
    │   │       ├── bitget.php
    │   │       ├── bithumb.php
    │   │       ├── bitmart.php
    │   │       ├── bitmex.php
    │   │       ├── bitopro.php
    │   │       ├── bitpanda.php
    │   │       ├── bitrue.php
    │   │       ├── bitso.php
    │   │       ├── bitstamp.php
    │   │       ├── bitteam.php
    │   │       ├── bitvavo.php
    │   │       ├── bl3p.php
    │   │       ├── blockchaincom.php
    │   │       ├── blofin.php
    │   │       ├── btcalpha.php
    │   │       ├── btcbox.php
    │   │       ├── btcmarkets.php
    │   │       ├── btcturk.php
    │   │       ├── bybit.php
    │   │       ├── cex.php
    │   │       ├── coinbase.php
    │   │       ├── coinbaseadvanced.php
    │   │       ├── coinbaseexchange.php
    │   │       ├── coinbaseinternational.php
    │   │       ├── coincatch.php
    │   │       ├── coincheck.php
    │   │       ├── coinex.php
    │   │       ├── coinlist.php
    │   │       ├── coinmate.php
    │   │       ├── coinmetro.php
    │   │       ├── coinone.php
    │   │       ├── coinsph.php
    │   │       ├── coinspot.php
    │   │       ├── cryptocom.php
    │   │       ├── currencycom.php
    │   │       ├── defx.php
    │   │       ├── delta.php
    │   │       ├── deribit.php
    │   │       ├── digifinex.php
    │   │       ├── ellipx.php
    │   │       ├── exmo.php
    │   │       ├── fmfwio.php
    │   │       ├── gate.php
    │   │       ├── gateio.php
    │   │       ├── gemini.php
    │   │       ├── hashkey.php
    │   │       ├── hitbtc.php
    │   │       ├── hollaex.php
    │   │       ├── htx.php
    │   │       ├── huobi.php
    │   │       ├── huobijp.php
    │   │       ├── hyperliquid.php
    │   │       ├── idex.php
    │   │       ├── independentreserve.php
    │   │       ├── indodax.php
    │   │       ├── kraken.php
    │   │       ├── krakenfutures.php
    │   │       ├── kucoin.php
    │   │       ├── kucoinfutures.php
    │   │       ├── kuna.php
    │   │       ├── latoken.php
    │   │       ├── lbank.php
    │   │       ├── luno.php
    │   │       ├── mercado.php
    │   │       ├── mexc.php
    │   │       ├── myokx.php
    │   │       ├── ndax.php
    │   │       ├── novadax.php
    │   │       ├── oceanex.php
    │   │       ├── okcoin.php
    │   │       ├── okx.php
    │   │       ├── onetrading.php
    │   │       ├── oxfun.php
    │   │       ├── p2b.php
    │   │       ├── paradex.php
    │   │       ├── paymium.php
    │   │       ├── phemex.php
    │   │       ├── poloniex.php
    │   │       ├── poloniexfutures.php
    │   │       ├── probit.php
    │   │       ├── timex.php
    │   │       ├── tokocrypto.php
    │   │       ├── tradeogre.php
    │   │       ├── upbit.php
    │   │       ├── vertex.php
    │   │       ├── wavesexchange.php
    │   │       ├── whitebit.php
    │   │       ├── woo.php
    │   │       ├── woofipro.php
    │   │       ├── xt.php
    │   │       ├── yobit.php
    │   │       ├── zaif.php
    │   │       └── zonda.php
    │   ├── pro/
    │   │   ├── ArrayCache.php
    │   │   ├── ArrayCacheBySymbolById.php
    │   │   ├── ArrayCacheBySymbolBySide.php
    │   │   ├── ArrayCacheByTimestamp.php
    │   │   ├── BaseCache.php
    │   │   ├── Client.php
    │   │   ├── ClientTrait.php
    │   │   ├── Exchange.php
    │   │   ├── Future.php
    │   │   ├── OrderBook.php
    │   │   ├── OrderBookSide.php
    │   │   ├── alpaca.php
    │   │   ├── ascendex.php
    │   │   ├── bequant.php
    │   │   ├── binance.php
    │   │   ├── binancecoinm.php
    │   │   ├── binanceus.php
    │   │   ├── binanceusdm.php
    │   │   ├── bingx.php
    │   │   ├── bitcoincom.php
    │   │   ├── bitfinex.php
    │   │   ├── bitfinex1.php
    │   │   ├── bitget.php
    │   │   ├── bithumb.php
    │   │   ├── bitmart.php
    │   │   ├── bitmex.php
    │   │   ├── bitopro.php
    │   │   ├── bitpanda.php
    │   │   ├── bitrue.php
    │   │   ├── bitstamp.php
    │   │   ├── bitvavo.php
    │   │   ├── blockchaincom.php
    │   │   ├── blofin.php
    │   │   ├── bybit.php
    │   │   ├── cex.php
    │   │   ├── coinbase.php
    │   │   ├── coinbaseadvanced.php
    │   │   ├── coinbaseexchange.php
    │   │   ├── coinbaseinternational.php
    │   │   ├── coincatch.php
    │   │   ├── coincheck.php
    │   │   ├── coinex.php
    │   │   ├── coinone.php
    │   │   ├── cryptocom.php
    │   │   ├── currencycom.php
    │   │   ├── defx.php
    │   │   ├── deribit.php
    │   │   ├── exmo.php
    │   │   ├── gate.php
    │   │   ├── gateio.php
    │   │   ├── gemini.php
    │   │   ├── hashkey.php
    │   │   ├── hitbtc.php
    │   │   ├── hollaex.php
    │   │   ├── htx.php
    │   │   ├── huobi.php
    │   │   ├── huobijp.php
    │   │   ├── hyperliquid.php
    │   │   ├── idex.php
    │   │   ├── independentreserve.php
    │   │   ├── kraken.php
    │   │   ├── krakenfutures.php
    │   │   ├── kucoin.php
    │   │   ├── kucoinfutures.php
    │   │   ├── lbank.php
    │   │   ├── luno.php
    │   │   ├── mexc.php
    │   │   ├── myokx.php
    │   │   ├── ndax.php
    │   │   ├── okcoin.php
    │   │   ├── okx.php
    │   │   ├── onetrading.php
    │   │   ├── oxfun.php
    │   │   ├── p2b.php
    │   │   ├── paradex.php
    │   │   ├── phemex.php
    │   │   ├── poloniex.php
    │   │   ├── poloniexfutures.php
    │   │   ├── probit.php
    │   │   ├── upbit.php
    │   │   ├── vertex.php
    │   │   ├── wazirx.php
    │   │   ├── whitebit.php
    │   │   ├── woo.php
    │   │   ├── woofipro.php
    │   │   ├── xt.php
    │   │   ├── base/
    │   │   │   └── functions.php
    │   │   └── test/
    │   │       ├── Exchange/
    │   │       │   ├── test_watch_balance.php
    │   │       │   ├── test_watch_bids_asks.php
    │   │       │   ├── test_watch_liquidations.php
    │   │       │   ├── test_watch_liquidations_for_symbols.php
    │   │       │   ├── test_watch_my_trades.php
    │   │       │   ├── test_watch_ohlcv.php
    │   │       │   ├── test_watch_ohlcv_for_symbols.php
    │   │       │   ├── test_watch_order_book.php
    │   │       │   ├── test_watch_order_book_for_symbols.php
    │   │       │   ├── test_watch_orders.php
    │   │       │   ├── test_watch_position.php
    │   │       │   ├── test_watch_positions.php
    │   │       │   ├── test_watch_ticker.php
    │   │       │   ├── test_watch_tickers.php
    │   │       │   ├── test_watch_trades.php
    │   │       │   └── test_watch_trades_for_symbols.php
    │   │       ├── base/
    │   │       │   ├── test_cache.php
    │   │       │   ├── test_client_resolve.php
    │   │       │   ├── test_close.php
    │   │       │   ├── test_order_book.php
    │   │       │   ├── tests_init.php
    │   │       │   └── .gitkeep
    │   │       └── custom/
    │   │           └── syntax.php
    │   ├── static_dependencies/
    │   │   ├── README.md
    │   │   ├── BI/
    │   │   │   └── BigInteger.php
    │   │   ├── BN/
    │   │   │   ├── BN.php
    │   │   │   └── Red.php
    │   │   ├── MessagePack/
    │   │   │   ├── BufferUnpacker.php
    │   │   │   ├── CanBePacked.php
    │   │   │   ├── CanPack.php
    │   │   │   ├── Extension.php
    │   │   │   ├── MessagePack.php
    │   │   │   ├── PackOptions.php
    │   │   │   ├── Packer.php
    │   │   │   ├── UnpackOptions.php
    │   │   │   ├── Exception/
    │   │   │   │   ├── InsufficientDataException.php
    │   │   │   │   ├── InvalidOptionException.php
    │   │   │   │   ├── PackingFailedException.php
    │   │   │   │   └── UnpackingFailedException.php
    │   │   │   ├── Extension/
    │   │   │   │   └── TimestampExtension.php
    │   │   │   ├── Type/
    │   │   │   │   ├── Bin.php
    │   │   │   │   ├── Ext.php
    │   │   │   │   ├── Map.php
    │   │   │   │   └── Timestamp.php
    │   │   │   └── TypeTransformer/
    │   │   │       ├── StreamTransformer.php
    │   │   │       └── TraversableTransformer.php
    │   │   ├── Sop/
    │   │   │   └── ASN1/
    │   │   │       ├── DERData.php
    │   │   │       ├── Element.php
    │   │   │       ├── Component/
    │   │   │       │   ├── Identifier.php
    │   │   │       │   └── Length.php
    │   │   │       ├── Exception/
    │   │   │       │   └── DecodeException.php
    │   │   │       ├── Feature/
    │   │   │       │   ├── ElementBase.php
    │   │   │       │   ├── Encodable.php
    │   │   │       │   └── Stringable.php
    │   │   │       ├── Type/
    │   │   │       │   ├── BaseString.php
    │   │   │       │   ├── BaseTime.php
    │   │   │       │   ├── PrimitiveString.php
    │   │   │       │   ├── PrimitiveType.php
    │   │   │       │   ├── StringType.php
    │   │   │       │   ├── Structure.php
    │   │   │       │   ├── TaggedType.php
    │   │   │       │   ├── TimeType.php
    │   │   │       │   ├── UniversalClass.php
    │   │   │       │   ├── UnspecifiedType.php
    │   │   │       │   ├── Constructed/
    │   │   │       │   │   ├── ConstructedString.php
    │   │   │       │   │   ├── Sequence.php
    │   │   │       │   │   └── Set.php
    │   │   │       │   ├── Primitive/
    │   │   │       │   │   ├── BMPString.php
    │   │   │       │   │   ├── BitString.php
    │   │   │       │   │   ├── Boolean.php
    │   │   │       │   │   ├── CharacterString.php
    │   │   │       │   │   ├── EOC.php
    │   │   │       │   │   ├── Enumerated.php
    │   │   │       │   │   ├── GeneralString.php
    │   │   │       │   │   ├── GeneralizedTime.php
    │   │   │       │   │   ├── GraphicString.php
    │   │   │       │   │   ├── IA5String.php
    │   │   │       │   │   ├── Integer.php
    │   │   │       │   │   ├── NullType.php
    │   │   │       │   │   ├── NumericString.php
    │   │   │       │   │   ├── ObjectDescriptor.php
    │   │   │       │   │   ├── ObjectIdentifier.php
    │   │   │       │   │   ├── OctetString.php
    │   │   │       │   │   ├── PrintableString.php
    │   │   │       │   │   ├── Real.php
    │   │   │       │   │   ├── RelativeOID.php
    │   │   │       │   │   ├── T61String.php
    │   │   │       │   │   ├── UTCTime.php
    │   │   │       │   │   ├── UTF8String.php
    │   │   │       │   │   ├── UniversalString.php
    │   │   │       │   │   ├── VideotexString.php
    │   │   │       │   │   └── VisibleString.php
    │   │   │       │   └── Tagged/
    │   │   │       │       ├── ApplicationType.php
    │   │   │       │       ├── ContextSpecificType.php
    │   │   │       │       ├── DERTaggedType.php
    │   │   │       │       ├── ExplicitTagging.php
    │   │   │       │       ├── ExplicitlyTaggedType.php
    │   │   │       │       ├── ImplicitTagging.php
    │   │   │       │       ├── ImplicitlyTaggedType.php
    │   │   │       │       ├── PrivateType.php
    │   │   │       │       └── TaggedTypeWrap.php
    │   │   │       └── Util/
    │   │   │           ├── BigInt.php
    │   │   │           └── Flags.php
    │   │   ├── elliptic-php/
    │   │   │   ├── LICENSE.md
    │   │   │   ├── composer.json
    │   │   │   └── lib/
    │   │   │       ├── Curves.php
    │   │   │       ├── EC.php
    │   │   │       ├── EdDSA.php
    │   │   │       ├── HmacDRBG.php
    │   │   │       ├── Utils.php
    │   │   │       ├── Curve/
    │   │   │       │   ├── BaseCurve.php
    │   │   │       │   ├── EdwardsCurve.php
    │   │   │       │   ├── MontCurve.php
    │   │   │       │   ├── PresetCurve.php
    │   │   │       │   ├── ShortCurve.php
    │   │   │       │   ├── BaseCurve/
    │   │   │       │   │   └── Point.php
    │   │   │       │   ├── EdwardsCurve/
    │   │   │       │   │   └── Point.php
    │   │   │       │   ├── MontCurve/
    │   │   │       │   │   └── Point.php
    │   │   │       │   └── ShortCurve/
    │   │   │       │       ├── JPoint.php
    │   │   │       │       └── Point.php
    │   │   │       ├── EC/
    │   │   │       │   ├── KeyPair.php
    │   │   │       │   └── Signature.php
    │   │   │       └── EdDSA/
    │   │   │           ├── KeyPair.php
    │   │   │           └── Signature.php
    │   │   ├── kornrunner/
    │   │   │   └── keccak/
    │   │   │       ├── README.md
    │   │   │       ├── LICENSE
    │   │   │       └── src/
    │   │   │           └── Keccak.php
    │   │   ├── phpseclib/
    │   │   │   └── Math/
    │   │   │       └── BigInteger.php
    │   │   ├── proxies/
    │   │   │   └── reactphp-http-proxy/
    │   │   │       ├── LICENSE
    │   │   │       ├── composer.json
    │   │   │       └── src/
    │   │   │           └── ProxyConnector.php
    │   │   ├── ratchet/
    │   │   │   ├── pawl/
    │   │   │   │   ├── README.md
    │   │   │   │   ├── LICENSE
    │   │   │   │   ├── composer.json
    │   │   │   │   ├── phpunit.xml.dist
    │   │   │   │   ├── phpunit.xml.legacy
    │   │   │   │   ├── .gitignore
    │   │   │   │   ├── src/
    │   │   │   │   │   ├── Connector.php
    │   │   │   │   │   ├── WebSocket.php
    │   │   │   │   │   ├── functions.php
    │   │   │   │   │   └── functions_include.php
    │   │   │   │   ├── tests/
    │   │   │   │   │   ├── autobahn/
    │   │   │   │   │   │   ├── fuzzingserver.json
    │   │   │   │   │   │   └── runner.php
    │   │   │   │   │   └── unit/
    │   │   │   │   │       ├── ConnectorTest.php
    │   │   │   │   │       └── RequestUriTest.php
    │   │   │   │   └── .github/
    │   │   │   │       └── workflows/
    │   │   │   │           └── ci.yml
    │   │   │   └── rfc6455/
    │   │   │       ├── README.md
    │   │   │       ├── LICENSE
    │   │   │       ├── composer.json
    │   │   │       ├── phpunit.xml.dist
    │   │   │       ├── .gitignore
    │   │   │       ├── src/
    │   │   │       │   ├── Handshake/
    │   │   │       │   │   ├── ClientNegotiator.php
    │   │   │       │   │   ├── InvalidPermessageDeflateOptionsException.php
    │   │   │       │   │   ├── NegotiatorInterface.php
    │   │   │       │   │   ├── PermessageDeflateOptions.php
    │   │   │       │   │   ├── RequestVerifier.php
    │   │   │       │   │   ├── ResponseVerifier.php
    │   │   │       │   │   └── ServerNegotiator.php
    │   │   │       │   └── Messaging/
    │   │   │       │       ├── CloseFrameChecker.php
    │   │   │       │       ├── DataInterface.php
    │   │   │       │       ├── Frame.php
    │   │   │       │       ├── FrameInterface.php
    │   │   │       │       ├── Message.php
    │   │   │       │       ├── MessageBuffer.php
    │   │   │       │       └── MessageInterface.php
    │   │   │       ├── tests/
    │   │   │       │   ├── AbResultsTest.php
    │   │   │       │   ├── bootstrap.php
    │   │   │       │   ├── ab/
    │   │   │       │   │   ├── clientRunner.php
    │   │   │       │   │   ├── docker_bootstrap.sh
    │   │   │       │   │   ├── fuzzingclient.json
    │   │   │       │   │   ├── fuzzingclient_skip_deflate.json
    │   │   │       │   │   ├── fuzzingserver.json
    │   │   │       │   │   ├── fuzzingserver_skip_deflate.json
    │   │   │       │   │   ├── run_ab_tests.sh
    │   │   │       │   │   └── startServer.php
    │   │   │       │   └── unit/
    │   │   │       │       ├── Handshake/
    │   │   │       │       │   ├── PermessageDeflateOptionsTest.php
    │   │   │       │       │   ├── RequestVerifierTest.php
    │   │   │       │       │   ├── ResponseVerifierTest.php
    │   │   │       │       │   └── ServerNegotiatorTest.php
    │   │   │       │       └── Messaging/
    │   │   │       │           ├── FrameTest.php
    │   │   │       │           ├── MessageBufferTest.php
    │   │   │       │           └── MessageTest.php
    │   │   │       └── .github/
    │   │   │           └── workflows/
    │   │   │               └── ci.yml
    │   │   ├── ringcentral-psr7/
    │   │   │   ├── README.md
    │   │   │   ├── LICENSE
    │   │   │   ├── composer.json
    │   │   │   ├── loader.php
    │   │   │   └── src/
    │   │   │       ├── MessageTrait.php
    │   │   │       ├── Request.php
    │   │   │       ├── Response.php
    │   │   │       ├── Stream.php
    │   │   │       ├── StreamDecoratorTrait.php
    │   │   │       ├── functions.php
    │   │   │       └── functions_include.php
    │   │   ├── starknet.php/
    │   │   │   └── src/
    │   │   │       ├── Constants.php
    │   │   │       ├── Hash.php
    │   │   │       ├── TypedData.php
    │   │   │       ├── Utils.php
    │   │   │       ├── Cairo/
    │   │   │       │   └── Felt.php
    │   │   │       └── Crypto/
    │   │   │           ├── Curve.php
    │   │   │           ├── FastPedersenHash.php
    │   │   │           ├── Hash.php
    │   │   │           ├── Key.php
    │   │   │           └── PedersenHash.php
    │   │   └── web3.php/
    │   │       └── src/
    │   │           ├── Utils.php
    │   │           ├── Contracts/
    │   │           │   ├── Ethabi.php
    │   │           │   ├── SolidityType.php
    │   │           │   ├── TypedDataEncoder.php
    │   │           │   └── Types/
    │   │           │       ├── Address.php
    │   │           │       ├── BaseArray.php
    │   │           │       ├── Boolean.php
    │   │           │       ├── Bytes.php
    │   │           │       ├── DynamicArray.php
    │   │           │       ├── DynamicBytes.php
    │   │           │       ├── IType.php
    │   │           │       ├── Integer.php
    │   │           │       ├── SizedArray.php
    │   │           │       ├── Str.php
    │   │           │       ├── Tuple.php
    │   │           │       └── Uinteger.php
    │   │           └── Formatters/
    │   │               ├── AddressFormatter.php
    │   │               ├── BigNumberFormatter.php
    │   │               ├── BooleanFormatter.php
    │   │               ├── FeeHistoryFormatter.php
    │   │               ├── HexFormatter.php
    │   │               ├── IFormatter.php
    │   │               ├── IntegerFormatter.php
    │   │               ├── NumberFormatter.php
    │   │               ├── OptionalQuantityFormatter.php
    │   │               ├── PostFormatter.php
    │   │               ├── QuantityFormatter.php
    │   │               ├── StringFormatter.php
    │   │               └── TransactionFormatter.php
    │   └── test/
    │       ├── bootstrap.php
    │       ├── tests_async.php
    │       ├── tests_helpers.php
    │       ├── tests_init.php
    │       ├── tests_sync.php
    │       ├── base/
    │       │   ├── test_after_constructor.php
    │       │   ├── test_cryptography.php
    │       │   ├── test_datetime.php
    │       │   ├── test_deep_extend.php
    │       │   ├── test_extend.php
    │       │   ├── test_filter_by.php
    │       │   ├── test_group_by.php
    │       │   ├── test_json.php
    │       │   ├── test_number.php
    │       │   ├── test_omit.php
    │       │   ├── test_safe_methods.php
    │       │   ├── test_sort_by.php
    │       │   ├── test_sum.php
    │       │   ├── tests_init.php
    │       │   └── language_specific/
    │       │       └── test_language_specific.php
    │       ├── custom/
    │       │   ├── fail_on_all_errors.php
    │       │   └── syntax.php
    │       └── exchange/
    │           ├── async/
    │           │   ├── test_create_order.php
    │           │   ├── test_features.php
    │           │   ├── test_fetch_accounts.php
    │           │   ├── test_fetch_balance.php
    │           │   ├── test_fetch_borrow_interest.php
    │           │   ├── test_fetch_closed_orders.php
    │           │   ├── test_fetch_currencies.php
    │           │   ├── test_fetch_deposit_withdrawals.php
    │           │   ├── test_fetch_deposits.php
    │           │   ├── test_fetch_funding_rate_history.php
    │           │   ├── test_fetch_l2_order_book.php
    │           │   ├── test_fetch_last_prices.php
    │           │   ├── test_fetch_ledger.php
    │           │   ├── test_fetch_ledger_entry.php
    │           │   ├── test_fetch_leverage_tiers.php
    │           │   ├── test_fetch_liquidations.php
    │           │   ├── test_fetch_margin_mode.php
    │           │   ├── test_fetch_margin_modes.php
    │           │   ├── test_fetch_market_leverage_tiers.php
    │           │   ├── test_fetch_markets.php
    │           │   ├── test_fetch_my_liquidations.php
    │           │   ├── test_fetch_my_trades.php
    │           │   ├── test_fetch_ohlcv.php
    │           │   ├── test_fetch_open_interest_history.php
    │           │   ├── test_fetch_open_orders.php
    │           │   ├── test_fetch_order_book.php
    │           │   ├── test_fetch_order_books.php
    │           │   ├── test_fetch_orders.php
    │           │   ├── test_fetch_positions.php
    │           │   ├── test_fetch_status.php
    │           │   ├── test_fetch_ticker.php
    │           │   ├── test_fetch_tickers.php
    │           │   ├── test_fetch_trades.php
    │           │   ├── test_fetch_trading_fee.php
    │           │   ├── test_fetch_trading_fees.php
    │           │   ├── test_fetch_transaction_fees.php
    │           │   ├── test_fetch_withdrawals.php
    │           │   ├── test_load_markets.php
    │           │   ├── test_proxies.php
    │           │   └── test_sign_in.php
    │           ├── base/
    │           │   ├── test_account.php
    │           │   ├── test_balance.php
    │           │   ├── test_borrow_interest.php
    │           │   ├── test_borrow_rate.php
    │           │   ├── test_currency.php
    │           │   ├── test_deposit_withdrawal.php
    │           │   ├── test_funding_rate_history.php
    │           │   ├── test_last_price.php
    │           │   ├── test_ledger_entry.php
    │           │   ├── test_leverage_tier.php
    │           │   ├── test_liquidation.php
    │           │   ├── test_margin_mode.php
    │           │   ├── test_margin_modification.php
    │           │   ├── test_market.php
    │           │   ├── test_ohlcv.php
    │           │   ├── test_open_interest.php
    │           │   ├── test_order.php
    │           │   ├── test_order_book.php
    │           │   ├── test_position.php
    │           │   ├── test_shared_methods.php
    │           │   ├── test_status.php
    │           │   ├── test_ticker.php
    │           │   ├── test_trade.php
    │           │   └── test_trading_fee.php
    │           └── sync/
    │               ├── test_create_order.php
    │               ├── test_features.php
    │               ├── test_fetch_accounts.php
    │               ├── test_fetch_balance.php
    │               ├── test_fetch_borrow_interest.php
    │               ├── test_fetch_closed_orders.php
    │               ├── test_fetch_currencies.php
    │               ├── test_fetch_deposit_withdrawals.php
    │               ├── test_fetch_deposits.php
    │               ├── test_fetch_funding_rate_history.php
    │               ├── test_fetch_l2_order_book.php
    │               ├── test_fetch_last_prices.php
    │               ├── test_fetch_ledger.php
    │               ├── test_fetch_ledger_entry.php
    │               ├── test_fetch_leverage_tiers.php
    │               ├── test_fetch_liquidations.php
    │               ├── test_fetch_margin_mode.php
    │               ├── test_fetch_margin_modes.php
    │               ├── test_fetch_market_leverage_tiers.php
    │               ├── test_fetch_markets.php
    │               ├── test_fetch_my_liquidations.php
    │               ├── test_fetch_my_trades.php
    │               ├── test_fetch_ohlcv.php
    │               ├── test_fetch_open_interest_history.php
    │               ├── test_fetch_open_orders.php
    │               ├── test_fetch_order_book.php
    │               ├── test_fetch_order_books.php
    │               ├── test_fetch_orders.php
    │               ├── test_fetch_positions.php
    │               ├── test_fetch_status.php
    │               ├── test_fetch_ticker.php
    │               ├── test_fetch_tickers.php
    │               ├── test_fetch_trades.php
    │               ├── test_fetch_trading_fee.php
    │               ├── test_fetch_trading_fees.php
    │               ├── test_fetch_transaction_fees.php
    │               ├── test_fetch_withdrawals.php
    │               ├── test_load_markets.php
    │               ├── test_proxies.php
    │               └── test_sign_in.php
    ├── python/
    │   ├── README.md
    │   ├── LICENSE.txt
    │   ├── MANIFEST.in
    │   ├── README.rst
    │   ├── deploy.sh
    │   ├── fastflake.sh
    │   ├── mypy.ini
    │   ├── package.json
    │   ├── qa.py
    │   ├── setup.cfg
    │   ├── setup.py
    │   ├── tox.ini
    │   └── ccxt/
    │       ├── __init__.py
    │       ├── ace.py
    │       ├── alpaca.py
    │       ├── ascendex.py
    │       ├── bequant.py
    │       ├── bigone.py
    │       ├── binance.py
    │       ├── binancecoinm.py
    │       ├── binanceus.py
    │       ├── binanceusdm.py
    │       ├── bingx.py
    │       ├── bit2c.py
    │       ├── bitbank.py
    │       ├── bitbns.py
    │       ├── bitcoincom.py
    │       ├── bitfinex.py
    │       ├── bitfinex1.py
    │       ├── bitflyer.py
    │       ├── bitget.py
    │       ├── bithumb.py
    │       ├── bitmart.py
    │       ├── bitmex.py
    │       ├── bitopro.py
    │       ├── bitpanda.py
    │       ├── bitrue.py
    │       ├── bitso.py
    │       ├── bitstamp.py
    │       ├── bitteam.py
    │       ├── bitvavo.py
    │       ├── bl3p.py
    │       ├── blockchaincom.py
    │       ├── blofin.py
    │       ├── btcalpha.py
    │       ├── btcbox.py
    │       ├── btcmarkets.py
    │       ├── btcturk.py
    │       ├── bybit.py
    │       ├── cex.py
    │       ├── coinbase.py
    │       ├── coinbaseadvanced.py
    │       ├── coinbaseexchange.py
    │       ├── coinbaseinternational.py
    │       ├── coincatch.py
    │       ├── coincheck.py
    │       ├── coinex.py
    │       ├── coinlist.py
    │       ├── coinmate.py
    │       ├── coinmetro.py
    │       ├── coinone.py
    │       ├── coinsph.py
    │       ├── coinspot.py
    │       ├── cryptocom.py
    │       ├── currencycom.py
    │       ├── defx.py
    │       ├── delta.py
    │       ├── deribit.py
    │       ├── digifinex.py
    │       ├── ellipx.py
    │       ├── exmo.py
    │       ├── fmfwio.py
    │       ├── gate.py
    │       ├── gateio.py
    │       ├── gemini.py
    │       ├── hashkey.py
    │       ├── hitbtc.py
    │       ├── hollaex.py
    │       ├── htx.py
    │       ├── huobi.py
    │       ├── huobijp.py
    │       ├── hyperliquid.py
    │       ├── idex.py
    │       ├── independentreserve.py
    │       ├── indodax.py
    │       ├── kraken.py
    │       ├── krakenfutures.py
    │       ├── kucoin.py
    │       ├── kucoinfutures.py
    │       ├── kuna.py
    │       ├── latoken.py
    │       ├── lbank.py
    │       ├── luno.py
    │       ├── mercado.py
    │       ├── mexc.py
    │       ├── myokx.py
    │       ├── ndax.py
    │       ├── novadax.py
    │       ├── oceanex.py
    │       ├── okcoin.py
    │       ├── okx.py
    │       ├── onetrading.py
    │       ├── oxfun.py
    │       ├── p2b.py
    │       ├── paradex.py
    │       ├── paymium.py
    │       ├── phemex.py
    │       ├── poloniex.py
    │       ├── poloniexfutures.py
    │       ├── probit.py
    │       ├── timex.py
    │       ├── tokocrypto.py
    │       ├── tradeogre.py
    │       ├── upbit.py
    │       ├── vertex.py
    │       ├── wavesexchange.py
    │       ├── whitebit.py
    │       ├── woo.py
    │       ├── woofipro.py
    │       ├── xt.py
    │       ├── yobit.py
    │       ├── zaif.py
    │       ├── zonda.py
    │       ├── abstract/
    │       │   ├── __init__.py
    │       │   ├── ace.py
    │       │   ├── alpaca.py
    │       │   ├── ascendex.py
    │       │   ├── bequant.py
    │       │   ├── bigone.py
    │       │   ├── binance.py
    │       │   ├── binancecoinm.py
    │       │   ├── binanceus.py
    │       │   ├── binanceusdm.py
    │       │   ├── bingx.py
    │       │   ├── bit2c.py
    │       │   ├── bitbank.py
    │       │   ├── bitbns.py
    │       │   ├── bitcoincom.py
    │       │   ├── bitfinex.py
    │       │   ├── bitfinex1.py
    │       │   ├── bitflyer.py
    │       │   ├── bitget.py
    │       │   ├── bithumb.py
    │       │   ├── bitmart.py
    │       │   ├── bitmex.py
    │       │   ├── bitopro.py
    │       │   ├── bitpanda.py
    │       │   ├── bitrue.py
    │       │   ├── bitso.py
    │       │   ├── bitstamp.py
    │       │   ├── bitteam.py
    │       │   ├── bitvavo.py
    │       │   ├── bl3p.py
    │       │   ├── blockchaincom.py
    │       │   ├── blofin.py
    │       │   ├── btcalpha.py
    │       │   ├── btcbox.py
    │       │   ├── btcmarkets.py
    │       │   ├── btcturk.py
    │       │   ├── bybit.py
    │       │   ├── cex.py
    │       │   ├── coinbase.py
    │       │   ├── coinbaseadvanced.py
    │       │   ├── coinbaseexchange.py
    │       │   ├── coinbaseinternational.py
    │       │   ├── coincatch.py
    │       │   ├── coincheck.py
    │       │   ├── coinex.py
    │       │   ├── coinlist.py
    │       │   ├── coinmate.py
    │       │   ├── coinmetro.py
    │       │   ├── coinone.py
    │       │   ├── coinsph.py
    │       │   ├── coinspot.py
    │       │   ├── cryptocom.py
    │       │   ├── currencycom.py
    │       │   ├── defx.py
    │       │   ├── delta.py
    │       │   ├── deribit.py
    │       │   ├── digifinex.py
    │       │   ├── ellipx.py
    │       │   ├── exmo.py
    │       │   ├── fmfwio.py
    │       │   ├── gate.py
    │       │   ├── gateio.py
    │       │   ├── gemini.py
    │       │   ├── hashkey.py
    │       │   ├── hitbtc.py
    │       │   ├── hollaex.py
    │       │   ├── htx.py
    │       │   ├── huobi.py
    │       │   ├── huobijp.py
    │       │   ├── hyperliquid.py
    │       │   ├── idex.py
    │       │   ├── independentreserve.py
    │       │   ├── indodax.py
    │       │   ├── kraken.py
    │       │   ├── krakenfutures.py
    │       │   ├── kucoin.py
    │       │   ├── kucoinfutures.py
    │       │   ├── kuna.py
    │       │   ├── latoken.py
    │       │   ├── lbank.py
    │       │   ├── luno.py
    │       │   ├── mercado.py
    │       │   ├── mexc.py
    │       │   ├── myokx.py
    │       │   ├── ndax.py
    │       │   ├── novadax.py
    │       │   ├── oceanex.py
    │       │   ├── okcoin.py
    │       │   ├── okx.py
    │       │   ├── onetrading.py
    │       │   ├── oxfun.py
    │       │   ├── p2b.py
    │       │   ├── paradex.py
    │       │   ├── paymium.py
    │       │   ├── phemex.py
    │       │   ├── poloniex.py
    │       │   ├── poloniexfutures.py
    │       │   ├── probit.py
    │       │   ├── timex.py
    │       │   ├── tokocrypto.py
    │       │   ├── tradeogre.py
    │       │   ├── upbit.py
    │       │   ├── vertex.py
    │       │   ├── wavesexchange.py
    │       │   ├── whitebit.py
    │       │   ├── woo.py
    │       │   ├── woofipro.py
    │       │   ├── xt.py
    │       │   ├── yobit.py
    │       │   ├── zaif.py
    │       │   └── zonda.py
    │       ├── async_support/
    │       │   ├── __init__.py
    │       │   ├── ace.py
    │       │   ├── alpaca.py
    │       │   ├── ascendex.py
    │       │   ├── bequant.py
    │       │   ├── bigone.py
    │       │   ├── binance.py
    │       │   ├── binancecoinm.py
    │       │   ├── binanceus.py
    │       │   ├── binanceusdm.py
    │       │   ├── bingx.py
    │       │   ├── bit2c.py
    │       │   ├── bitbank.py
    │       │   ├── bitbns.py
    │       │   ├── bitcoincom.py
    │       │   ├── bitfinex.py
    │       │   ├── bitfinex1.py
    │       │   ├── bitflyer.py
    │       │   ├── bitget.py
    │       │   ├── bithumb.py
    │       │   ├── bitmart.py
    │       │   ├── bitmex.py
    │       │   ├── bitopro.py
    │       │   ├── bitpanda.py
    │       │   ├── bitrue.py
    │       │   ├── bitso.py
    │       │   ├── bitstamp.py
    │       │   ├── bitteam.py
    │       │   ├── bitvavo.py
    │       │   ├── bl3p.py
    │       │   ├── blockchaincom.py
    │       │   ├── blofin.py
    │       │   ├── btcalpha.py
    │       │   ├── btcbox.py
    │       │   ├── btcmarkets.py
    │       │   ├── btcturk.py
    │       │   ├── bybit.py
    │       │   ├── cex.py
    │       │   ├── coinbase.py
    │       │   ├── coinbaseadvanced.py
    │       │   ├── coinbaseexchange.py
    │       │   ├── coinbaseinternational.py
    │       │   ├── coincatch.py
    │       │   ├── coincheck.py
    │       │   ├── coinex.py
    │       │   ├── coinlist.py
    │       │   ├── coinmate.py
    │       │   ├── coinmetro.py
    │       │   ├── coinone.py
    │       │   ├── coinsph.py
    │       │   ├── coinspot.py
    │       │   ├── cryptocom.py
    │       │   ├── currencycom.py
    │       │   ├── defx.py
    │       │   ├── delta.py
    │       │   ├── deribit.py
    │       │   ├── digifinex.py
    │       │   ├── ellipx.py
    │       │   ├── exmo.py
    │       │   ├── fmfwio.py
    │       │   ├── gate.py
    │       │   ├── gateio.py
    │       │   ├── gemini.py
    │       │   ├── hashkey.py
    │       │   ├── hitbtc.py
    │       │   ├── hollaex.py
    │       │   ├── htx.py
    │       │   ├── huobi.py
    │       │   ├── huobijp.py
    │       │   ├── hyperliquid.py
    │       │   ├── idex.py
    │       │   ├── independentreserve.py
    │       │   ├── indodax.py
    │       │   ├── kraken.py
    │       │   ├── krakenfutures.py
    │       │   ├── kucoin.py
    │       │   ├── kucoinfutures.py
    │       │   ├── kuna.py
    │       │   ├── latoken.py
    │       │   ├── lbank.py
    │       │   ├── luno.py
    │       │   ├── mercado.py
    │       │   ├── mexc.py
    │       │   ├── myokx.py
    │       │   ├── ndax.py
    │       │   ├── novadax.py
    │       │   ├── oceanex.py
    │       │   ├── okcoin.py
    │       │   ├── okx.py
    │       │   ├── onetrading.py
    │       │   ├── oxfun.py
    │       │   ├── p2b.py
    │       │   ├── paradex.py
    │       │   ├── paymium.py
    │       │   ├── phemex.py
    │       │   ├── poloniex.py
    │       │   ├── poloniexfutures.py
    │       │   ├── probit.py
    │       │   ├── timex.py
    │       │   ├── tokocrypto.py
    │       │   ├── tradeogre.py
    │       │   ├── upbit.py
    │       │   ├── vertex.py
    │       │   ├── wavesexchange.py
    │       │   ├── whitebit.py
    │       │   ├── woo.py
    │       │   ├── woofipro.py
    │       │   ├── xt.py
    │       │   ├── yobit.py
    │       │   ├── zaif.py
    │       │   ├── zonda.py
    │       │   └── base/
    │       │       ├── __init__.py
    │       │       ├── exchange.py
    │       │       ├── throttler.py
    │       │       └── ws/
    │       │           ├── __init__.py
    │       │           ├── aiohttp_client.py
    │       │           ├── cache.py
    │       │           ├── client.py
    │       │           ├── fast_client.py
    │       │           ├── functions.py
    │       │           ├── future.py
    │       │           ├── order_book.py
    │       │           └── order_book_side.py
    │       ├── base/
    │       │   ├── __init__.py
    │       │   ├── decimal_to_precision.py
    │       │   ├── errors.py
    │       │   ├── exchange.py
    │       │   ├── precise.py
    │       │   └── types.py
    │       ├── pro/
    │       │   ├── __init__.py
    │       │   ├── alpaca.py
    │       │   ├── ascendex.py
    │       │   ├── bequant.py
    │       │   ├── binance.py
    │       │   ├── binancecoinm.py
    │       │   ├── binanceus.py
    │       │   ├── binanceusdm.py
    │       │   ├── bingx.py
    │       │   ├── bitcoincom.py
    │       │   ├── bitfinex.py
    │       │   ├── bitfinex1.py
    │       │   ├── bitget.py
    │       │   ├── bithumb.py
    │       │   ├── bitmart.py
    │       │   ├── bitmex.py
    │       │   ├── bitopro.py
    │       │   ├── bitpanda.py
    │       │   ├── bitrue.py
    │       │   ├── bitstamp.py
    │       │   ├── bitvavo.py
    │       │   ├── blockchaincom.py
    │       │   ├── blofin.py
    │       │   ├── bybit.py
    │       │   ├── cex.py
    │       │   ├── coinbase.py
    │       │   ├── coinbaseadvanced.py
    │       │   ├── coinbaseexchange.py
    │       │   ├── coinbaseinternational.py
    │       │   ├── coincatch.py
    │       │   ├── coincheck.py
    │       │   ├── coinex.py
    │       │   ├── coinone.py
    │       │   ├── cryptocom.py
    │       │   ├── currencycom.py
    │       │   ├── defx.py
    │       │   ├── deribit.py
    │       │   ├── exmo.py
    │       │   ├── gate.py
    │       │   ├── gateio.py
    │       │   ├── gemini.py
    │       │   ├── hashkey.py
    │       │   ├── hitbtc.py
    │       │   ├── hollaex.py
    │       │   ├── htx.py
    │       │   ├── huobi.py
    │       │   ├── huobijp.py
    │       │   ├── hyperliquid.py
    │       │   ├── idex.py
    │       │   ├── independentreserve.py
    │       │   ├── kraken.py
    │       │   ├── krakenfutures.py
    │       │   ├── kucoin.py
    │       │   ├── kucoinfutures.py
    │       │   ├── lbank.py
    │       │   ├── luno.py
    │       │   ├── mexc.py
    │       │   ├── myokx.py
    │       │   ├── ndax.py
    │       │   ├── okcoin.py
    │       │   ├── okx.py
    │       │   ├── onetrading.py
    │       │   ├── oxfun.py
    │       │   ├── p2b.py
    │       │   ├── paradex.py
    │       │   ├── phemex.py
    │       │   ├── poloniex.py
    │       │   ├── poloniexfutures.py
    │       │   ├── probit.py
    │       │   ├── upbit.py
    │       │   ├── vertex.py
    │       │   ├── wazirx.py
    │       │   ├── whitebit.py
    │       │   ├── woo.py
    │       │   ├── woofipro.py
    │       │   ├── xt.py
    │       │   └── test/
    │       │       ├── Exchange/
    │       │       │   ├── test_watch_balance.py
    │       │       │   ├── test_watch_bids_asks.py
    │       │       │   ├── test_watch_liquidations.py
    │       │       │   ├── test_watch_liquidations_for_symbols.py
    │       │       │   ├── test_watch_my_trades.py
    │       │       │   ├── test_watch_ohlcv.py
    │       │       │   ├── test_watch_ohlcv_for_symbols.py
    │       │       │   ├── test_watch_order_book.py
    │       │       │   ├── test_watch_order_book_for_symbols.py
    │       │       │   ├── test_watch_orders.py
    │       │       │   ├── test_watch_position.py
    │       │       │   ├── test_watch_positions.py
    │       │       │   ├── test_watch_ticker.py
    │       │       │   ├── test_watch_tickers.py
    │       │       │   ├── test_watch_trades.py
    │       │       │   └── test_watch_trades_for_symbols.py
    │       │       ├── base/
    │       │       │   ├── test_abnormal_close.py
    │       │       │   ├── test_cache.py
    │       │       │   ├── test_client_resolve.py
    │       │       │   ├── test_close.py
    │       │       │   ├── test_future.py
    │       │       │   ├── test_order_book.py
    │       │       │   ├── tests_init.py
    │       │       │   └── .gitkeep
    │       │       └── exchange/
    │       │           ├── test_watch_balance.py
    │       │           ├── test_watch_bids_asks.py
    │       │           ├── test_watch_liquidations.py
    │       │           ├── test_watch_liquidations_for_symbols.py
    │       │           ├── test_watch_my_trades.py
    │       │           ├── test_watch_ohlcv.py
    │       │           ├── test_watch_ohlcv_for_symbols.py
    │       │           ├── test_watch_order_book.py
    │       │           ├── test_watch_order_book_for_symbols.py
    │       │           ├── test_watch_orders.py
    │       │           ├── test_watch_position.py
    │       │           ├── test_watch_positions.py
    │       │           ├── test_watch_ticker.py
    │       │           ├── test_watch_tickers.py
    │       │           ├── test_watch_trades.py
    │       │           └── test_watch_trades_for_symbols.py
    │       ├── static_dependencies/
    │       │   ├── README.md
    │       │   ├── __init__.py
    │       │   ├── ecdsa/
    │       │   │   ├── __init__.py
    │       │   │   ├── _version.py
    │       │   │   ├── curves.py
    │       │   │   ├── der.py
    │       │   │   ├── ecdsa.py
    │       │   │   ├── ellipticcurve.py
    │       │   │   ├── keys.py
    │       │   │   ├── numbertheory.py
    │       │   │   ├── rfc6979.py
    │       │   │   └── util.py
    │       │   ├── ethereum/
    │       │   │   ├── __init__.py
    │       │   │   ├── abi/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── abi.py
    │       │   │   │   ├── base.py
    │       │   │   │   ├── codec.py
    │       │   │   │   ├── constants.py
    │       │   │   │   ├── decoding.py
    │       │   │   │   ├── encoding.py
    │       │   │   │   ├── exceptions.py
    │       │   │   │   ├── grammar.py
    │       │   │   │   ├── packed.py
    │       │   │   │   ├── py.typed
    │       │   │   │   ├── registry.py
    │       │   │   │   ├── tools/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── _strategies.py
    │       │   │   │   └── utils/
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── numeric.py
    │       │   │   │       ├── padding.py
    │       │   │   │       └── string.py
    │       │   │   ├── account/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── messages.py
    │       │   │   │   ├── py.typed
    │       │   │   │   └── encode_typed_data/
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── encoding_and_hashing.py
    │       │   │   │       └── helpers.py
    │       │   │   ├── hexbytes/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── _utils.py
    │       │   │   │   ├── main.py
    │       │   │   │   └── py.typed
    │       │   │   ├── typing/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── abi.py
    │       │   │   │   ├── bls.py
    │       │   │   │   ├── discovery.py
    │       │   │   │   ├── encoding.py
    │       │   │   │   ├── enums.py
    │       │   │   │   ├── ethpm.py
    │       │   │   │   ├── evm.py
    │       │   │   │   ├── networks.py
    │       │   │   │   └── py.typed
    │       │   │   └── utils/
    │       │   │       ├── __init__.py
    │       │   │       ├── abi.py
    │       │   │       ├── address.py
    │       │   │       ├── applicators.py
    │       │   │       ├── conversions.py
    │       │   │       ├── currency.py
    │       │   │       ├── debug.py
    │       │   │       ├── decorators.py
    │       │   │       ├── encoding.py
    │       │   │       ├── exceptions.py
    │       │   │       ├── functional.py
    │       │   │       ├── hexadecimal.py
    │       │   │       ├── humanize.py
    │       │   │       ├── logging.py
    │       │   │       ├── module_loading.py
    │       │   │       ├── numeric.py
    │       │   │       ├── py.typed
    │       │   │       ├── toolz.py
    │       │   │       ├── types.py
    │       │   │       ├── units.py
    │       │   │       ├── curried/
    │       │   │       │   └── __init__.py
    │       │   │       └── typing/
    │       │   │           ├── __init__.py
    │       │   │           └── misc.py
    │       │   ├── keccak/
    │       │   │   ├── __init__.py
    │       │   │   └── keccak.py
    │       │   ├── lark/
    │       │   │   ├── __init__.py
    │       │   │   ├── ast_utils.py
    │       │   │   ├── common.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── grammar.py
    │       │   │   ├── indenter.py
    │       │   │   ├── lark.py
    │       │   │   ├── lexer.py
    │       │   │   ├── load_grammar.py
    │       │   │   ├── parse_tree_builder.py
    │       │   │   ├── parser_frontends.py
    │       │   │   ├── py.typed
    │       │   │   ├── reconstruct.py
    │       │   │   ├── tree.py
    │       │   │   ├── tree_matcher.py
    │       │   │   ├── tree_templates.py
    │       │   │   ├── utils.py
    │       │   │   ├── visitors.py
    │       │   │   ├── __pyinstaller/
    │       │   │   │   ├── __init__.py
    │       │   │   │   └── hook-lark.py
    │       │   │   ├── grammars/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── common.lark
    │       │   │   │   ├── lark.lark
    │       │   │   │   ├── python.lark
    │       │   │   │   └── unicode.lark
    │       │   │   ├── parsers/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── cyk.py
    │       │   │   │   ├── earley.py
    │       │   │   │   ├── earley_common.py
    │       │   │   │   ├── earley_forest.py
    │       │   │   │   ├── grammar_analysis.py
    │       │   │   │   ├── lalr_analysis.py
    │       │   │   │   ├── lalr_interactive_parser.py
    │       │   │   │   ├── lalr_parser.py
    │       │   │   │   ├── lalr_parser_state.py
    │       │   │   │   └── xearley.py
    │       │   │   └── tools/
    │       │   │       ├── __init__.py
    │       │   │       ├── nearley.py
    │       │   │       ├── serialize.py
    │       │   │       └── standalone.py
    │       │   ├── marshmallow/
    │       │   │   ├── __init__.py
    │       │   │   ├── base.py
    │       │   │   ├── class_registry.py
    │       │   │   ├── decorators.py
    │       │   │   ├── error_store.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── fields.py
    │       │   │   ├── orderedset.py
    │       │   │   ├── py.typed
    │       │   │   ├── schema.py
    │       │   │   ├── types.py
    │       │   │   ├── utils.py
    │       │   │   ├── validate.py
    │       │   │   └── warnings.py
    │       │   ├── marshmallow_dataclass/
    │       │   │   ├── __init__.py
    │       │   │   ├── collection_field.py
    │       │   │   ├── lazy_class_attribute.py
    │       │   │   ├── mypy.py
    │       │   │   ├── py.typed
    │       │   │   ├── typing.py
    │       │   │   └── union_field.py
    │       │   ├── marshmallow_oneofschema/
    │       │   │   ├── __init__.py
    │       │   │   ├── one_of_schema.py
    │       │   │   └── py.typed
    │       │   ├── msgpack/
    │       │   │   ├── __init__.py
    │       │   │   ├── _cmsgpack.pyx
    │       │   │   ├── _packer.pyx
    │       │   │   ├── _unpacker.pyx
    │       │   │   ├── buff_converter.h
    │       │   │   ├── exceptions.py
    │       │   │   ├── ext.py
    │       │   │   ├── fallback.py
    │       │   │   ├── pack.h
    │       │   │   ├── pack_template.h
    │       │   │   ├── sysdep.h
    │       │   │   ├── unpack.h
    │       │   │   ├── unpack_define.h
    │       │   │   └── unpack_template.h
    │       │   ├── parsimonious/
    │       │   │   ├── __init__.py
    │       │   │   ├── exceptions.py
    │       │   │   ├── expressions.py
    │       │   │   ├── grammar.py
    │       │   │   ├── nodes.py
    │       │   │   └── utils.py
    │       │   ├── starknet/
    │       │   │   ├── __init__.py
    │       │   │   ├── ccxt_utils.py
    │       │   │   ├── common.py
    │       │   │   ├── constants.py
    │       │   │   ├── abi/
    │       │   │   │   ├── v0/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── model.py
    │       │   │   │   │   ├── parser.py
    │       │   │   │   │   ├── schemas.py
    │       │   │   │   │   └── shape.py
    │       │   │   │   ├── v1/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── core_structures.json
    │       │   │   │   │   ├── model.py
    │       │   │   │   │   ├── parser.py
    │       │   │   │   │   ├── parser_transformer.py
    │       │   │   │   │   ├── schemas.py
    │       │   │   │   │   └── shape.py
    │       │   │   │   └── v2/
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── model.py
    │       │   │   │       ├── parser.py
    │       │   │   │       ├── parser_transformer.py
    │       │   │   │       ├── schemas.py
    │       │   │   │       └── shape.py
    │       │   │   ├── cairo/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── data_types.py
    │       │   │   │   ├── felt.py
    │       │   │   │   ├── type_parser.py
    │       │   │   │   ├── deprecated_parse/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   ├── cairo_types.py
    │       │   │   │   │   ├── parser.py
    │       │   │   │   │   └── parser_transformer.py
    │       │   │   │   ├── v1/
    │       │   │   │   │   ├── __init__.py
    │       │   │   │   │   └── type_parser.py
    │       │   │   │   └── v2/
    │       │   │   │       ├── __init__.py
    │       │   │   │       └── type_parser.py
    │       │   │   ├── hash/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── address.py
    │       │   │   │   ├── compiled_class_hash_objects.py
    │       │   │   │   ├── selector.py
    │       │   │   │   ├── storage.py
    │       │   │   │   └── utils.py
    │       │   │   ├── models/
    │       │   │   │   ├── __init__.py
    │       │   │   │   └── typed_data.py
    │       │   │   ├── serialization/
    │       │   │   │   ├── __init__.py
    │       │   │   │   ├── _calldata_reader.py
    │       │   │   │   ├── _context.py
    │       │   │   │   ├── errors.py
    │       │   │   │   ├── factory.py
    │       │   │   │   ├── function_serialization_adapter.py
    │       │   │   │   ├── tuple_dataclass.py
    │       │   │   │   └── data_serializers/
    │       │   │   │       ├── __init__.py
    │       │   │   │       ├── _common.py
    │       │   │   │       ├── array_serializer.py
    │       │   │   │       ├── bool_serializer.py
    │       │   │   │       ├── byte_array_serializer.py
    │       │   │   │       ├── cairo_data_serializer.py
    │       │   │   │       ├── enum_serializer.py
    │       │   │   │       ├── felt_serializer.py
    │       │   │   │       ├── named_tuple_serializer.py
    │       │   │   │       ├── option_serializer.py
    │       │   │   │       ├── output_serializer.py
    │       │   │   │       ├── payload_serializer.py
    │       │   │   │       ├── struct_serializer.py
    │       │   │   │       ├── tuple_serializer.py
    │       │   │   │       ├── uint256_serializer.py
    │       │   │   │       ├── uint_serializer.py
    │       │   │   │       └── unit_serializer.py
    │       │   │   └── utils/
    │       │   │       ├── __init__.py
    │       │   │       ├── constructor_args_translator.py
    │       │   │       ├── iterable.py
    │       │   │       ├── schema.py
    │       │   │       └── typed_data.py
    │       │   ├── starkware/
    │       │   │   ├── __init__.py
    │       │   │   └── crypto/
    │       │   │       ├── __init__.py
    │       │   │       ├── fast_pedersen_hash.py
    │       │   │       ├── math_utils.py
    │       │   │       ├── signature.py
    │       │   │       └── utils.py
    │       │   ├── sympy/
    │       │   │   ├── __init__.py
    │       │   │   ├── core/
    │       │   │   │   ├── __init__.py
    │       │   │   │   └── intfunc.py
    │       │   │   └── external/
    │       │   │       ├── __init__.py
    │       │   │       ├── gmpy.py
    │       │   │       ├── importtools.py
    │       │   │       ├── ntheory.py
    │       │   │       └── pythonmpq.py
    │       │   ├── toolz/
    │       │   │   ├── __init__.py
    │       │   │   ├── _signatures.py
    │       │   │   ├── _version.py
    │       │   │   ├── compatibility.py
    │       │   │   ├── dicttoolz.py
    │       │   │   ├── functoolz.py
    │       │   │   ├── itertoolz.py
    │       │   │   ├── recipes.py
    │       │   │   ├── utils.py
    │       │   │   └── curried/
    │       │   │       ├── __init__.py
    │       │   │       ├── exceptions.py
    │       │   │       └── operator.py
    │       │   └── typing_inspect/
    │       │       ├── __init__.py
    │       │       └── typing_inspect.py
    │       └── test/
    │           ├── __init__.py
    │           ├── tests_async.py
    │           ├── tests_helpers.py
    │           ├── tests_init.py
    │           ├── tests_sync.py
    │           ├── base/
    │           │   ├── test_after_constructor.py
    │           │   ├── test_cryptography.py
    │           │   ├── test_datetime.py
    │           │   ├── test_deep_extend.py
    │           │   ├── test_extend.py
    │           │   ├── test_filter_by.py
    │           │   ├── test_group_by.py
    │           │   ├── test_json.py
    │           │   ├── test_number.py
    │           │   ├── test_omit.py
    │           │   ├── test_safe_methods.py
    │           │   ├── test_sort_by.py
    │           │   ├── test_sum.py
    │           │   ├── tests_init.py
    │           │   └── language_specific/
    │           │       └── test_language_specific.py
    │           ├── custom/
    │           │   └── .gitignore
    │           └── exchange/
    │               ├── async/
    │               │   ├── test_create_order.py
    │               │   ├── test_features.py
    │               │   ├── test_fetch_accounts.py
    │               │   ├── test_fetch_balance.py
    │               │   ├── test_fetch_borrow_interest.py
    │               │   ├── test_fetch_closed_orders.py
    │               │   ├── test_fetch_currencies.py
    │               │   ├── test_fetch_deposit_withdrawals.py
    │               │   ├── test_fetch_deposits.py
    │               │   ├── test_fetch_funding_rate_history.py
    │               │   ├── test_fetch_l2_order_book.py
    │               │   ├── test_fetch_last_prices.py
    │               │   ├── test_fetch_ledger.py
    │               │   ├── test_fetch_ledger_entry.py
    │               │   ├── test_fetch_leverage_tiers.py
    │               │   ├── test_fetch_liquidations.py
    │               │   ├── test_fetch_margin_mode.py
    │               │   ├── test_fetch_margin_modes.py
    │               │   ├── test_fetch_market_leverage_tiers.py
    │               │   ├── test_fetch_markets.py
    │               │   ├── test_fetch_my_liquidations.py
    │               │   ├── test_fetch_my_trades.py
    │               │   ├── test_fetch_ohlcv.py
    │               │   ├── test_fetch_open_interest_history.py
    │               │   ├── test_fetch_open_orders.py
    │               │   ├── test_fetch_order_book.py
    │               │   ├── test_fetch_order_books.py
    │               │   ├── test_fetch_orders.py
    │               │   ├── test_fetch_positions.py
    │               │   ├── test_fetch_status.py
    │               │   ├── test_fetch_ticker.py
    │               │   ├── test_fetch_tickers.py
    │               │   ├── test_fetch_trades.py
    │               │   ├── test_fetch_trading_fee.py
    │               │   ├── test_fetch_trading_fees.py
    │               │   ├── test_fetch_transaction_fees.py
    │               │   ├── test_fetch_withdrawals.py
    │               │   ├── test_load_markets.py
    │               │   ├── test_proxies.py
    │               │   └── test_sign_in.py
    │               ├── base/
    │               │   ├── __init__.py
    │               │   ├── test_account.py
    │               │   ├── test_balance.py
    │               │   ├── test_borrow_interest.py
    │               │   ├── test_borrow_rate.py
    │               │   ├── test_currency.py
    │               │   ├── test_deposit_withdrawal.py
    │               │   ├── test_funding_rate_history.py
    │               │   ├── test_last_price.py
    │               │   ├── test_ledger_entry.py
    │               │   ├── test_leverage_tier.py
    │               │   ├── test_liquidation.py
    │               │   ├── test_margin_mode.py
    │               │   ├── test_margin_modification.py
    │               │   ├── test_market.py
    │               │   ├── test_ohlcv.py
    │               │   ├── test_open_interest.py
    │               │   ├── test_order.py
    │               │   ├── test_order_book.py
    │               │   ├── test_position.py
    │               │   ├── test_shared_methods.py
    │               │   ├── test_status.py
    │               │   ├── test_ticker.py
    │               │   ├── test_trade.py
    │               │   └── test_trading_fee.py
    │               └── sync/
    │                   ├── test_create_order.py
    │                   ├── test_features.py
    │                   ├── test_fetch_accounts.py
    │                   ├── test_fetch_balance.py
    │                   ├── test_fetch_borrow_interest.py
    │                   ├── test_fetch_closed_orders.py
    │                   ├── test_fetch_currencies.py
    │                   ├── test_fetch_deposit_withdrawals.py
    │                   ├── test_fetch_deposits.py
    │                   ├── test_fetch_funding_rate_history.py
    │                   ├── test_fetch_l2_order_book.py
    │                   ├── test_fetch_last_prices.py
    │                   ├── test_fetch_ledger.py
    │                   ├── test_fetch_ledger_entry.py
    │                   ├── test_fetch_leverage_tiers.py
    │                   ├── test_fetch_liquidations.py
    │                   ├── test_fetch_margin_mode.py
    │                   ├── test_fetch_margin_modes.py
    │                   ├── test_fetch_market_leverage_tiers.py
    │                   ├── test_fetch_markets.py
    │                   ├── test_fetch_my_liquidations.py
    │                   ├── test_fetch_my_trades.py
    │                   ├── test_fetch_ohlcv.py
    │                   ├── test_fetch_open_interest_history.py
    │                   ├── test_fetch_open_orders.py
    │                   ├── test_fetch_order_book.py
    │                   ├── test_fetch_order_books.py
    │                   ├── test_fetch_orders.py
    │                   ├── test_fetch_positions.py
    │                   ├── test_fetch_status.py
    │                   ├── test_fetch_ticker.py
    │                   ├── test_fetch_tickers.py
    │                   ├── test_fetch_trades.py
    │                   ├── test_fetch_trading_fee.py
    │                   ├── test_fetch_trading_fees.py
    │                   ├── test_fetch_transaction_fees.py
    │                   ├── test_fetch_withdrawals.py
    │                   ├── test_load_markets.py
    │                   ├── test_proxies.py
    │                   └── test_sign_in.py
    ├── ts/
    │   ├── ccxt.ts
    │   └── src/
    │       ├── ace.ts
    │       ├── alpaca.ts
    │       ├── ascendex.ts
    │       ├── bequant.ts
    │       ├── bigone.ts
    │       ├── binance.ts
    │       ├── binancecoinm.ts
    │       ├── binanceus.ts
    │       ├── binanceusdm.ts
    │       ├── bingx.ts
    │       ├── bit2c.ts
    │       ├── bitbank.ts
    │       ├── bitbns.ts
    │       ├── bitcoincom.ts
    │       ├── bitfinex.ts
    │       ├── bitfinex1.ts
    │       ├── bitflyer.ts
    │       ├── bitget.ts
    │       ├── bithumb.ts
    │       ├── bitmart.ts
    │       ├── bitmex.ts
    │       ├── bitopro.ts
    │       ├── bitpanda.ts
    │       ├── bitrue.ts
    │       ├── bitso.ts
    │       ├── bitstamp.ts
    │       ├── bitteam.ts
    │       ├── bitvavo.ts
    │       ├── bl3p.ts
    │       ├── blockchaincom.ts
    │       ├── blofin.ts
    │       ├── btcalpha.ts
    │       ├── btcbox.ts
    │       ├── btcmarkets.ts
    │       ├── btcturk.ts
    │       ├── bybit.ts
    │       ├── cex.ts
    │       ├── coinbase.ts
    │       ├── coinbaseadvanced.ts
    │       ├── coinbaseexchange.ts
    │       ├── coinbaseinternational.ts
    │       ├── coincatch.ts
    │       ├── coincheck.ts
    │       ├── coinex.ts
    │       ├── coinlist.ts
    │       ├── coinmate.ts
    │       ├── coinmetro.ts
    │       ├── coinone.ts
    │       ├── coinsph.ts
    │       ├── coinspot.ts
    │       ├── cryptocom.ts
    │       ├── currencycom.ts
    │       ├── defx.ts
    │       ├── delta.ts
    │       ├── deribit.ts
    │       ├── digifinex.ts
    │       ├── ellipx.ts
    │       ├── exmo.ts
    │       ├── fmfwio.ts
    │       ├── gate.ts
    │       ├── gateio.ts
    │       ├── gemini.ts
    │       ├── hashkey.ts
    │       ├── hitbtc.ts
    │       ├── hollaex.ts
    │       ├── htx.ts
    │       ├── huobi.ts
    │       ├── huobijp.ts
    │       ├── hyperliquid.ts
    │       ├── idex.ts
    │       ├── independentreserve.ts
    │       ├── indodax.ts
    │       ├── kraken.ts
    │       ├── krakenfutures.ts
    │       ├── kucoin.ts
    │       ├── kucoinfutures.ts
    │       ├── kuna.ts
    │       ├── latoken.ts
    │       ├── lbank.ts
    │       ├── luno.ts
    │       ├── mercado.ts
    │       ├── mexc.ts
    │       ├── myokx.ts
    │       ├── ndax.ts
    │       ├── novadax.ts
    │       ├── oceanex.ts
    │       ├── okcoin.ts
    │       ├── okx.ts
    │       ├── onetrading.ts
    │       ├── oxfun.ts
    │       ├── p2b.ts
    │       ├── paradex.ts
    │       ├── paymium.ts
    │       ├── phemex.ts
    │       ├── poloniex.ts
    │       ├── poloniexfutures.ts
    │       ├── probit.ts
    │       ├── timex.ts
    │       ├── tokocrypto.ts
    │       ├── tradeogre.ts
    │       ├── upbit.ts
    │       ├── vertex.ts
    │       ├── wavesexchange.ts
    │       ├── whitebit.ts
    │       ├── woo.ts
    │       ├── woofipro.ts
    │       ├── xt.ts
    │       ├── yobit.ts
    │       ├── zaif.ts
    │       ├── zonda.ts
    │       ├── .eslintrc
    │       ├── abstract/
    │       │   ├── ace.ts
    │       │   ├── alpaca.ts
    │       │   ├── ascendex.ts
    │       │   ├── bequant.ts
    │       │   ├── bigone.ts
    │       │   ├── binance.ts
    │       │   ├── binancecoinm.ts
    │       │   ├── binanceus.ts
    │       │   ├── binanceusdm.ts
    │       │   ├── bingx.ts
    │       │   ├── bit2c.ts
    │       │   ├── bitbank.ts
    │       │   ├── bitbns.ts
    │       │   ├── bitcoincom.ts
    │       │   ├── bitfinex.ts
    │       │   ├── bitfinex1.ts
    │       │   ├── bitflyer.ts
    │       │   ├── bitget.ts
    │       │   ├── bithumb.ts
    │       │   ├── bitmart.ts
    │       │   ├── bitmex.ts
    │       │   ├── bitopro.ts
    │       │   ├── bitpanda.ts
    │       │   ├── bitrue.ts
    │       │   ├── bitso.ts
    │       │   ├── bitstamp.ts
    │       │   ├── bitteam.ts
    │       │   ├── bitvavo.ts
    │       │   ├── bl3p.ts
    │       │   ├── blockchaincom.ts
    │       │   ├── blofin.ts
    │       │   ├── btcalpha.ts
    │       │   ├── btcbox.ts
    │       │   ├── btcmarkets.ts
    │       │   ├── btcturk.ts
    │       │   ├── bybit.ts
    │       │   ├── cex.ts
    │       │   ├── coinbase.ts
    │       │   ├── coinbaseadvanced.ts
    │       │   ├── coinbaseexchange.ts
    │       │   ├── coinbaseinternational.ts
    │       │   ├── coincatch.ts
    │       │   ├── coincheck.ts
    │       │   ├── coinex.ts
    │       │   ├── coinlist.ts
    │       │   ├── coinmate.ts
    │       │   ├── coinmetro.ts
    │       │   ├── coinone.ts
    │       │   ├── coinsph.ts
    │       │   ├── coinspot.ts
    │       │   ├── cryptocom.ts
    │       │   ├── currencycom.ts
    │       │   ├── defx.ts
    │       │   ├── delta.ts
    │       │   ├── deribit.ts
    │       │   ├── digifinex.ts
    │       │   ├── ellipx.ts
    │       │   ├── exmo.ts
    │       │   ├── fmfwio.ts
    │       │   ├── gate.ts
    │       │   ├── gateio.ts
    │       │   ├── gemini.ts
    │       │   ├── hashkey.ts
    │       │   ├── hitbtc.ts
    │       │   ├── hollaex.ts
    │       │   ├── htx.ts
    │       │   ├── huobi.ts
    │       │   ├── huobijp.ts
    │       │   ├── hyperliquid.ts
    │       │   ├── idex.ts
    │       │   ├── independentreserve.ts
    │       │   ├── indodax.ts
    │       │   ├── kraken.ts
    │       │   ├── krakenfutures.ts
    │       │   ├── kucoin.ts
    │       │   ├── kucoinfutures.ts
    │       │   ├── kuna.ts
    │       │   ├── latoken.ts
    │       │   ├── lbank.ts
    │       │   ├── luno.ts
    │       │   ├── mercado.ts
    │       │   ├── mexc.ts
    │       │   ├── myokx.ts
    │       │   ├── ndax.ts
    │       │   ├── novadax.ts
    │       │   ├── oceanex.ts
    │       │   ├── okcoin.ts
    │       │   ├── okx.ts
    │       │   ├── onetrading.ts
    │       │   ├── oxfun.ts
    │       │   ├── p2b.ts
    │       │   ├── paradex.ts
    │       │   ├── paymium.ts
    │       │   ├── phemex.ts
    │       │   ├── poloniex.ts
    │       │   ├── poloniexfutures.ts
    │       │   ├── probit.ts
    │       │   ├── timex.ts
    │       │   ├── tokocrypto.ts
    │       │   ├── tradeogre.ts
    │       │   ├── upbit.ts
    │       │   ├── vertex.ts
    │       │   ├── wavesexchange.ts
    │       │   ├── whitebit.ts
    │       │   ├── woo.ts
    │       │   ├── woofipro.ts
    │       │   ├── xt.ts
    │       │   ├── yobit.ts
    │       │   ├── zaif.ts
    │       │   └── zonda.ts
    │       ├── base/
    │       │   ├── Exchange.ts
    │       │   ├── Precise.ts
    │       │   ├── errorHierarchy.ts
    │       │   ├── errors.ts
    │       │   ├── functions.ts
    │       │   ├── types.ts
    │       │   ├── functions/
    │       │   │   ├── crypto.ts
    │       │   │   ├── encode.ts
    │       │   │   ├── generic.ts
    │       │   │   ├── misc.ts
    │       │   │   ├── number.ts
    │       │   │   ├── platform.ts
    │       │   │   ├── rsa.ts
    │       │   │   ├── string.ts
    │       │   │   ├── throttle.ts
    │       │   │   ├── time.ts
    │       │   │   ├── totp.ts
    │       │   │   └── type.ts
    │       │   └── ws/
    │       │       ├── Cache.ts
    │       │       ├── Client.ts
    │       │       ├── Future.ts
    │       │       ├── OrderBook.ts
    │       │       ├── OrderBookSide.ts
    │       │       ├── WsClient.ts
    │       │       ├── functions.ts
    │       │       └── .eslintrc.cjs
    │       ├── pro/
    │       │   ├── alpaca.ts
    │       │   ├── ascendex.ts
    │       │   ├── bequant.ts
    │       │   ├── binance.ts
    │       │   ├── binancecoinm.ts
    │       │   ├── binanceus.ts
    │       │   ├── binanceusdm.ts
    │       │   ├── bingx.ts
    │       │   ├── bitcoincom.ts
    │       │   ├── bitfinex.ts
    │       │   ├── bitfinex1.ts
    │       │   ├── bitget.ts
    │       │   ├── bithumb.ts
    │       │   ├── bitmart.ts
    │       │   ├── bitmex.ts
    │       │   ├── bitopro.ts
    │       │   ├── bitpanda.ts
    │       │   ├── bitrue.ts
    │       │   ├── bitstamp.ts
    │       │   ├── bitvavo.ts
    │       │   ├── blockchaincom.ts
    │       │   ├── blofin.ts
    │       │   ├── bybit.ts
    │       │   ├── cex.ts
    │       │   ├── coinbase.ts
    │       │   ├── coinbaseadvanced.ts
    │       │   ├── coinbaseexchange.ts
    │       │   ├── coinbaseinternational.ts
    │       │   ├── coincatch.ts
    │       │   ├── coincheck.ts
    │       │   ├── coinex.ts
    │       │   ├── coinone.ts
    │       │   ├── cryptocom.ts
    │       │   ├── currencycom.ts
    │       │   ├── defx.ts
    │       │   ├── deribit.ts
    │       │   ├── exmo.ts
    │       │   ├── gate.ts
    │       │   ├── gateio.ts
    │       │   ├── gemini.ts
    │       │   ├── hashkey.ts
    │       │   ├── hitbtc.ts
    │       │   ├── hollaex.ts
    │       │   ├── htx.ts
    │       │   ├── huobi.ts
    │       │   ├── huobijp.ts
    │       │   ├── hyperliquid.ts
    │       │   ├── idex.ts
    │       │   ├── independentreserve.ts
    │       │   ├── kraken.ts
    │       │   ├── krakenfutures.ts
    │       │   ├── kucoin.ts
    │       │   ├── kucoinfutures.ts
    │       │   ├── lbank.ts
    │       │   ├── luno.ts
    │       │   ├── mexc.ts
    │       │   ├── myokx.ts
    │       │   ├── ndax.ts
    │       │   ├── okcoin.ts
    │       │   ├── okx.ts
    │       │   ├── onetrading.ts
    │       │   ├── oxfun.ts
    │       │   ├── p2b.ts
    │       │   ├── paradex.ts
    │       │   ├── phemex.ts
    │       │   ├── poloniex.ts
    │       │   ├── poloniexfutures.ts
    │       │   ├── probit.ts
    │       │   ├── upbit.ts
    │       │   ├── vertex.ts
    │       │   ├── whitebit.ts
    │       │   ├── woo.ts
    │       │   ├── woofipro.ts
    │       │   ├── xt.ts
    │       │   └── test/
    │       │       ├── .eslintrc
    │       │       ├── Exchange/
    │       │       │   ├── test.watchBalance.ts
    │       │       │   ├── test.watchBidsAsks.ts
    │       │       │   ├── test.watchLiquidations.ts
    │       │       │   ├── test.watchLiquidationsForSymbols.ts
    │       │       │   ├── test.watchMyTrades.ts
    │       │       │   ├── test.watchOHLCV.ts
    │       │       │   ├── test.watchOHLCVForSymbols.ts
    │       │       │   ├── test.watchOrderBook.ts
    │       │       │   ├── test.watchOrderBookForSymbols.ts
    │       │       │   ├── test.watchOrders.ts
    │       │       │   ├── test.watchPosition.ts
    │       │       │   ├── test.watchPositions.ts
    │       │       │   ├── test.watchTicker.ts
    │       │       │   ├── test.watchTickers.ts
    │       │       │   ├── test.watchTrades.ts
    │       │       │   └── test.watchTradesForSymbols.ts
    │       │       ├── base/
    │       │       │   ├── test.cache.ts
    │       │       │   ├── test.client.resolve.ts
    │       │       │   ├── test.close.ts
    │       │       │   ├── test.orderBook.ts
    │       │       │   ├── test.watchWithDelay.ts
    │       │       │   └── tests.init.ts
    │       │       └── custom/
    │       │           ├── fastMessageServer.ts
    │       │           └── server.ts
    │       ├── static_dependencies/
    │       │   ├── README.md
    │       │   ├── ethers/
    │       │   │   ├── abi-coder.ts
    │       │   │   ├── bytes32.ts
    │       │   │   ├── fragments.ts
    │       │   │   ├── index.ts
    │       │   │   ├── interface.ts
    │       │   │   ├── typed.ts
    │       │   │   ├── address/
    │       │   │   │   ├── address.ts
    │       │   │   │   ├── checks.ts
    │       │   │   │   ├── contract-address.ts
    │       │   │   │   └── index.ts
    │       │   │   ├── coders/
    │       │   │   │   ├── abstract-coder.ts
    │       │   │   │   ├── address.ts
    │       │   │   │   ├── anonymous.ts
    │       │   │   │   ├── array.ts
    │       │   │   │   ├── boolean.ts
    │       │   │   │   ├── bytes.ts
    │       │   │   │   ├── fixed-bytes.ts
    │       │   │   │   ├── null.ts
    │       │   │   │   ├── number.ts
    │       │   │   │   ├── string.ts
    │       │   │   │   └── tuple.ts
    │       │   │   ├── hash/
    │       │   │   │   ├── index.ts
    │       │   │   │   ├── solidity.ts
    │       │   │   │   └── typed-data.ts
    │       │   │   └── utils/
    │       │   │       ├── base58.ts
    │       │   │       ├── base64-browser.ts
    │       │   │       ├── base64.ts
    │       │   │       ├── data.ts
    │       │   │       ├── errors.ts
    │       │   │       ├── events.ts
    │       │   │       ├── fixednumber.ts
    │       │   │       ├── index.ts
    │       │   │       ├── maths.ts
    │       │   │       ├── properties.ts
    │       │   │       ├── rlp-decode.ts
    │       │   │       ├── rlp-encode.ts
    │       │   │       ├── rlp.ts
    │       │   │       ├── test.txt
    │       │   │       ├── units.ts
    │       │   │       ├── utf8.ts
    │       │   │       └── uuid.ts
    │       │   ├── fflake/
    │       │   │   └── browser.js
    │       │   ├── jsencrypt/
    │       │   │   ├── JSEncrypt.ts
    │       │   │   ├── JSEncryptRSAKey.ts
    │       │   │   ├── LICENSE.txt
    │       │   │   ├── index.ts
    │       │   │   └── lib/
    │       │   │       ├── asn1js/
    │       │   │       │   ├── LICENSE.txt
    │       │   │       │   ├── asn1.ts
    │       │   │       │   ├── base64.ts
    │       │   │       │   ├── hex.ts
    │       │   │       │   ├── int10.ts
    │       │   │       │   └── oids.ts
    │       │   │       ├── jsbn/
    │       │   │       │   ├── README.md
    │       │   │       │   ├── LICENSE.txt
    │       │   │       │   ├── base64.ts
    │       │   │       │   ├── jsbn.ts
    │       │   │       │   ├── prng4.ts
    │       │   │       │   ├── rng.ts
    │       │   │       │   ├── rsa.ts
    │       │   │       │   └── util.ts
    │       │   │       └── jsrsasign/
    │       │   │           ├── LICENSE.txt
    │       │   │           ├── asn1-1.0.d.ts
    │       │   │           ├── asn1-1.0.ts
    │       │   │           ├── yahoo.d.ts
    │       │   │           └── yahoo.js
    │       │   ├── messagepack/
    │       │   │   ├── msgpack.d.ts
    │       │   │   └── msgpack.js
    │       │   ├── noble-curves/
    │       │   │   ├── README.md
    │       │   │   ├── _shortw_utils.ts
    │       │   │   ├── bn.ts
    │       │   │   ├── ed25519.ts
    │       │   │   ├── ed448.ts
    │       │   │   ├── index.ts
    │       │   │   ├── jubjub.ts
    │       │   │   ├── p256.ts
    │       │   │   ├── p384.ts
    │       │   │   ├── p521.ts
    │       │   │   ├── pasta.ts
    │       │   │   ├── secp256k1.ts
    │       │   │   └── abstract/
    │       │   │       ├── curve.ts
    │       │   │       ├── edwards.ts
    │       │   │       ├── hash-to-curve.ts
    │       │   │       ├── modular.ts
    │       │   │       ├── montgomery.ts
    │       │   │       ├── poseidon.ts
    │       │   │       ├── utils.ts
    │       │   │       └── weierstrass.ts
    │       │   ├── noble-hashes/
    │       │   │   ├── README.md
    │       │   │   ├── _assert.ts
    │       │   │   ├── _blake2.ts
    │       │   │   ├── _sha2.ts
    │       │   │   ├── _u64.ts
    │       │   │   ├── argon2.ts
    │       │   │   ├── blake2b.ts
    │       │   │   ├── blake2s.ts
    │       │   │   ├── blake3.ts
    │       │   │   ├── crypto.ts
    │       │   │   ├── cryptoNode.ts
    │       │   │   ├── eskdf.ts
    │       │   │   ├── hkdf.ts
    │       │   │   ├── hmac.ts
    │       │   │   ├── index.ts
    │       │   │   ├── md5.ts
    │       │   │   ├── pbkdf2.ts
    │       │   │   ├── ripemd160.ts
    │       │   │   ├── scrypt.ts
    │       │   │   ├── sha1.ts
    │       │   │   ├── sha256.ts
    │       │   │   ├── sha3-addons.ts
    │       │   │   ├── sha3.ts
    │       │   │   ├── sha512.ts
    │       │   │   └── utils.ts
    │       │   ├── node-fetch/
    │       │   │   ├── body.js
    │       │   │   ├── diff.txt
    │       │   │   ├── headers.js
    │       │   │   ├── index.d.ts
    │       │   │   ├── index.js
    │       │   │   ├── request.js
    │       │   │   ├── response.js
    │       │   │   ├── errors/
    │       │   │   │   ├── abort-error.js
    │       │   │   │   ├── base.js
    │       │   │   │   └── fetch-error.js
    │       │   │   └── utils/
    │       │   │       ├── get-search.js
    │       │   │       ├── is-redirect.js
    │       │   │       ├── is.js
    │       │   │       └── referrer.js
    │       │   ├── proxies/
    │       │   │   ├── agent-base/
    │       │   │   │   ├── README.md
    │       │   │   │   ├── helpers.ts
    │       │   │   │   └── index.ts
    │       │   │   ├── http-proxy-agent/
    │       │   │   │   ├── LICENSE
    │       │   │   │   └── index.ts
    │       │   │   └── https-proxy-agent/
    │       │   │       ├── README.md
    │       │   │       ├── index.ts
    │       │   │       └── parse-proxy-response.ts
    │       │   ├── qs/
    │       │   │   ├── formats.cjs
    │       │   │   ├── index.cjs
    │       │   │   ├── parse.cjs
    │       │   │   ├── stringify.cjs
    │       │   │   └── utils.cjs
    │       │   ├── scure-base/
    │       │   │   ├── README.md
    │       │   │   └── index.ts
    │       │   ├── scure-starknet/
    │       │   │   ├── README.md
    │       │   │   └── index.ts
    │       │   ├── starknet/
    │       │   │   ├── README.md
    │       │   │   ├── constants.ts
    │       │   │   ├── index.ts
    │       │   │   ├── types/
    │       │   │   │   ├── cairoEnum.ts
    │       │   │   │   ├── calldata.ts
    │       │   │   │   ├── index.ts
    │       │   │   │   ├── typedData.ts
    │       │   │   │   └── lib/
    │       │   │   │       ├── index.ts
    │       │   │   │       └── contract/
    │       │   │   │           ├── abi.ts
    │       │   │   │           ├── index.ts
    │       │   │   │           ├── legacy.ts
    │       │   │   │           └── sierra.ts
    │       │   │   └── utils/
    │       │   │       ├── address.ts
    │       │   │       ├── assert.ts
    │       │   │       ├── encode.ts
    │       │   │       ├── merkle.ts
    │       │   │       ├── num.ts
    │       │   │       ├── selector.ts
    │       │   │       ├── shortString.ts
    │       │   │       ├── starknetId.ts
    │       │   │       ├── typedData.ts
    │       │   │       ├── uint256.ts
    │       │   │       ├── url.ts
    │       │   │       ├── cairoDataTypes/
    │       │   │       │   ├── felt.ts
    │       │   │       │   ├── uint256.ts
    │       │   │       │   └── uint512.ts
    │       │   │       ├── calldata/
    │       │   │       │   ├── byteArray.ts
    │       │   │       │   ├── cairo.ts
    │       │   │       │   ├── formatter.ts
    │       │   │       │   ├── index.ts
    │       │   │       │   ├── propertyOrder.ts
    │       │   │       │   ├── requestParser.ts
    │       │   │       │   ├── responseParser.ts
    │       │   │       │   ├── tuple.ts
    │       │   │       │   ├── validate.ts
    │       │   │       │   ├── enum/
    │       │   │       │   │   ├── CairoCustomEnum.ts
    │       │   │       │   │   ├── CairoOption.ts
    │       │   │       │   │   ├── CairoResult.ts
    │       │   │       │   │   └── index.ts
    │       │   │       │   └── parser/
    │       │   │       │       ├── index.ts
    │       │   │       │       ├── interface.ts
    │       │   │       │       ├── parser-0-1.1.0.ts
    │       │   │       │       └── parser-2.0.0.ts
    │       │   │       └── hash/
    │       │   │           ├── classHash.ts
    │       │   │           └── index.ts
    │       │   └── watchable/
    │       │       ├── README.md
    │       │       ├── CHANGELOG.md
    │       │       ├── LICENSE
    │       │       └── src/
    │       │           ├── index.ts
    │       │           ├── types.ts
    │       │           └── unpromise.ts
    │       └── test/
    │           ├── tests.helpers.ts
    │           ├── tests.init.ts
    │           ├── tests.ts
    │           ├── .eslintrc
    │           ├── Exchange/
    │           │   ├── test.createOrder.ts
    │           │   ├── test.features.ts
    │           │   ├── test.fetchAccounts.ts
    │           │   ├── test.fetchBalance.ts
    │           │   ├── test.fetchBorrowInterest.ts
    │           │   ├── test.fetchClosedOrders.ts
    │           │   ├── test.fetchCurrencies.ts
    │           │   ├── test.fetchDepositWithdrawals.ts
    │           │   ├── test.fetchDeposits.ts
    │           │   ├── test.fetchFundingRateHistory.ts
    │           │   ├── test.fetchL2OrderBook.ts
    │           │   ├── test.fetchLastPrices.ts
    │           │   ├── test.fetchLedger.ts
    │           │   ├── test.fetchLedgerEntry.ts
    │           │   ├── test.fetchLeverageTiers.ts
    │           │   ├── test.fetchLiquidations.ts
    │           │   ├── test.fetchMarginMode.ts
    │           │   ├── test.fetchMarginModes.ts
    │           │   ├── test.fetchMarketLeverageTiers.ts
    │           │   ├── test.fetchMarkets.ts
    │           │   ├── test.fetchMyLiquidations.ts
    │           │   ├── test.fetchMyTrades.ts
    │           │   ├── test.fetchOHLCV.ts
    │           │   ├── test.fetchOpenInterestHistory.ts
    │           │   ├── test.fetchOpenOrders.ts
    │           │   ├── test.fetchOrderBook.ts
    │           │   ├── test.fetchOrderBooks.ts
    │           │   ├── test.fetchOrders.ts
    │           │   ├── test.fetchPositions.ts
    │           │   ├── test.fetchStatus.ts
    │           │   ├── test.fetchTicker.ts
    │           │   ├── test.fetchTickers.ts
    │           │   ├── test.fetchTrades.ts
    │           │   ├── test.fetchTradingFee.ts
    │           │   ├── test.fetchTradingFees.ts
    │           │   ├── test.fetchTransactionFees.ts
    │           │   ├── test.fetchWithdrawals.ts
    │           │   ├── test.loadMarkets.ts
    │           │   ├── test.proxies.ts
    │           │   ├── test.signIn.ts
    │           │   └── base/
    │           │       ├── test.account.ts
    │           │       ├── test.balance.ts
    │           │       ├── test.borrowInterest.ts
    │           │       ├── test.borrowRate.ts
    │           │       ├── test.currency.ts
    │           │       ├── test.depositWithdrawal.ts
    │           │       ├── test.fundingRateHistory.ts
    │           │       ├── test.lastPrice.ts
    │           │       ├── test.ledgerEntry.ts
    │           │       ├── test.leverageTier.ts
    │           │       ├── test.liquidation.ts
    │           │       ├── test.marginMode.ts
    │           │       ├── test.marginModification.ts
    │           │       ├── test.market.ts
    │           │       ├── test.ohlcv.ts
    │           │       ├── test.openInterest.ts
    │           │       ├── test.order.ts
    │           │       ├── test.orderBook.ts
    │           │       ├── test.position.ts
    │           │       ├── test.sharedMethods.ts
    │           │       ├── test.status.ts
    │           │       ├── test.ticker.ts
    │           │       ├── test.trade.ts
    │           │       └── test.tradingFee.ts
    │           ├── base/
    │           │   ├── test.afterConstructor.ts
    │           │   ├── test.cryptography.ts
    │           │   ├── test.datetime.ts
    │           │   ├── test.deepExtend.ts
    │           │   ├── test.extend.ts
    │           │   ├── test.filterBy.ts
    │           │   ├── test.groupBy.ts
    │           │   ├── test.json.ts
    │           │   ├── test.number.ts
    │           │   ├── test.omit.ts
    │           │   ├── test.safeMethods.ts
    │           │   ├── test.sortBy.ts
    │           │   ├── test.sum.ts
    │           │   ├── tests.init.ts
    │           │   ├── errors/
    │           │   │   ├── test.InsufficientFunds.ts
    │           │   │   ├── test.InvalidNonce.ts
    │           │   │   ├── test.InvalidOrder.ts
    │           │   │   └── test.OrderNotFound.ts
    │           │   └── language_specific/
    │           │       ├── test.aggregate.ts
    │           │       ├── test.calculateFee.ts
    │           │       ├── test.camelcase.ts
    │           │       ├── test.config.ts
    │           │       ├── test.languageSpecific.ts
    │           │       ├── test.legacyHas.ts
    │           │       ├── test.safeBalance.ts
    │           │       ├── test.throttle.ts
    │           │       ├── test.time.ts
    │           │       ├── test.timeout_hang.ts
    │           │       ├── test.type.ts
    │           │       └── test.uncamelcase.ts
    │           ├── custom/
    │           │   └── .gitignore
    │           └── static/
    │               ├── currencies/
    │               │   ├── ace.json
    │               │   ├── alpaca.json
    │               │   ├── ascendex.json
    │               │   ├── bequant.json
    │               │   ├── bigone.json
    │               │   ├── binance.json
    │               │   ├── binanceus.json
    │               │   ├── bingx.json
    │               │   ├── bit2c.json
    │               │   ├── bitbns.json
    │               │   ├── bitfinex.json
    │               │   ├── bitfinex1.json
    │               │   ├── bitflyer.json
    │               │   ├── bitget.json
    │               │   ├── bithumb.json
    │               │   ├── bitmart.json
    │               │   ├── bitmex.json
    │               │   ├── bitopro.json
    │               │   ├── bitrue.json
    │               │   ├── bitso.json
    │               │   ├── bitstamp.json
    │               │   ├── bitteam.json
    │               │   ├── bitvavo.json
    │               │   ├── bl3p.json
    │               │   ├── blockchaincom.json
    │               │   ├── blofin.json
    │               │   ├── btcalpha.json
    │               │   ├── bybit.json
    │               │   ├── cex.json
    │               │   ├── coinbase.json
    │               │   ├── coinbaseexchange.json
    │               │   ├── coinbaseinternational.json
    │               │   ├── coincatch.json
    │               │   ├── coinex.json
    │               │   ├── coinlist.json
    │               │   ├── coinmate.json
    │               │   ├── coinmetro.json
    │               │   ├── coinone.json
    │               │   ├── coinsph.json
    │               │   ├── cryptocom.json
    │               │   ├── currencycom.json
    │               │   ├── defx.json
    │               │   ├── delta.json
    │               │   ├── deribit.json
    │               │   ├── digifinex.json
    │               │   ├── ellipx.json
    │               │   ├── exmo.json
    │               │   ├── gate.json
    │               │   ├── gemini.json
    │               │   ├── hashkey.json
    │               │   ├── hitbtc.json
    │               │   ├── hollaex.json
    │               │   ├── htx.json
    │               │   ├── huobijp.json
    │               │   ├── hyperliquid.json
    │               │   ├── idex.json
    │               │   ├── independentreserve.json
    │               │   ├── indodax.json
    │               │   ├── kraken.json
    │               │   ├── krakenfutures.json
    │               │   ├── kucoin.json
    │               │   ├── kucoinfutures.json
    │               │   ├── kuna.json
    │               │   ├── latoken.json
    │               │   ├── lbank.json
    │               │   ├── lbank2.json
    │               │   ├── luno.json
    │               │   ├── mexc.json
    │               │   ├── ndax.json
    │               │   ├── oceanex.json
    │               │   ├── okcoin.json
    │               │   ├── okx.json
    │               │   ├── onetrading.json
    │               │   ├── oxfun.json
    │               │   ├── p2b.json
    │               │   ├── paradex.json
    │               │   ├── phemex.json
    │               │   ├── poloniex.json
    │               │   ├── poloniexfutures.json
    │               │   ├── probit.json
    │               │   ├── timex.json
    │               │   ├── tokocrypto.json
    │               │   ├── tradeogre.json
    │               │   ├── upbit.json
    │               │   ├── vertex.json
    │               │   ├── wavesexchange.json
    │               │   ├── whitebit.json
    │               │   ├── woo.json
    │               │   ├── woofipro.json
    │               │   ├── xt.json
    │               │   ├── yobit.json
    │               │   └── zonda.json
    │               ├── markets/
    │               │   ├── ace.json
    │               │   ├── alpaca.json
    │               │   ├── ascendex.json
    │               │   ├── bequant.json
    │               │   ├── bigone.json
    │               │   ├── binance.json
    │               │   ├── binanceus.json
    │               │   ├── bingx.json
    │               │   ├── bit2c.json
    │               │   ├── bitbns.json
    │               │   ├── bitfinex.json
    │               │   ├── bitfinex1.json
    │               │   ├── bitflyer.json
    │               │   ├── bitget.json
    │               │   ├── bithumb.json
    │               │   ├── bitmart.json
    │               │   ├── bitmex.json
    │               │   ├── bitopro.json
    │               │   ├── bitrue.json
    │               │   ├── bitso.json
    │               │   ├── bitstamp.json
    │               │   ├── bitteam.json
    │               │   ├── bitvavo.json
    │               │   ├── bl3p.json
    │               │   ├── blockchaincom.json
    │               │   ├── blofin.json
    │               │   ├── btcalpha.json
    │               │   ├── bybit.json
    │               │   ├── cex.json
    │               │   ├── coinbase.json
    │               │   ├── coinbaseexchange.json
    │               │   ├── coinbaseinternational.json
    │               │   ├── coincatch.json
    │               │   ├── coinex.json
    │               │   ├── coinlist.json
    │               │   ├── coinmate.json
    │               │   ├── coinmetro.json
    │               │   ├── coinone.json
    │               │   ├── coinsph.json
    │               │   ├── cryptocom.json
    │               │   ├── currencycom.json
    │               │   ├── defx.json
    │               │   ├── delta.json
    │               │   ├── deribit.json
    │               │   ├── digifinex.json
    │               │   ├── ellipx.json
    │               │   ├── exmo.json
    │               │   ├── gate.json
    │               │   ├── gemini.json
    │               │   ├── hashkey.json
    │               │   ├── hitbtc.json
    │               │   ├── hollaex.json
    │               │   ├── htx.json
    │               │   ├── huobijp.json
    │               │   ├── hyperliquid.json
    │               │   ├── idex.json
    │               │   ├── independentreserve.json
    │               │   ├── indodax.json
    │               │   ├── kraken.json
    │               │   ├── krakenfutures.json
    │               │   ├── kucoin.json
    │               │   ├── kucoinfutures.json
    │               │   ├── kuna.json
    │               │   ├── latoken.json
    │               │   ├── lbank.json
    │               │   ├── luno.json
    │               │   ├── mexc.json
    │               │   ├── ndax.json
    │               │   ├── oceanex.json
    │               │   ├── okcoin.json
    │               │   ├── okx.json
    │               │   ├── onetrading.json
    │               │   ├── oxfun.json
    │               │   ├── p2b.json
    │               │   ├── paradex.json
    │               │   ├── phemex.json
    │               │   ├── poloniex.json
    │               │   ├── poloniexfutures.json
    │               │   ├── probit.json
    │               │   ├── timex.json
    │               │   ├── tokocrypto.json
    │               │   ├── tradeogre.json
    │               │   ├── upbit.json
    │               │   ├── vertex.json
    │               │   ├── wavesexchange.json
    │               │   ├── whitebit.json
    │               │   ├── woo.json
    │               │   ├── woofipro.json
    │               │   ├── xt.json
    │               │   ├── yobit.json
    │               │   └── zonda.json
    │               ├── request/
    │               │   ├── ace.json
    │               │   ├── alpaca.json
    │               │   ├── ascendex.json
    │               │   ├── bequant.json
    │               │   ├── bigone.json
    │               │   ├── binance.json
    │               │   ├── binanceus.json
    │               │   ├── bingx.json
    │               │   ├── bit2c.json
    │               │   ├── bitbns.json
    │               │   ├── bitfinex.json
    │               │   ├── bitfinex1.json
    │               │   ├── bitflyer.json
    │               │   ├── bitget.json
    │               │   ├── bithumb.json
    │               │   ├── bitmart.json
    │               │   ├── bitmex.json
    │               │   ├── bitopro.json
    │               │   ├── bitrue.json
    │               │   ├── bitso.json
    │               │   ├── bitstamp.json
    │               │   ├── bitteam.json
    │               │   ├── bitvavo.json
    │               │   ├── bl3p.json
    │               │   ├── blockchaincom.json
    │               │   ├── blofin.json
    │               │   ├── btcalpha.json
    │               │   ├── bybit.json
    │               │   ├── cex.json
    │               │   ├── coinbase.json
    │               │   ├── coinbaseexchange.json
    │               │   ├── coinbaseinternational.json
    │               │   ├── coincatch.json
    │               │   ├── coinex.json
    │               │   ├── coinlist.json
    │               │   ├── coinmate.json
    │               │   ├── coinmetro.json
    │               │   ├── coinone.json
    │               │   ├── coinsph.json
    │               │   ├── cryptocom.json
    │               │   ├── currencycom.json
    │               │   ├── defx.json
    │               │   ├── delta.json
    │               │   ├── deribit.json
    │               │   ├── digifinex.json
    │               │   ├── ellipx.json
    │               │   ├── exmo.json
    │               │   ├── gate.json
    │               │   ├── gemini.json
    │               │   ├── hashkey.json
    │               │   ├── hitbtc.json
    │               │   ├── hollaex.json
    │               │   ├── htx.json
    │               │   ├── huobijp.json
    │               │   ├── hyperliquid.json
    │               │   ├── idex.json
    │               │   ├── independentreserve.json
    │               │   ├── indodax.json
    │               │   ├── kraken.json
    │               │   ├── krakenfutures.json
    │               │   ├── kucoin.json
    │               │   ├── kucoinfutures.json
    │               │   ├── kuna.json
    │               │   ├── latoken.json
    │               │   ├── lbank.json
    │               │   ├── luno.json
    │               │   ├── mexc.json
    │               │   ├── ndax.json
    │               │   ├── oceanex.json
    │               │   ├── okcoin.json
    │               │   ├── okx.json
    │               │   ├── onetrading.json
    │               │   ├── oxfun.json
    │               │   ├── p2b.json
    │               │   ├── paradex.json
    │               │   ├── phemex.json
    │               │   ├── poloniex.json
    │               │   ├── poloniexfutures.json
    │               │   ├── probit.json
    │               │   ├── timex.json
    │               │   ├── tokocrypto.json
    │               │   ├── tradeogre.json
    │               │   ├── upbit.json
    │               │   ├── vertex.json
    │               │   ├── wavesexchange.json
    │               │   ├── whitebit.json
    │               │   ├── woo.json
    │               │   ├── woofipro.json
    │               │   ├── xt.json
    │               │   ├── yobit.json
    │               │   └── zonda.json
    │               └── response/
    │                   ├── ace.json
    │                   ├── alpaca.json
    │                   ├── ascendex.json
    │                   ├── bequant.json
    │                   ├── bigone.json
    │                   ├── binance.json
    │                   ├── binanceus.json
    │                   ├── bingx.json
    │                   ├── bit2c.json
    │                   ├── bitbns.json
    │                   ├── bitfinex.json
    │                   ├── bitfinex1.json
    │                   ├── bitget.json
    │                   ├── bithumb.json
    │                   ├── bitmart.json
    │                   ├── bitmex.json
    │                   ├── bitopro.json
    │                   ├── bitrue.json
    │                   ├── bitso.json
    │                   ├── bitstamp.json
    │                   ├── bitteam.json
    │                   ├── bitvavo.json
    │                   ├── bl3p.json
    │                   ├── blockchaincom.json
    │                   ├── blofin.json
    │                   ├── btcalpha.json
    │                   ├── bybit.json
    │                   ├── cex.json
    │                   ├── coinbase.json
    │                   ├── coinbaseexchange.json
    │                   ├── coinbaseinternational.json
    │                   ├── coincatch.json
    │                   ├── coinex.json
    │                   ├── coinlist.json
    │                   ├── coinmate.json
    │                   ├── coinmetro.json
    │                   ├── coinone.json
    │                   ├── coinsph.json
    │                   ├── cryptocom.json
    │                   ├── currencycom.json
    │                   ├── defx.json
    │                   ├── delta.json
    │                   ├── deribit.json
    │                   ├── digifinex.json
    │                   ├── ellipx.json
    │                   ├── exmo.json
    │                   ├── gate.json
    │                   ├── gemini.json
    │                   ├── hashkey.json
    │                   ├── hitbtc.json
    │                   ├── hollaex.json
    │                   ├── htx.json
    │                   ├── huobijp.json
    │                   ├── hyperliquid.json
    │                   ├── idex.json
    │                   ├── independentreserve.json
    │                   ├── indodax.json
    │                   ├── kraken.json
    │                   ├── krakenfutures.json
    │                   ├── kucoin.json
    │                   ├── kucoinfutures.json
    │                   ├── kuna.json
    │                   ├── latoken.json
    │                   ├── lbank.json
    │                   ├── luno.json
    │                   ├── mexc.json
    │                   ├── ndax.json
    │                   ├── okcoin.json
    │                   ├── okx.json
    │                   ├── onetrading.json
    │                   ├── oxfun.json
    │                   ├── p2b.json
    │                   ├── paradex.json
    │                   ├── phemex.json
    │                   ├── poloniex.json
    │                   ├── poloniexfutures.json
    │                   ├── probit.json
    │                   ├── timex.json
    │                   ├── tokocrypto.json
    │                   ├── tradeogre.json
    │                   ├── upbit.json
    │                   ├── vertex.json
    │                   ├── wavesexchange.json
    │                   ├── whitebit.json
    │                   ├── woo.json
    │                   ├── woofipro.json
    │                   ├── xt.json
    │                   ├── yobit.json
    │                   └── zonda.json
    ├── utils/
    │   ├── change.sh
    │   ├── check_modified_files.sh
    │   ├── init_actions.sh
    │   ├── move-jsdoc.ts
    │   ├── multilang.sh
    │   ├── package-test.sh
    │   ├── restore_shared_env.sh
    │   ├── test-commonjs.cjs
    │   ├── test-freshness.ts
    │   ├── update-static-json.ts
    │   ├── update-static-tests-data.js
    │   ├── dev-helpers/
    │   │   └── required-symbols-for-methods.ts
    │   └── package-test/
    │       ├── package.json
    │       ├── test-cjs.cjs
    │       └── test-esm.mjs
    ├── wiki/
    │   ├── README.md
    │   ├── Awesome.md
    │   ├── CHANGELOG.md
    │   ├── CHANGELOG.md
    │   ├── CLI.md
    │   ├── CONTRIBUTING.md
    │   ├── CONTRIBUTING.md
    │   ├── Certification.md
    │   ├── Examples.md
    │   ├── Exchange-Markets-By-Country.md
    │   ├── Exchange-Markets.md
    │   ├── FAQ.md
    │   ├── Install.md
    │   ├── Manual.md
    │   ├── Requirements.md
    │   ├── Stats.md
    │   ├── _coverpage.md
    │   ├── _sidebar.md
    │   ├── ccxt.pro.manual.md
    │   ├── ccxt.pro.md
    │   ├── helpers.cjs
    │   ├── index.html
    │   ├── spec.hbs
    │   ├── .nojekyll
    │   ├── basePartials/
    │   │   ├── body.hbs
    │   │   ├── deprecated.hbs
    │   │   ├── docs.hbs
    │   │   ├── header.hbs
    │   │   ├── member-index-list.hbs
    │   │   ├── members.hbs
    │   │   ├── params-table.hbs
    │   │   └── returns.hbs
    │   ├── exchangePartials/
    │   │   ├── body.hbs
    │   │   ├── deprecated.hbs
    │   │   ├── docs.hbs
    │   │   ├── header.hbs
    │   │   ├── member-index-list.hbs
    │   │   ├── members.hbs
    │   │   ├── params-table.hbs
    │   │   └── returns.hbs
    │   ├── exchanges/
    │   │   └── .gitkeep
    │   └── partials/
    │       ├── body.hbs
    │       ├── deprecated.hbs
    │       ├── docs.hbs
    │       ├── header.hbs
    │       ├── member-index-list.hbs
    │       ├── members.hbs
    │       ├── params-table.hbs
    │       └── returns.hbs
    ├── .git-templates/
    │   └── hooks/
    │       └── pre-push
    └── .github/
        ├── FUNDING.yml
        ├── ISSUE_TEMPLATE/
        │   ├── BUG_REPORT.yml
        │   ├── FEATURE_REQUEST.yml
        │   ├── NEW_EXCHANGE.yml
        │   └── config.yml
        └── workflows/
            ├── cs.yml
            ├── go-app.yml
            ├── js.yml
            ├── php.yml
            ├── python.yml
            └── release.yml


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
File: CODEOWNERS
================================================
*    @kroitor @frosty00 @carlosmiei


================================================
File: Dockerfile
================================================
FROM ubuntu:20.04

# Supresses unwanted user interaction (like "Please select the geographic area" when installing tzdata)
ENV DEBIAN_FRONTEND=noninteractive

ADD ./ /ccxt
WORKDIR /ccxt

# Update packages (use us.archive.ubuntu.com instead of archive.ubuntu.com — solves the painfully slow apt-get update)
RUN sed -i 's/archive\.ubuntu\.com/us\.archive\.ubuntu\.com/' /etc/apt/sources.list

# Miscellaneous deps
RUN apt-get update && apt-get install -y --no-install-recommends curl gnupg git ca-certificates
# PHP
RUN apt-get install -y software-properties-common && add-apt-repository -y ppa:ondrej/php
RUN apt-get update && apt-get install -y --no-install-recommends php8.1 php8.1-curl php8.1-iconv php8.1-mbstring php8.1-bcmath php8.1-gmp
# Node
RUN apt-get update
RUN apt-get install -y ca-certificates curl gnupg
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
ENV NODE_MAJOR=20
RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list
RUN apt-get update && apt-get install -y nodejs
# Python 3
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip
RUN pip3 install 'idna==2.9' --force-reinstall
RUN pip3 install --upgrade setuptools==65.7.0
RUN pip3 install tox
RUN pip3 install aiohttp
RUN pip3 install cryptography
RUN pip3 install requests
RUN pip3 install psutil
# Dotnet
RUN curl -fsSL https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -o packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb
RUN apt-get update
RUN apt-get install -y dotnet-sdk-7.0
# Installs as a local Node & Python module, so that `require ('ccxt')` and `import ccxt` should work after that
RUN npm install
RUN ln -s /ccxt /usr/lib/node_modules/
RUN echo "export NODE_PATH=/usr/lib/node_modules" >> $HOME/.bashrc
RUN cd python \
    && pip3 install -e . \
    && cd ..
## Install composer and everything else that it needs and manages
RUN /ccxt/composer-install.sh
RUN apt-get update && apt-get install -y --no-install-recommends zip unzip php-zip
RUN mv /ccxt/composer.phar /usr/local/bin/composer
RUN composer install
## Remove apt sources
RUN apt-get -y autoremove && apt-get clean && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

================================================
File: ISSUE_TEMPLATE.md
================================================
MUST READ THIS BEFORE SUBMITTING ISSUES (read the links, then delete this message before submitting):

- https://github.com/ccxt/ccxt/wiki/FAQ
- https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-submit-an-issue

Make sure your local version of CCXT is up to date. Check by comparing the output of `ccxt.version` to https://github.com/ccxt/ccxt/blob/master/package.json#L3

- OS:
- Programming Language version:
- CCXT version:

```
REPLACE_THIS_WITH_YOUR_CODE_TO_REPRODUCE_THE_ISSUE_WITHOUT_YOUR_KEYS
```

```
REPLACE_THIS_WITH_YOUR_OUTPUT_ERROR_EXCEPTION_IN_TEXT_NO_SCREENSHOTS
```


================================================
File: LICENSE.txt
================================================
MIT License

Copyright © 2024 Igor Kroitor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


================================================
File: build-go.sh
================================================
#!/bin/bash

# Function to print a message with elapsed time
print_message() {
  local start_time=$1
  while true; do
    elapsed=$((SECONDS - start_time))
    echo "GO Build is still running... Elapsed time: ${elapsed}s"
    sleep 30
  done
}


timeout_kill() {
  local pid=$1
  local timeout=$((60 * 15)) # 10 minutes in seconds
  local elapsed=0

  echo "Monitoring process $pid for timeout..."

  while kill -0 "$pid" 2>/dev/null; do
    if (( elapsed >= timeout )); then
      cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')  # CPU usage as a percentage
      mem_usage=$(free -m | awk '/Mem:/ { printf "%.2f%%", $3/$2 * 100 }')  # Memory usage as a percentage
      echo "Stats before killing | CPU Usage: ${cpu_usage}% | RAM Usage: ${mem_usage}"
      echo "Timeout reached: Killing the go build process (PID: $pid)"
      kill -6 "$pid"
      return
    fi
    sleep 1
    ((elapsed++))
  done

  echo "Process $pid has completed within the timeout."
}


# Capture the start time
start_time=$SECONDS

# Start the message-printing function in the background, passing the start time
print_message $start_time &
message_pid=$!

# Trap SIGINT (Ctrl+C) and SIGTERM to clean up background processes
cleanup() {
  echo "Stopping background process..."
  kill $message_pid 2>/dev/null
  wait $message_pid 2>/dev/null
  exit 1
}
trap cleanup SIGINT SIGTERM

# Run the main command and capture its exit code
export GOMAXPROCS=1

# Command to run
echo "Will download modules"
# go mod download
echo "Will build the project"
go build -p=1 -x -trimpath -ldflags="-s -w" -o ccxt ./go/ccxt &
pid_go_build=$!

if [[ -z "$pid_go_build" ]]; then
  echo "Error: Failed to capture PID for go build."
  exit 1
fi

# Start the timeout monitoring in the background
timeout_kill "$pid_go_build" &
wait $pid_go_build
command_exit_code=$?

# Kill the background message-printing process
kill $message_pid 2>/dev/null
wait $message_pid 2>/dev/null

# Exit with the same code as the main command
exit $command_exit_code

================================================
File: build.sh
================================================
#!/usr/bin/env bash

# note, don't run commands inline, as shown https://github.com/ccxt/ccxt/pull/24460
set -e

if [ "${BASH_VERSION:0:1}" -lt 4 ]; then
  echo "EPROGMISMATCH: bash version must be at least 4" >&2
  exit 75
fi

if [ $# -gt 0 ]; then
  echo "E2BIG: too many arguments" >&2
  exit 7
fi

[[ -n "$TRAVIS_BUILD_ID" ]] && IS_TRAVIS="TRUE" || IS_TRAVIS="FALSE"

msgPrefix="⬤ BUILD.SH : "

function run_tests {
  local rest_args=
  local ws_args=
  if [ $# -eq 2 ]; then
    rest_args="$1"
    ws_args="$2"
    if [ -z "$rest_args" ]; then
      : &
      local rest_pid=$!
    fi
    if [ -z "$ws_args" ]; then
      : &
      local ws_pid=$!
    fi
  fi

  if [ -z "$rest_pid" ]; then
    if [ -z "$rest_args" ] || { [ -n "$rest_args" ] && [ "$rest_args" != "skip" ]; }; then
      # shellcheck disable=SC2086
      npm run live-tests -- --js --python-async --php-async --csharp $rest_args &
      local rest_pid=$!
    fi
  fi
  if [ -z "$ws_pid" ]; then
    if [ -z "$ws_args" ] || { [ -n "$ws_args" ] && [ "$ws_args" != "skip" ]; }; then
      # shellcheck disable=SC2086
      npm run live-tests -- --js --python-async --php-async --csharp --ws $ws_args &
      local ws_pid=$!
    fi
  fi

  if [ -n "$rest_pid" ] && [ -n "$ws_pid" ]; then
    wait $rest_pid && wait $ws_pid
  elif [ -n "$rest_pid" ]; then
    wait $rest_pid
  else
    wait $ws_pid
  fi
}

build_and_test_all () {
  npm run force-build
  if [ "$IS_TRAVIS" = "TRUE" ]; then
    merged_pull_request="$(git show --format="%s" -s HEAD | sed -nE 's/Merge pull request #([0-9]{5}).+$/\1/p')"
    echo "DEBUG: $merged_pull_request" # for debugging
    if [ -n "$merged_pull_request" ]; then
      echo "Travis is building merge commit #$merged_pull_request"
      # run every 3 merged pull requests
      # if [ $(("${merged_pull_request:0-1}" % 3)) -eq 0 ]; then
      #   # update pyenv
      #   (cd "$(pyenv root)" && git pull -q origin master)
      #   # install python interpreters
      #   pyenv install -s 3.7.17
      #   pyenv install -s 3.8.18
      #   pyenv install -s 3.9.18
      #   pyenv install -s 3.10.13
      #   pyenv install -s 3.11.6
      #   pyenv global 3.7 3.8 3.9 3.10 3.11
      #   cd python
      #   if ! tox run-parallel; then
      #     exit 1
      #   fi
      #   cd  ..
      # fi
    fi
    npm run test-base-rest
    npm run test-base-ws
    npm run id-tests
    npm run request-tests
    npm run response-tests
    npm run commonjs-test
    npm run package-test
    npm run test-freshness
    if [ "$IS_TRAVIS" = "TRUE" ] && [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
      echo "Travis built all files and static/base tests passed, will push to master before running live tests"
      echo "Not pushing to master, github actions will handle it"
      # env COMMIT_MESSAGE="${TRAVIS_COMMIT_MESSAGE}" GITHUB_TOKEN=${GITHUB_TOKEN} SHOULD_TAG=false ./build/push.sh;
    fi
    last_commit_message=$(git log -1 --pretty=%B)
    echo "Last commit: $last_commit_message" # for debugging
    if [[ "$last_commit_message" == *"skip-tests"* ]]; then
        echo "[SKIP-TESTS] Will skip tests!"
        exit
    fi
    run_tests
  fi
  exit
}

### CHECK IF THIS IS A PR ###
# for appveyor, when PR is from fork, APPVEYOR_REPO_BRANCH is "master" and "APPVEYOR_PULL_REQUEST_HEAD_REPO_BRANCH" is branch name. if PR is from same repo, only APPVEYOR_REPO_BRANCH is set (and it is branch name)
if { [ "$IS_TRAVIS" = "TRUE" ] && [ "$TRAVIS_PULL_REQUEST" = "false" ]; } || { [ "$IS_TRAVIS" != "TRUE" ] && [ -z "$APPVEYOR_PULL_REQUEST_HEAD_REPO_BRANCH" ]; }; then

  echo "$msgPrefix This is a master commit (not a PR), will build everything"
  build_and_test_all
fi

##### DETECT CHANGES #####
# in appveyor, there is no origin/master locally, so we need to fetch it.
if [[ "$IS_TRAVIS" != "TRUE" ]]; then
  git remote set-branches origin 'master'
  git fetch --depth=1 --no-tags
fi

diff=$(git diff origin/master --name-only)
# temporarily remove the below scripts from diff
diff=$(echo "$diff" | sed -e "s/^build\.sh//")
diff=$(echo "$diff" | sed -e "s/^skip\-tests\.json//")
diff_without_statics=$(echo "$diff" | sed -e "s/^ts\/src\/test\/static.*json//")
# diff=$(echo "$diff" | sed -e "s/^\.travis\.yml//")
# diff=$(echo "$diff" | sed -e "s/^package\-lock\.json//")
# diff=$(echo "$diff" | sed -e "s/python\/qa\.py//")
#echo $diff 

critical_pattern='Client(Trait)?\.php|Exchange\.php|\/base|^build|static_dependencies|^run-tests|package(-lock)?\.json|composer\.json|ccxt\.ts|__init__.py|test' # add \/test|
if [[ "$diff_without_statics" =~ $critical_pattern ]]; then
  echo "$msgPrefix Important changes detected - doing full build & test"
  echo "$diff_without_statics"
  build_and_test_all
fi

echo "$msgPrefix Unimportant changes detected - build & test only specific exchange(s)"
readarray -t y <<<"$diff"
rest_pattern='ts\/src\/([A-Za-z0-9_-]+).ts' # \w not working for some reason
ws_pattern='ts\/src\/pro\/([A-Za-z0-9_-]+)\.ts'
pattern_static_request='ts\/src\/test\/static\/request\/([A-Za-z0-9_-]+)\.json'
pattern_static_response='ts\/src\/test\/static\/response\/([A-Za-z0-9_-]+)\.json'

REST_EXCHANGES=()
WS_EXCHANGES=()
for file in "${y[@]}"; do
  if [[ "$file" =~ $rest_pattern ]]; then
    modified_exchange="${BASH_REMATCH[1]}"
    REST_EXCHANGES+=($modified_exchange)
  elif [[ "$file" =~ $pattern_static_request ]]; then
    modified_exchange="${BASH_REMATCH[1]}"
    REST_EXCHANGES+=($modified_exchange)
  elif [[ "$file" =~ $pattern_static_response ]]; then
    modified_exchange="${BASH_REMATCH[1]}"
    REST_EXCHANGES+=($modified_exchange)
  elif [[ "$file" =~ $ws_pattern ]]; then
    modified_exchange="${BASH_REMATCH[1]}"
    WS_EXCHANGES+=($modified_exchange)
  fi
done


### BUILD SPECIFIC EXCHANGES ###
# faster version of pre-transpile (without bundle and atomic linting)
npm run export-exchanges && npm run tsBuild && npm run emitAPI

# check return types
npm run validate-types ${REST_EXCHANGES[*]}

echo "$msgPrefix REST_EXCHANGES TO BE TRANSPILED: ${REST_EXCHANGES[*]}"
PYTHON_FILES=()
for exchange in "${REST_EXCHANGES[@]}"; do
  npm run eslint "ts/src/$exchange.ts"
  npm run transpileRest -- $exchange --force --child
  npm run transpileCsSingle -- $exchange
  PYTHON_FILES+=("python/ccxt/$exchange.py")
  PYTHON_FILES+=("python/ccxt/async_support/$exchange.py")
done
echo "$msgPrefix WS_EXCHANGES TO BE TRANSPILED: ${WS_EXCHANGES[*]}"
for exchange in "${WS_EXCHANGES[@]}"; do
  npm run eslint "ts/src/pro/$exchange.ts"
  npm run transpileWs -- $exchange --force --child
  npm run transpileCsSingle -- $exchange --ws
  PYTHON_FILES+=("python/ccxt/pro/$exchange.py")
done
# faster version of post-transpile
npm run check-php-syntax

# only run the python linter if exchange related files are changed
if [ ${#PYTHON_FILES[@]} -gt 0 ]; then
  echo "$msgPrefix Linting python files: ${PYTHON_FILES[*]}"
  ruff check "${PYTHON_FILES[@]}"
fi


### RUN SPECIFIC TESTS (ONLY IN TRAVIS) ###
if [[ "$IS_TRAVIS" != "TRUE" ]]; then
  exit
fi
if [ ${#REST_EXCHANGES[@]} -eq 0 ] && [ ${#WS_EXCHANGES[@]} -eq 0 ]; then
  echo "$msgPrefix no exchanges to test, exiting"
  exit
fi

# build dotnet project
npm run buildCS

# run base tests (base js,py,php, brokerId )
# npm run test-base
npm run test-base-rest && npm run test-base-ws && npm run id-tests

# rest_args=${REST_EXCHANGES[*]} || "skip"
rest_args=$(IFS=" " ; echo "${REST_EXCHANGES[*]}") || "skip"
# ws_args=${WS_EXCHANGES[*]} || "skip"
ws_args=$(IFS=" " ; echo "${WS_EXCHANGES[*]}") || "skip"


#request static tests
for exchange in "${REST_EXCHANGES[@]}"; do
  npm run request-js -- $exchange
  npm run request-py-sync -- $exchange
  npm run request-py-async -- $exchange
  npm run request-php-sync -- $exchange
  npm run request-php-async -- $exchange
  npm run request-cs -- $exchange
done

#response static tests
for exchange in "${REST_EXCHANGES[@]}"; do
  npm run response-js -- $exchange
  npm run response-py-sync -- $exchange
  npm run response-py-async -- $exchange
  npm run response-php-sync -- $exchange
  npm run response-php-async -- $exchange
  npm run response-cs -- $exchange
done

run_tests "$rest_args" "$ws_args"


================================================
File: ccxt.php
================================================
<?php

/*

MIT License

Copyright (c) 2017 Igor Kroitor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*/

//-----------------------------------------------------------------------------

namespace ccxt;

if (defined('PATH_TO_CCXT')) {
    return;
}

define('PATH_TO_CCXT', __DIR__ . DIRECTORY_SEPARATOR . 'php' . DIRECTORY_SEPARATOR);
define('PATH_TO_WS_CCXT', __DIR__ . DIRECTORY_SEPARATOR . 'php' . DIRECTORY_SEPARATOR . 'pro' .  DIRECTORY_SEPARATOR);
define('PATH_TO_CCXT_ASYNC', PATH_TO_CCXT . 'async' . DIRECTORY_SEPARATOR);

spl_autoload_register(function ($class) {
    // used to include static dependencies
    $PATH = PATH_TO_CCXT . 'static_dependencies/';
    if (strpos($class, 'kornrunner') !== false || strpos($class, 'Web3') !== false) {
        $version = phpversion();
        if (intval(explode('.', $version)[0]) < 7) {
            throw new \RuntimeException($class . " requires php7 or greater, your version: " . $version);
        }
    }
    $class_name = str_replace('kornrunner\\Keccak', 'kornrunner/keccak/src/Keccak', $class);
    $class_name = str_replace('Web3\\', 'web3.php/src/', $class_name);
    $class_name = str_replace('StarkNet\\', 'starknet.php/src/', $class_name);
    $class_name = str_replace('phpseclib\\Math\\BigInteger', 'phpseclib/Math/BigInteger', $class_name);
    $class_name = str_replace('Sop\\', 'Sop/', $class_name);
    $class_name = str_replace('Elliptic\\', 'elliptic-php/lib/', $class_name);
    $class_name = str_replace('Ratchet\\Client', 'ratchet\\pawl\\src', $class_name);
    $class_name = str_replace('Ratchet\\RFC6455', 'ratchet\\rfc6455\\src', $class_name);
    $class_name = str_replace('\\', DIRECTORY_SEPARATOR, $class_name);
    $file = $PATH . $class_name . '.php';
    if (file_exists($file)) {
        require_once $file;
    }
});

require_once PATH_TO_CCXT . 'BaseError.php';
require_once PATH_TO_CCXT . 'ExchangeError.php';
require_once PATH_TO_CCXT . 'AuthenticationError.php';
require_once PATH_TO_CCXT . 'PermissionDenied.php';
require_once PATH_TO_CCXT . 'AccountNotEnabled.php';
require_once PATH_TO_CCXT . 'AccountSuspended.php';
require_once PATH_TO_CCXT . 'ArgumentsRequired.php';
require_once PATH_TO_CCXT . 'BadRequest.php';
require_once PATH_TO_CCXT . 'BadSymbol.php';
require_once PATH_TO_CCXT . 'OperationRejected.php';
require_once PATH_TO_CCXT . 'NoChange.php';
require_once PATH_TO_CCXT . 'MarginModeAlreadySet.php';
require_once PATH_TO_CCXT . 'MarketClosed.php';
require_once PATH_TO_CCXT . 'ManualInteractionNeeded.php';
require_once PATH_TO_CCXT . 'InsufficientFunds.php';
require_once PATH_TO_CCXT . 'InvalidAddress.php';
require_once PATH_TO_CCXT . 'AddressPending.php';
require_once PATH_TO_CCXT . 'InvalidOrder.php';
require_once PATH_TO_CCXT . 'OrderNotFound.php';
require_once PATH_TO_CCXT . 'OrderNotCached.php';
require_once PATH_TO_CCXT . 'OrderImmediatelyFillable.php';
require_once PATH_TO_CCXT . 'OrderNotFillable.php';
require_once PATH_TO_CCXT . 'DuplicateOrderId.php';
require_once PATH_TO_CCXT . 'ContractUnavailable.php';
require_once PATH_TO_CCXT . 'NotSupported.php';
require_once PATH_TO_CCXT . 'InvalidProxySettings.php';
require_once PATH_TO_CCXT . 'ExchangeClosedByUser.php';
require_once PATH_TO_CCXT . 'OperationFailed.php';
require_once PATH_TO_CCXT . 'NetworkError.php';
require_once PATH_TO_CCXT . 'DDoSProtection.php';
require_once PATH_TO_CCXT . 'RateLimitExceeded.php';
require_once PATH_TO_CCXT . 'ExchangeNotAvailable.php';
require_once PATH_TO_CCXT . 'OnMaintenance.php';
require_once PATH_TO_CCXT . 'InvalidNonce.php';
require_once PATH_TO_CCXT . 'ChecksumError.php';
require_once PATH_TO_CCXT . 'RequestTimeout.php';
require_once PATH_TO_CCXT . 'BadResponse.php';
require_once PATH_TO_CCXT . 'NullResponse.php';
require_once PATH_TO_CCXT . 'CancelPending.php';
require_once PATH_TO_CCXT . 'UnsubscribeError.php';


require_once PATH_TO_WS_CCXT . 'ClientTrait.php';
require_once PATH_TO_CCXT . 'Precise.php';
require_once PATH_TO_CCXT . 'Exchange.php';
require_once PATH_TO_CCXT_ASYNC . 'Exchange.php';


$autoloadFile = __DIR__ . DIRECTORY_SEPARATOR . 'vendor' . DIRECTORY_SEPARATOR . 'autoload.php';
if (file_exists($autoloadFile)) {
    require_once $autoloadFile;
}

spl_autoload_register(function ($class_name) {
    $sections = explode("\\", $class_name);
    if (in_array("ccxt\\pro",$sections)) {
        $class_name = str_replace("ccxt\\pro\\", "", $class_name);
        $sections = explode("\\", $class_name);
        $class_name = str_replace ("ccxt\\pro\\", "", $class_name);
        $file = PATH_TO_WS_CCXT . $class_name . '.php';
        if (file_exists ($file)) {
            require_once $file;
        }
        return;
    }

    $class_name = str_replace("ccxt\\", "", $class_name);
    $sections = explode("\\", $class_name);

    $file = PATH_TO_CCXT . implode(DIRECTORY_SEPARATOR, $sections) . '.php';
    if (file_exists($file)) {
        require_once $file;
    }
});

// require_once __DIR__ . DIRECTORY_SEPARATOR . 'php' . DIRECTORY_SEPARATOR . 'pro.php';


namespace ccxt\pro;
require_once PATH_TO_WS_CCXT . 'Future.php';
require_once PATH_TO_WS_CCXT . 'Client.php';
require_once PATH_TO_WS_CCXT . 'OrderBook.php';
require_once PATH_TO_WS_CCXT . 'OrderBookSide.php';
require_once PATH_TO_WS_CCXT . 'BaseCache.php';
require_once PATH_TO_WS_CCXT . 'ArrayCache.php';
require_once PATH_TO_WS_CCXT . 'ArrayCacheByTimestamp.php';
require_once PATH_TO_WS_CCXT . 'ArrayCacheBySymbolById.php';
require_once PATH_TO_WS_CCXT . 'Exchange.php';


================================================
File: ci-requirements.txt
================================================
setuptools>=60.9.0
certifi>=2018.1.18
requests>=2.18.4
cryptography>=2.6.1
typing_extensions>=4.4.0
aiohttp<=3.10.11
aiodns>=1.1.1
yarl>=1.7.2
ruff==0.0.292
tox>=4.8.0
mypy==1.6.1
pyopenssl
psutil


================================================
File: cleanup.sh
================================================
#!/usr/bin/env bash
git checkout HEAD package.json
git checkout HEAD package-lock.json
git checkout HEAD yarn.lock
git checkout HEAD README.md
git checkout HEAD js
git checkout HEAD cs/ccxt/api
git checkout HEAD cs/ccxt/exchanges
git checkout HEAD cs/tests/Generated
git checkout HEAD cs/ccxt/wrappers/
git checkout HEAD cs/ccxt/base/Exchange.Wrappers.cs
git checkout HEAD cs/ccxt/base/Exchange.BaseMethods.cs
git checkout HEAD cs/ccxt/base/Exchange.MetaData.cs
git checkout HEAD ts/ccxt.ts
git checkout HEAD ts/src/abstract
git checkout HEAD python
git checkout HEAD php
git checkout HEAD dist
git checkout HEAD examples
git checkout HEAD go/v4/exchange_metadata.go
git checkout HEAD wiki/Exchange-Markets.md
git checkout HEAD wiki/Manual.md


================================================
File: coin-ws.js
================================================
import WebSocket from 'ws';
const webSocket = new WebSocket ('https://stream.coindcx.com');

webSocket.onmessage = (ev) => {
    console.log (ev)
};

webSocket.onopen = (ev) => {
    console.log (ev)
}


================================================
File: composer-install.sh
================================================
#!/bin/sh
# This script taken from the composer installation instructions at
# https://getcomposer.org/doc/faqs/how-to-install-composer-programmatically.md

EXPECTED_CHECKSUM="$(php -r 'copy("https://composer.github.io/installer.sig", "php://stdout");')"
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
ACTUAL_CHECKSUM="$(php -r "echo hash_file('sha384', 'composer-setup.php');")"

if [ "$EXPECTED_CHECKSUM" != "$ACTUAL_CHECKSUM" ]
then
    >&2 echo 'ERROR: Invalid installer checksum'
    rm composer-setup.php
    exit 1
fi

php composer-setup.php --quiet
RESULT=$?
rm composer-setup.php
exit $RESULT



================================================
File: composer.json
================================================
{
    "name": "ccxt/ccxt",
    "type": "library",
    "description": "A JavaScript / TypeScript / Python / C# / PHP cryptocurrency trading library with support for more than 100 bitcoin/altcoin exchanges",
    "keywords": [
        "algorithmic",
        "algotrading",
        "altcoin",
        "altcoins",
        "api",
        "arbitrage",
        "backtest",
        "backtesting",
        "bitcoin",
        "bot",
        "btc",
        "cny",
        "coin",
        "coins",
        "crypto",
        "cryptocurrency",
        "crypto currency",
        "crypto market",
        "currency",
        "currencies",
        "darkcoin",
        "dash",
        "digital currency",
        "doge",
        "dogecoin",
        "e-commerce",
        "etc",
        "eth",
        "ether",
        "ethereum",
        "exchange",
        "exchanges",
        "eur",
        "framework",
        "invest",
        "investing",
        "investor",
        "library",
        "light",
        "litecoin",
        "ltc",
        "market",
        "market data",
        "markets",
        "merchandise",
        "merchant",
        "minimal",
        "order",
        "orderbook",
        "order book",
        "price",
        "price data",
        "pricefeed",
        "private",
        "public",
        "ripple",
        "strategy",
        "toolkit",
        "trade",
        "trader",
        "trading",
        "usd",
        "volume",
        "xbt",
        "xrp",
        "zec",
        "zerocoin",
        "1Broker",
        "1BTCXE",
        "ACX",
        "acx.io",
        "ANX",
        "ANXPro",
        "Binance",
        "binance.com",
        "bit2c.co.il",
        "Bit2C",
        "BitBay",
        "BitBays",
        "bitcoincoid",
        "Bitcoin.co.id",
        "Bitfinex",
        "bitFLyer",
        "bitflyer.jp",
        "bithumb",
        "bithumb.com",
        "bitlish",
        "BitMarket",
        "BitMEX",
        "Bitso",
        "Bitstamp",
        "Bittrex",
        "BL3P",
        "Bleutrade",
        "bleutrade.com",
        "BlinkTrade",
        "BtcBox",
        "btcbox.co.jp",
        "BTCC",
        "BTCChina",
        "BTC-e",
        "BTCe",
        "BTCExchange",
        "btcexchange.ph",
        "BTC Markets",
        "btcmarkets",
        "btcmarkets.net",
        "BTCTrader",
        "btctrader.com",
        "btc-trade.com.ua",
        "BTC Trade UA",
        "BTCTurk",
        "btcturk.com",
        "BTCX",
        "btc-x",
        "bter",
        "Bter.com",
        "BX.in.th",
        "ccex",
        "C-CEX",
        "cex",
        "CEX.IO",
        "CHBTC",
        "ChileBit",
        "chilebit.net",
        "coincheck",
        "coingi",
        "coingi.com",
        "CoinMarketCap",
        "CoinMate",
        "Coinsecure",
        "CoinSpot",
        "coinspot.com.au",
        "Crypto Capital",
        "cryptocapital.co",
        "DSX",
        "dsx.uk",
        "EXMO",
        "flowBTC",
        "flowbtc.com",
        "FoxBit",
        "foxbit.exchange",
        "FYB-SE",
        "FYB-SG",
        "Gatecoin",
        "GDAX",
        "Gemini",
        "HitBTC",
        "Huobi",
        "HuobiPRO",
        "huobi.pro",
        "Independent Reserve",
        "independentreserve.com",
        "itBit",
        "jubi.com",
        "Kraken",
        "LakeBTC",
        "lakebtc.com",
        "LiveCoin",
        "Liqui",
        "liqui.io",
        "luno",
        "mercado",
        "MercadoBitcoin",
        "mercadobitcoin.br",
        "mixcoins",
        "mixcoins.com",
        "nova",
        "novaexchange",
        "novaexchange.com",
        "OKCoin",
        "OKCoin.com",
        "OKCoin.cn",
        "OKEX",
        "okex.com",
        "Paymium",
        "Poloniex",
        "QuadrigaCX",
        "Qryptos",
        "QUOINE",
        "Southxchange",
        "SurBitcoin",
        "surbitcoin.com",
        "Tidex",
        "tidex.com",
        "TheRockTrading",
        "UrduBit",
        "urdubit.com",
        "Vaultoro",
        "VBTC",
        "vbtc.exchange",
        "vbtc.vn",
        "VirWoX",
        "WEX",
        "wex.nz",
        "xBTCe",
        "xbtce.com",
        "YoBit",
        "yobit.net",
        "YUNBI",
        "Zaif"
    ],
    "homepage": "https://github.com/ccxt/ccxt",
    "license": "MIT",
    "authors": [{
        "name": "Igor Kroitor",
        "email": "igor.kroitor@gmail.com",
        "homepage": "https://github.com/kroitor",
        "role": "Developer"
    }, {
        "name": "Carlo Revelli",
        "email": "carlo.revelli@berkeley.edu",
        "homepage": "https://github.com/frosty00",
        "role": "Junior Developer"
    }],
    "autoload": {
        "psr-4": {
            "ccxt\\" : "php/",
            "ccxt\\async\\": "php/async/",
            "ccxt\\pro\\" : "php/pro/"
        },
        "files": [ "ccxt.php", "php/pro/base/functions.php" ]
    },
    "require": {
        "php": ">=8.1.0",
        "ext-bcmath": "*",
        "ext-curl": "*",
        "ext-iconv": "*",
        "ext-pcre": "*",
        "ext-json": "*",
        "ext-openssl": "*",
        "ext-gmp": "*",
        "symfony/polyfill-mbstring": "^1.7",
        "pear/console_table": "1.3.1",
        "react/http": ">=1.11.0",
        "react/async": "^4.3.0",
        "react/promise": "^3.2.0",
        "react/promise-timer": "^1.11",
        "evenement/evenement": "^3.0",
        "guzzlehttp/psr7": "^2.0"
    },
    "suggest": {
        "recoil/recoil": "Required for asynchronous API calls to exchanges with PHP",
        "recoil/react": "Required for asynchronous API calls to exchanges with PHP",
        "react/http": "Required for asynchronous API calls to exchanges with PHP",
        "clue/buzz-react": "Required for asynchronous API calls to exchanges with PHP",
        "react/event-loop": "Required for asynchronous API calls to exchanges with PHP",
        "clue/http-proxy-react": "Required for using a proxy when doing asynchronous API calls to exchanges with PHP"
    },
    "archive": {
        "exclude": [
            "/build",
            "/dist",
            "/doc",
            "/js",
            "/python",
            "/wiki"
        ]
    }
}


================================================
File: composer.lock
================================================
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "11f3bf426d903fc8cecff7fd3fd536a7",
    "packages": [
        {
            "name": "evenement/evenement",
            "version": "v3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/igorw/evenement.git",
                "reference": "0a16b0d71ab13284339abb99d9d2bd813640efbc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/igorw/evenement/zipball/0a16b0d71ab13284339abb99d9d2bd813640efbc",
                "reference": "0a16b0d71ab13284339abb99d9d2bd813640efbc",
                "shasum": ""
            },
            "require": {
                "php": ">=7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9 || ^6"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Evenement\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Igor Wiedler",
                    "email": "igor@wiedler.ch"
                }
            ],
            "description": "Événement is a very simple event dispatching library for PHP",
            "keywords": [
                "event-dispatcher",
                "event-emitter"
            ],
            "support": {
                "issues": "https://github.com/igorw/evenement/issues",
                "source": "https://github.com/igorw/evenement/tree/v3.0.2"
            },
            "time": "2023-08-08T05:53:35+00:00"
        },
        {
            "name": "fig/http-message-util",
            "version": "1.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-message-util.git",
                "reference": "9d94dc0154230ac39e5bf89398b324a86f63f765"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-message-util/zipball/9d94dc0154230ac39e5bf89398b324a86f63f765",
                "reference": "9d94dc0154230ac39e5bf89398b324a86f63f765",
                "shasum": ""
            },
            "require": {
                "php": "^5.3 || ^7.0 || ^8.0"
            },
            "suggest": {
                "psr/http-message": "The package containing the PSR-7 interfaces"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Fig\\Http\\Message\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Utility classes and constants for use with PSR-7 (psr/http-message)",
            "keywords": [
                "http",
                "http-message",
                "psr",
                "psr-7",
                "request",
                "response"
            ],
            "support": {
                "issues": "https://github.com/php-fig/http-message-util/issues",
                "source": "https://github.com/php-fig/http-message-util/tree/1.1.5"
            },
            "time": "2020-11-24T22:02:12+00:00"
        },
        {
            "name": "guzzlehttp/psr7",
            "version": "2.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/psr7.git",
                "reference": "a70f5c95fb43bc83f07c9c948baa0dc1829bf201"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/psr7/zipball/a70f5c95fb43bc83f07c9c948baa0dc1829bf201",
                "reference": "a70f5c95fb43bc83f07c9c948baa0dc1829bf201",
                "shasum": ""
            },
            "require": {
                "php": "^7.2.5 || ^8.0",
                "psr/http-factory": "^1.0",
                "psr/http-message": "^1.1 || ^2.0",
                "ralouphie/getallheaders": "^3.0"
            },
            "provide": {
                "psr/http-factory-implementation": "1.0",
                "psr/http-message-implementation": "1.0"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.8.2",
                "http-interop/http-factory-tests": "0.9.0",
                "phpunit/phpunit": "^8.5.39 || ^9.6.20"
            },
            "suggest": {
                "laminas/laminas-httphandlerrunner": "Emit PSR-7 responses"
            },
            "type": "library",
            "extra": {
                "bamarni-bin": {
                    "bin-links": true,
                    "forward-command": false
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Psr7\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Graham Campbell",
                    "email": "hello@gjcampbell.co.uk",
                    "homepage": "https://github.com/GrahamCampbell"
                },
                {
                    "name": "Michael Dowling",
                    "email": "mtdowling@gmail.com",
                    "homepage": "https://github.com/mtdowling"
                },
                {
                    "name": "George Mponos",
                    "email": "gmponos@gmail.com",
                    "homepage": "https://github.com/gmponos"
                },
                {
                    "name": "Tobias Nyholm",
                    "email": "tobias.nyholm@gmail.com",
                    "homepage": "https://github.com/Nyholm"
                },
                {
                    "name": "Márk Sági-Kazár",
                    "email": "mark.sagikazar@gmail.com",
                    "homepage": "https://github.com/sagikazarmark"
                },
                {
                    "name": "Tobias Schultze",
                    "email": "webmaster@tubo-world.de",
                    "homepage": "https://github.com/Tobion"
                },
                {
                    "name": "Márk Sági-Kazár",
                    "email": "mark.sagikazar@gmail.com",
                    "homepage": "https://sagikazarmark.hu"
                }
            ],
            "description": "PSR-7 message implementation that also provides common utility methods",
            "keywords": [
                "http",
                "message",
                "psr-7",
                "request",
                "response",
                "stream",
                "uri",
                "url"
            ],
            "support": {
                "issues": "https://github.com/guzzle/psr7/issues",
                "source": "https://github.com/guzzle/psr7/tree/2.7.0"
            },
            "funding": [
                {
                    "url": "https://github.com/GrahamCampbell",
                    "type": "github"
                },
                {
                    "url": "https://github.com/Nyholm",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/guzzlehttp/psr7",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-18T11:15:46+00:00"
        },
        {
            "name": "pear/console_table",
            "version": "v1.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/pear/Console_Table.git",
                "reference": "1930c11897ca61fd24b95f2f785e99e0f36dcdea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear/Console_Table/zipball/1930c11897ca61fd24b95f2f785e99e0f36dcdea",
                "reference": "1930c11897ca61fd24b95f2f785e99e0f36dcdea",
                "shasum": ""
            },
            "require": {
                "php": ">=5.2.0"
            },
            "suggest": {
                "pear/Console_Color2": ">=0.1.2"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "Table.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-2-Clause"
            ],
            "authors": [
                {
                    "name": "Jan Schneider",
                    "homepage": "http://pear.php.net/user/yunosh"
                },
                {
                    "name": "Tal Peer",
                    "homepage": "http://pear.php.net/user/tal"
                },
                {
                    "name": "Xavier Noguer",
                    "homepage": "http://pear.php.net/user/xnoguer"
                },
                {
                    "name": "Richard Heyes",
                    "homepage": "http://pear.php.net/user/richard"
                }
            ],
            "description": "Library that makes it easy to build console style tables.",
            "homepage": "http://pear.php.net/package/Console_Table/",
            "keywords": [
                "console"
            ],
            "support": {
                "issues": "http://pear.php.net/bugs/search.php?cmd=display&package_name[]=Console_Table",
                "source": "https://github.com/pear/Console_Table"
            },
            "time": "2018-01-25T20:47:17+00:00"
        },
        {
            "name": "psr/http-factory",
            "version": "1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-factory.git",
                "reference": "2b4765fddfe3b508ac62f829e852b1501d3f6e8a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-factory/zipball/2b4765fddfe3b508ac62f829e852b1501d3f6e8a",
                "reference": "2b4765fddfe3b508ac62f829e852b1501d3f6e8a",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1",
                "psr/http-message": "^1.0 || ^2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Http\\Message\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "PSR-17: Common interfaces for PSR-7 HTTP message factories",
            "keywords": [
                "factory",
                "http",
                "message",
                "psr",
                "psr-17",
                "psr-7",
                "request",
                "response"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-factory"
            },
            "time": "2024-04-15T12:06:14+00:00"
        },
        {
            "name": "psr/http-message",
            "version": "1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-message.git",
                "reference": "cb6ce4845ce34a8ad9e68117c10ee90a29919eba"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-message/zipball/cb6ce4845ce34a8ad9e68117c10ee90a29919eba",
                "reference": "cb6ce4845ce34a8ad9e68117c10ee90a29919eba",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Http\\Message\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interface for HTTP messages",
            "homepage": "https://github.com/php-fig/http-message",
            "keywords": [
                "http",
                "http-message",
                "psr",
                "psr-7",
                "request",
                "response"
            ],
            "support": {
                "source": "https://github.com/php-fig/http-message/tree/1.1"
            },
            "time": "2023-04-04T09:50:52+00:00"
        },
        {
            "name": "ralouphie/getallheaders",
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/ralouphie/getallheaders.git",
                "reference": "120b605dfeb996808c31b6477290a714d356e822"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ralouphie/getallheaders/zipball/120b605dfeb996808c31b6477290a714d356e822",
                "reference": "120b605dfeb996808c31b6477290a714d356e822",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.1",
                "phpunit/phpunit": "^5 || ^6.5"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/getallheaders.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ralph Khattar",
                    "email": "ralph.khattar@gmail.com"
                }
            ],
            "description": "A polyfill for getallheaders.",
            "support": {
                "issues": "https://github.com/ralouphie/getallheaders/issues",
                "source": "https://github.com/ralouphie/getallheaders/tree/develop"
            },
            "time": "2019-03-08T08:55:37+00:00"
        },
        {
            "name": "react/async",
            "version": "v4.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/async.git",
                "reference": "635d50e30844a484495713e8cb8d9e079c0008a5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/async/zipball/635d50e30844a484495713e8cb8d9e079c0008a5",
                "reference": "635d50e30844a484495713e8cb8d9e079c0008a5",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "react/event-loop": "^1.2",
                "react/promise": "^3.2 || ^2.8 || ^1.2.1"
            },
            "require-dev": {
                "phpstan/phpstan": "1.10.39",
                "phpunit/phpunit": "^9.6"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/functions_include.php"
                ],
                "psr-4": {
                    "React\\Async\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "Async utilities and fibers for ReactPHP",
            "keywords": [
                "async",
                "reactphp"
            ],
            "support": {
                "issues": "https://github.com/reactphp/async/issues",
                "source": "https://github.com/reactphp/async/tree/v4.3.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2024-06-04T14:40:02+00:00"
        },
        {
            "name": "react/cache",
            "version": "v1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/cache.git",
                "reference": "d47c472b64aa5608225f47965a484b75c7817d5b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/cache/zipball/d47c472b64aa5608225f47965a484b75c7817d5b",
                "reference": "d47c472b64aa5608225f47965a484b75c7817d5b",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0",
                "react/promise": "^3.0 || ^2.0 || ^1.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.5 || ^5.7 || ^4.8.35"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "React\\Cache\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "Async, Promise-based cache interface for ReactPHP",
            "keywords": [
                "cache",
                "caching",
                "promise",
                "reactphp"
            ],
            "support": {
                "issues": "https://github.com/reactphp/cache/issues",
                "source": "https://github.com/reactphp/cache/tree/v1.2.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2022-11-30T15:59:55+00:00"
        },
        {
            "name": "react/dns",
            "version": "v1.13.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/dns.git",
                "reference": "eb8ae001b5a455665c89c1df97f6fb682f8fb0f5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/dns/zipball/eb8ae001b5a455665c89c1df97f6fb682f8fb0f5",
                "reference": "eb8ae001b5a455665c89c1df97f6fb682f8fb0f5",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0",
                "react/cache": "^1.0 || ^0.6 || ^0.5",
                "react/event-loop": "^1.2",
                "react/promise": "^3.2 || ^2.7 || ^1.2.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.6 || ^5.7 || ^4.8.36",
                "react/async": "^4.3 || ^3 || ^2",
                "react/promise-timer": "^1.11"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "React\\Dns\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "Async DNS resolver for ReactPHP",
            "keywords": [
                "async",
                "dns",
                "dns-resolver",
                "reactphp"
            ],
            "support": {
                "issues": "https://github.com/reactphp/dns/issues",
                "source": "https://github.com/reactphp/dns/tree/v1.13.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2024-06-13T14:18:03+00:00"
        },
        {
            "name": "react/event-loop",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/event-loop.git",
                "reference": "bbe0bd8c51ffc05ee43f1729087ed3bdf7d53354"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/event-loop/zipball/bbe0bd8c51ffc05ee43f1729087ed3bdf7d53354",
                "reference": "bbe0bd8c51ffc05ee43f1729087ed3bdf7d53354",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.6 || ^5.7 || ^4.8.36"
            },
            "suggest": {
                "ext-pcntl": "For signal handling support when using the StreamSelectLoop"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "React\\EventLoop\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "ReactPHP's core reactor event loop that libraries can use for evented I/O.",
            "keywords": [
                "asynchronous",
                "event-loop"
            ],
            "support": {
                "issues": "https://github.com/reactphp/event-loop/issues",
                "source": "https://github.com/reactphp/event-loop/tree/v1.5.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2023-11-13T13:48:05+00:00"
        },
        {
            "name": "react/http",
            "version": "v1.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/http.git",
                "reference": "8db02de41dcca82037367f67a2d4be365b1c4db9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/http/zipball/8db02de41dcca82037367f67a2d4be365b1c4db9",
                "reference": "8db02de41dcca82037367f67a2d4be365b1c4db9",
                "shasum": ""
            },
            "require": {
                "evenement/evenement": "^3.0 || ^2.0 || ^1.0",
                "fig/http-message-util": "^1.1",
                "php": ">=5.3.0",
                "psr/http-message": "^1.0",
                "react/event-loop": "^1.2",
                "react/promise": "^3.2 || ^2.3 || ^1.2.1",
                "react/socket": "^1.16",
                "react/stream": "^1.4"
            },
            "require-dev": {
                "clue/http-proxy-react": "^1.8",
                "clue/reactphp-ssh-proxy": "^1.4",
                "clue/socks-react": "^1.4",
                "phpunit/phpunit": "^9.6 || ^5.7 || ^4.8.36",
                "react/async": "^4.2 || ^3 || ^2",
                "react/promise-stream": "^1.4",
                "react/promise-timer": "^1.11"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "React\\Http\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "Event-driven, streaming HTTP client and server implementation for ReactPHP",
            "keywords": [
                "async",
                "client",
                "event-driven",
                "http",
                "http client",
                "http server",
                "https",
                "psr-7",
                "reactphp",
                "server",
                "streaming"
            ],
            "support": {
                "issues": "https://github.com/reactphp/http/issues",
                "source": "https://github.com/reactphp/http/tree/v1.11.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2024-11-20T15:24:08+00:00"
        },
        {
            "name": "react/promise",
            "version": "v3.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/promise.git",
                "reference": "8a164643313c71354582dc850b42b33fa12a4b63"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/promise/zipball/8a164643313c71354582dc850b42b33fa12a4b63",
                "reference": "8a164643313c71354582dc850b42b33fa12a4b63",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1.0"
            },
            "require-dev": {
                "phpstan/phpstan": "1.10.39 || 1.4.10",
                "phpunit/phpunit": "^9.6 || ^7.5"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/functions_include.php"
                ],
                "psr-4": {
                    "React\\Promise\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "A lightweight implementation of CommonJS Promises/A for PHP",
            "keywords": [
                "promise",
                "promises"
            ],
            "support": {
                "issues": "https://github.com/reactphp/promise/issues",
                "source": "https://github.com/reactphp/promise/tree/v3.2.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2024-05-24T10:39:05+00:00"
        },
        {
            "name": "react/promise-timer",
            "version": "v1.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/promise-timer.git",
                "reference": "4f70306ed66b8b44768941ca7f142092600fafc1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/promise-timer/zipball/4f70306ed66b8b44768941ca7f142092600fafc1",
                "reference": "4f70306ed66b8b44768941ca7f142092600fafc1",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3",
                "react/event-loop": "^1.2",
                "react/promise": "^3.2 || ^2.7.0 || ^1.2.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.6 || ^5.7 || ^4.8.36"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/functions_include.php"
                ],
                "psr-4": {
                    "React\\Promise\\Timer\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "A trivial implementation of timeouts for Promises, built on top of ReactPHP.",
            "homepage": "https://github.com/reactphp/promise-timer",
            "keywords": [
                "async",
                "event-loop",
                "promise",
                "reactphp",
                "timeout",
                "timer"
            ],
            "support": {
                "issues": "https://github.com/reactphp/promise-timer/issues",
                "source": "https://github.com/reactphp/promise-timer/tree/v1.11.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2024-06-04T14:27:45+00:00"
        },
        {
            "name": "react/socket",
            "version": "v1.16.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/socket.git",
                "reference": "23e4ff33ea3e160d2d1f59a0e6050e4b0fb0eac1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/socket/zipball/23e4ff33ea3e160d2d1f59a0e6050e4b0fb0eac1",
                "reference": "23e4ff33ea3e160d2d1f59a0e6050e4b0fb0eac1",
                "shasum": ""
            },
            "require": {
                "evenement/evenement": "^3.0 || ^2.0 || ^1.0",
                "php": ">=5.3.0",
                "react/dns": "^1.13",
                "react/event-loop": "^1.2",
                "react/promise": "^3.2 || ^2.6 || ^1.2.1",
                "react/stream": "^1.4"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.6 || ^5.7 || ^4.8.36",
                "react/async": "^4.3 || ^3.3 || ^2",
                "react/promise-stream": "^1.4",
                "react/promise-timer": "^1.11"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "React\\Socket\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "Async, streaming plaintext TCP/IP and secure TLS socket server and client connections for ReactPHP",
            "keywords": [
                "Connection",
                "Socket",
                "async",
                "reactphp",
                "stream"
            ],
            "support": {
                "issues": "https://github.com/reactphp/socket/issues",
                "source": "https://github.com/reactphp/socket/tree/v1.16.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2024-07-26T10:38:09+00:00"
        },
        {
            "name": "react/stream",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/stream.git",
                "reference": "1e5b0acb8fe55143b5b426817155190eb6f5b18d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/stream/zipball/1e5b0acb8fe55143b5b426817155190eb6f5b18d",
                "reference": "1e5b0acb8fe55143b5b426817155190eb6f5b18d",
                "shasum": ""
            },
            "require": {
                "evenement/evenement": "^3.0 || ^2.0 || ^1.0",
                "php": ">=5.3.8",
                "react/event-loop": "^1.2"
            },
            "require-dev": {
                "clue/stream-filter": "~1.2",
                "phpunit/phpunit": "^9.6 || ^5.7 || ^4.8.36"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "React\\Stream\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "Event-driven readable and writable streams for non-blocking I/O in ReactPHP",
            "keywords": [
                "event-driven",
                "io",
                "non-blocking",
                "pipe",
                "reactphp",
                "readable",
                "stream",
                "writable"
            ],
            "support": {
                "issues": "https://github.com/reactphp/stream/issues",
                "source": "https://github.com/reactphp/stream/tree/v1.4.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2024-06-11T12:45:25+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.31.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "85181ba99b2345b0ef10ce42ecac37612d9fd341"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/85181ba99b2345b0ef10ce42ecac37612d9fd341",
                "reference": "85181ba99b2345b0ef10ce42ecac37612d9fd341",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "provide": {
                "ext-mbstring": "*"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.31.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-09-09T11:45:10+00:00"
        }
    ],
    "packages-dev": [],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": {},
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": ">=8.1.0",
        "ext-bcmath": "*",
        "ext-curl": "*",
        "ext-iconv": "*",
        "ext-pcre": "*",
        "ext-json": "*",
        "ext-openssl": "*",
        "ext-gmp": "*"
    },
    "platform-dev": {},
    "plugin-api-version": "2.6.0"
}


================================================
File: docker-compose.yml
================================================
version: '2.1'
services:

  # Runs a CCXT build & test environment with all the required dependencies installed:
  #
  #     docker-compose run --rm ccxt
  #
  ccxt:
    build:
      context: .
    volumes:
      - .:/ccxt
      - /ccxt/node_modules/ # Prevents exposing container's node_modules to the host filesystem
      - /ccxt/vendor/ # Prevents exposing container's vendor to the host filesystem
    entrypoint: /bin/bash
    stdin_open: true
    tty: true


================================================
File: examples2md.js
================================================
import fs from 'fs'
import path from 'path'

const toTitleCase = (phrase) => {
    return phrase
      .toLowerCase()
      .split(' ')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  };

// Define the Markdown file path
const docsDir = './wiki'
const examplesDir = './examples'
// Copy readme file
console.log ('📰 Creating Examples.md ');
const readmePath = './examples/README.md';
const readmeContent = fs.readFileSync(readmePath, 'utf8');
// replace github links to docs links
const modifiedContent = readmeContent.replaceAll('https://github.com/ccxt/ccxt/tree/master/examples', '/examples').replace (/#+ See Also[\S\s]+/, '')
fs.writeFileSync(path.join(docsDir, 'Examples.md'), modifiedContent);

const languagePaths = {
    'javascript': './examples/js',
    'python': './examples/py',
    'typescript': './examples/ts',
    'php': './examples/php',
}

// Define the Markdown content

const languages = Object.keys(languagePaths);

// create examples folder if doesn't exist
if (!fs.existsSync('./wiki/examples')) {
    fs.mkdirSync('./wiki/examples');
}

languages.forEach(language => {
    console.log (`📰 Creating docs for ${language} examples`);
    const languageDir = languagePaths[language];
    // create language folder if doesn't exist
    const docsLanguageDir = path.join(docsDir, languageDir);
    if (!fs.existsSync(docsLanguageDir)) {
        fs.mkdirSync(docsLanguageDir);
    }
    let mdContent = `<style>ul { margin-bottom: -10px; }</style>\n\n# [<-](Examples?id=${language})\n\n`;
    fs.readdirSync(languageDir).forEach(file => {
        // add to glossary of examplex
        const filename = path.basename(file, path.extname(file));
        //ignore files that start with .
        if (filename.startsWith('.')) return;
        const fileTitle = toTitleCase (filename.replaceAll ('-', ' '));
        // README file: add to existing readme
        if (filename === 'README' && path.extname(file) === '.md') {
            const readmeContent = fs.readFileSync(path.join(languageDir, file), 'utf8');
            mdContent += readmeContent + '\n\n';
            return;
        }
        // Folder: add to gloassy and create link to github
        if (fs.statSync(path.join(languageDir, file)).isDirectory()) {
            mdContent += `- [📂 ${fileTitle}](https://github.com/ccxt/ccxt/tree/master/${languageDir}/${filename})\n\n`;
            return
        }
        // Example file: add to glossary and create markdown file
        mdContent += `- [${fileTitle}](${languageDir}/${filename}.md)\n\n`;
        // create markdown file for example code
        let code = fs.readFileSync(path.join(languageDir, file), 'utf8');
        if (language === 'python') {
            code = code.replace (/^.*os.path.dirname.*$/mg, '').replace (/^sys.path.append.*$\n\n?/mg, '')
        } else if (language === 'php') {
            code = code.replace (/\n^\$root = .*$\n/mg, '').replace (/^include \$root.*$/mg, 'include \'./ccxt.php\';')
        }
        code = code.replace (/\n^#\s?-+$\n\n?/mg, '')
        const codeMd = `- [${fileTitle}](${languageDir}/)\n\n\n \`\`\`${language.replace('typescript', 'javascript')}\n ${code} \n\`\`\``;
        fs.writeFileSync(path.join(docsLanguageDir, `${filename}.md`), codeMd);
    });
    fs.writeFileSync(path.join(docsLanguageDir, 'README.md'), mdContent);
});


================================================
File: exchanges.cfg
================================================
# -------------------------------------------------------------------------------
# You can create a custom bundle of CCXT including only the exchanges you need.
# Add or uncomment ids below and launch `npm run build`.
# Leaving this config empty will build all exchanges.
# -------------------------------------------------------------------------------

# binance
# huobi
# kraken


================================================
File: gource.sh
================================================
#!/bin/sh

gource -1920x1080 -c 4 -s 0.75 -b 000000 --colour-images --padding 1.2 --hide filenames,mouse,progress --bloom-multiplier 0.75 --bloom-intensity 1.5 --logo ccxt-logo-white.svg --highlight-users -o - | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 gource.mp4

================================================
File: index.html
================================================
<html xmlns="http://www.w3.org/1999/xhtml">    
  <head>      
    <title>CryptoCurrency eXchange Trading Library</title>      
    <meta http-equiv="refresh" content="0;URL='http://github.com/ccxt/ccxt'" />    
  </head>
  <body></body>
</html>


================================================
File: jsdoc2md.js
================================================
'use strict'
import jsdoc2md from 'jsdoc-to-markdown'
import fs from 'fs'
import path from 'path'


/* input and output paths */

// Function to get all files that match the glob pattern
const findByExtensionSync = (dir, ext) => {
  const matchedFiles = [];

  const files = fs.readdirSync(dir);

  for (const file of files) {
    const fileExt = path.extname(file);

    if (fileExt === `.${ext}`) {
      matchedFiles.push(path.join(dir,file));
    }
  }

  return matchedFiles;
};

// main function
(async ()=> {

// Get all files to read js docs
const inputFiles = findByExtensionSync('js/src', 'js')
const proInputFiles = findByExtensionSync('js/src/pro', 'js');
const basePartials = './wiki/basePartials/'
const basePartial = fs.readdirSync (basePartials).map (file => basePartials + file)
const exchangePartials = './wiki/exchangePartials/'
const exchangePartial = fs.readdirSync (exchangePartials).map (file => exchangePartials + file)
const outputFolder = './wiki/'
const outputFile = './wiki/baseSpec.md'
const helper = './wiki/helpers.cjs'

console.log ('📰 loading js docs...')
let templateData = await Promise.all(inputFiles.map (file => jsdoc2md.getTemplateData({ files: file })));
templateData = templateData.filter (x => x.length > 0)
// TODO: handle alias exchanges

let proTemplateData = await Promise.all(proInputFiles.map (file => jsdoc2md.getTemplateData({ files: file })));
proTemplateData = proTemplateData.filter (x => x.length > 0)

// assign pro classes to REST template data
proTemplateData.forEach((proData) => {
  const classArray = templateData.find ((template) => template[0].id === proData[0].memberof);
  if (classArray) {
    const classArray = templateData.find ((template) => template[0].id === proData[0].memberof);
    classArray.push(...proData);
  }
})

console.log ('📰 rendering docs for each exchange...')
const template = fs.readFileSync ('./wiki/spec.hbs', 'utf8')

const outputByExchange = await Promise.all (templateData.map (data => jsdoc2md.render ({ template, data, partial: exchangePartial, helper })))
// Group docs by method
const groupedByMethod = templateData.reduce((acc, arr) => {
  arr.filter(obj => obj.kind === 'function' && !obj.ignore).forEach(obj => {
    const method = obj.name;
    if (!acc[method]) {
      acc[method] = [{
        id: method,
        longname: method,
        name: method,
        kind: "",
        scope: "instance",
        description: obj.description,
        params: obj.params,
        returns: obj.returns,
      }];
    }
    obj.exchange = obj.memberof
    obj.memberof = method
    acc[method].push(obj);
  });
  return acc;
}, {});

let duplicateIds = []
const templateDataGroupedByMethod = Object.values(groupedByMethod)
    .map(group => {
        // Filter out duplicate IDs within each group's data array. This is done to avoid Jsdoc2md error: Maximum call stack size exceeded
        return group.filter((item, index, self) => {
            if (index === self.findIndex(el => el.id === item.id)) {
                return true
            } else {
                console.error ('🚨 duplicate id found: ', item.id)
                duplicateIds.push (item.id)
                return false
            }
          }
        );
    })
    .sort((a, b) => a[0].name < b[0].name ? -1 : 1);

if (duplicateIds.length > 0) {
  throw new Error ('🚨 duplicate ids found: ' + duplicateIds.join (', '))
}

const baseOutput = await Promise.all(templateDataGroupedByMethod.map(data => 
    jsdoc2md.render({ template, data, partial: basePartial, helper})
));

console.log ('📰 creating index of exchange functions')
const exchangeLinks = []
outputByExchange.forEach ((output, i) => {
  const name = templateData[i][0].id
  const fileName = 'exchanges/' + name + '.md'
  try {
    fs.writeFileSync(outputFolder + fileName, output)
  } catch (e) {
    const error = `Error writing file ${fileName}: ${e.message}`
    console.error(error)
    throw error
  }
  exchangeLinks.push (`\t- [${name}](${fileName})`)
})


fs.writeFileSync (outputFile, baseOutput.join ('\n---\n'))

const sidebar =
`
- [Install](Install.md)
- [Examples](Examples.md)
- [Manual](Manual.md)
- [CCXT Pro](ccxt.pro.manual.md)
- [Contributing](CONTRIBUTING.md)
- [Supported Exchanges](Exchange-Markets.md)
- [Exchanges By Country](Exchange-Markets-By-Country.md)
- [API Spec By Method](baseSpec.md)
- [FAQ](FAQ.md)
- [Changelog](CHANGELOG.md)
- [Awesome](Awesome.md)
- API Spec by Exchange
${exchangeLinks.join('\n')}
`
fs.writeFileSync('./wiki/_sidebar.md', sidebar);

console.log ('📰 finished rendering docs! 🙌 😶‍🌫')

})()



================================================
File: keys.json
================================================
{
    "sampleExchange" : {
        "httpProxy": "012.345.678.910",
        "apiKey": "xxxxxxxx",
        "secret": "xxxxxxxx",
        "options": {
            "defaultType": "spot"
        }
    }
}


================================================
File: package.json
================================================
{
  "name": "ccxt",
  "version": "4.4.61",
  "description": "A JavaScript / TypeScript / Python / C# / PHP cryptocurrency trading library with support for 100+ exchanges",
  "unpkg": "dist/ccxt.browser.min.js",
  "type": "module",
  "exports": {
    ".": {
      "import": "./js/ccxt.js",
      "require": "./dist/ccxt.cjs"
    }
  },
  "bin": {
    "ccxt": "examples/js/cli.js"
  },
  "engines": {
    "node": ">=15.0.0"
  },
  "publishConfig": {
    "registry": "https://registry.npmjs.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/ccxt/ccxt.git"
  },
  "readme": "README.md",
  "scripts": {
    "instrument": "nyc instrument js/ jsInstrumented/",
    "nyc-coverage": "nyc --reporter=html --reporter=lcov --exclude='js/src/pro/**' --exclude='js/src/base/**' --exclude='js/src/test/**' --exclude='js/src/abstract/**' --exclude='js/src/static_dependencies' node jsInstrumented/src/test/tests.init.js --requestTests --responseTests",
    "coverage-js": "npm run instrument && npm run nyc-coverage && rm -rf jsInstrumented",
    "docker": "docker-compose run --rm ccxt",
    "fixTSBug": "node build/fixTSBug",
    "transpileCsSingle": "tsx build/csharpTranspiler.ts",
    "transpileCS": "tsx build/csharpTranspiler.ts --multi",
    "transpileCSWs": "tsx build/csharpTranspiler.ts --ws",
    "buildCS": "dotnet build cs/ccxt.sln",
    "buildGO": "cd go && go build ./v4 && cd ..",
    "transpileGO": "tsx build/goTranspiler.ts",
    "buildCSRelease": "dotnet build cs --configuration Release",
    "csharp": "npm run transpileCS && npm run transpileCSWs && npm run buildCS",
    "go": "npm run transpileGO && npm run buildGO",
    "force-build//WithoutGo": "npm run pre-transpile && npm run force-transpile-fast && npm run csharp && npm run post-transpile && npm run update-badges",
    "force-build": "npm run pre-transpile && npm run go && npm run force-transpile-fast && npm run csharp && npm run post-transpile && npm run update-badges",
    "//TMPCommentforce-build": "npm run pre-transpile && npm run force-transpile-fast && npm run csharp && npm run go && npm run post-transpile && npm run update-badges",
    "build-docs": "node jsdoc2md.js && node examples2md.js",
    "serve-docs": "docsify serve ./wiki",
    "tsBuildFile": "tsc --skipLibCheck --strictNullChecks false --strict --noImplicitAny false --esModuleInterop --isolatedModules false --forceConsistentCasingInFileNames --removeComments false --target ES2020 --declaration --allowJs --checkJs false --moduleResolution Node --module ES2022 --outDir ./js/src --lib ES2020.BigInt --lib dom ",
    "addJsHeaders": "tsx build/transpile.ts --js-headers",
    "tsBuild": "tsc && npm run addJsHeaders || echo \"\"",
    "tsBuildExamples": "tsc -p ./examples/tsconfig.json",
    "emitAPI": "tsx build/generateImplicitAPI.ts",
    "emitAPITs": "tsx build/generateImplicitAPI.ts -- --ts",
    "emitAPIPy": "tsx build/generateImplicitAPI.ts -- --python",
    "emitAPIPhp": "tsx build/generateImplicitAPI.ts -- --php",
    "emitAPIGo": "tsx build/generateImplicitAPI.ts -- --go",
    "emitAPICs": "tsx build/generateImplicitAPI.ts -- --csharp",
    "build": "npm run pre-transpile && npm run transpile && npm run post-transpile && npm run update-badges && npm run build-docs",
    "force-build-slow": "npm run pre-transpile && npm run force-transpile && npm run post-transpile && npm run update-badges",
    "pre-transpile-js": "npm run export-exchanges && npm run vss && npm run emitAPITs && npm run tsBuild && npm run validate-types && npm run tsBuildExamples && npm run check-js-syntax && npm run bundle",
    "pre-transpile-py": "npm run export-exchanges && npm run emitAPIPy",
    "pre-transpile-php": "npm run export-exchanges && npm run emitAPIPhp",
    "pre-transpile-go": "npm run export-exchanges && npm run emitAPIGo",
    "pre-transpile-js-simple": "npm run export-exchanges && npm run emitAPITs && tsc && npm run validate-types",
    "pre-transpile-cs": "npm run export-exchanges && npm run emitAPICs",
    "pre-transpile": "npm run export-exchanges && npm run vss && npm run tsBuild && npm run emitAPI && npm run validate-types && npm run tsBuildExamples && npm run copy-python-files && npm run check-js-syntax && npm run bundle",
    "pre-transpile-pr": "npm run export-exchanges && npm run tsBuild && npm run emitAPI && npm run check-js-syntax",
    "post-transpile": "npm run check-python-syntax && npm run check-php-syntax",
    "cli.js": "node ./examples/js/cli.js",
    "cli.py": "python3 ./examples/py/cli.py",
    "cli.php": "php ./examples/php/cli.php",
    "cli.ts": "tsx examples/ts/cli.ts",
    "cli.cs": "dotnet run --project \"./cs/cli/cli.csproj\"",
    "cli.go": "go run ./go/cli/main.go",
    "export-exchanges": "node build/export-exchanges",
    "capabilities": "node ./examples/js/exchange-capabilities.js",
    "git-ignore-generated-files": "node build/git-ignore-generated-files.cjs",
    "git-unignore-generated-files": "node build/git-ignore-generated-files.cjs --unignore",
    "update-badges": "node build/update-badges",
    "update-links": "node build/update-links",
    "transpile": "npm run transpileRest && npm run transpileWs",
    "transpileRest": "tsx build/transpile.ts",
    "transpileWs": "tsx build/transpileWS.ts",
    "force-transpile": "npm run force-transpileRest && npm run force-transpileWs",
    "force-transpile-fast": "npm run dev-force-transpile",
    "force-transpile-fast-py": "npm run fast-force-transpileRest-py && npm run fast-force-transpileWs-py",
    "force-transpile-fast-php": "npm run fast-force-transpileRest-php && npm run fast-force-transpileWs-php",
    "dev-force-transpile": "npm run fast-force-transpileRest && npm run fast-force-transpileWs",
    "force-transpileRest": "tsx build/transpile.ts --force",
    "fast-force-transpileRest-py": "tsx build/transpile.ts --multiprocess --force --python",
    "fast-force-transpileRest-php": "tsx build/transpile.ts --multiprocess --force --php",
    "fast-force-transpileRest": "tsx build/transpile.ts --multiprocess --force",
    "force-transpileWs": "tsx build/transpileWS.ts --force",
    "fast-force-transpileWs": "tsx build/transpileWS.ts --multiprocess --force",
    "fast-force-transpileWs-py": "tsx build/transpileWS.ts --multiprocess --force --python",
    "fast-force-transpileWs-php": "tsx build/transpileWS.ts --multiprocess --force --php",
    "vss": "node build/vss",
    "lint": "eslint \"ts/src/*.ts\" \"ts/src/base/Exchange.ts\" \"ts/src/pro/*.ts\" --cache --cache-location .cache/eslintcache --cache-strategy metadata",
    "check-syntax": "npm run transpile && npm run check-js-syntax && npm run check-python-syntax && npm run check-php-syntax",
    "check-js-syntax": "node -e \"console.log(process.cwd())\" && eslint --version && npm run lint",
    "eslint": "eslint",
    "check-python-syntax": "cd python && tox -e qa && cd ..",
    "check-python-types": "cd python && tox -e type && cd ..",
    "check-php-syntax": "npm run check-rest-php-syntax && npm run check-ws-php-syntax",
    "check-rest-php-syntax": "php -f php/test/custom/syntax.php",
    "check-ws-php-syntax": "php -f php/pro/test/custom/syntax.php",
    "bundle": "npm run bundle-cjs && npm run bundle-browser",
    "bundle-cjs": "rollup -c rollup.config.js",
    "bundle-browser": "webpack build -c webpack.config.js && webpack build -c webpack.config.js --optimization-minimize --output-filename ccxt.browser.min.js",
    "copy-python-files": "npm run copy-python-package && npm run copy-python-license && npm run copy-python-keys && npm run copy-python-readme",
    "copy-python-package": "node build/copy package.json python/package.json",
    "copy-python-license": "node build/copy LICENSE.txt python/LICENSE.txt",
    "copy-python-keys": "node build/copy keys.json python/keys.json",
    "copy-python-readme": "node build/copy README.md python/README.md",
    "postinstall": "node postinstall.js",
    "validate-types": "tsx build/validate-types.ts",
    "runtests": "node run-tests",
    "live-tests": "node run-tests --useProxy",
    "live-tests-rest": "npm run live-tests",
    "live-tests-ws": "npm run live-tests -- --ws",
    "live-tests-rest-ts": "npm run live-tests -- --ts",
    "live-tests-ws-ts": "npm run live-tests -- --ts     --ws",
    "live-tests-rest-js": "npm run live-tests -- --js",
    "live-tests-ws-js": "npm run live-tests -- --js     --ws",
    "live-tests-rest-py": "npm run live-tests -- --python",
    "live-tests-ws-py": "npm run live-tests -- --python --ws",
    "live-tests-rest-php": "npm run live-tests -- --php",
    "live-tests-ws-php": "npm run live-tests -- --php    --ws",
    "live-tests-rest-csharp": "npm run live-tests -- --csharp",
    "live-tests-rest-go": "npm run live-tests -- --go",
    "live-tests-ws-csharp": "npm run live-tests -- --csharp --ws",
    "ti-ts": "tsx ts/src/test/tests.init.ts",
    "ti-js": "node js/src/test/tests.init.js",
    "ti-py": "python3 python/ccxt/test/tests_init.py",
    "ti-php": "php php/test/tests_init.php",
    "ti-cs": "dotnet run --project cs/tests/tests.csproj",
    "ti-go": "cd go/ && go run ./tests/main.go",
    "request-ts": "npm run ti-ts  -- --requestTests",
    "request-js": "npm run ti-js  -- --requestTests",
    "request-py-async": "npm run ti-py  -- --requestTests",
    "request-py-sync": "npm run ti-py  -- --requestTests --sync",
    "request-py": "npm run request-py-sync && npm run request-py-async",
    "request-php-async": "npm run ti-php -- --requestTests",
    "request-php-sync": "npm run ti-php -- --requestTests --sync",
    "request-php": "npm run request-php-sync && npm run request-php-async",
    "request-cs": "npm run ti-cs  -- --requestTests",
    "request-go": "cd go/ && npm run ti-go -- --requestTests && cd ../",
    "request-tests//withoutGo": "npm run request-js && npm run request-py && npm run request-php && npm run request-cs",
    "request-tests": "npm run request-js && npm run request-py && npm run request-php && npm run request-cs && npm run request-go",
    "response-ts": "npm run ti-ts  -- --responseTests",
    "response-js": "npm run ti-js  -- --responseTests",
    "response-py-sync": "npm run ti-py  -- --responseTests --sync",
    "response-py-async": "npm run ti-py  -- --responseTests",
    "response-py": "npm run response-py-sync && npm run response-py-async",
    "response-cs": "npm run ti-cs  -- --responseTests",
    "response-go": "cd go/ && npm run ti-go  -- --responseTests && cd ../",
    "response-php-async": "npm run ti-php -- --responseTests",
    "response-php-sync": "npm run ti-php -- --responseTests --sync",
    "response-php": "npm run response-php-sync && npm run response-php-async",
    "response-tests": "npm run response-js && npm run response-py && npm run response-php && npm run response-cs && npm run response-go",
    "response-tests//withoutGo": "npm run response-js && npm run response-py && npm run response-php && npm run response-cs",
    "static-updater": "tsx ./utils/update-static-json --update",
    "id-tests-js": "npm run ti-js  -- --idTests",
    "id-tests-py": "npm run ti-py  -- --idTests",
    "id-tests-php": "npm run ti-php -- --idTests",
    "id-tests-cs": "npm run ti-cs  -- --idTests",
    "id-tests-go": "npm run ti-go  -- --idTests",
    "id-tests": "npm run id-tests-js && npm run id-tests-py && npm run id-tests-php && npm run id-tests-cs",
    "id-tests//withGO": "npm run id-tests-js && npm run id-tests-py && npm run id-tests-php && npm run id-tests-cs && npm run id-tests-go",
    "test-base-rest-ts": "npm run ti-ts  -- --baseTests",
    "test-base-rest-js": "npm run ti-js  -- --baseTests",
    "test-base-rest-py": "npm run ti-py  -- --baseTests",
    "test-base-rest-php": "npm run ti-php -- --baseTests",
    "test-base-rest-cs": "npm run ti-cs  -- --baseTests",
    "test-base-rest-go": "cd go/ && npm run ti-go  -- --baseTests && cd ../",
    "test-base-ws-ts": "npm run ti-ts  -- --baseTests --ws",
    "test-base-ws-js": "npm run ti-js  -- --baseTests --ws",
    "test-base-ws-py": "npm run ti-py  -- --baseTests --ws",
    "test-base-ws-php": "npm run ti-php -- --baseTests --ws",
    "test-base-ws-cs": "npm run ti-cs  -- --baseTests --ws",
    "test-base-rest": "npm run test-base-rest-js && npm run test-base-rest-py && npm run test-base-rest-php && npm run test-base-rest-cs",
    "test-base-ws": "npm run test-base-ws-js   && npm run test-base-ws-py   && npm run test-base-ws-php   && npm run test-base-ws-cs",
    "test": "npm run build && npm run commonjs-test && npm run id-tests && npm run request-tests && npm run response-tests && npm run live-tests",
    "commonjs-test": "node ./utils/test-commonjs.cjs",
    "package-test": "./utils/package-test.sh",
    "test-freshness": "tsx ./utils/test-freshness.ts",
    "benchmark": "tsx examples/ts/benchmark.ts",
    "cleanup-old-tags": "tsx ./build/cleanup-old-tags.ts",
    "test-types-go": "cd go && go run ./tests/types/types.go"
  },
  "types": "./js/ccxt.d.ts",
  "devDependencies": {
    "@rollup/plugin-commonjs": "^21.0.3",
    "@rollup/plugin-json": "^4.1.0",
    "@rollup/plugin-node-resolve": "^15.2.3",
    "@types/node": "^18.15.11",
    "@typescript-eslint/eslint-plugin": "^5.30.5",
    "@typescript-eslint/parser": "^5.30.5",
    "ansicolor": "1.1.81",
    "as-table": "1.0.37",
    "asciichart": "^1.5.25",
    "assert": "^2.0.0",
    "ast-transpiler": "^0.0.65",
    "docsify": "^4.11.4",
    "eslint": "8.22.0",
    "eslint-config-airbnb-base": "15.0.0",
    "eslint-plugin-import": "2.25.4",
    "eslint-plugin-jsdoc": "^46.9.0",
    "esmify": "^2.1.1",
    "https-proxy-agent": "^5.0.1",
    "jsdoc-to-markdown": "^8.0.0",
    "ololog": "1.1.155",
    "piscina": "^3.2.0",
    "replace-in-file": "^6.3.5",
    "rollup": "^2.70.1",
    "rollup-plugin-execute": "1.1.1",
    "terser-webpack-plugin": "^5.3.9",
    "ts-loader": "^9.4.2",
    "tsx": "^4.7.2",
    "typescript": "4.7.4",
    "webpack": "^5.76.2",
    "webpack-cli": "^5.0.1"
  },
  "author": {
    "name": "Igor Kroitor",
    "email": "igor.kroitor@gmail.com",
    "url": "https://github.com/kroitor"
  },
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/ccxt/ccxt/issues"
  },
  "homepage": "https://ccxt.com",
  "keywords": [
    "algorithmic",
    "algotrading",
    "altcoin",
    "altcoins",
    "api",
    "arbitrage",
    "real-time",
    "realtime",
    "backtest",
    "backtesting",
    "bitcoin",
    "bot",
    "btc",
    "cny",
    "coin",
    "coins",
    "crypto",
    "cryptocurrency",
    "crypto currency",
    "crypto market",
    "currency",
    "currencies",
    "darkcoin",
    "dash",
    "digital currency",
    "doge",
    "dogecoin",
    "e-commerce",
    "etc",
    "eth",
    "ether",
    "ethereum",
    "exchange",
    "exchanges",
    "eur",
    "framework",
    "invest",
    "investing",
    "investor",
    "library",
    "light",
    "litecoin",
    "ltc",
    "market",
    "market data",
    "markets",
    "merchandise",
    "merchant",
    "minimal",
    "ohlcv",
    "order",
    "orderbook",
    "order book",
    "price",
    "price data",
    "pricefeed",
    "private",
    "public",
    "ripple",
    "strategy",
    "ticker",
    "tickers",
    "toolkit",
    "trade",
    "trader",
    "trading",
    "usd",
    "volume",
    "websocket",
    "websockets",
    "web socket",
    "web sockets",
    "ws",
    "xbt",
    "xrp",
    "zec",
    "zerocoin"
  ],
  "collective": {
    "type": "opencollective",
    "url": "https://opencollective.com/ccxt",
    "logo": "https://opencollective.com/ccxt/logo.txt"
  },
  "ethereum": "0x26a3CB49578F07000575405a57888681249c35Fd",
  "dependencies": {
    "ws": "^8.8.1"
  }
}


================================================
File: phpunit.xml.dist
================================================
<?xml version="1.0" encoding="UTF-8"?>

<phpunit bootstrap="php/test/bootstrap.php"
         backupGlobals="false"
         backupStaticAttributes="false"
         colors="true"
         verbose="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         processIsolation="true"
         stopOnFailure="false">

    <testsuites>
        <testsuite name="ccxt Test Suite">
            <directory>php/test</directory>
        </testsuite>
    </testsuites>

    <filter>
        <whitelist>
            <directory suffix=".php">php</directory>
        </whitelist>
    </filter>

    <php>
        <ini name="memory_limit" value="-1" />
    </php>
</phpunit>


================================================
File: postinstall.js
================================================
import fetch from './js/src/static_dependencies/node-fetch/index.js'

function style(s, style) {
    return style + s + '\x1b[0m'
}

const colors = {
    black: 30,
    red: 31,
    green: 32,
    yellow: 33,
    blue: 34,
    white: 37,
    gray: 90,
}

let colorFunctions = {}
for (let color of Object.keys (colors)) {
    colorFunctions[color] = (s) => console.log (style (s, '\x1b[' + colors[color].toString () + 'm'))
}

let ascii = [
    '                                                              ',
    '                                                              ',
    '                     ████████████████████████████████████     ',
    '                     ████████████████████████████████████     ',
    '                     ████            ████            ████     ',
    '                     ████            ████            ████     ',
    '                     ████    ████████████    ████████████     ',
    '                     ████    ████████████    ████████████     ',
    '                     ████            ████            ████     ',
    '                     ████            ████            ████     ',
    '                     ████████████████████████████████████     ',
    '                     ████████████████████████████████████     ',
    '                     ████    ████    ████            ████     ',
    '                     ████    ████    ████            ████     ',
    '                     ████████    ████████████    ████████     ',
    '                     ████████    ████████████    ████████     ',
    '                     ████    ████    ████████    ████████     ',
    '                     ████    ████    ████████    ████████     ',
    '                     ████████████████████████████████████     ',
    '                     ████████████████████████████████████     ',
    '                                                              ',
    '                                                              ',
]

async function getData () {
    const [collectiveData_result, githubData_result] = await Promise.all ([fetch ('https://opencollective.com/ccxt.json'), fetch ('https://api.github.com/repos/ccxt/ccxt')])
    const collectiveData = await collectiveData_result.json()
    const githubData = await githubData_result.json()

    return {
        contributors: collectiveData['contributorsCount'].toLocaleString (),
        backers: collectiveData['backersCount'].toLocaleString (),
        balance: Math.floor (collectiveData['balance'] / 100).toLocaleString (),
        budget: Math.floor (collectiveData['yearlyIncome'] / 100).toLocaleString (),
        stars: githubData['stargazers_count'].toLocaleString (),
        forks: githubData['forks_count'].toLocaleString (),
        size: (githubData['size'] / 1000000).toFixed (2)
    }
}

function pad (string) {
    const padding = 80 - string.length
    const half = Math.floor (padding / 2)
    return ' '.repeat (half + (padding % 2)) + string + ' '.repeat (half)
}

async function main () {

    try {

        const data = await getData()

        colorFunctions['blue'] (ascii.join ('\n'))
        colorFunctions['red'] (pad (`Stars: ${data.stars}`))
        colorFunctions['red'] (pad (`Forks: ${data.forks}`))
        colorFunctions['red'] (pad (`Size: ${data.size}MB`))
        colorFunctions['yellow'] ('\n' + pad ('Thanks for installing ccxt 🙏'))
        colorFunctions['gray'] (pad ('Please consider donating to our open collective'))
        colorFunctions['gray'] (pad ('to help us maintain this package.'))
        colorFunctions['yellow'] (pad ('👉 Donate: https://opencollective.com/ccxt/donate 🎉'))

    } catch (e) {

        // console.log (e.constructor.name, e.message)
    }
}

main()


================================================
File: pyproject.toml
================================================
[tool.ruff]
preview = true
select = ["W", "F", "E"]
ignore = ["F722","F841","F821","E402","E501","E902","E713","E741","E714", "E275","E721"]

exclude = [
"static_dependencies"
]

================================================
File: rollup.config.js
================================================
import commonjs from "@rollup/plugin-commonjs";
import json from "@rollup/plugin-json";
import execute from 'rollup-plugin-execute';
import nodeResolve from '@rollup/plugin-node-resolve'

export default [
  {
    preserveModules: true,
    input: "./js/ccxt.js",
    output: [
      {
        dir: "./dist/cjs/",
        format: "cjs",
      }
    ],
    plugins: [
      nodeResolve({
        preferBuiltins: true,
        // node resolve generate dist/cjs/js directory 
        jail: '/src'
      }),
      json(),
      commonjs({
        transformMixedEsModules: true,
        dynamicRequireTargets: ["**/js/src/static_dependencies/**/*.cjs"],
      }),
      execute("echo '{ \"type\": \"commonjs\" }' > ./dist/cjs/package.json") // this is needed to make node treat files inside dist/cjs as CJS modules
    ],
    onwarn: ( warning, next ) => {
      if ( warning.message.indexOf('is implicitly using "default" export mode') > -1 ) return;
      next( warning );
    },
    external: [
      'socks-proxy-agent',
      // node resolve generate dist/cjs/js directory, treat ws, debug as external
      'ws', 'debug'
    ]
  }
];

================================================
File: run-tests-simul.sh
================================================
#!/bin/bash

# Check for provided arguments
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 [args...]"
    exit 1
fi

function run_all {
    local lang="$1"
    # Run the command twice in the background
    echo "Running all 'npm run live-tests $lang' Rest and WS tests in parallel..."

    npm run live-tests -- $lang &
    PID1=$! # Store the PID of the first background process

    npm run live-tests-ws -- $lang &
    PID2=$! # Store the PID of the second background process

    wait $PID1
    STATUS1=$?

    wait $PID2
    STATUS2=$?

    if [ $STATUS1 -eq 0 ] && [ $STATUS2 -eq 0 ]; then
        echo "Both 'npm run live-tests --$lang' completed successfully."
        exit 0
    else
        echo "One or both 'npm run live-tests $lang' commands failed."
        exit 1
    fi

}

function run_specific_tests {
  local rest_args=
  local ws_args=
  local lang=
  if [ $# -eq 3 ]; then
    lang="$1"
    rest_args="$2"
    ws_args="$3"
    # echo "inside rest_args: $rest_args"
    # echo "inside ws_args: $ws_args"
    if [ -z "$rest_args" ]; then
      : &
      local rest_pid=$!
    fi
    if [ -z "$ws_args" ]; then
      : &
      local ws_pid=$!
    fi
  fi

  if [ -z "$rest_pid" ]; then
    if [ -z "$rest_args" ] || { [ -n "$rest_args" ] && [ "$rest_args" != "skip" ]; }; then
      # shellcheck disable=SC2086
      npm run live-tests -- $lang $rest_args &
      local rest_pid=$!
    fi
  fi
  if [ -z "$ws_pid" ]; then
    if [ -z "$ws_args" ] || { [ -n "$ws_args" ] && [ "$ws_args" != "skip" ]; }; then
      # shellcheck disable=SC2086
      npm run live-tests -- $lang --ws $ws_args &
      local ws_pid=$!
    fi
  fi

  if [ -n "$rest_pid" ] && [ -n "$ws_pid" ]; then
    wait $rest_pid && wait $ws_pid
  elif [ -n "$rest_pid" ]; then
    wait $rest_pid
  else
    wait $ws_pid
  fi
}



lang="$1"

if [ "$#" -lt 2 ]; then
    run_all "$lang"
else
    rest_exchanges="$2"
    ws_exchanges="$3"
    # echo "beofre calling run_specific_tests"
    # echo "rest_exchanges: $rest_exchanges"
    # echo "ws_exchanges: $ws_exchanges"
    run_specific_tests "$lang" "$rest_exchanges" "$ws_exchanges"
fi


================================================
File: run-tests.js
================================================
/*  ---------------------------------------------------------------------------

A tests launcher. Runs tests for all languages and all exchanges, in
parallel, with a humanized error reporting.

Usage: node run-tests [--php] [--js] [--python] [--python-async] [exchange] [method|symbol]

--------------------------------------------------------------------------- */

import fs from 'fs'
import ansi from 'ansicolor'
import log from 'ololog'
import ps from 'child_process'
ansi.nice
//  --------------------------------------------------------------------------- //

process.on ('uncaughtException',  e => { log.bright.red.error (e); process.exit (1) })
process.on ('unhandledRejection', e => { log.bright.red.error (e); process.exit (1) })

//  --------------------------------------------------------------------------- //

const [,, ...args] = process.argv

const langKeys = {
    '--ts': false,      // run TypeScript tests only
    '--js': false,      // run JavaScript tests only
    '--php': false,     // run PHP tests only
    '--python': false,  // run Python 3 tests only
    '--python-async': false, // run Python 3 async tests only
    '--csharp': false,  // run C# tests only
    '--php-async': false,    // run php async tests only,
    '--go': false,      // run GO tests only
}

const debugKeys = {
    '--warnings': false,
    '--info': false,
}

const exchangeSpecificFlags = {
    '--ws': false,
    '--sandbox': false,
    '--useProxy': false,
    '--verbose': false,
    '--private': false,
    '--privateOnly': false,
    '--request': false,
    '--response': false,
}

let exchanges = []
let symbol = 'all'
let method = undefined
let maxConcurrency = 5 // Number.MAX_VALUE // no limit

for (const arg of args) {
    if (arg in exchangeSpecificFlags)        { exchangeSpecificFlags[arg] = true }
    else if (arg.startsWith ('--'))          {
        if (arg in langKeys) {
            langKeys[arg] = true
        } else if (arg in debugKeys) {
            debugKeys[arg] = true
        } else {
            log.bright.red ('\nUnknown option', arg.white, '\n');
        }
    }
    else if (arg.includes ('()'))            { method = arg }
    else if (arg.includes ('/'))             { symbol = arg }
    else if (Number.isFinite (Number (arg))) { maxConcurrency = Number (arg) }
    else                                     { exchanges.push (arg) }
}

const wsFlag = exchangeSpecificFlags['--ws'] ? 'WS': '';

// for REST exchange test, we might need to wait for 200+ seconds for some exchanges
// for WS, watchOHLCV might need 60 seconds for update (so, spot & swap ~ 120sec)
const timeoutSeconds = wsFlag ? 120 : 250;


//  --------------------------------------------------------------------------- //

const exchangeOptions = []
for (const key of Object.keys (exchangeSpecificFlags)) {
    if (exchangeSpecificFlags[key]) {
        exchangeOptions.push (key)
    }
}
//  --------------------------------------------------------------------------- //

const content = fs.readFileSync ('./skip-tests.json', 'utf8');
const skipSettings = JSON.parse (content);

if (!exchanges.length) {

    if (!fs.existsSync ('./exchanges.json')) {

        log.bright.red ('\n\tNo', 'exchanges.json'.white, 'found, please run', 'npm run build'.white, 'to generate it!\n')
        process.exit (1)
    }
    let exchangesFile =  fs.readFileSync('./exchanges.json');
    exchangesFile = JSON.parse(exchangesFile)
    exchanges = wsFlag ? exchangesFile.ws : exchangesFile.ids
}

//  --------------------------------------------------------------------------- //

const sleep = s => new Promise (resolve => setTimeout (resolve, s*1000))
const timeout = (s, promise) => Promise.race ([ promise, sleep (s).then (() => {
    throw new Error ('RUNTEST_TIMED_OUT');
}) ])

//  --------------------------------------------------------------------------- //

const exec = (bin, ...args) => { 

/*  A custom version of child_process.exec that captures both stdout and
    stderr,  not separating them into distinct buffers — so that we can show
    the same output as if it were running in a terminal.                        */

    let output = ''
    let stderr = ''

    const generateResultFromOutput = (output, stderr, code) => {
            // keep this commented code for a while (just in case), as the below avoids vscode false positive warnings from output: https://github.com/nodejs/node/issues/34799 during debugging
            // const removeDebuger = (str) => str.replace ('Debugger attached.','').replace('Waiting for the debugger to disconnect...', '').replace(/\(node:\d+\) ExperimentalWarning: Custom ESM Loaders is an experimental feature and might change at any time\n\(Use `node --trace-warnings ...` to show where the warning was created\)\n/, '');
            // stderr = removeDebuger(stderr), output = removeDebuger(output);

            output = ansi.strip (output.trim ())

            // detect error
            const hasFailed = (
                // exception caught in "test -> testMethod"
                output.indexOf('[TEST_FAILURE]') > -1 ||
                // 1) thrown from JS assert module
                output.indexOf('AssertionError:') > -1 ||
                // 2) thrown from PYTHON (i.e. [AssertionError], [KeyError], [ValueError], etc)
                output.match(/\[\w+Error\]/) ||
                // 3) thrown from PHP assert hook
                output.indexOf('[ASSERT_ERROR]') > -1 ||
                // 4) thrown from PHP async library
                output.indexOf('Fatal error:') > -1
            );

            // ### Infos ###
            const infos = []
            // check output for pattern like `[INFO:TESTING] xyz message`
            if (output.length) {
                const infoRegex = /\[INFO(|:([\w_-]+))\].+$(?!\n)*/gm
                let matchInfo;
                while ((matchInfo = infoRegex.exec (output))) {
                    infos.push (matchInfo[0])
                }
            }

            // ### Warnings ###
            const warnings = []
            // check output for pattern like `[TEST_WARNING] whatever`
            if (output.length) {
                const warningRegex = /\[TEST_WARNING\].+$(?!\n)*/gmi
                let matchWarnings; 
                while (matchWarnings = warningRegex.exec (stderr)) {
                    warnings.push (matchWarnings[0])
                }
            }
            // check stderr
            if (stderr.length > 0) {
                warnings.push (stderr)
            }

            return {
                failed: hasFailed || code !== 0,
                output,
                warnings,
                infos,
            }
    }

    return timeout (timeoutSeconds, new Promise (resolver => {

        const psSpawn = ps.spawn (bin, args)

        psSpawn.stdout.on ('data', data => { output += data.toString () })
        psSpawn.stderr.on ('data', data => { output += data.toString (); stderr += data.toString ().trim (); })

        psSpawn.on ('exit', code => {
            const result = generateResultFromOutput (output, stderr, code)
            return resolver (result) ;
        })

    })).catch (e => {
        const isTimeout = e.message === 'RUNTEST_TIMED_OUT';
        if (isTimeout) {
            stderr += '\n' + 'RUNTEST_TIMED_OUT: ';
            const result = generateResultFromOutput (output, stderr, 0);
            return result;
        }
        return {
            failed: true,
            output: e.message,
            warnings: [],
            infos: [],
        }
    } );
};

//  ------------------------------------------------------------------------ //

// const execWithRetry = () => {

//     // Sometimes execution (on a remote CI server) is just fails with no
//     // apparent reason, leaving an empty stdout/stderr behind. I suspect
//     // it's related to out-of-memory errors. So in that case we will re-try
//     // until it eventually finalizes.
// }

//  ------------------------------------------------------------------------ //

let numExchangesTested = 0

//  Tests of different languages for the same exchange should be run sequentially to prevent the interleaving nonces problem. //

const sequentialMap = async (input, fn) => {

    const result = []
    for (const item of input) { result.push (await fn (item)) }
    return result
}

//  ------------------------------------------------------------------------ //

const percentsDone = () => ((numExchangesTested / exchanges.length) * 100).toFixed (0) + '%';

const testExchange = async (exchange) => {

    // no need to test alias classes
    if (exchange.alias) {
        numExchangesTested++;
        log.bright (('[' + percentsDone() + ']').dim, 'Tested', exchange.cyan, wsFlag, '[Skipped alias]'.yellow)
        return [];
    }

    if (
        skipSettings[exchange] && 
        (
            (skipSettings[exchange].skip && !wsFlag)
                ||
            (skipSettings[exchange].skipWs && wsFlag)
        ) 
    ) {
        if (!('until' in skipSettings[exchange]) || new Date(skipSettings[exchange].until) > new Date()) {
            numExchangesTested++;
            const reason = ('until' in skipSettings[exchange]) ? ' till ' + skipSettings[exchange].until : '';
            log.bright (('[' + percentsDone() + ']').dim, 'Tested', exchange.cyan, wsFlag, ('[Skipped]' + reason).yellow)
            return [];
        }
    }

    //  Run tests for all/selected languages (in parallel)     //
    let args = [exchange];
    if (symbol !== undefined && symbol !== 'all') {
        args.push(symbol);
    }
    if (method !== undefined) {
        args.push(method);
    }
    args = args.concat(exchangeOptions)
    // pass it to the test(ts/py/php) script too
    if (debugKeys['--info']) {
        args.push ('--info')
    }
    let allTests = [
        { key: '--js',           language: 'JavaScript',   exec: ['node',      'js/src/test/tests.init.js',                     ...args] },
        { key: '--python-async', language: 'Python Async', exec: ['python3',   'python/ccxt/test/tests_init.py',          ...args] },
        { key: '--php-async',    language: 'PHP Async',    exec: ['php', '-f', 'php/test/tests_init.php',                 ...args] },
        { key: '--csharp',       language: 'C#',           exec: ['dotnet', 'run', '--project', 'cs/tests/tests.csproj',  ...args] },
        { key: '--ts',           language: 'TypeScript',   exec: ['node',  '--import', 'tsx', 'ts/src/test/tests.init.ts',      ...args] },
        { key: '--python',       language: 'Python',       exec: ['python3',   'python/ccxt/test/tests_init.py',  '--sync',  ...args] },
        { key: '--php',          language: 'PHP',          exec: ['php', '-f', 'php/test/tests_init.php', '--', '--sync',  ...args] },
        { key: '--go',           language: 'GO',           exec: [ 'cd go/ && go run tests/main.go',          ...args] },
    ];

    // select tests based on cli arguments
    let selectedTests = [];
    const langsAreProvided = (Object.values (langKeys).filter (x => x===true)).length > 0;
    if (langsAreProvided) {
        selectedTests = allTests.filter (t => langKeys[t.key]);
    } else {
        selectedTests = allTests.filter (t => t.key !== '--ts'); // exclude TypeScript when running all tests without specific languages
    }

    // remove skipped tests
    if (skipSettings[exchange]) {
        if (skipSettings[exchange].skipCSharp)   selectedTests = selectedTests.filter (t => t.key !== '--csharp'); 
        if (skipSettings[exchange].skipPhpAsync) selectedTests = selectedTests.filter (t => t.key !== '--php-async');
    }
    // if it's WS tests, then remove sync versions (php & python) from queue
    if (wsFlag) {
        selectedTests = selectedTests.filter (t => t.key !== '--python' && t.key !== '--php');
    }

    const completeTests  = await sequentialMap (selectedTests, async test => Object.assign (test, await  exec (...test.exec)));
    const failed         = completeTests.find (test => test.failed);
    const hasWarnings    = completeTests.find (test => test.warnings.length);
    const warnings       = completeTests.reduce (
        (total, { warnings }) => {
            return warnings.length ? total.concat(['\n\n']).concat (warnings) : []
        }, []
    );
    const infos          = completeTests.reduce (
        (total, { infos }) => {
            return infos.length ? total.concat(['\n\n']).concat (infos) : []
        }, []
    );

    // Print interactive log output
    let logMessage = '';
    if (failed) {
        logMessage = 'FAIL'.red;
    } else if (hasWarnings) {
        logMessage = ('WARN: ' + (warnings.length ? warnings.join (' ') : '')).yellow;
    } else {
        logMessage = 'OK'.green;
    }

    numExchangesTested++;
    log.bright (('[' + percentsDone() + ']').dim, 'Tested', exchange.cyan, wsFlag, logMessage)

    // independenly of the success result, show infos
    // ( these infos will be shown as soon as each exchange test is finished, and will not wait 100% of all tests to be finished )
    const displayInfos = true; // temporarily disable from run-tests, because they are still outputed in console from individual langs
    if (displayInfos) {
        if (debugKeys['--info'] && infos.length) {
            // show info if enabled
            log.indent (1).bright ((
                '\n|-------------- INFO --------------|\n' +
                infos.join('\n') +
                '\n|--------------------------------------------|\n'
            ).blue);
        }
    }

    // Return collected data to main loop
    return {
        exchange,
        failed,
        hasWarnings,
        explain () {
            for (let { language, failed, output, warnings, infos } of completeTests) {
                const fullSkip = output.indexOf('[SKIPPED]') >= 0;
                if (fullSkip)
                    continue;
                // if failed, then show full output (includes warnings)
                if (failed) {
                    log.bright ('\nFAILED'.bgBrightRed.white, exchange.red,    '(' + language + ' ' + wsFlag + '):\n')
                    log.indent (1) ('\n', output)
                }
                // if not failed, but there are warnings, then show them
                else if (warnings.length) {
                    log.bright ('\nWARN'.yellow.inverse,     exchange.yellow, '(' + language + ' ' + wsFlag + '):\n')
                    log.indent (1) ('\n', warnings.join ('\n'))
                }
            }
        }
    }
}

//  ------------------------------------------------------------------------ //

function TaskPool (maxConcurrency) {

    const pending = []
        , queue   = []

    let numActive = 0

    return {

        pending,

        run (task) {

            if (numActive >= maxConcurrency) { // queue task

                return new Promise (resolve => queue.push (() => this.run (task).then (resolve)))

            } else { // execute task

                let p = task ().then (x => {
                    numActive--
                    return (queue.length && (numActive < maxConcurrency))
                                ? queue.shift () ().then (() => x)
                                : x
                })
                numActive++
                pending.push (p)
                return p
            }
        }
    }
}

//  ------------------------------------------------------------------------ //

async function testAllExchanges () {

    const taskPool = TaskPool (maxConcurrency)
    const results = []

    for (const exchange of exchanges) {
        taskPool.run (() => testExchange (exchange).then (x => results.push (x)))
    }

    await Promise.all (taskPool.pending)

    return results
}

//  ------------------------------------------------------------------------ //

(async function () {

    // show output like `Testing { exchanges: ["binance"], symbol: "all", debugKeys: { '--warnings': false, '--info': true }, langKeys: { '--ts': false, '--js': false, '--php': false, '--python': false, '--python-async': false, '--php-async': false }, exchangeSpecificFlags: { '--ws': true, '--sandbox': false, '--verbose': false, '--private': false, '--privateOnly': false }, maxConcurrency: 100 }`
    log.bright.magenta.noPretty (
        'Testing'.white, 
        Object.assign ({ exchanges, method, symbol, debugKeys, langKeys, exchangeSpecificFlags }, maxConcurrency >= Number.MAX_VALUE ? {} : { maxConcurrency })
    )

    const tested    = await testAllExchanges ()
        , warnings  = tested.filter (t => !t.failed && t.hasWarnings)
        , failed    = tested.filter (t =>  t.failed)
        , succeeded = tested.filter (t => !t.failed && !t.hasWarnings)

    log.newline ()

    warnings.forEach (t => t.explain ())
    failed.forEach (t => t.explain ())

    log.newline ()

    if (failed.length)   { log.noPretty.bright.red    ('FAIL'.bgBrightRed.white, failed.map (t => t.exchange)) }
    if (warnings.length) { log.noPretty.bright.yellow ('WARN'.inverse,           warnings.map (t => t.exchange)) }

    log.newline ()

    log.bright ('All done,', [failed.length   && (failed.length    + ' failed')   .red,
                             succeeded.length && (succeeded.length + ' succeeded').green,
                             warnings.length  && (warnings.length  + ' warnings') .yellow].filter (s => s).join (', '))

    if (failed.length) {

        await sleep (10) // to fight TravisCI log truncation issue, see https://github.com/travis-ci/travis-ci/issues/8189
        process.exit (1)

    } else {
        process.exit (0)
    }

}) ();

//  ------------------------------------------------------------------------ //


================================================
File: setup.cfg
================================================
[flake8]
ignore = E501
exclude =
    .ropeproject,
    .tox,
    .eggs,
    # No need to traverse our git directory
    .git,
    # There's no value in checking cache directories
    __pycache__,
    # Other special cases
    node_modules,
    .nyc_output,
    build,
    tmp,
    # No need to check the basecode
    ccxt.py


================================================
File: tests-manager.sh
================================================
#!/usr/bin/env bash

if [ "${BASH_VERSION:0:1}" -lt 4 ]; then
  echo "EPROGMISMATCH: bash version must be at least 4" >&2
  exit 75
fi

if [ $# -gt 0 ]; then
  echo "E2BIG: too many arguments" >&2
  exit 7
fi

cache_path="$TRAVIS_BUILD_DIR/.cache"
if ! [ -d "$cache_path" ]; then
  echo "ENOENT: .cache not found" >&2
  exit 2
fi

timestamps_path="$cache_path/timestamps"
urls_path="$cache_path/urls"

# slug is of the form owner_name/repo_name
# our file name is of the form owner_name:remote_branch_name
if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
  slug="$TRAVIS_REPO_SLUG"
  branch="$TRAVIS_BRANCH"
else
  slug="$TRAVIS_PULL_REQUEST_SLUG"
  branch="$TRAVIS_PULL_REQUEST_BRANCH"
fi
cache_file_name="$(cut -d '/' -f1 <<< "$slug"):$(tr '/' '|' <<< "$branch")"

mkdir "$timestamps_path" 2> /dev/null
mkdir "$urls_path" 2> /dev/null

cached_timestamp_file="$timestamps_path/$cache_file_name.txt"
cached_url_file="$urls_path/$cache_file_name.txt"

if ! [ -f "$cached_timestamp_file" ]; then
  # we initialise the cached timestamp to the current time
  # even before running a successful build so that pull requests
  date +%s > "$cached_timestamp_file"
fi
last_run=$(< "$cached_timestamp_file")
if [ "$last_run" -ne "$last_run" ] 2> /dev/null; then
  # check that last run is an integer
  last_run=0
fi

now=$(date +%s)
delta=$((now - last_run))
six_hours=$((60 * 60 * 6))
diff=$(git diff origin/master --name-only)

# begin debug
echo "$cached_timestamp_file"
echo "$cached_url_file"
# end debug

echo "last build url: $(cat "$cached_url_file" 2> /dev/null)"
echo "completed at: $(date -d "@$last_run" -u '+%H:%M on %B %d') - $((delta / 3600)) hours ago"

function run_tests {
  local rest_args=
  local ws_args=
  if [ $# -eq 2 ]; then
    rest_args="$1"
    ws_args="$2"
    if [ -z "$rest_args" ]; then
      : &
      local rest_pid=$!
    fi
    if [ -z "$ws_args" ]; then
      : &
      local ws_pid=$!
    fi
  fi
  if [ -z "$rest_pid" ]; then
    # shellcheck disable=SC2086
    node ./utils/test-commonjs.cjs && node run-tests --js --python-async --php-async --csharp --go --useProxy $rest_args &
    local rest_pid=$!
  fi
  if [ -z "$ws_pid" ]; then
    # shellcheck disable=SC2086
    node run-tests-ws --js --python-async --php-async --useProxy $ws_args &
    local ws_pid=$!
  fi
  wait $rest_pid && wait $ws_pid && echo "$TRAVIS_BUILD_WEB_URL" > "$cached_url_file"
}

if [ "$delta" -gt $six_hours ] || grep -q -E 'Client(Trait)?\.php$|Exchange\.php$|/test|/base|^build|static_dependencies|^run-tests|package(-lock)?\.json$' <<< "$diff"; then
  # shellcheck disable=SC2155
  run_tests && date +%s > "$cached_timestamp_file"
else
  run_tests "$(sed -E -n 's:^ts/src/([^/]+)\.ts$:\1:p' <<< "$diff" | xargs)" "$(sed -E -n 's:^ts/src/pro/([^/]+)\.ts$:\1:p' <<< "$diff" | xargs)"
fi


================================================
File: tsconfig.json
================================================
{
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig.json to read more about this file */

    /* Projects */
    // "incremental": true,                              /* Enable incremental compilation */
    // "composite": true,                                /* Enable constraints that allow a TypeScript project to be used with project references. */
    // "tsBuildInfoFile": "./",                          /* Specify the folder for .tsbuildinfo incremental compilation files. */
    // "disableSourceOfProjectReferenceRedirect": true,  /* Disable preferring source files instead of declaration files when referencing composite projects */
    // "disableSolutionSearching": true,                 /* Opt a project out of multi-project reference checking when editing. */
    // "disableReferencedProjectLoad": true,             /* Reduce the number of projects loaded automatically by TypeScript. */

    /* Language and Environment */
    "target": "ES2021",                                  /* Set the JavaScript language version for emitted JavaScript and include compatible library declarations. */
    "lib": [
      "ES2020.BigInt",
      "ES2021",
      "dom"
    ],                          /* Specify a set of bundled library declaration files that describe the target runtime environment. */
    // "jsx": "preserve",                                /* Specify what JSX code is generated. */
    // "experimentalDecorators": true,                   /* Enable experimental support for TC39 stage 2 draft decorators. */
    // "emitDecoratorMetadata": true,                    /* Emit design-type metadata for decorated declarations in source files. */
    // "jsxFactory": "",                                 /* Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h' */
    // "jsxFragmentFactory": "",                         /* Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g. 'React.Fragment' or 'Fragment'. */
    // "jsxImportSource": "",                            /* Specify module specifier used to import the JSX factory functions when using `jsx: react-jsx*`.` */
    // "reactNamespace": "",                             /* Specify the object invoked for `createElement`. This only applies when targeting `react` JSX emit. */
    // "noLib": true,                                    /* Disable including any library files, including the default lib.d.ts. */
    // "useDefineForClassFields": true,                  /* Emit ECMAScript-standard-compliant class fields. */

    /* Modules */
    "module": "ES2022",                                /* Specify what module code is generated. */
    // "rootDir": "./ts",                                  /* Specify the root folder within your source files. */
    "moduleResolution": "Node",                       /* Specify how TypeScript looks up a file from a given module specifier. */
    // "baseUrl": "./ts",                                  /* Specify the base directory to resolve non-relative module names. */
    // "paths": {},                                      /* Specify a set of entries that re-map imports to additional lookup locations. */
    // "rootDirs": [],                                   /* Allow multiple folders to be treated as one when resolving modules. */
    // "typeRoots": [],                                  /* Specify multiple folders that act like `./node_modules/@types`. */
    // "types": [],                                      /* Specify type package names to be included without being referenced in a source file. */
    // "allowUmdGlobalAccess": true,                     /* Allow accessing UMD globals from modules. */
    // "resolveJsonModule": true,                        /* Enable importing .json files */
    // "noResolve": true,                                /* Disallow `import`s, `require`s or `<reference>`s from expanding the number of files TypeScript should add to a project. */

    /* JavaScript Support */
    "allowJs": true,                                  /* Allow JavaScript files to be a part of your program. Use the `checkJS` option to get errors from these files. */
    "checkJs": false,                                  /* Enable error reporting in type-checked JavaScript files. */
    // "maxNodeModuleJsDepth": 1,                        /* Specify the maximum folder depth used for checking JavaScript files from `node_modules`. Only applicable with `allowJs`. */
    /* Emit */
    "declaration": true,                              /* Generate .d.ts files from TypeScript and JavaScript files in your project. */
    // "declarationMap": true,                           /* Create sourcemaps for d.ts files. */
    // "emitDeclarationOnly": true,                      /* Only output d.ts files and not JavaScript files. */
    // "sourceMap": true,                                /* Create source map files for emitted JavaScript files. */
    // "outFile": "./",                                  /* Specify a file that bundles all outputs into one JavaScript file. If `declaration` is true, also designates a file that bundles all .d.ts output. */
    "outDir": "./js",                                   /* Specify an output folder for all emitted files. */
    "removeComments": false,                           /* Disable emitting comments. */
    // "noEmit": true,                                   /* Disable emitting files from a compilation. */
    // "importHelpers": true,                            /* Allow importing helper functions from tslib once per project, instead of including them per-file. */
    // "importsNotUsedAsValues": "remove",               /* Specify emit/checking behavior for imports that are only used for types */
    // "downlevelIteration": true,                       /* Emit more compliant, but verbose and less performant JavaScript for iteration. */
    // "sourceRoot": "",                                 /* Specify the root path for debuggers to find the reference source code. */
    // "mapRoot": "",                                    /* Specify the location where debugger should locate map files instead of generated locations. */
    // "inlineSourceMap": true,                          /* Include sourcemap files inside the emitted JavaScript. */
    // "inlineSources": true,                            /* Include source code in the sourcemaps inside the emitted JavaScript. */
    // "emitBOM": true,                                  /* Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files. */
    // "newLine": "crlf",                                /* Set the newline character for emitting files. */
    // "stripInternal": true,                            /* Disable emitting declarations that have `@internal` in their JSDoc comments. */
    // "noEmitHelpers": true,                            /* Disable generating custom helper functions like `__extends` in compiled output. */
    // "noEmitOnError": true,                            /* Disable emitting files if any type checking errors are reported. */
    // "preserveConstEnums": true,                       /* Disable erasing `const enum` declarations in generated code. */
    // "declarationDir": "./",                           /* Specify the output directory for generated declaration files. */
    // "preserveValueImports": true,                     /* Preserve unused imported values in the JavaScript output that would otherwise be removed. */

    /* Interop Constraints */
    "isolatedModules": false,                          /* Ensure that each file can be safely transpiled without relying on other imports. */
    // "allowSyntheticDefaultImports": true,             /* Allow 'import x from y' when a module doesn't have a default export. */
    "esModuleInterop": true,                             /* Emit additional JavaScript to ease support for importing CommonJS modules. This enables `allowSyntheticDefaultImports` for type compatibility. */
    // "preserveSymlinks": true,                         /* Disable resolving symlinks to their realpath. This correlates to the same flag in node. */
    "forceConsistentCasingInFileNames": true,            /* Ensure that casing is correct in imports. */

    /* Type Checking */
    "strict": true,                                      /* Enable all strict type-checking options. */
    "noImplicitAny": false,                            /* Enable error reporting for expressions and declarations with an implied `any` type.. */
    // "strictNullChecks": true,                         /* When type checking, take into account `null` and `undefined`. */
    // "strictFunctionTypes": true,                      /* When assigning functions, check to ensure parameters and the return values are subtype-compatible. */
    // "strictBindCallApply": true,                      /* Check that the arguments for `bind`, `call`, and `apply` methods match the original function. */
    // "strictPropertyInitialization": true,             /* Check for class properties that are declared but not set in the constructor. */
    // "noImplicitThis": true,                           /* Enable error reporting when `this` is given the type `any`. */
    // "useUnknownInCatchVariables": true,               /* Type catch clause variables as 'unknown' instead of 'any'. */
    // "alwaysStrict": true,                             /* Ensure 'use strict' is always emitted. */
    // "noUnusedLocals": true,                           /* Enable error reporting when a local variables aren't read. */
    // "noUnusedParameters": true,                       /* Raise an error when a function parameter isn't read */
    // "exactOptionalPropertyTypes": true,               /* Interpret optional property types as written, rather than adding 'undefined'. */
    // "noImplicitReturns": true,                        /* Enable error reporting for codepaths that do not explicitly return in a function. */
    // "noFallthroughCasesInSwitch": true,               /* Enable error reporting for fallthrough cases in switch statements. */
    // "noUncheckedIndexedAccess": false,                 /* Include 'undefined' in index signature results */
    // "noImplicitOverride": true,                       /* Ensure overriding members in derived classes are marked with an override modifier. */
    // "noPropertyAccessFromIndexSignature": true,       /* Enforces using indexed accessors for keys declared using an indexed type */
    // "allowUnusedLabels": true,                        /* Disable error reporting for unused labels. */
    // "allowUnreachableCode": true,                     /* Disable error reporting for unreachable code. */

    /* Completeness */
    // "skipDefaultLibCheck": true,                      /* Skip type checking .d.ts files that are included with TypeScript. */
    "skipLibCheck": true,                                 /* Skip type checking all .d.ts files. */
    "strictNullChecks":false
  },
  "include": [
    "ts/**/*"
  ],
  "exclude": [
    "node_modules",
    "./ts/src/static_dependencies/**/*.cjs"
  ]
}


================================================
File: webpack.config.js
================================================
import path from 'path';
import url from 'url';
import TerserPlugin from "terser-webpack-plugin";

const cwd = url.fileURLToPath (import.meta.url);
const outputDirectory = path.normalize (path.join (path.dirname (cwd), 'dist'))

export default {
  entry : './ts/ccxt.ts',
  output: {
    path: outputDirectory,
    filename: 'ccxt.browser.js',
    library: {
      type: 'self', // we are targeting the browser (including webworkers)
      name: 'ccxt',
    },
    chunkFormat: 'array-push',
    chunkLoading: 'jsonp',
  },
  cache: {
    type: 'filesystem',
  },
  module: {
    rules: [{
      test: /\.ts$/,
      use: 'ts-loader',
      exclude: [ /node_modules/ ],
      sideEffects: false,
    }],
  },
  resolve: {
    extensions: [ '.ts' ],
    // this line is needed because we use import xxx.js in ccxt
    extensionAlias: {
     '.js': [ '.js', '.ts' ],
    },
  },
  mode: 'production',
  target: 'web',
  optimization: {
    minimize: false,
    minimizer: [new TerserPlugin ({ extractComments: false })],
    usedExports: true, // these two lines line turns on tree shaking
    concatenateModules: false,
  },
}


================================================
File: .dockerignore
================================================
.git
.dockerignore
Dockerfile
node_modules
vendor
*.swp
*.pyc


================================================
File: .eslintignore
================================================
build/*


================================================
File: .npmignore
================================================
# Initally ignore all files
*

# Files to include
!package.json
!package-lock.json
!postinstall.js
!LICENSE.txt
!README.md

# Folders to include
!js/**/*
!dist/**/*

# Ignore tests
js/src/test/**/*
js/src/pro/test/**/*

#Ignore browser bundle
dist/ccxt.browser.js
!dist/ccxt.browser.min.js
!dist/ccxt.browser.min.js.LICENSE.txt


================================================
File: .travis.yml
================================================
# language: python
# dist: jammy
# python:
# - 3.8.3
# git:
#   depth: 2
# addons:
#   artifacts:
#     debug: true
# cache:
#   directories:
#   - ".cache"
# before_install:
# - |
#     if [[ "$TRAVIS_BRANCH" == "master" ]]; then
#       if [[ "$TRAVIS_COMMIT_MESSAGE" == "[Automated Changes]"* ]]; then
#         echo "Skipping build for automated commit: $TRAVIS_COMMIT_MESSAGE"
#         exit 0
#       fi
#       if [[ "$TRAVIS_COMMIT_MESSAGE" == "Merge branch 'master' of "* ]]; then
#         echo "Skipping build for master merge commit: $TRAVIS_COMMIT_MESSAGE"
#         exit 0
#       fi
#     fi
# # - set -e
# # - ". $HOME/.nvm/nvm.sh"
# # - nvm ls
# # - nvm ls-remote
# # - nvm install v18.17.0
# # - rm -rf node_modules
# # # common commands
# # - npm ci --include=dev
# # - git checkout package.json package-lock.json
# # - git config pull.rebase false
# # - git fetch --depth=1 --no-tags --verbose --progress
# # - pip install tox cryptography requests ruff # common packages
# # - pip install twine # used to publish python package
# # - pip install pyopenssl aiohttp # used to run real-time tests
# # - pip install typing-extensions # required by python <3.11
# # - pip install psutil # used for python ws base test
# # - php -i | grep php.ini
# # - composer install
# # - sudo apt update
# # - sudo apt install apt-transport-https -y
# # - sudo apt update -y
# # - sudo apt-get install -y dotnet-sdk-7.0
# # - sudo apt-get install -y dotnet-runtime-7.0
# # - dotnet --version
# # - dotnet --info
# # - wget https://go.dev/dl/go1.21.6.linux-amd64.tar.gz
# # - sudo tar -xvf go1.21.6.linux-amd64.tar.gz -C /usr/local
# # - echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile
# # - go version
# # - type -p curl >/dev/null || ( apt update &&  apt install curl -y)
# # - curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update && sudo apt install gh -y

# script:
# # - ./build.sh 2>&1
# # - git checkout master composer.json
# # - if [ "$TRAVIS_PULL_REQUEST" = "false" ] && [ "$TRAVIS_BRANCH" = "master" ]; then
# #     export SHOULD_DEPLOY=false;
# #     DEPLOY_OUTPUT=$(env DEPLOY_CACHE=.cache/deploy SECONDS_BEFORE_NEXT_DEPLOY=43200 TRAVIS_COMMIT_MESSAGE="${TRAVIS_COMMIT_MESSAGE}" ./build/deploy.sh) && SHOULD_DEPLOY=true;
# #     echo "----------------";
# #     echo "${DEPLOY_OUTPUT}";
# #     echo "${SHOULD_DEPLOY}";
# #     echo "----------------";
# #     if $SHOULD_DEPLOY; then
# #       echo "Publishing";
# #       npm config set git-tag-version=false && NPM_VERSION=$(npm version patch);
# #       npm run vss && npm run copy-python-files && npm run buildCSRelease;
# #       env COMMIT_MESSAGE=${NPM_VERSION:1} GITHUB_TOKEN=${GITHUB_TOKEN} SHOULD_TAG=${SHOULD_DEPLOY} ./build/push.sh;
# #       ./cs/deploy.sh;
# #       cd python && env PYPI_TOKEN=${PYPI_TOKEN} ./deploy.sh && cd ..;
# #     else
# #       echo "Not publishing";
# #       env COMMIT_MESSAGE="${TRAVIS_COMMIT_MESSAGE}" GITHUB_TOKEN=${GITHUB_TOKEN} GH_TOKEN=${GITHUB_TOKEN} SHOULD_TAG=${SHOULD_DEPLOY} ./build/push.sh;
# #     fi;
# #   fi
# after_failure:
# - sleep 10
# before_deploy:
# - echo $SHOULD_DEPLOY
# deploy:
# - provider: npm
#   email: igor.kroitor@gmail.com
#   api_key:
#     secure: euGp3OIlxbY+ZqgJYOAE1MH4EyCVIRLxMksHcj+w/V6MEkRchLIUDE68kLdK5ZUFGHnoFQtR1N65i428gvcjy8P/0K0p9maVpZaHuk0Q2GrnIAAe0D6jZu2s2D0JPhWCZ5U4Aiek5ExhTblEYWTwOtpG/JwAa+2/IT+2DvtNf37HBM0tEvI3FLRexTv74vMDH172681UFHz2h0dvfgOzBwCiydsp6eihnV90AetsYT4Y9VpZDjAdmATO1ydLw8SnH2skWssmH8snyDDVOPkdu6mRBHZB6ckSZzyQLiIbn4dlzAt6Zi1/NjSJg4z/+vIK8o8SOHPu3AkCab+E6kBeuCBnphquIa/i3bToxJSa1AScisg+5rQZCsY/L7ey8El/nOvVn7B6xATk7w4Cm/dy5gTyriNqgFoJvDLhlntfPp+7w9GGc7Hi6UL9RWw0CCW9c2I1cyDmNpSv95gspMJAI847ykaHgXl01Cxo2yWGqwxpCR/suqdTySvo3NgqFQrM2aRkPQT+yQlL2hrrqX2l2w7gU+2y9W89WB/75x674RR3fpSID6HGrt52frZDk1mgi6ggHv0ta+hOHQCIhLM7tB/pR9ehF4RGcVjRTEBa0CG2XeXDWDFDjLEzZPmvf6vCL+PDMk91sR6YB+djsaPEwLV6pjWngYSrNdYVe1djdl8=
#   on:
#     condition: $SHOULD_DEPLOY = true
# after_deploy:
# - cat ~/.npm/_logs/*-debug.log
# env:
#   global:
#   - GO111MODULE=on
#   # PYPI_TOKEN
#   - secure: QCQa8tn40loCqSx9tR7PFAa7h5Gucl9IaEARiskiPF3zlLoZTst6ThnFl1rQDKx2jIJsN1z8Vwd12I4kYGED+Tgd345kE+J/n2hVEpTwSB+oOUWlwgkTQbCQB0XxPJRPila9lt3Ogpbvrp//L7IkFM06gu+N+qwQEOjn7dkLrVAkg5vl9nouuzqHadaQ1oOMG/v3DgPq5NHaCEWK0285Oqs8dqecVRSFGAtRPTDHzO/nv4stsbnmEWO1pu/SYXyxum1CYv9glfFaRNWoQ9EWjl8ogCzBsH3lkFeNhwLOcSyMFmTpXH1soXcLzJTWoUgfx9hiiC8IqOxx4nGurOK6OyY9QO8aVwyRdYlbpdLFuEiGuadfI6Rbz41TewZ+r3OmFn4gy5oRIM0fE+2Osj3btmsdZYktXdErqhRm18bV/oO/IOteKEXdbC7+PJ5obnpbBKKfcSNOAF8F/en+qouAywghq8UBJ9zHtWSsDXOUeCdvXLGKA01pbdaDpmtHBU9u5iX+KnSbBP+iAb7+i/uymxFTJbseYllPa1IFUf4wNf6AFlfgLnZT064KF1oiIGnvpczqD+UV4fDIukKaBaC0gK2nUQUiSNPs1kFJbs7QiQO5I07RgpAACigDWlp6tKLSUoA4wUXIG1APF5Eh001FAQ01lCjsxhMh3OmtgEIaxkI=
#   # new new GITHUB_TOKEN
#   - secure: koZWVx9bBt1QZ43OUGH6DE0tQseqYxL+LGubjSndpCQfx1OLbUOjuxa4ka8S2mVTX61IQ+Pl7VambRahmXrSp/+cIYf2l/7BfE/vmaAxs+mM7+YbvAmIbmp3ohw2Ib+SnkCPUsQWBPdOedbuDXUkTvd6T22EwftFOBYrcBxmABpvNNRwaaK7fnNJQMnJo3yiaM0sCOjcyBJOzGhO2+aW7T7LaSa0CdmD/yBIAfqxmfFCf8gOTnRep8iCay/fMAhdDD/zzUNBJoKupMWHkwSik8BeKA/Ny4OO0zvR1ZF+t1PD4qXnK17bKf3kS+JKPCK8q7wGwJWTJFezKRG0JbIZRMxi4Dsawu+QvHs4+ekSCWLuPD0bnn6TMue+bOWaCnLVQAmzTbiykWF2tuHN0Zj/c8DJJKjA62EKPKJh/69OdEV6VIwy5m2o+ij6MWK0yaAcNNOfDRiM9sAJL8eUcncFVOOzyEkFTRuke/gerJEUknH/25tYCXbmRYRolSoFvSW8PaB2Q8RXizL9LtnyRcR02wxs12jpCTAJ9rpR0XIb3D4W8BWkWgJvHp9JZOAlzESz4moROv3C6EvPFX4uZAAx/RgdFicLB7tgP9EC6RAPs1yPJwjNcv7EPLsl5OPBsFkOa8Qq5guNbeX6XuBWsIRJL+XJBODw29kISxiWDh49Dlg=
#   # NUGGET_TOKEN
#   - secure: Mnryg2kNRpl7qFGahaKeVkGQ0GeUQxcJAiS+IP1AnMOfzNomhd0ykTaeCWxxTjAPOLagOL5XyFwOj7k3VJ8wMvFozpUMZKx5NkF6cCu3M7y4sW4dMe/3Wjq0iskPv4t6wgtsAGNpzv+j6RF0aBy72xDcnuK437utVU5uukd3V6BzRxs1iQezLM4neIU1eG7SCfPjZbvJj0UdbUDwYhU80mHu5cscuEhZKSqi6aMY3jBZm6L8Pe17vRzHPBmMcNgoXOHEAfw8K9WgiMqMmG/caAllkJLNLU6pDPWQfe7u7csBpK8OPZRC+HejoUoLZN6IWizLrp+DodjskUqiTJLllT1UFBurtl4LzjfiSHd5a7yct07QKCT6hE6J0xLUCPEcPAUlbeWJKst3+WYepj/EB0jahGKi6npnSQK+o4I4yVSKp7Dmgbc+wQN0nF9alx/fT+Z/ENeoXhPdzyPOMaKq1ftyQPQTGAhCMScgmgqTKyVQdsF8x+BuZofK/WOBHLhJNEPxyQJ0j0v8JbYv0/JhvU1tRUHRtcb2rcQ/waxupUeicHhSbI0gQXrrQurznLFjLXK5nrxIE9xDMon4IkBIjAFeVf2XsGvJitSfIYvBAoOCFN/ldP398dkAw/3yUqVt62PXrVjoyWIaSfjBeB58wDV46lMK7qfmlaWygjtZbPc=


================================================
File: cs/ccxt.sln
================================================
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.0.31903.59
MinimumVisualStudioVersion = 10.0.40219.1
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "ccxt", "ccxt\ccxt.csproj", "{DE6A2140-A0DD-4582-82F1-FB12E16A48E3}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "tests", "tests\tests.csproj", "{077D9860-062D-46AB-9F24-60789A2B3794}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "cli", "cli\cli.csproj", "{D04F0D67-4A3A-4B5F-80C2-45555F83610C}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{DE6A2140-A0DD-4582-82F1-FB12E16A48E3}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{DE6A2140-A0DD-4582-82F1-FB12E16A48E3}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{DE6A2140-A0DD-4582-82F1-FB12E16A48E3}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{DE6A2140-A0DD-4582-82F1-FB12E16A48E3}.Release|Any CPU.Build.0 = Release|Any CPU
		{077D9860-062D-46AB-9F24-60789A2B3794}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{077D9860-062D-46AB-9F24-60789A2B3794}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{077D9860-062D-46AB-9F24-60789A2B3794}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{077D9860-062D-46AB-9F24-60789A2B3794}.Release|Any CPU.Build.0 = Release|Any CPU
		{D04F0D67-4A3A-4B5F-80C2-45555F83610C}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{D04F0D67-4A3A-4B5F-80C2-45555F83610C}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{D04F0D67-4A3A-4B5F-80C2-45555F83610C}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{D04F0D67-4A3A-4B5F-80C2-45555F83610C}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
EndGlobal


================================================
File: cs/deploy.sh
================================================
version=$(cat package.json | jq -r '.version')

bin_folder="./cs/ccxt/bin/Release/"

bin_file="ccxt.${version}.nupkg"

bin_path="${bin_folder}${bin_file}"

echo "Will publish nuget package: ${bin_path}"

dotnet nuget push ${bin_path} -k ${NUGGET_TOKEN} -s https://api.nuget.org/v3/index.json

================================================
File: cs/.editorconfig
================================================
root = true

# All files
[*]
indent_style = space

# Xml files
[*.xml]
indent_size = 2

# C# files
[*.cs]

#### Core EditorConfig Options ####

# Indentation and spacing
indent_size = 4
tab_width = 4

# New line preferences
end_of_line = crlf
insert_final_newline = false

#### .NET Coding Conventions ####
[*.{cs,vb}]

# Organize usings
dotnet_separate_import_directive_groups = true
dotnet_sort_system_directives_first = true
file_header_template = unset

# this. and Me. preferences
dotnet_style_qualification_for_event = false:silent
dotnet_style_qualification_for_field = false:silent
dotnet_style_qualification_for_method = false:silent
dotnet_style_qualification_for_property = false:silent

# Language keywords vs BCL types preferences
dotnet_style_predefined_type_for_locals_parameters_members = true:silent
dotnet_style_predefined_type_for_member_access = true:silent

# Parentheses preferences
dotnet_style_parentheses_in_arithmetic_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_other_binary_operators = always_for_clarity:silent
dotnet_style_parentheses_in_other_operators = never_if_unnecessary:silent
dotnet_style_parentheses_in_relational_binary_operators = always_for_clarity:silent

# Modifier preferences
dotnet_style_require_accessibility_modifiers = for_non_interface_members:silent

# Expression-level preferences
dotnet_style_coalesce_expression = true:suggestion
dotnet_style_collection_initializer = true:suggestion
dotnet_style_explicit_tuple_names = true:suggestion
dotnet_style_null_propagation = true:suggestion
dotnet_style_object_initializer = true:suggestion
dotnet_style_operator_placement_when_wrapping = beginning_of_line
dotnet_style_prefer_auto_properties = true:suggestion
dotnet_style_prefer_compound_assignment = true:suggestion
dotnet_style_prefer_conditional_expression_over_assignment = true:suggestion
dotnet_style_prefer_conditional_expression_over_return = true:suggestion
dotnet_style_prefer_inferred_anonymous_type_member_names = true:suggestion
dotnet_style_prefer_inferred_tuple_names = true:suggestion
dotnet_style_prefer_is_null_check_over_reference_equality_method = true:suggestion
dotnet_style_prefer_simplified_boolean_expressions = true:suggestion
dotnet_style_prefer_simplified_interpolation = true:suggestion

# Field preferences
dotnet_style_readonly_field = true:warning

# Parameter preferences
dotnet_code_quality_unused_parameters = all:suggestion

# Suppression preferences
dotnet_remove_unnecessary_suppression_exclusions = none

#### C# Coding Conventions ####
[*.cs]

# var preferences
csharp_style_var_elsewhere = false:silent
csharp_style_var_for_built_in_types = false:silent
csharp_style_var_when_type_is_apparent = false:silent

# Expression-bodied members
csharp_style_expression_bodied_accessors = true:silent
csharp_style_expression_bodied_constructors = false:silent
csharp_style_expression_bodied_indexers = true:silent
csharp_style_expression_bodied_lambdas = true:suggestion
csharp_style_expression_bodied_local_functions = false:silent
csharp_style_expression_bodied_methods = false:silent
csharp_style_expression_bodied_operators = false:silent
csharp_style_expression_bodied_properties = true:silent

# Pattern matching preferences
csharp_style_pattern_matching_over_as_with_null_check = true:suggestion
csharp_style_pattern_matching_over_is_with_cast_check = true:suggestion
csharp_style_prefer_not_pattern = true:suggestion
csharp_style_prefer_pattern_matching = true:silent
csharp_style_prefer_switch_expression = true:suggestion

# Null-checking preferences
csharp_style_conditional_delegate_call = true:suggestion

# Modifier preferences
csharp_prefer_static_local_function = true:warning
csharp_preferred_modifier_order = public,private,protected,internal,static,extern,new,virtual,abstract,sealed,override,readonly,unsafe,volatile,async:silent

# Code-block preferences
csharp_prefer_braces = true:silent
csharp_prefer_simple_using_statement = true:suggestion

# Expression-level preferences
csharp_prefer_simple_default_expression = true:suggestion
csharp_style_deconstructed_variable_declaration = true:suggestion
csharp_style_inlined_variable_declaration = true:suggestion
csharp_style_pattern_local_over_anonymous_function = true:suggestion
csharp_style_prefer_index_operator = true:suggestion
csharp_style_prefer_range_operator = true:suggestion
csharp_style_throw_expression = true:suggestion
csharp_style_unused_value_assignment_preference = discard_variable:suggestion
csharp_style_unused_value_expression_statement_preference = discard_variable:silent

# 'using' directive preferences
csharp_using_directive_placement = outside_namespace:silent

#### C# Formatting Rules ####

# New line preferences
csharp_new_line_before_catch = true
csharp_new_line_before_else = true
csharp_new_line_before_finally = true
csharp_new_line_before_members_in_anonymous_types = true
csharp_new_line_before_members_in_object_initializers = true
csharp_new_line_before_open_brace = all
csharp_new_line_between_query_expression_clauses = true

# Indentation preferences
csharp_indent_block_contents = true
csharp_indent_braces = false
csharp_indent_case_contents = true
csharp_indent_case_contents_when_block = true
csharp_indent_labels = one_less_than_current
csharp_indent_switch_labels = true

# Space preferences
csharp_space_after_cast = false
csharp_space_after_colon_in_inheritance_clause = true
csharp_space_after_comma = true
csharp_space_after_dot = false
csharp_space_after_keywords_in_control_flow_statements = true
csharp_space_after_semicolon_in_for_statement = true
csharp_space_around_binary_operators = before_and_after
csharp_space_around_declaration_statements = false
csharp_space_before_colon_in_inheritance_clause = true
csharp_space_before_comma = false
csharp_space_before_dot = false
csharp_space_before_open_square_brackets = false
csharp_space_before_semicolon_in_for_statement = false
csharp_space_between_empty_square_brackets = false
csharp_space_between_method_call_empty_parameter_list_parentheses = false
csharp_space_between_method_call_name_and_opening_parenthesis = false
csharp_space_between_method_call_parameter_list_parentheses = false
csharp_space_between_method_declaration_empty_parameter_list_parentheses = false
csharp_space_between_method_declaration_name_and_open_parenthesis = false
csharp_space_between_method_declaration_parameter_list_parentheses = false
csharp_space_between_parentheses = false
csharp_space_between_square_brackets = false

# Wrapping preferences
csharp_preserve_single_line_blocks = true
csharp_preserve_single_line_statements = true

#### Naming styles ####
[*.{cs,vb}]

# Naming rules

dotnet_naming_rule.types_and_namespaces_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.types_and_namespaces_should_be_pascalcase.symbols = types_and_namespaces
dotnet_naming_rule.types_and_namespaces_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.interfaces_should_be_ipascalcase.severity = suggestion
dotnet_naming_rule.interfaces_should_be_ipascalcase.symbols = interfaces
dotnet_naming_rule.interfaces_should_be_ipascalcase.style = ipascalcase

dotnet_naming_rule.type_parameters_should_be_tpascalcase.severity = suggestion
dotnet_naming_rule.type_parameters_should_be_tpascalcase.symbols = type_parameters
dotnet_naming_rule.type_parameters_should_be_tpascalcase.style = tpascalcase

dotnet_naming_rule.methods_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.methods_should_be_pascalcase.symbols = methods
dotnet_naming_rule.methods_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.properties_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.properties_should_be_pascalcase.symbols = properties
dotnet_naming_rule.properties_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.events_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.events_should_be_pascalcase.symbols = events
dotnet_naming_rule.events_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.local_variables_should_be_camelcase.severity = suggestion
dotnet_naming_rule.local_variables_should_be_camelcase.symbols = local_variables
dotnet_naming_rule.local_variables_should_be_camelcase.style = camelcase

dotnet_naming_rule.local_constants_should_be_camelcase.severity = suggestion
dotnet_naming_rule.local_constants_should_be_camelcase.symbols = local_constants
dotnet_naming_rule.local_constants_should_be_camelcase.style = camelcase

dotnet_naming_rule.parameters_should_be_camelcase.severity = suggestion
dotnet_naming_rule.parameters_should_be_camelcase.symbols = parameters
dotnet_naming_rule.parameters_should_be_camelcase.style = camelcase

dotnet_naming_rule.public_fields_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.public_fields_should_be_pascalcase.symbols = public_fields
dotnet_naming_rule.public_fields_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.private_fields_should_be__camelcase.severity = suggestion
dotnet_naming_rule.private_fields_should_be__camelcase.symbols = private_fields
dotnet_naming_rule.private_fields_should_be__camelcase.style = _camelcase

dotnet_naming_rule.private_static_fields_should_be_s_camelcase.severity = suggestion
dotnet_naming_rule.private_static_fields_should_be_s_camelcase.symbols = private_static_fields
dotnet_naming_rule.private_static_fields_should_be_s_camelcase.style = s_camelcase

dotnet_naming_rule.public_constant_fields_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.public_constant_fields_should_be_pascalcase.symbols = public_constant_fields
dotnet_naming_rule.public_constant_fields_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.private_constant_fields_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.private_constant_fields_should_be_pascalcase.symbols = private_constant_fields
dotnet_naming_rule.private_constant_fields_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.public_static_readonly_fields_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.public_static_readonly_fields_should_be_pascalcase.symbols = public_static_readonly_fields
dotnet_naming_rule.public_static_readonly_fields_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.private_static_readonly_fields_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.private_static_readonly_fields_should_be_pascalcase.symbols = private_static_readonly_fields
dotnet_naming_rule.private_static_readonly_fields_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.enums_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.enums_should_be_pascalcase.symbols = enums
dotnet_naming_rule.enums_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.local_functions_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.local_functions_should_be_pascalcase.symbols = local_functions
dotnet_naming_rule.local_functions_should_be_pascalcase.style = pascalcase

dotnet_naming_rule.non_field_members_should_be_pascalcase.severity = suggestion
dotnet_naming_rule.non_field_members_should_be_pascalcase.symbols = non_field_members
dotnet_naming_rule.non_field_members_should_be_pascalcase.style = pascalcase

# Symbol specifications

dotnet_naming_symbols.interfaces.applicable_kinds = interface
dotnet_naming_symbols.interfaces.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.interfaces.required_modifiers = 

dotnet_naming_symbols.enums.applicable_kinds = enum
dotnet_naming_symbols.enums.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.enums.required_modifiers = 

dotnet_naming_symbols.events.applicable_kinds = event
dotnet_naming_symbols.events.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.events.required_modifiers = 

dotnet_naming_symbols.methods.applicable_kinds = method
dotnet_naming_symbols.methods.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.methods.required_modifiers = 

dotnet_naming_symbols.properties.applicable_kinds = property
dotnet_naming_symbols.properties.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.properties.required_modifiers = 

dotnet_naming_symbols.public_fields.applicable_kinds = field
dotnet_naming_symbols.public_fields.applicable_accessibilities = public, internal
dotnet_naming_symbols.public_fields.required_modifiers = 

dotnet_naming_symbols.private_fields.applicable_kinds = field
dotnet_naming_symbols.private_fields.applicable_accessibilities = private, protected, protected_internal, private_protected
dotnet_naming_symbols.private_fields.required_modifiers = 

dotnet_naming_symbols.private_static_fields.applicable_kinds = field
dotnet_naming_symbols.private_static_fields.applicable_accessibilities = private, protected, protected_internal, private_protected
dotnet_naming_symbols.private_static_fields.required_modifiers = static

dotnet_naming_symbols.types_and_namespaces.applicable_kinds = namespace, class, struct, interface, enum
dotnet_naming_symbols.types_and_namespaces.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.types_and_namespaces.required_modifiers = 

dotnet_naming_symbols.non_field_members.applicable_kinds = property, event, method
dotnet_naming_symbols.non_field_members.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected
dotnet_naming_symbols.non_field_members.required_modifiers = 

dotnet_naming_symbols.type_parameters.applicable_kinds = namespace
dotnet_naming_symbols.type_parameters.applicable_accessibilities = *
dotnet_naming_symbols.type_parameters.required_modifiers = 

dotnet_naming_symbols.private_constant_fields.applicable_kinds = field
dotnet_naming_symbols.private_constant_fields.applicable_accessibilities = private, protected, protected_internal, private_protected
dotnet_naming_symbols.private_constant_fields.required_modifiers = const

dotnet_naming_symbols.local_variables.applicable_kinds = local
dotnet_naming_symbols.local_variables.applicable_accessibilities = local
dotnet_naming_symbols.local_variables.required_modifiers = 

dotnet_naming_symbols.local_constants.applicable_kinds = local
dotnet_naming_symbols.local_constants.applicable_accessibilities = local
dotnet_naming_symbols.local_constants.required_modifiers = const

dotnet_naming_symbols.parameters.applicable_kinds = parameter
dotnet_naming_symbols.parameters.applicable_accessibilities = *
dotnet_naming_symbols.parameters.required_modifiers = 

dotnet_naming_symbols.public_constant_fields.applicable_kinds = field
dotnet_naming_symbols.public_constant_fields.applicable_accessibilities = public, internal
dotnet_naming_symbols.public_constant_fields.required_modifiers = const

dotnet_naming_symbols.public_static_readonly_fields.applicable_kinds = field
dotnet_naming_symbols.public_static_readonly_fields.applicable_accessibilities = public, internal
dotnet_naming_symbols.public_static_readonly_fields.required_modifiers = readonly, static

dotnet_naming_symbols.private_static_readonly_fields.applicable_kinds = field
dotnet_naming_symbols.private_static_readonly_fields.applicable_accessibilities = private, protected, protected_internal, private_protected
dotnet_naming_symbols.private_static_readonly_fields.required_modifiers = readonly, static

dotnet_naming_symbols.local_functions.applicable_kinds = local_function
dotnet_naming_symbols.local_functions.applicable_accessibilities = *
dotnet_naming_symbols.local_functions.required_modifiers = 

# Naming styles

dotnet_naming_style.pascalcase.required_prefix = 
dotnet_naming_style.pascalcase.required_suffix = 
dotnet_naming_style.pascalcase.word_separator = 
dotnet_naming_style.pascalcase.capitalization = pascal_case

dotnet_naming_style.ipascalcase.required_prefix = I
dotnet_naming_style.ipascalcase.required_suffix = 
dotnet_naming_style.ipascalcase.word_separator = 
dotnet_naming_style.ipascalcase.capitalization = pascal_case

dotnet_naming_style.tpascalcase.required_prefix = T
dotnet_naming_style.tpascalcase.required_suffix = 
dotnet_naming_style.tpascalcase.word_separator = 
dotnet_naming_style.tpascalcase.capitalization = pascal_case

dotnet_naming_style._camelcase.required_prefix = _
dotnet_naming_style._camelcase.required_suffix = 
dotnet_naming_style._camelcase.word_separator = 
dotnet_naming_style._camelcase.capitalization = camel_case

dotnet_naming_style.camelcase.required_prefix = 
dotnet_naming_style.camelcase.required_suffix = 
dotnet_naming_style.camelcase.word_separator = 
dotnet_naming_style.camelcase.capitalization = camel_case

dotnet_naming_style.s_camelcase.required_prefix = s_
dotnet_naming_style.s_camelcase.required_suffix = 
dotnet_naming_style.s_camelcase.word_separator = 
dotnet_naming_style.s_camelcase.capitalization = camel_case


[*.{cs,vb}]

# IDE0002: Name can be simplified
dotnet_diagnostic.IDE0002.severity = suggestion

# IDE0005: Remove unnecessary imports
dotnet_diagnostic.IDE0005.severity = suggestion

================================================
File: cs/.gitignore
================================================
.vs/
obj/
bin/

================================================
File: cs/ccxt/ccxt.csproj
================================================
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFrameworks>netstandard2.1;netstandard2.0</TargetFrameworks>
    <LangVersion>10.0</LangVersion>
    <OutputType>Library</OutputType>
    <RootNamespace>ccxt</RootNamespace>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
  <PropertyGroup>
    <PackageId>ccxt</PackageId>
    <Authors>Carlos, Kroitor, Carlo</Authors>
    <PackageVersion>4.4.61</PackageVersion>
    <AssemblyVersion>4.4.61</AssemblyVersion>
    <FileVersion>4.4.61</FileVersion>
    <PackageReadmeFile>README.md</PackageReadmeFile>
    <Description>Cryptocurrency trading API with support for more than 100 bitcoin/altcoin exchanges</Description>
    <PackageRequireLicenseAcceptance>false</PackageRequireLicenseAcceptance>
    <PackageTags>Binance Bybit Kucoin OKX Bitget C# .Net CryptoCurrency Exchange API wrapper Rest API trading bot arbitrage bitcoin eth ltc altcoin</PackageTags>
    <RepositoryType>git</RepositoryType>
    <RepositoryUrl>https://github.com/ccxt/ccxt</RepositoryUrl>
    <PackageProjectUrl>https://github.com/ccxt/ccxt</PackageProjectUrl>
    <PackageIcon>ccxt4.png</PackageIcon>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <NeutralLanguage>en</NeutralLanguage>
    <GeneratePackageOnBuild>true</GeneratePackageOnBuild>
    <PackageReleaseNotes />
    <NoWarn>CS1998,CS0168, CS0108, CS8604, CS8600, CS8601, CS8602, CS8603, CS8625, CS8618, CS8981, CA2200, CS8974, CS043, CS0436, CA2200, CS8619</NoWarn>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="*" />
          </ItemGroup>
  <ItemGroup>
    <None Include="img/ccxt4.png" Pack="true" PackagePath="" />
    <None Include="../../README.md" Pack="true" PackagePath="" />
</ItemGroup>
<ItemGroup>
  <None Update="static/StarkSharp/StarkSharp.Signer/StarkCurveSigner\pedersen_params.json">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    <Pack>true</Pack>
  </None>
</ItemGroup>

</Project>

================================================
File: cs/ccxt/api/ace.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class ace : Exchange
{
    public ace (object args = null): base(args) {}

    public async Task<object> publicGetOapiV2ListTradePrice (object parameters = null)
    {
        return await this.callAsync ("publicGetOapiV2ListTradePrice",parameters);
    }

    public async Task<object> publicGetOapiV2ListMarketPair (object parameters = null)
    {
        return await this.callAsync ("publicGetOapiV2ListMarketPair",parameters);
    }

    public async Task<object> publicGetOpenV2PublicGetOrderBook (object parameters = null)
    {
        return await this.callAsync ("publicGetOpenV2PublicGetOrderBook",parameters);
    }

    public async Task<object> privatePostV2CoinCustomerAccount (object parameters = null)
    {
        return await this.callAsync ("privatePostV2CoinCustomerAccount",parameters);
    }

    public async Task<object> privatePostV2KlineGetKline (object parameters = null)
    {
        return await this.callAsync ("privatePostV2KlineGetKline",parameters);
    }

    public async Task<object> privatePostV2OrderOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostV2OrderOrder",parameters);
    }

    public async Task<object> privatePostV2OrderCancel (object parameters = null)
    {
        return await this.callAsync ("privatePostV2OrderCancel",parameters);
    }

    public async Task<object> privatePostV2OrderGetOrderList (object parameters = null)
    {
        return await this.callAsync ("privatePostV2OrderGetOrderList",parameters);
    }

    public async Task<object> privatePostV2OrderShowOrderStatus (object parameters = null)
    {
        return await this.callAsync ("privatePostV2OrderShowOrderStatus",parameters);
    }

    public async Task<object> privatePostV2OrderShowOrderHistory (object parameters = null)
    {
        return await this.callAsync ("privatePostV2OrderShowOrderHistory",parameters);
    }

    public async Task<object> privatePostV2OrderGetTradeList (object parameters = null)
    {
        return await this.callAsync ("privatePostV2OrderGetTradeList",parameters);
    }

}

================================================
File: cs/ccxt/api/alpaca.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class alpaca : Exchange
{
    public alpaca (object args = null): base(args) {}

    public async Task<object> traderPrivateGetV2Account (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Account",parameters);
    }

    public async Task<object> traderPrivateGetV2Orders (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Orders",parameters);
    }

    public async Task<object> traderPrivateGetV2OrdersOrderId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2OrdersOrderId",parameters);
    }

    public async Task<object> traderPrivateGetV2Positions (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Positions",parameters);
    }

    public async Task<object> traderPrivateGetV2PositionsSymbolOrAssetId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2PositionsSymbolOrAssetId",parameters);
    }

    public async Task<object> traderPrivateGetV2AccountPortfolioHistory (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2AccountPortfolioHistory",parameters);
    }

    public async Task<object> traderPrivateGetV2Watchlists (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Watchlists",parameters);
    }

    public async Task<object> traderPrivateGetV2WatchlistsWatchlistId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2WatchlistsWatchlistId",parameters);
    }

    public async Task<object> traderPrivateGetV2WatchlistsByName (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2WatchlistsByName",parameters);
    }

    public async Task<object> traderPrivateGetV2AccountConfigurations (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2AccountConfigurations",parameters);
    }

    public async Task<object> traderPrivateGetV2AccountActivities (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2AccountActivities",parameters);
    }

    public async Task<object> traderPrivateGetV2AccountActivitiesActivityType (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2AccountActivitiesActivityType",parameters);
    }

    public async Task<object> traderPrivateGetV2Calendar (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Calendar",parameters);
    }

    public async Task<object> traderPrivateGetV2Clock (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Clock",parameters);
    }

    public async Task<object> traderPrivateGetV2Assets (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Assets",parameters);
    }

    public async Task<object> traderPrivateGetV2AssetsSymbolOrAssetId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2AssetsSymbolOrAssetId",parameters);
    }

    public async Task<object> traderPrivateGetV2CorporateActionsAnnouncementsId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2CorporateActionsAnnouncementsId",parameters);
    }

    public async Task<object> traderPrivateGetV2CorporateActionsAnnouncements (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2CorporateActionsAnnouncements",parameters);
    }

    public async Task<object> traderPrivateGetV2Wallets (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2Wallets",parameters);
    }

    public async Task<object> traderPrivateGetV2WalletsTransfers (object parameters = null)
    {
        return await this.callAsync ("traderPrivateGetV2WalletsTransfers",parameters);
    }

    public async Task<object> traderPrivatePostV2Orders (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePostV2Orders",parameters);
    }

    public async Task<object> traderPrivatePostV2Watchlists (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePostV2Watchlists",parameters);
    }

    public async Task<object> traderPrivatePostV2WatchlistsWatchlistId (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePostV2WatchlistsWatchlistId",parameters);
    }

    public async Task<object> traderPrivatePostV2WatchlistsByName (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePostV2WatchlistsByName",parameters);
    }

    public async Task<object> traderPrivatePostV2WalletsTransfers (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePostV2WalletsTransfers",parameters);
    }

    public async Task<object> traderPrivatePutV2OrdersOrderId (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePutV2OrdersOrderId",parameters);
    }

    public async Task<object> traderPrivatePutV2WatchlistsWatchlistId (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePutV2WatchlistsWatchlistId",parameters);
    }

    public async Task<object> traderPrivatePutV2WatchlistsByName (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePutV2WatchlistsByName",parameters);
    }

    public async Task<object> traderPrivatePatchV2OrdersOrderId (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePatchV2OrdersOrderId",parameters);
    }

    public async Task<object> traderPrivatePatchV2AccountConfigurations (object parameters = null)
    {
        return await this.callAsync ("traderPrivatePatchV2AccountConfigurations",parameters);
    }

    public async Task<object> traderPrivateDeleteV2Orders (object parameters = null)
    {
        return await this.callAsync ("traderPrivateDeleteV2Orders",parameters);
    }

    public async Task<object> traderPrivateDeleteV2OrdersOrderId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateDeleteV2OrdersOrderId",parameters);
    }

    public async Task<object> traderPrivateDeleteV2Positions (object parameters = null)
    {
        return await this.callAsync ("traderPrivateDeleteV2Positions",parameters);
    }

    public async Task<object> traderPrivateDeleteV2PositionsSymbolOrAssetId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateDeleteV2PositionsSymbolOrAssetId",parameters);
    }

    public async Task<object> traderPrivateDeleteV2WatchlistsWatchlistId (object parameters = null)
    {
        return await this.callAsync ("traderPrivateDeleteV2WatchlistsWatchlistId",parameters);
    }

    public async Task<object> traderPrivateDeleteV2WatchlistsByName (object parameters = null)
    {
        return await this.callAsync ("traderPrivateDeleteV2WatchlistsByName",parameters);
    }

    public async Task<object> traderPrivateDeleteV2WatchlistsWatchlistIdSymbol (object parameters = null)
    {
        return await this.callAsync ("traderPrivateDeleteV2WatchlistsWatchlistIdSymbol",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocBars (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocBars",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocLatestBars (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocLatestBars",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocLatestOrderbooks (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocLatestOrderbooks",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocLatestQuotes (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocLatestQuotes",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocLatestTrades (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocLatestTrades",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocQuotes (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocQuotes",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocSnapshots (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocSnapshots",parameters);
    }

    public async Task<object> marketPublicGetV1beta3CryptoLocTrades (object parameters = null)
    {
        return await this.callAsync ("marketPublicGetV1beta3CryptoLocTrades",parameters);
    }

    public async Task<object> marketPrivateGetV1beta1CorporateActions (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV1beta1CorporateActions",parameters);
    }

    public async Task<object> marketPrivateGetV1beta1ForexLatestRates (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV1beta1ForexLatestRates",parameters);
    }

    public async Task<object> marketPrivateGetV1beta1ForexRates (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV1beta1ForexRates",parameters);
    }

    public async Task<object> marketPrivateGetV1beta1LogosSymbol (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV1beta1LogosSymbol",parameters);
    }

    public async Task<object> marketPrivateGetV1beta1News (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV1beta1News",parameters);
    }

    public async Task<object> marketPrivateGetV1beta1ScreenerStocksMostActives (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV1beta1ScreenerStocksMostActives",parameters);
    }

    public async Task<object> marketPrivateGetV1beta1ScreenerMarketTypeMovers (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV1beta1ScreenerMarketTypeMovers",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksAuctions (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksAuctions",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksBars (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksBars",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksBarsLatest (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksBarsLatest",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksMetaConditionsTicktype (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksMetaConditionsTicktype",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksMetaExchanges (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksMetaExchanges",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksQuotes (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksQuotes",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksQuotesLatest (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksQuotesLatest",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSnapshots (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSnapshots",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksTrades (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksTrades",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksTradesLatest (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksTradesLatest",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolAuctions (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolAuctions",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolBars (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolBars",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolBarsLatest (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolBarsLatest",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolQuotes (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolQuotes",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolQuotesLatest (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolQuotesLatest",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolSnapshot (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolSnapshot",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolTrades (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolTrades",parameters);
    }

    public async Task<object> marketPrivateGetV2StocksSymbolTradesLatest (object parameters = null)
    {
        return await this.callAsync ("marketPrivateGetV2StocksSymbolTradesLatest",parameters);
    }

}

================================================
File: cs/ccxt/api/ascendex.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class ascendex : Exchange
{
    public ascendex (object args = null): base(args) {}

    public async Task<object> v1PublicGetAssets (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetAssets",parameters);
    }

    public async Task<object> v1PublicGetProducts (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetProducts",parameters);
    }

    public async Task<object> v1PublicGetTicker (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetTicker",parameters);
    }

    public async Task<object> v1PublicGetBarhistInfo (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetBarhistInfo",parameters);
    }

    public async Task<object> v1PublicGetBarhist (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetBarhist",parameters);
    }

    public async Task<object> v1PublicGetDepth (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetDepth",parameters);
    }

    public async Task<object> v1PublicGetTrades (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetTrades",parameters);
    }

    public async Task<object> v1PublicGetCashAssets (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetCashAssets",parameters);
    }

    public async Task<object> v1PublicGetCashProducts (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetCashProducts",parameters);
    }

    public async Task<object> v1PublicGetMarginAssets (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetMarginAssets",parameters);
    }

    public async Task<object> v1PublicGetMarginProducts (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetMarginProducts",parameters);
    }

    public async Task<object> v1PublicGetFuturesCollateral (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetFuturesCollateral",parameters);
    }

    public async Task<object> v1PublicGetFuturesContracts (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetFuturesContracts",parameters);
    }

    public async Task<object> v1PublicGetFuturesRefPx (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetFuturesRefPx",parameters);
    }

    public async Task<object> v1PublicGetFuturesMarketData (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetFuturesMarketData",parameters);
    }

    public async Task<object> v1PublicGetFuturesFundingRates (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetFuturesFundingRates",parameters);
    }

    public async Task<object> v1PublicGetRiskLimitInfo (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetRiskLimitInfo",parameters);
    }

    public async Task<object> v1PublicGetExchangeInfo (object parameters = null)
    {
        return await this.callAsync ("v1PublicGetExchangeInfo",parameters);
    }

    public async Task<object> v1PrivateGetInfo (object parameters = null)
    {
        return await this.callAsync ("v1PrivateGetInfo",parameters);
    }

    public async Task<object> v1PrivateGetWalletTransactions (object parameters = null)
    {
        return await this.callAsync ("v1PrivateGetWalletTransactions",parameters);
    }

    public async Task<object> v1PrivateGetWalletDepositAddress (object parameters = null)
    {
        return await this.callAsync ("v1PrivateGetWalletDepositAddress",parameters);
    }

    public async Task<object> v1PrivateGetDataBalanceSnapshot (object parameters = null)
    {
        return await this.callAsync ("v1PrivateGetDataBalanceSnapshot",parameters);
    }

    public async Task<object> v1PrivateGetDataBalanceHistory (object parameters = null)
    {
        return await this.callAsync ("v1PrivateGetDataBalanceHistory",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryGetBalance (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryGetBalance",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryGetOrderOpen (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryGetOrderOpen",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryGetOrderStatus (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryGetOrderStatus",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryGetOrderHistCurrent (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryGetOrderHistCurrent",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryGetRisk (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryGetRisk",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryPostOrder (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryPostOrder",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryPostOrderBatch (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryPostOrderBatch",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryDeleteOrder (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryDeleteOrder",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryDeleteOrderAll (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryDeleteOrderAll",parameters);
    }

    public async Task<object> v1PrivateAccountCategoryDeleteOrderBatch (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountCategoryDeleteOrderBatch",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetCashBalance (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetCashBalance",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetMarginBalance (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetMarginBalance",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetMarginRisk (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetMarginRisk",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetFuturesCollateralBalance (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetFuturesCollateralBalance",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetFuturesPosition (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetFuturesPosition",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetFuturesRisk (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetFuturesRisk",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetFuturesFundingPayments (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetFuturesFundingPayments",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetOrderHist (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetOrderHist",parameters);
    }

    public async Task<object> v1PrivateAccountGroupGetSpotFee (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupGetSpotFee",parameters);
    }

    public async Task<object> v1PrivateAccountGroupPostTransfer (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupPostTransfer",parameters);
    }

    public async Task<object> v1PrivateAccountGroupPostFuturesTransferDeposit (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupPostFuturesTransferDeposit",parameters);
    }

    public async Task<object> v1PrivateAccountGroupPostFuturesTransferWithdraw (object parameters = null)
    {
        return await this.callAsync ("v1PrivateAccountGroupPostFuturesTransferWithdraw",parameters);
    }

    public async Task<object> v2PublicGetAssets (object parameters = null)
    {
        return await this.callAsync ("v2PublicGetAssets",parameters);
    }

    public async Task<object> v2PublicGetFuturesContract (object parameters = null)
    {
        return await this.callAsync ("v2PublicGetFuturesContract",parameters);
    }

    public async Task<object> v2PublicGetFuturesCollateral (object parameters = null)
    {
        return await this.callAsync ("v2PublicGetFuturesCollateral",parameters);
    }

    public async Task<object> v2PublicGetFuturesPricingData (object parameters = null)
    {
        return await this.callAsync ("v2PublicGetFuturesPricingData",parameters);
    }

    public async Task<object> v2PublicGetFuturesTicker (object parameters = null)
    {
        return await this.callAsync ("v2PublicGetFuturesTicker",parameters);
    }

    public async Task<object> v2PublicGetRiskLimitInfo (object parameters = null)
    {
        return await this.callAsync ("v2PublicGetRiskLimitInfo",parameters);
    }

    public async Task<object> v2PrivateDataGetOrderHist (object parameters = null)
    {
        return await this.callAsync ("v2PrivateDataGetOrderHist",parameters);
    }

    public async Task<object> v2PrivateGetAccountInfo (object parameters = null)
    {
        return await this.callAsync ("v2PrivateGetAccountInfo",parameters);
    }

    public async Task<object> v2PrivateAccountGroupGetOrderHist (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupGetOrderHist",parameters);
    }

    public async Task<object> v2PrivateAccountGroupGetFuturesPosition (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupGetFuturesPosition",parameters);
    }

    public async Task<object> v2PrivateAccountGroupGetFuturesFreeMargin (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupGetFuturesFreeMargin",parameters);
    }

    public async Task<object> v2PrivateAccountGroupGetFuturesOrderHistCurrent (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupGetFuturesOrderHistCurrent",parameters);
    }

    public async Task<object> v2PrivateAccountGroupGetFuturesFundingPayments (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupGetFuturesFundingPayments",parameters);
    }

    public async Task<object> v2PrivateAccountGroupGetFuturesOrderOpen (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupGetFuturesOrderOpen",parameters);
    }

    public async Task<object> v2PrivateAccountGroupGetFuturesOrderStatus (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupGetFuturesOrderStatus",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesIsolatedPositionMargin (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesIsolatedPositionMargin",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesMarginType (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesMarginType",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesLeverage (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesLeverage",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesTransferDeposit (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesTransferDeposit",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesTransferWithdraw (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesTransferWithdraw",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesOrder",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesOrderBatch (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesOrderBatch",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostFuturesOrderOpen (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostFuturesOrderOpen",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostSubuserSubuserTransfer (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostSubuserSubuserTransfer",parameters);
    }

    public async Task<object> v2PrivateAccountGroupPostSubuserSubuserTransferHist (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupPostSubuserSubuserTransferHist",parameters);
    }

    public async Task<object> v2PrivateAccountGroupDeleteFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupDeleteFuturesOrder",parameters);
    }

    public async Task<object> v2PrivateAccountGroupDeleteFuturesOrderBatch (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupDeleteFuturesOrderBatch",parameters);
    }

    public async Task<object> v2PrivateAccountGroupDeleteFuturesOrderAll (object parameters = null)
    {
        return await this.callAsync ("v2PrivateAccountGroupDeleteFuturesOrderAll",parameters);
    }

}

================================================
File: cs/ccxt/api/bequant.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class bequant : hitbtc
{
    public bequant (object args = null): base(args) {}

    public async Task<object> publicGetPublicCurrency (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCurrency",parameters);
    }

    public async Task<object> publicGetPublicCurrencyCurrency (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCurrencyCurrency",parameters);
    }

    public async Task<object> publicGetPublicSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicSymbol",parameters);
    }

    public async Task<object> publicGetPublicSymbolSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicSymbolSymbol",parameters);
    }

    public async Task<object> publicGetPublicTicker (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTicker",parameters);
    }

    public async Task<object> publicGetPublicTickerSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTickerSymbol",parameters);
    }

    public async Task<object> publicGetPublicPriceRate (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceRate",parameters);
    }

    public async Task<object> publicGetPublicPriceHistory (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceHistory",parameters);
    }

    public async Task<object> publicGetPublicPriceTicker (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceTicker",parameters);
    }

    public async Task<object> publicGetPublicPriceTickerSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceTickerSymbol",parameters);
    }

    public async Task<object> publicGetPublicTrades (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTrades",parameters);
    }

    public async Task<object> publicGetPublicTradesSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTradesSymbol",parameters);
    }

    public async Task<object> publicGetPublicOrderbook (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicOrderbook",parameters);
    }

    public async Task<object> publicGetPublicOrderbookSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicOrderbookSymbol",parameters);
    }

    public async Task<object> publicGetPublicCandles (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCandles",parameters);
    }

    public async Task<object> publicGetPublicCandlesSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCandlesSymbol",parameters);
    }

    public async Task<object> publicGetPublicConvertedCandles (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicConvertedCandles",parameters);
    }

    public async Task<object> publicGetPublicConvertedCandlesSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicConvertedCandlesSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesInfo (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesInfo",parameters);
    }

    public async Task<object> publicGetPublicFuturesInfoSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesInfoSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesHistoryFunding (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesHistoryFunding",parameters);
    }

    public async Task<object> publicGetPublicFuturesHistoryFundingSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesHistoryFundingSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesIndexPrice (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesIndexPrice",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesIndexPriceSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesIndexPriceSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesMarkPrice (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesMarkPrice",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesMarkPriceSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesMarkPriceSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesPremiumIndex (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesPremiumIndex",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesPremiumIndexSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesPremiumIndexSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesOpenInterest (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesOpenInterest",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesOpenInterestSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesOpenInterestSymbol",parameters);
    }

    public async Task<object> privateGetSpotBalance (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotBalance",parameters);
    }

    public async Task<object> privateGetSpotBalanceCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotBalanceCurrency",parameters);
    }

    public async Task<object> privateGetSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotOrder",parameters);
    }

    public async Task<object> privateGetSpotOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotOrderClientOrderId",parameters);
    }

    public async Task<object> privateGetSpotFee (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotFee",parameters);
    }

    public async Task<object> privateGetSpotFeeSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotFeeSymbol",parameters);
    }

    public async Task<object> privateGetSpotHistoryOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotHistoryOrder",parameters);
    }

    public async Task<object> privateGetSpotHistoryTrade (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotHistoryTrade",parameters);
    }

    public async Task<object> privateGetMarginAccount (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginAccount",parameters);
    }

    public async Task<object> privateGetMarginAccountIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginAccountIsolatedSymbol",parameters);
    }

    public async Task<object> privateGetMarginAccountCrossCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginAccountCrossCurrency",parameters);
    }

    public async Task<object> privateGetMarginOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginOrder",parameters);
    }

    public async Task<object> privateGetMarginOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginOrderClientOrderId",parameters);
    }

    public async Task<object> privateGetMarginConfig (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginConfig",parameters);
    }

    public async Task<object> privateGetMarginHistoryOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryOrder",parameters);
    }

    public async Task<object> privateGetMarginHistoryTrade (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryTrade",parameters);
    }

    public async Task<object> privateGetMarginHistoryPositions (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryPositions",parameters);
    }

    public async Task<object> privateGetMarginHistoryClearing (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryClearing",parameters);
    }

    public async Task<object> privateGetFuturesBalance (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesBalance",parameters);
    }

    public async Task<object> privateGetFuturesBalanceCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesBalanceCurrency",parameters);
    }

    public async Task<object> privateGetFuturesAccount (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesAccount",parameters);
    }

    public async Task<object> privateGetFuturesAccountIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesAccountIsolatedSymbol",parameters);
    }

    public async Task<object> privateGetFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesOrder",parameters);
    }

    public async Task<object> privateGetFuturesOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesOrderClientOrderId",parameters);
    }

    public async Task<object> privateGetFuturesConfig (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesConfig",parameters);
    }

    public async Task<object> privateGetFuturesFee (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesFee",parameters);
    }

    public async Task<object> privateGetFuturesFeeSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesFeeSymbol",parameters);
    }

    public async Task<object> privateGetFuturesHistoryOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryOrder",parameters);
    }

    public async Task<object> privateGetFuturesHistoryTrade (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryTrade",parameters);
    }

    public async Task<object> privateGetFuturesHistoryPositions (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryPositions",parameters);
    }

    public async Task<object> privateGetFuturesHistoryClearing (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryClearing",parameters);
    }

    public async Task<object> privateGetWalletBalance (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletBalance",parameters);
    }

    public async Task<object> privateGetWalletBalanceCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletBalanceCurrency",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddress (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddress",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddressRecentDeposit (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddressRecentDeposit",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddressRecentWithdraw (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddressRecentWithdraw",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddressCheckMine (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddressCheckMine",parameters);
    }

    public async Task<object> privateGetWalletTransactions (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletTransactions",parameters);
    }

    public async Task<object> privateGetWalletTransactionsTxId (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletTransactionsTxId",parameters);
    }

    public async Task<object> privateGetWalletCryptoFeeEstimate (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoFeeEstimate",parameters);
    }

    public async Task<object> privateGetWalletAirdrops (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletAirdrops",parameters);
    }

    public async Task<object> privateGetWalletAmountLocks (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletAmountLocks",parameters);
    }

    public async Task<object> privateGetSubAccount (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccount",parameters);
    }

    public async Task<object> privateGetSubAccountAcl (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccountAcl",parameters);
    }

    public async Task<object> privateGetSubAccountBalanceSubAccID (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccountBalanceSubAccID",parameters);
    }

    public async Task<object> privateGetSubAccountCryptoAddressSubAccIDCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccountCryptoAddressSubAccIDCurrency",parameters);
    }

    public async Task<object> privatePostSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostSpotOrder",parameters);
    }

    public async Task<object> privatePostSpotOrderList (object parameters = null)
    {
        return await this.callAsync ("privatePostSpotOrderList",parameters);
    }

    public async Task<object> privatePostMarginOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostMarginOrder",parameters);
    }

    public async Task<object> privatePostMarginOrderList (object parameters = null)
    {
        return await this.callAsync ("privatePostMarginOrderList",parameters);
    }

    public async Task<object> privatePostFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostFuturesOrder",parameters);
    }

    public async Task<object> privatePostFuturesOrderList (object parameters = null)
    {
        return await this.callAsync ("privatePostFuturesOrderList",parameters);
    }

    public async Task<object> privatePostWalletCryptoAddress (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoAddress",parameters);
    }

    public async Task<object> privatePostWalletCryptoWithdraw (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoWithdraw",parameters);
    }

    public async Task<object> privatePostWalletConvert (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletConvert",parameters);
    }

    public async Task<object> privatePostWalletTransfer (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletTransfer",parameters);
    }

    public async Task<object> privatePostWalletInternalWithdraw (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletInternalWithdraw",parameters);
    }

    public async Task<object> privatePostWalletCryptoCheckOffchainAvailable (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoCheckOffchainAvailable",parameters);
    }

    public async Task<object> privatePostWalletCryptoFeesEstimate (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoFeesEstimate",parameters);
    }

    public async Task<object> privatePostWalletAirdropsIdClaim (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletAirdropsIdClaim",parameters);
    }

    public async Task<object> privatePostSubAccountFreeze (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountFreeze",parameters);
    }

    public async Task<object> privatePostSubAccountActivate (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountActivate",parameters);
    }

    public async Task<object> privatePostSubAccountTransfer (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountTransfer",parameters);
    }

    public async Task<object> privatePostSubAccountAcl (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountAcl",parameters);
    }

    public async Task<object> privatePatchSpotOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privatePatchSpotOrderClientOrderId",parameters);
    }

    public async Task<object> privatePatchMarginOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privatePatchMarginOrderClientOrderId",parameters);
    }

    public async Task<object> privatePatchFuturesOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privatePatchFuturesOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privateDeleteSpotOrder",parameters);
    }

    public async Task<object> privateDeleteSpotOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteSpotOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteMarginPosition (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginPosition",parameters);
    }

    public async Task<object> privateDeleteMarginPositionIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginPositionIsolatedSymbol",parameters);
    }

    public async Task<object> privateDeleteMarginOrder (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginOrder",parameters);
    }

    public async Task<object> privateDeleteMarginOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteFuturesPosition (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesPosition",parameters);
    }

    public async Task<object> privateDeleteFuturesPositionMarginModeSymbol (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesPositionMarginModeSymbol",parameters);
    }

    public async Task<object> privateDeleteFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesOrder",parameters);
    }

    public async Task<object> privateDeleteFuturesOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteWalletCryptoWithdrawId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteWalletCryptoWithdrawId",parameters);
    }

    public async Task<object> privatePutMarginAccountIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privatePutMarginAccountIsolatedSymbol",parameters);
    }

    public async Task<object> privatePutFuturesAccountIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privatePutFuturesAccountIsolatedSymbol",parameters);
    }

    public async Task<object> privatePutWalletCryptoWithdrawId (object parameters = null)
    {
        return await this.callAsync ("privatePutWalletCryptoWithdrawId",parameters);
    }

}

================================================
File: cs/ccxt/api/bigone.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class bigone : Exchange
{
    public bigone (object args = null): base(args) {}

    public async Task<object> publicGetPing (object parameters = null)
    {
        return await this.callAsync ("publicGetPing",parameters);
    }

    public async Task<object> publicGetAssetPairs (object parameters = null)
    {
        return await this.callAsync ("publicGetAssetPairs",parameters);
    }

    public async Task<object> publicGetAssetPairsAssetPairNameDepth (object parameters = null)
    {
        return await this.callAsync ("publicGetAssetPairsAssetPairNameDepth",parameters);
    }

    public async Task<object> publicGetAssetPairsAssetPairNameTrades (object parameters = null)
    {
        return await this.callAsync ("publicGetAssetPairsAssetPairNameTrades",parameters);
    }

    public async Task<object> publicGetAssetPairsAssetPairNameTicker (object parameters = null)
    {
        return await this.callAsync ("publicGetAssetPairsAssetPairNameTicker",parameters);
    }

    public async Task<object> publicGetAssetPairsAssetPairNameCandles (object parameters = null)
    {
        return await this.callAsync ("publicGetAssetPairsAssetPairNameCandles",parameters);
    }

    public async Task<object> publicGetAssetPairsTickers (object parameters = null)
    {
        return await this.callAsync ("publicGetAssetPairsTickers",parameters);
    }

    public async Task<object> privateGetAccounts (object parameters = null)
    {
        return await this.callAsync ("privateGetAccounts",parameters);
    }

    public async Task<object> privateGetFundAccounts (object parameters = null)
    {
        return await this.callAsync ("privateGetFundAccounts",parameters);
    }

    public async Task<object> privateGetAssetsAssetSymbolAddress (object parameters = null)
    {
        return await this.callAsync ("privateGetAssetsAssetSymbolAddress",parameters);
    }

    public async Task<object> privateGetOrders (object parameters = null)
    {
        return await this.callAsync ("privateGetOrders",parameters);
    }

    public async Task<object> privateGetOrdersId (object parameters = null)
    {
        return await this.callAsync ("privateGetOrdersId",parameters);
    }

    public async Task<object> privateGetOrdersMulti (object parameters = null)
    {
        return await this.callAsync ("privateGetOrdersMulti",parameters);
    }

    public async Task<object> privateGetTrades (object parameters = null)
    {
        return await this.callAsync ("privateGetTrades",parameters);
    }

    public async Task<object> privateGetWithdrawals (object parameters = null)
    {
        return await this.callAsync ("privateGetWithdrawals",parameters);
    }

    public async Task<object> privateGetDeposits (object parameters = null)
    {
        return await this.callAsync ("privateGetDeposits",parameters);
    }

    public async Task<object> privatePostOrders (object parameters = null)
    {
        return await this.callAsync ("privatePostOrders",parameters);
    }

    public async Task<object> privatePostOrdersIdCancel (object parameters = null)
    {
        return await this.callAsync ("privatePostOrdersIdCancel",parameters);
    }

    public async Task<object> privatePostOrdersCancel (object parameters = null)
    {
        return await this.callAsync ("privatePostOrdersCancel",parameters);
    }

    public async Task<object> privatePostWithdrawals (object parameters = null)
    {
        return await this.callAsync ("privatePostWithdrawals",parameters);
    }

    public async Task<object> privatePostTransfer (object parameters = null)
    {
        return await this.callAsync ("privatePostTransfer",parameters);
    }

    public async Task<object> contractPublicGetSymbols (object parameters = null)
    {
        return await this.callAsync ("contractPublicGetSymbols",parameters);
    }

    public async Task<object> contractPublicGetInstruments (object parameters = null)
    {
        return await this.callAsync ("contractPublicGetInstruments",parameters);
    }

    public async Task<object> contractPublicGetDepthSymbolSnapshot (object parameters = null)
    {
        return await this.callAsync ("contractPublicGetDepthSymbolSnapshot",parameters);
    }

    public async Task<object> contractPublicGetInstrumentsDifference (object parameters = null)
    {
        return await this.callAsync ("contractPublicGetInstrumentsDifference",parameters);
    }

    public async Task<object> contractPublicGetInstrumentsPrices (object parameters = null)
    {
        return await this.callAsync ("contractPublicGetInstrumentsPrices",parameters);
    }

    public async Task<object> contractPrivateGetAccounts (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetAccounts",parameters);
    }

    public async Task<object> contractPrivateGetOrdersId (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetOrdersId",parameters);
    }

    public async Task<object> contractPrivateGetOrders (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetOrders",parameters);
    }

    public async Task<object> contractPrivateGetOrdersOpening (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetOrdersOpening",parameters);
    }

    public async Task<object> contractPrivateGetOrdersCount (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetOrdersCount",parameters);
    }

    public async Task<object> contractPrivateGetOrdersOpeningCount (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetOrdersOpeningCount",parameters);
    }

    public async Task<object> contractPrivateGetTrades (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetTrades",parameters);
    }

    public async Task<object> contractPrivateGetTradesCount (object parameters = null)
    {
        return await this.callAsync ("contractPrivateGetTradesCount",parameters);
    }

    public async Task<object> contractPrivatePostOrders (object parameters = null)
    {
        return await this.callAsync ("contractPrivatePostOrders",parameters);
    }

    public async Task<object> contractPrivatePostOrdersBatch (object parameters = null)
    {
        return await this.callAsync ("contractPrivatePostOrdersBatch",parameters);
    }

    public async Task<object> contractPrivatePutPositionsSymbolMargin (object parameters = null)
    {
        return await this.callAsync ("contractPrivatePutPositionsSymbolMargin",parameters);
    }

    public async Task<object> contractPrivatePutPositionsSymbolRiskLimit (object parameters = null)
    {
        return await this.callAsync ("contractPrivatePutPositionsSymbolRiskLimit",parameters);
    }

    public async Task<object> contractPrivateDeleteOrdersId (object parameters = null)
    {
        return await this.callAsync ("contractPrivateDeleteOrdersId",parameters);
    }

    public async Task<object> contractPrivateDeleteOrdersBatch (object parameters = null)
    {
        return await this.callAsync ("contractPrivateDeleteOrdersBatch",parameters);
    }

    public async Task<object> webExchangeGetV3Assets (object parameters = null)
    {
        return await this.callAsync ("webExchangeGetV3Assets",parameters);
    }

}

================================================
File: cs/ccxt/api/bingx.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class bingx : Exchange
{
    public bingx (object args = null): base(args) {}

    public async Task<object> spotV1PublicGetServerTime (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetServerTime",parameters);
    }

    public async Task<object> spotV1PublicGetCommonSymbols (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetCommonSymbols",parameters);
    }

    public async Task<object> spotV1PublicGetMarketTrades (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetMarketTrades",parameters);
    }

    public async Task<object> spotV1PublicGetMarketDepth (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetMarketDepth",parameters);
    }

    public async Task<object> spotV1PublicGetMarketKline (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetMarketKline",parameters);
    }

    public async Task<object> spotV1PublicGetTicker24hr (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetTicker24hr",parameters);
    }

    public async Task<object> spotV1PublicGetTickerPrice (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetTickerPrice",parameters);
    }

    public async Task<object> spotV1PublicGetTickerBookTicker (object parameters = null)
    {
        return await this.callAsync ("spotV1PublicGetTickerBookTicker",parameters);
    }

    public async Task<object> spotV1PrivateGetTradeQuery (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivateGetTradeQuery",parameters);
    }

    public async Task<object> spotV1PrivateGetTradeOpenOrders (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivateGetTradeOpenOrders",parameters);
    }

    public async Task<object> spotV1PrivateGetTradeHistoryOrders (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivateGetTradeHistoryOrders",parameters);
    }

    public async Task<object> spotV1PrivateGetTradeMyTrades (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivateGetTradeMyTrades",parameters);
    }

    public async Task<object> spotV1PrivateGetUserCommissionRate (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivateGetUserCommissionRate",parameters);
    }

    public async Task<object> spotV1PrivateGetAccountBalance (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivateGetAccountBalance",parameters);
    }

    public async Task<object> spotV1PrivatePostTradeOrder (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivatePostTradeOrder",parameters);
    }

    public async Task<object> spotV1PrivatePostTradeCancel (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivatePostTradeCancel",parameters);
    }

    public async Task<object> spotV1PrivatePostTradeBatchOrders (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivatePostTradeBatchOrders",parameters);
    }

    public async Task<object> spotV1PrivatePostTradeOrderCancelReplace (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivatePostTradeOrderCancelReplace",parameters);
    }

    public async Task<object> spotV1PrivatePostTradeCancelOrders (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivatePostTradeCancelOrders",parameters);
    }

    public async Task<object> spotV1PrivatePostTradeCancelOpenOrders (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivatePostTradeCancelOpenOrders",parameters);
    }

    public async Task<object> spotV1PrivatePostTradeCancelAllAfter (object parameters = null)
    {
        return await this.callAsync ("spotV1PrivatePostTradeCancelAllAfter",parameters);
    }

    public async Task<object> spotV2PublicGetMarketDepth (object parameters = null)
    {
        return await this.callAsync ("spotV2PublicGetMarketDepth",parameters);
    }

    public async Task<object> spotV2PublicGetMarketKline (object parameters = null)
    {
        return await this.callAsync ("spotV2PublicGetMarketKline",parameters);
    }

    public async Task<object> spotV3PrivateGetGetAssetTransfer (object parameters = null)
    {
        return await this.callAsync ("spotV3PrivateGetGetAssetTransfer",parameters);
    }

    public async Task<object> spotV3PrivateGetAssetTransfer (object parameters = null)
    {
        return await this.callAsync ("spotV3PrivateGetAssetTransfer",parameters);
    }

    public async Task<object> spotV3PrivateGetCapitalDepositHisrec (object parameters = null)
    {
        return await this.callAsync ("spotV3PrivateGetCapitalDepositHisrec",parameters);
    }

    public async Task<object> spotV3PrivateGetCapitalWithdrawHistory (object parameters = null)
    {
        return await this.callAsync ("spotV3PrivateGetCapitalWithdrawHistory",parameters);
    }

    public async Task<object> spotV3PrivatePostPostAssetTransfer (object parameters = null)
    {
        return await this.callAsync ("spotV3PrivatePostPostAssetTransfer",parameters);
    }

    public async Task<object> swapV1PublicGetTickerPrice (object parameters = null)
    {
        return await this.callAsync ("swapV1PublicGetTickerPrice",parameters);
    }

    public async Task<object> swapV1PublicGetMarketHistoricalTrades (object parameters = null)
    {
        return await this.callAsync ("swapV1PublicGetMarketHistoricalTrades",parameters);
    }

    public async Task<object> swapV1PublicGetMarketMarkPriceKlines (object parameters = null)
    {
        return await this.callAsync ("swapV1PublicGetMarketMarkPriceKlines",parameters);
    }

    public async Task<object> swapV1PublicGetTradeMultiAssetsRules (object parameters = null)
    {
        return await this.callAsync ("swapV1PublicGetTradeMultiAssetsRules",parameters);
    }

    public async Task<object> swapV1PrivateGetPositionSideDual (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetPositionSideDual",parameters);
    }

    public async Task<object> swapV1PrivateGetTradeBatchCancelReplace (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetTradeBatchCancelReplace",parameters);
    }

    public async Task<object> swapV1PrivateGetTradeFullOrder (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetTradeFullOrder",parameters);
    }

    public async Task<object> swapV1PrivateGetMaintMarginRatio (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetMaintMarginRatio",parameters);
    }

    public async Task<object> swapV1PrivateGetTradePositionHistory (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetTradePositionHistory",parameters);
    }

    public async Task<object> swapV1PrivateGetPositionMarginHistory (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetPositionMarginHistory",parameters);
    }

    public async Task<object> swapV1PrivateGetTwapOpenOrders (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetTwapOpenOrders",parameters);
    }

    public async Task<object> swapV1PrivateGetTwapHistoryOrders (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetTwapHistoryOrders",parameters);
    }

    public async Task<object> swapV1PrivateGetTwapOrderDetail (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetTwapOrderDetail",parameters);
    }

    public async Task<object> swapV1PrivateGetTradeAssetMode (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetTradeAssetMode",parameters);
    }

    public async Task<object> swapV1PrivateGetUserMarginAssets (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivateGetUserMarginAssets",parameters);
    }

    public async Task<object> swapV1PrivatePostTradeCancelReplace (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostTradeCancelReplace",parameters);
    }

    public async Task<object> swapV1PrivatePostPositionSideDual (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostPositionSideDual",parameters);
    }

    public async Task<object> swapV1PrivatePostTradeBatchCancelReplace (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostTradeBatchCancelReplace",parameters);
    }

    public async Task<object> swapV1PrivatePostTradeClosePosition (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostTradeClosePosition",parameters);
    }

    public async Task<object> swapV1PrivatePostTradeGetVst (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostTradeGetVst",parameters);
    }

    public async Task<object> swapV1PrivatePostTwapOrder (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostTwapOrder",parameters);
    }

    public async Task<object> swapV1PrivatePostTwapCancelOrder (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostTwapCancelOrder",parameters);
    }

    public async Task<object> swapV1PrivatePostTradeAssetMode (object parameters = null)
    {
        return await this.callAsync ("swapV1PrivatePostTradeAssetMode",parameters);
    }

    public async Task<object> swapV2PublicGetServerTime (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetServerTime",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteContracts (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteContracts",parameters);
    }

    public async Task<object> swapV2PublicGetQuotePrice (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuotePrice",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteDepth (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteDepth",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteTrades (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteTrades",parameters);
    }

    public async Task<object> swapV2PublicGetQuotePremiumIndex (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuotePremiumIndex",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteFundingRate (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteFundingRate",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteKlines (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteKlines",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteOpenInterest (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteOpenInterest",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteTicker (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteTicker",parameters);
    }

    public async Task<object> swapV2PublicGetQuoteBookTicker (object parameters = null)
    {
        return await this.callAsync ("swapV2PublicGetQuoteBookTicker",parameters);
    }

    public async Task<object> swapV2PrivateGetUserBalance (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetUserBalance",parameters);
    }

    public async Task<object> swapV2PrivateGetUserPositions (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetUserPositions",parameters);
    }

    public async Task<object> swapV2PrivateGetUserIncome (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetUserIncome",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeOpenOrders (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeOpenOrders",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeOpenOrder (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeOpenOrder",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeOrder (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeOrder",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeMarginType (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeMarginType",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeLeverage (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeLeverage",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeForceOrders (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeForceOrders",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeAllOrders (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeAllOrders",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeAllFillOrders (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeAllFillOrders",parameters);
    }

    public async Task<object> swapV2PrivateGetTradeFillHistory (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetTradeFillHistory",parameters);
    }

    public async Task<object> swapV2PrivateGetUserIncomeExport (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetUserIncomeExport",parameters);
    }

    public async Task<object> swapV2PrivateGetUserCommissionRate (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetUserCommissionRate",parameters);
    }

    public async Task<object> swapV2PrivateGetQuoteBookTicker (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateGetQuoteBookTicker",parameters);
    }

    public async Task<object> swapV2PrivatePostTradeOrder (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradeOrder",parameters);
    }

    public async Task<object> swapV2PrivatePostTradeBatchOrders (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradeBatchOrders",parameters);
    }

    public async Task<object> swapV2PrivatePostTradeCloseAllPositions (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradeCloseAllPositions",parameters);
    }

    public async Task<object> swapV2PrivatePostTradeCancelAllAfter (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradeCancelAllAfter",parameters);
    }

    public async Task<object> swapV2PrivatePostTradeMarginType (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradeMarginType",parameters);
    }

    public async Task<object> swapV2PrivatePostTradeLeverage (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradeLeverage",parameters);
    }

    public async Task<object> swapV2PrivatePostTradePositionMargin (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradePositionMargin",parameters);
    }

    public async Task<object> swapV2PrivatePostTradeOrderTest (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivatePostTradeOrderTest",parameters);
    }

    public async Task<object> swapV2PrivateDeleteTradeOrder (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateDeleteTradeOrder",parameters);
    }

    public async Task<object> swapV2PrivateDeleteTradeBatchOrders (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateDeleteTradeBatchOrders",parameters);
    }

    public async Task<object> swapV2PrivateDeleteTradeAllOpenOrders (object parameters = null)
    {
        return await this.callAsync ("swapV2PrivateDeleteTradeAllOpenOrders",parameters);
    }

    public async Task<object> swapV3PublicGetQuoteKlines (object parameters = null)
    {
        return await this.callAsync ("swapV3PublicGetQuoteKlines",parameters);
    }

    public async Task<object> cswapV1PublicGetMarketContracts (object parameters = null)
    {
        return await this.callAsync ("cswapV1PublicGetMarketContracts",parameters);
    }

    public async Task<object> cswapV1PublicGetMarketPremiumIndex (object parameters = null)
    {
        return await this.callAsync ("cswapV1PublicGetMarketPremiumIndex",parameters);
    }

    public async Task<object> cswapV1PublicGetMarketOpenInterest (object parameters = null)
    {
        return await this.callAsync ("cswapV1PublicGetMarketOpenInterest",parameters);
    }

    public async Task<object> cswapV1PublicGetMarketKlines (object parameters = null)
    {
        return await this.callAsync ("cswapV1PublicGetMarketKlines",parameters);
    }

    public async Task<object> cswapV1PublicGetMarketDepth (object parameters = null)
    {
        return await this.callAsync ("cswapV1PublicGetMarketDepth",parameters);
    }

    public async Task<object> cswapV1PublicGetMarketTicker (object parameters = null)
    {
        return await this.callAsync ("cswapV1PublicGetMarketTicker",parameters);
    }

    public async Task<object> cswapV1PrivateGetTradeLeverage (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetTradeLeverage",parameters);
    }

    public async Task<object> cswapV1PrivateGetTradeForceOrders (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetTradeForceOrders",parameters);
    }

    public async Task<object> cswapV1PrivateGetTradeAllFillOrders (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetTradeAllFillOrders",parameters);
    }

    public async Task<object> cswapV1PrivateGetTradeOpenOrders (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetTradeOpenOrders",parameters);
    }

    public async Task<object> cswapV1PrivateGetTradeOrderDetail (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetTradeOrderDetail",parameters);
    }

    public async Task<object> cswapV1PrivateGetTradeOrderHistory (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetTradeOrderHistory",parameters);
    }

    public async Task<object> cswapV1PrivateGetTradeMarginType (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetTradeMarginType",parameters);
    }

    public async Task<object> cswapV1PrivateGetUserCommissionRate (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetUserCommissionRate",parameters);
    }

    public async Task<object> cswapV1PrivateGetUserPositions (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetUserPositions",parameters);
    }

    public async Task<object> cswapV1PrivateGetUserBalance (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateGetUserBalance",parameters);
    }

    public async Task<object> cswapV1PrivatePostTradeOrder (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivatePostTradeOrder",parameters);
    }

    public async Task<object> cswapV1PrivatePostTradeLeverage (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivatePostTradeLeverage",parameters);
    }

    public async Task<object> cswapV1PrivatePostTradeAllOpenOrders (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivatePostTradeAllOpenOrders",parameters);
    }

    public async Task<object> cswapV1PrivatePostTradeCloseAllPositions (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivatePostTradeCloseAllPositions",parameters);
    }

    public async Task<object> cswapV1PrivatePostTradeMarginType (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivatePostTradeMarginType",parameters);
    }

    public async Task<object> cswapV1PrivatePostTradePositionMargin (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivatePostTradePositionMargin",parameters);
    }

    public async Task<object> cswapV1PrivateDeleteTradeAllOpenOrders (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateDeleteTradeAllOpenOrders",parameters);
    }

    public async Task<object> cswapV1PrivateDeleteTradeCancelOrder (object parameters = null)
    {
        return await this.callAsync ("cswapV1PrivateDeleteTradeCancelOrder",parameters);
    }

    public async Task<object> contractV1PrivateGetAllPosition (object parameters = null)
    {
        return await this.callAsync ("contractV1PrivateGetAllPosition",parameters);
    }

    public async Task<object> contractV1PrivateGetAllOrders (object parameters = null)
    {
        return await this.callAsync ("contractV1PrivateGetAllOrders",parameters);
    }

    public async Task<object> contractV1PrivateGetBalance (object parameters = null)
    {
        return await this.callAsync ("contractV1PrivateGetBalance",parameters);
    }

    public async Task<object> walletsV1PrivateGetCapitalConfigGetall (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivateGetCapitalConfigGetall",parameters);
    }

    public async Task<object> walletsV1PrivateGetCapitalDepositAddress (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivateGetCapitalDepositAddress",parameters);
    }

    public async Task<object> walletsV1PrivateGetCapitalInnerTransferRecords (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivateGetCapitalInnerTransferRecords",parameters);
    }

    public async Task<object> walletsV1PrivateGetCapitalSubAccountDepositAddress (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivateGetCapitalSubAccountDepositAddress",parameters);
    }

    public async Task<object> walletsV1PrivateGetCapitalDepositSubHisrec (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivateGetCapitalDepositSubHisrec",parameters);
    }

    public async Task<object> walletsV1PrivateGetCapitalSubAccountInnerTransferRecords (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivateGetCapitalSubAccountInnerTransferRecords",parameters);
    }

    public async Task<object> walletsV1PrivateGetCapitalDepositRiskRecords (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivateGetCapitalDepositRiskRecords",parameters);
    }

    public async Task<object> walletsV1PrivatePostCapitalWithdrawApply (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivatePostCapitalWithdrawApply",parameters);
    }

    public async Task<object> walletsV1PrivatePostCapitalInnerTransferApply (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivatePostCapitalInnerTransferApply",parameters);
    }

    public async Task<object> walletsV1PrivatePostCapitalSubAccountInnerTransferApply (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivatePostCapitalSubAccountInnerTransferApply",parameters);
    }

    public async Task<object> walletsV1PrivatePostCapitalDepositCreateSubAddress (object parameters = null)
    {
        return await this.callAsync ("walletsV1PrivatePostCapitalDepositCreateSubAddress",parameters);
    }

    public async Task<object> subAccountV1PrivateGetList (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivateGetList",parameters);
    }

    public async Task<object> subAccountV1PrivateGetAssets (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivateGetAssets",parameters);
    }

    public async Task<object> subAccountV1PrivateGetAllAccountBalance (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivateGetAllAccountBalance",parameters);
    }

    public async Task<object> subAccountV1PrivatePostCreate (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivatePostCreate",parameters);
    }

    public async Task<object> subAccountV1PrivatePostApiKeyCreate (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivatePostApiKeyCreate",parameters);
    }

    public async Task<object> subAccountV1PrivatePostApiKeyEdit (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivatePostApiKeyEdit",parameters);
    }

    public async Task<object> subAccountV1PrivatePostApiKeyDel (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivatePostApiKeyDel",parameters);
    }

    public async Task<object> subAccountV1PrivatePostUpdateStatus (object parameters = null)
    {
        return await this.callAsync ("subAccountV1PrivatePostUpdateStatus",parameters);
    }

    public async Task<object> accountV1PrivateGetUid (object parameters = null)
    {
        return await this.callAsync ("accountV1PrivateGetUid",parameters);
    }

    public async Task<object> accountV1PrivateGetApiKeyQuery (object parameters = null)
    {
        return await this.callAsync ("accountV1PrivateGetApiKeyQuery",parameters);
    }

    public async Task<object> accountV1PrivateGetAccountApiPermissions (object parameters = null)
    {
        return await this.callAsync ("accountV1PrivateGetAccountApiPermissions",parameters);
    }

    public async Task<object> accountV1PrivatePostInnerTransferAuthorizeSubAccount (object parameters = null)
    {
        return await this.callAsync ("accountV1PrivatePostInnerTransferAuthorizeSubAccount",parameters);
    }

    public async Task<object> accountTransferV1PrivateGetSubAccountAssetTransferHistory (object parameters = null)
    {
        return await this.callAsync ("accountTransferV1PrivateGetSubAccountAssetTransferHistory",parameters);
    }

    public async Task<object> accountTransferV1PrivatePostSubAccountTransferAssetSupportCoins (object parameters = null)
    {
        return await this.callAsync ("accountTransferV1PrivatePostSubAccountTransferAssetSupportCoins",parameters);
    }

    public async Task<object> accountTransferV1PrivatePostSubAccountTransferAsset (object parameters = null)
    {
        return await this.callAsync ("accountTransferV1PrivatePostSubAccountTransferAsset",parameters);
    }

    public async Task<object> userAuthPrivatePostUserDataStream (object parameters = null)
    {
        return await this.callAsync ("userAuthPrivatePostUserDataStream",parameters);
    }

    public async Task<object> userAuthPrivatePutUserDataStream (object parameters = null)
    {
        return await this.callAsync ("userAuthPrivatePutUserDataStream",parameters);
    }

    public async Task<object> userAuthPrivateDeleteUserDataStream (object parameters = null)
    {
        return await this.callAsync ("userAuthPrivateDeleteUserDataStream",parameters);
    }

    public async Task<object> copyTradingV1PrivateGetSwapTraceCurrentTrack (object parameters = null)
    {
        return await this.callAsync ("copyTradingV1PrivateGetSwapTraceCurrentTrack",parameters);
    }

    public async Task<object> copyTradingV1PrivatePostSwapTraceCloseTrackOrder (object parameters = null)
    {
        return await this.callAsync ("copyTradingV1PrivatePostSwapTraceCloseTrackOrder",parameters);
    }

    public async Task<object> copyTradingV1PrivatePostSwapTraceSetTPSL (object parameters = null)
    {
        return await this.callAsync ("copyTradingV1PrivatePostSwapTraceSetTPSL",parameters);
    }

    public async Task<object> copyTradingV1PrivatePostSpotTraderSellOrder (object parameters = null)
    {
        return await this.callAsync ("copyTradingV1PrivatePostSpotTraderSellOrder",parameters);
    }

    public async Task<object> apiV3PrivateGetAssetTransfer (object parameters = null)
    {
        return await this.callAsync ("apiV3PrivateGetAssetTransfer",parameters);
    }

    public async Task<object> apiV3PrivateGetCapitalDepositHisrec (object parameters = null)
    {
        return await this.callAsync ("apiV3PrivateGetCapitalDepositHisrec",parameters);
    }

    public async Task<object> apiV3PrivateGetCapitalWithdrawHistory (object parameters = null)
    {
        return await this.callAsync ("apiV3PrivateGetCapitalWithdrawHistory",parameters);
    }

    public async Task<object> apiV3PrivatePostPostAssetTransfer (object parameters = null)
    {
        return await this.callAsync ("apiV3PrivatePostPostAssetTransfer",parameters);
    }

}

================================================
File: cs/ccxt/api/bit2c.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class bit2c : Exchange
{
    public bit2c (object args = null): base(args) {}

    public async Task<object> publicGetExchangesPairTicker (object parameters = null)
    {
        return await this.callAsync ("publicGetExchangesPairTicker",parameters);
    }

    public async Task<object> publicGetExchangesPairOrderbook (object parameters = null)
    {
        return await this.callAsync ("publicGetExchangesPairOrderbook",parameters);
    }

    public async Task<object> publicGetExchangesPairTrades (object parameters = null)
    {
        return await this.callAsync ("publicGetExchangesPairTrades",parameters);
    }

    public async Task<object> publicGetExchangesPairLasttrades (object parameters = null)
    {
        return await this.callAsync ("publicGetExchangesPairLasttrades",parameters);
    }

    public async Task<object> privatePostMerchantCreateCheckout (object parameters = null)
    {
        return await this.callAsync ("privatePostMerchantCreateCheckout",parameters);
    }

    public async Task<object> privatePostFundsAddCoinFundsRequest (object parameters = null)
    {
        return await this.callAsync ("privatePostFundsAddCoinFundsRequest",parameters);
    }

    public async Task<object> privatePostOrderAddFund (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderAddFund",parameters);
    }

    public async Task<object> privatePostOrderAddOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderAddOrder",parameters);
    }

    public async Task<object> privatePostOrderGetById (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderGetById",parameters);
    }

    public async Task<object> privatePostOrderAddOrderMarketPriceBuy (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderAddOrderMarketPriceBuy",parameters);
    }

    public async Task<object> privatePostOrderAddOrderMarketPriceSell (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderAddOrderMarketPriceSell",parameters);
    }

    public async Task<object> privatePostOrderCancelOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderCancelOrder",parameters);
    }

    public async Task<object> privatePostOrderAddCoinFundsRequest (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderAddCoinFundsRequest",parameters);
    }

    public async Task<object> privatePostOrderAddStopOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostOrderAddStopOrder",parameters);
    }

    public async Task<object> privatePostPaymentGetMyId (object parameters = null)
    {
        return await this.callAsync ("privatePostPaymentGetMyId",parameters);
    }

    public async Task<object> privatePostPaymentSend (object parameters = null)
    {
        return await this.callAsync ("privatePostPaymentSend",parameters);
    }

    public async Task<object> privatePostPaymentPay (object parameters = null)
    {
        return await this.callAsync ("privatePostPaymentPay",parameters);
    }

    public async Task<object> privateGetAccountBalance (object parameters = null)
    {
        return await this.callAsync ("privateGetAccountBalance",parameters);
    }

    public async Task<object> privateGetAccountBalanceV2 (object parameters = null)
    {
        return await this.callAsync ("privateGetAccountBalanceV2",parameters);
    }

    public async Task<object> privateGetOrderMyOrders (object parameters = null)
    {
        return await this.callAsync ("privateGetOrderMyOrders",parameters);
    }

    public async Task<object> privateGetOrderGetById (object parameters = null)
    {
        return await this.callAsync ("privateGetOrderGetById",parameters);
    }

    public async Task<object> privateGetOrderAccountHistory (object parameters = null)
    {
        return await this.callAsync ("privateGetOrderAccountHistory",parameters);
    }

    public async Task<object> privateGetOrderOrderHistory (object parameters = null)
    {
        return await this.callAsync ("privateGetOrderOrderHistory",parameters);
    }

}

================================================
File: cs/ccxt/api/bitbank.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class bitbank : Exchange
{
    public bitbank (object args = null): base(args) {}

    public async Task<object> publicGetPairTicker (object parameters = null)
    {
        return await this.callAsync ("publicGetPairTicker",parameters);
    }

    public async Task<object> publicGetTickers (object parameters = null)
    {
        return await this.callAsync ("publicGetTickers",parameters);
    }

    public async Task<object> publicGetTickersJpy (object parameters = null)
    {
        return await this.callAsync ("publicGetTickersJpy",parameters);
    }

    public async Task<object> publicGetPairDepth (object parameters = null)
    {
        return await this.callAsync ("publicGetPairDepth",parameters);
    }

    public async Task<object> publicGetPairTransactions (object parameters = null)
    {
        return await this.callAsync ("publicGetPairTransactions",parameters);
    }

    public async Task<object> publicGetPairTransactionsYyyymmdd (object parameters = null)
    {
        return await this.callAsync ("publicGetPairTransactionsYyyymmdd",parameters);
    }

    public async Task<object> publicGetPairCandlestickCandletypeYyyymmdd (object parameters = null)
    {
        return await this.callAsync ("publicGetPairCandlestickCandletypeYyyymmdd",parameters);
    }

    public async Task<object> publicGetPairCircuitBreakInfo (object parameters = null)
    {
        return await this.callAsync ("publicGetPairCircuitBreakInfo",parameters);
    }

    public async Task<object> privateGetUserAssets (object parameters = null)
    {
        return await this.callAsync ("privateGetUserAssets",parameters);
    }

    public async Task<object> privateGetUserSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetUserSpotOrder",parameters);
    }

    public async Task<object> privateGetUserSpotActiveOrders (object parameters = null)
    {
        return await this.callAsync ("privateGetUserSpotActiveOrders",parameters);
    }

    public async Task<object> privateGetUserMarginPositions (object parameters = null)
    {
        return await this.callAsync ("privateGetUserMarginPositions",parameters);
    }

    public async Task<object> privateGetUserSpotTradeHistory (object parameters = null)
    {
        return await this.callAsync ("privateGetUserSpotTradeHistory",parameters);
    }

    public async Task<object> privateGetUserDepositHistory (object parameters = null)
    {
        return await this.callAsync ("privateGetUserDepositHistory",parameters);
    }

    public async Task<object> privateGetUserUnconfirmedDeposits (object parameters = null)
    {
        return await this.callAsync ("privateGetUserUnconfirmedDeposits",parameters);
    }

    public async Task<object> privateGetUserDepositOriginators (object parameters = null)
    {
        return await this.callAsync ("privateGetUserDepositOriginators",parameters);
    }

    public async Task<object> privateGetUserWithdrawalAccount (object parameters = null)
    {
        return await this.callAsync ("privateGetUserWithdrawalAccount",parameters);
    }

    public async Task<object> privateGetUserWithdrawalHistory (object parameters = null)
    {
        return await this.callAsync ("privateGetUserWithdrawalHistory",parameters);
    }

    public async Task<object> privateGetSpotStatus (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotStatus",parameters);
    }

    public async Task<object> privateGetSpotPairs (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotPairs",parameters);
    }

    public async Task<object> privatePostUserSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostUserSpotOrder",parameters);
    }

    public async Task<object> privatePostUserSpotCancelOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostUserSpotCancelOrder",parameters);
    }

    public async Task<object> privatePostUserSpotCancelOrders (object parameters = null)
    {
        return await this.callAsync ("privatePostUserSpotCancelOrders",parameters);
    }

    public async Task<object> privatePostUserSpotOrdersInfo (object parameters = null)
    {
        return await this.callAsync ("privatePostUserSpotOrdersInfo",parameters);
    }

    public async Task<object> privatePostUserConfirmDeposits (object parameters = null)
    {
        return await this.callAsync ("privatePostUserConfirmDeposits",parameters);
    }

    public async Task<object> privatePostUserConfirmDepositsAll (object parameters = null)
    {
        return await this.callAsync ("privatePostUserConfirmDepositsAll",parameters);
    }

    public async Task<object> privatePostUserRequestWithdrawal (object parameters = null)
    {
        return await this.callAsync ("privatePostUserRequestWithdrawal",parameters);
    }

    public async Task<object> marketsGetSpotPairs (object parameters = null)
    {
        return await this.callAsync ("marketsGetSpotPairs",parameters);
    }

}

================================================
File: cs/ccxt/api/bitbns.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class bitbns : Exchange
{
    public bitbns (object args = null): base(args) {}

    public async Task<object> wwwGetOrderFetchMarkets (object parameters = null)
    {
        return await this.callAsync ("wwwGetOrderFetchMarkets",parameters);
    }

    public async Task<object> wwwGetOrderFetchTickers (object parameters = null)
    {
        return await this.callAsync ("wwwGetOrderFetchTickers",parameters);
    }

    public async Task<object> wwwGetOrderFetchOrderbook (object parameters = null)
    {
        return await this.callAsync ("wwwGetOrderFetchOrderbook",parameters);
    }

    public async Task<object> wwwGetOrderGetTickerWithVolume (object parameters = null)
    {
        return await this.callAsync ("wwwGetOrderGetTickerWithVolume",parameters);
    }

    public async Task<object> wwwGetExchangeDataOhlc (object parameters = null)
    {
        return await this.callAsync ("wwwGetExchangeDataOhlc",parameters);
    }

    public async Task<object> wwwGetExchangeDataOrderBook (object parameters = null)
    {
        return await this.callAsync ("wwwGetExchangeDataOrderBook",parameters);
    }

    public async Task<object> wwwGetExchangeDataTradedetails (object parameters = null)
    {
        return await this.callAsync ("wwwGetExchangeDataTradedetails",parameters);
    }

    public async Task<object> v1GetPlatformStatus (object parameters = null)
    {
        return await this.callAsync ("v1GetPlatformStatus",parameters);
    }

    public async Task<object> v1GetTickers (object parameters = null)
    {
        return await this.callAsync ("v1GetTickers",parameters);
    }

    public async Task<object> v1GetOrderbookSellSymbol (object parameters = null)
    {
        return await this.callAsync ("v1GetOrderbookSellSymbol",parameters);
    }

    public async Task<object> v1GetOrderbookBuySymbol (object parameters = null)
    {
        return await this.callAsync ("v1GetOrderbookBuySymbol",parameters);
    }

    public async Task<object> v1PostCurrentCoinBalanceEVERYTHING (object parameters = null)
    {
        return await this.callAsync ("v1PostCurrentCoinBalanceEVERYTHING",parameters);
    }

    public async Task<object> v1PostGetApiUsageStatusUSAGE (object parameters = null)
    {
        return await this.callAsync ("v1PostGetApiUsageStatusUSAGE",parameters);
    }

    public async Task<object> v1PostGetOrderSocketTokenUSAGE (object parameters = null)
    {
        return await this.callAsync ("v1PostGetOrderSocketTokenUSAGE",parameters);
    }

    public async Task<object> v1PostCurrentCoinBalanceSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostCurrentCoinBalanceSymbol",parameters);
    }

    public async Task<object> v1PostOrderStatusSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostOrderStatusSymbol",parameters);
    }

    public async Task<object> v1PostDepositHistorySymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostDepositHistorySymbol",parameters);
    }

    public async Task<object> v1PostWithdrawHistorySymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostWithdrawHistorySymbol",parameters);
    }

    public async Task<object> v1PostWithdrawHistoryAllSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostWithdrawHistoryAllSymbol",parameters);
    }

    public async Task<object> v1PostDepositHistoryAllSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostDepositHistoryAllSymbol",parameters);
    }

    public async Task<object> v1PostListOpenOrdersSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostListOpenOrdersSymbol",parameters);
    }

    public async Task<object> v1PostListOpenStopOrdersSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostListOpenStopOrdersSymbol",parameters);
    }

    public async Task<object> v1PostGetCoinAddressSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostGetCoinAddressSymbol",parameters);
    }

    public async Task<object> v1PostPlaceSellOrderSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostPlaceSellOrderSymbol",parameters);
    }

    public async Task<object> v1PostPlaceBuyOrderSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostPlaceBuyOrderSymbol",parameters);
    }

    public async Task<object> v1PostBuyStopLossSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostBuyStopLossSymbol",parameters);
    }

    public async Task<object> v1PostSellStopLossSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostSellStopLossSymbol",parameters);
    }

    public async Task<object> v1PostCancelOrderSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostCancelOrderSymbol",parameters);
    }

    public async Task<object> v1PostCancelStopLossOrderSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostCancelStopLossOrderSymbol",parameters);
    }

    public async Task<object> v1PostListExecutedOrdersSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostListExecutedOrdersSymbol",parameters);
    }

    public async Task<object> v1PostPlaceMarketOrderSymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostPlaceMarketOrderSymbol",parameters);
    }

    public async Task<object> v1PostPlaceMarketOrderQntySymbol (object parameters = null)
    {
        return await this.callAsync ("v1PostPlaceMarketOrderQntySymbol",parameters);
    }

    public async Task<object> v2PostOrders (object parameters = null)
    {
        return await this.callAsync ("v2PostOrders",parameters);
    }

    public async Task<object> v2PostCancel (object parameters = null)
    {
        return await this.callAsync ("v2PostCancel",parameters);
    }

    public async Task<object> v2PostGetordersnew (object parameters = null)
    {
        return await this.callAsync ("v2PostGetordersnew",parameters);
    }

    public async Task<object> v2PostMarginOrders (object parameters = null)
    {
        return await this.callAsync ("v2PostMarginOrders",parameters);
    }

}

================================================
File: cs/ccxt/api/bitcoincom.cs
================================================
// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

namespace ccxt;

public partial class bitcoincom : fmfwio
{
    public bitcoincom (object args = null): base(args) {}

    public async Task<object> publicGetPublicCurrency (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCurrency",parameters);
    }

    public async Task<object> publicGetPublicCurrencyCurrency (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCurrencyCurrency",parameters);
    }

    public async Task<object> publicGetPublicSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicSymbol",parameters);
    }

    public async Task<object> publicGetPublicSymbolSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicSymbolSymbol",parameters);
    }

    public async Task<object> publicGetPublicTicker (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTicker",parameters);
    }

    public async Task<object> publicGetPublicTickerSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTickerSymbol",parameters);
    }

    public async Task<object> publicGetPublicPriceRate (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceRate",parameters);
    }

    public async Task<object> publicGetPublicPriceHistory (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceHistory",parameters);
    }

    public async Task<object> publicGetPublicPriceTicker (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceTicker",parameters);
    }

    public async Task<object> publicGetPublicPriceTickerSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicPriceTickerSymbol",parameters);
    }

    public async Task<object> publicGetPublicTrades (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTrades",parameters);
    }

    public async Task<object> publicGetPublicTradesSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicTradesSymbol",parameters);
    }

    public async Task<object> publicGetPublicOrderbook (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicOrderbook",parameters);
    }

    public async Task<object> publicGetPublicOrderbookSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicOrderbookSymbol",parameters);
    }

    public async Task<object> publicGetPublicCandles (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCandles",parameters);
    }

    public async Task<object> publicGetPublicCandlesSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicCandlesSymbol",parameters);
    }

    public async Task<object> publicGetPublicConvertedCandles (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicConvertedCandles",parameters);
    }

    public async Task<object> publicGetPublicConvertedCandlesSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicConvertedCandlesSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesInfo (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesInfo",parameters);
    }

    public async Task<object> publicGetPublicFuturesInfoSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesInfoSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesHistoryFunding (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesHistoryFunding",parameters);
    }

    public async Task<object> publicGetPublicFuturesHistoryFundingSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesHistoryFundingSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesIndexPrice (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesIndexPrice",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesIndexPriceSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesIndexPriceSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesMarkPrice (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesMarkPrice",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesMarkPriceSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesMarkPriceSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesPremiumIndex (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesPremiumIndex",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesPremiumIndexSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesPremiumIndexSymbol",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesOpenInterest (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesOpenInterest",parameters);
    }

    public async Task<object> publicGetPublicFuturesCandlesOpenInterestSymbol (object parameters = null)
    {
        return await this.callAsync ("publicGetPublicFuturesCandlesOpenInterestSymbol",parameters);
    }

    public async Task<object> privateGetSpotBalance (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotBalance",parameters);
    }

    public async Task<object> privateGetSpotBalanceCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotBalanceCurrency",parameters);
    }

    public async Task<object> privateGetSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotOrder",parameters);
    }

    public async Task<object> privateGetSpotOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotOrderClientOrderId",parameters);
    }

    public async Task<object> privateGetSpotFee (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotFee",parameters);
    }

    public async Task<object> privateGetSpotFeeSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotFeeSymbol",parameters);
    }

    public async Task<object> privateGetSpotHistoryOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotHistoryOrder",parameters);
    }

    public async Task<object> privateGetSpotHistoryTrade (object parameters = null)
    {
        return await this.callAsync ("privateGetSpotHistoryTrade",parameters);
    }

    public async Task<object> privateGetMarginAccount (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginAccount",parameters);
    }

    public async Task<object> privateGetMarginAccountIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginAccountIsolatedSymbol",parameters);
    }

    public async Task<object> privateGetMarginAccountCrossCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginAccountCrossCurrency",parameters);
    }

    public async Task<object> privateGetMarginOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginOrder",parameters);
    }

    public async Task<object> privateGetMarginOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginOrderClientOrderId",parameters);
    }

    public async Task<object> privateGetMarginConfig (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginConfig",parameters);
    }

    public async Task<object> privateGetMarginHistoryOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryOrder",parameters);
    }

    public async Task<object> privateGetMarginHistoryTrade (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryTrade",parameters);
    }

    public async Task<object> privateGetMarginHistoryPositions (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryPositions",parameters);
    }

    public async Task<object> privateGetMarginHistoryClearing (object parameters = null)
    {
        return await this.callAsync ("privateGetMarginHistoryClearing",parameters);
    }

    public async Task<object> privateGetFuturesBalance (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesBalance",parameters);
    }

    public async Task<object> privateGetFuturesBalanceCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesBalanceCurrency",parameters);
    }

    public async Task<object> privateGetFuturesAccount (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesAccount",parameters);
    }

    public async Task<object> privateGetFuturesAccountIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesAccountIsolatedSymbol",parameters);
    }

    public async Task<object> privateGetFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesOrder",parameters);
    }

    public async Task<object> privateGetFuturesOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesOrderClientOrderId",parameters);
    }

    public async Task<object> privateGetFuturesConfig (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesConfig",parameters);
    }

    public async Task<object> privateGetFuturesFee (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesFee",parameters);
    }

    public async Task<object> privateGetFuturesFeeSymbol (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesFeeSymbol",parameters);
    }

    public async Task<object> privateGetFuturesHistoryOrder (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryOrder",parameters);
    }

    public async Task<object> privateGetFuturesHistoryTrade (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryTrade",parameters);
    }

    public async Task<object> privateGetFuturesHistoryPositions (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryPositions",parameters);
    }

    public async Task<object> privateGetFuturesHistoryClearing (object parameters = null)
    {
        return await this.callAsync ("privateGetFuturesHistoryClearing",parameters);
    }

    public async Task<object> privateGetWalletBalance (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletBalance",parameters);
    }

    public async Task<object> privateGetWalletBalanceCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletBalanceCurrency",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddress (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddress",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddressRecentDeposit (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddressRecentDeposit",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddressRecentWithdraw (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddressRecentWithdraw",parameters);
    }

    public async Task<object> privateGetWalletCryptoAddressCheckMine (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoAddressCheckMine",parameters);
    }

    public async Task<object> privateGetWalletTransactions (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletTransactions",parameters);
    }

    public async Task<object> privateGetWalletTransactionsTxId (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletTransactionsTxId",parameters);
    }

    public async Task<object> privateGetWalletCryptoFeeEstimate (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletCryptoFeeEstimate",parameters);
    }

    public async Task<object> privateGetWalletAirdrops (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletAirdrops",parameters);
    }

    public async Task<object> privateGetWalletAmountLocks (object parameters = null)
    {
        return await this.callAsync ("privateGetWalletAmountLocks",parameters);
    }

    public async Task<object> privateGetSubAccount (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccount",parameters);
    }

    public async Task<object> privateGetSubAccountAcl (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccountAcl",parameters);
    }

    public async Task<object> privateGetSubAccountBalanceSubAccID (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccountBalanceSubAccID",parameters);
    }

    public async Task<object> privateGetSubAccountCryptoAddressSubAccIDCurrency (object parameters = null)
    {
        return await this.callAsync ("privateGetSubAccountCryptoAddressSubAccIDCurrency",parameters);
    }

    public async Task<object> privatePostSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostSpotOrder",parameters);
    }

    public async Task<object> privatePostSpotOrderList (object parameters = null)
    {
        return await this.callAsync ("privatePostSpotOrderList",parameters);
    }

    public async Task<object> privatePostMarginOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostMarginOrder",parameters);
    }

    public async Task<object> privatePostMarginOrderList (object parameters = null)
    {
        return await this.callAsync ("privatePostMarginOrderList",parameters);
    }

    public async Task<object> privatePostFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("privatePostFuturesOrder",parameters);
    }

    public async Task<object> privatePostFuturesOrderList (object parameters = null)
    {
        return await this.callAsync ("privatePostFuturesOrderList",parameters);
    }

    public async Task<object> privatePostWalletCryptoAddress (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoAddress",parameters);
    }

    public async Task<object> privatePostWalletCryptoWithdraw (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoWithdraw",parameters);
    }

    public async Task<object> privatePostWalletConvert (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletConvert",parameters);
    }

    public async Task<object> privatePostWalletTransfer (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletTransfer",parameters);
    }

    public async Task<object> privatePostWalletInternalWithdraw (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletInternalWithdraw",parameters);
    }

    public async Task<object> privatePostWalletCryptoCheckOffchainAvailable (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoCheckOffchainAvailable",parameters);
    }

    public async Task<object> privatePostWalletCryptoFeesEstimate (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletCryptoFeesEstimate",parameters);
    }

    public async Task<object> privatePostWalletAirdropsIdClaim (object parameters = null)
    {
        return await this.callAsync ("privatePostWalletAirdropsIdClaim",parameters);
    }

    public async Task<object> privatePostSubAccountFreeze (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountFreeze",parameters);
    }

    public async Task<object> privatePostSubAccountActivate (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountActivate",parameters);
    }

    public async Task<object> privatePostSubAccountTransfer (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountTransfer",parameters);
    }

    public async Task<object> privatePostSubAccountAcl (object parameters = null)
    {
        return await this.callAsync ("privatePostSubAccountAcl",parameters);
    }

    public async Task<object> privatePatchSpotOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privatePatchSpotOrderClientOrderId",parameters);
    }

    public async Task<object> privatePatchMarginOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privatePatchMarginOrderClientOrderId",parameters);
    }

    public async Task<object> privatePatchFuturesOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privatePatchFuturesOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteSpotOrder (object parameters = null)
    {
        return await this.callAsync ("privateDeleteSpotOrder",parameters);
    }

    public async Task<object> privateDeleteSpotOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteSpotOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteMarginPosition (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginPosition",parameters);
    }

    public async Task<object> privateDeleteMarginPositionIsolatedSymbol (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginPositionIsolatedSymbol",parameters);
    }

    public async Task<object> privateDeleteMarginOrder (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginOrder",parameters);
    }

    public async Task<object> privateDeleteMarginOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteMarginOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteFuturesPosition (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesPosition",parameters);
    }

    public async Task<object> privateDeleteFuturesPositionMarginModeSymbol (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesPositionMarginModeSymbol",parameters);
    }

    public async Task<object> privateDeleteFuturesOrder (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesOrder",parameters);
    }

    public async Task<object> privateDeleteFuturesOrderClientOrderId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteFuturesOrderClientOrderId",parameters);
    }

    public async Task<object> privateDeleteWalletCryptoWithdrawId (object parameters = null)
    {
        return await this.callAsync ("privateDeleteWalletCryptoWithdrawId",parameters);
    }

    public async Task<object> privatePutMargi