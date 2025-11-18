# This is a sample Python script.
from ReMethod import FitterNumericaString, parseDigit, parseWord, parseSpace, parseSymbol, phoneNumberToSInteger, \
    parseLine, usefulMethod, pipiString, captureTime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(FitterNumericaString(
        strContent="Date: 2008-09-06 17:50:28 GMT (2 years, 14 weeks,escapeList 16 hours and 36 minutes ago"))
    #(?:\d+)\.(\d+),\d{1,9}\.(\d{1,9}
    print(parseDigit(pattern=r"\d{1,9}\.(\d{1,9})",
                     strContext="123-95,194,864-36,1-94,12.866,3.14"))
    print(parseWord(pattern=r'(?P<Country>\w+)-(?P<capital>\w+)-(?P<Area>\d{1,3}.\d{1,3})-(?P<Year>\d{1,4})-'
                            r'(?P<Month>\d{1,2})-(?P<Day>\d{1,2})',
                    strSet='Germany-Berlin-582.88-2011-9-15', mode='capGroup'))
    print(parseSpace(pattern=r'\s{2}', spaces="  expensive top-level  calculate  "))
    print(parseSymbol(pattern=r'\D{2}', sentence="//s@ ta ll^*W#0k (-Az)\t"))
    numberPhone = phoneNumberToSInteger(phoneNumbers='+59-(860)-512-8529')
    print(numberPhone)
    print(''.join(parseLine("hello\n greent\n is from\n los angel\n.")))
    print(usefulMethod(strContent=['hello', 'apple', 'fitter', 'running', 'love'], method='repeat'))
    print(pipiString(pattern=r'easy|doctor', strContent='basic is easy,advance is hard,doctor is difficult'))
    print(captureTime(strContent='at Monday 8:15 am on the but , Tuesday 3:16 pm is studying, Wednesday 22:18  is '
                                 'sleeping,Sunday 18:20 is running,'
                                 'Saturday 9:22 is singing song'))
    print(parseWord(pattern=r'\d{1,9}\.\d+(?=\s*dollar)',strSet='the skirt is 19.88 dollar'))
    print(parseWord(pattern=r'\d{1,9}\.\d+(?!\s*dollar)*',strSet='123.15day, 999.886 money, the skirt is 10.88 dollar'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
