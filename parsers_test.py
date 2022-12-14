import parsers
import driver_creation

drivers = driver_creation.create_drivers(2)
whitebit_parser = parsers.WhitebitParser(drivers[0])
binance_parser = parsers.BinanceParser(drivers[1])

try:
    # print(whitebit_parser.get_exchange_rate_on_whitebit("USDT", "UAH"))
    print("\n".join(str(x.__str__()) for x in binance_parser.get_sell_offers("USDT", "UAH", 'PrivatBank')))
finally:
    for driver in drivers:
        driver.quit()

    print("Drivers CLOSED!!")
