# This is a sample Python script.
from ReMethod import FitterNumericaString, parseDigit, parseWord, parseSpace, parseSymbol, phoneNumberToSInteger, \
    parseLine

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(FitterNumericaString(
        strContent="Date: 2008-09-06 17:50:28 GMT (2 years, 14 weeks,escapeList 16 hours and 36 minutes ago"))
    print(parseDigit(pattern=r"^\d\d:\d\d$",
                     strContext="12:34"))
    print(parseWord(pattern=r'\bRead\b', strSet="ReadState-RunningState-endState,Read"))
    print(parseSpace(pattern=r'\s{2}', spaces="  expensive top-level  calculate  "))
    print(parseSymbol(pattern=r'\D{2}', sentence="//s@ ta ll^*W#0k (-Az)\t"))
    numberPhone = phoneNumberToSInteger(phoneNumbers='+59-(860)-512-8529')
    print(numberPhone)
    print(''.join(parseLine("hello\n greent\n is from\n los angel\n.")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
