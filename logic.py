#Сори за то, что написано ниже
import parsers
class Calculate:

    def __init__(self, wb_parser: parsers.WhitebitParser):
        self.__wb_parser = wb_parser


    number = 30000
    WBit = 40.88;
    BMono = 41.03;
    BPrivat = 0;
    BPumb = 0;
    res = 0;
    resMono = []
    resPrivat = []
    resPumb = []

    def __get_wbit(self):
        return float(self.__wb_parser.get_exchange_rate_on_whitebit("USDT","UAH"))

    def WtoBmono(self):
        global number
        global res
        sum = 0
        for el in number:
            sum = ((el / self.__get_wbit() - 1 )* BMono) - el
            resMono.append(sum)
            # print(sum)

    def WtoBprivat(self, number):
        global res
        sum = 0
        sum = ((number / self.__get_wbit() - 1) * BPrivat) - number
        return sum


    def WtoBpumb(self):
        global number
        global res
        sum = 0
        for el in number:
            sum = ((el / self.__get_wbit() - 1) * BPumb) - el
            return



