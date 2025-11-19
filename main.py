# This is a sample Python script.
import re

import sympy

from ReMethod import FitterNumericString, parseDigit, parseWord, parseSpace, parseSymbol, phoneNumberToSInteger, \
    parseLine, usefulMethod, pipiString, captureTime, findPrefix, matchEmail, matchBegin, anyMatch, usefulSub, \
    splitSentence, flagRe


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press Ctrl+F8 to toggle the breakpoint.
def ToSqrt(nums):
    sqrtProcess = int(nums.group())
    return str(sympy.sqrt(sqrtProcess))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testList = [str(i) for i in range(1, 10)]
    print(FitterNumericString(
        strContent="Date: 2008-09-06 17:50:28 GMT (2 years, 14 weeks,escapeList 16 hours and 36 minutes ago"))
    #(?:\d+)\.(\d+),\d{1,9}\.(\d{1,9}
    print(parseDigit(pattern=r"\d{1,9}\.(\d{1,9})",
                     strContext="123-95,194,864-36,1-94,12.866,3.14"))
    print(parseWord(pattern=r'(?P<Country>\w+)-(?P<capital>\w+)-(?P<Area>\d{1,3}.\d{1,3})-(?P<Year>\d{1,4})-'
                            r'(?P<Month>\d{1,2})-(?P<Day>\d{1,2})',
                    strSet='Germany-Berlin-357.114-2011-9-15', mode='capGroup'))
    print(parseSpace(pattern=r'\s{2}', spaces="  expensive top-level  calculate  "))
    print(parseSymbol(pattern=r'\D{2}', sentence="//s@ ta ll^*W#0k (-Az)\t"))
    numberPhone = phoneNumberToSInteger(phoneNumbers='+59-(860)-512-8529')
    print(numberPhone)
    print(''.join(parseLine("hello\n greet\n is from\n los angel\n.")))
    print(usefulMethod(strContent=['hello', 'apple', 'fitter', 'running', 'love'], method='repeat'))
    #catch the easy,doctor
    print(pipiString(pattern=r'easy|doctor', strContent='basic is easy,advance is hard,doctor is difficult'))
    #catch the 8:15,3:16,22:18,18:20,9:22
    print(captureTime(strContent='at Monday 8:15 am on the but , Tuesday 3:16 pm is studying, Wednesday 22:18  is '
                                 'sleeping,Sunday 18:20 is running,'
                                 'Saturday 9:22 is singing song'))
    # catch the 19.88
    print(parseWord(pattern=r'\d{1,9}\.\d+(?=\s*dollar)', strSet='the skirt is 19.88 dollar'))
    #catch the 123.15,999.886,10.88
    print(
        parseWord(pattern=r'\d{1,9}\.\d+(?!\s*dollar)*', strSet='123.15day, 999.886 money, the skirt is 10.88 dollar'))
    # catch the 5
    print(parseWord(pattern=r"(?<=\$)\d+", strSet='9 cups of coffee cost $5.89 dollar'))
    #catch the 20.146
    print(parseWord(pattern=r"\d{1,9}\.\b(?<!\$)\d+\b", strSet="40.185 million dollar can eating the preface 30times "
                                                               "lunch"))
    print(findPrefix(prefix='im', strContent='Imagine,imagers imaginable,imaginal,imaginary,through,'
                                             'overwrite,dancing', mode='package'))
    print(matchEmail(email="cloudFlareDumpAgain@Error.us"))
    print(matchBegin(pattern=r"\w*S?tate+", strContent="readyState,StateOutside,threadState,threadFinish"))
    print(anyMatch(pattern=r'(.+?)\w+=*.', strContent="cyberpunk2077 is poplar game above last years"))
    print(anyMatch(searchWord='Oxygen', strContent='Lithium,Vanadium,Meitnerium,Rhenium,oxygen,lithium'))
    print(usefulSub(pattern='1', strContent='100001010'))
    print(usefulSub(strContent='github.com is the best *code development* wedsite ',
                    mode='back', nativeSymbol='*', replaceSymbol='🟌'))
    print(usefulSub(func=ToSqrt, stringList=testList, mode='function'))
    print(usefulSub(mode=''))
    print(splitSentence(sentence='... john love joining programming talking meeting ...'))
    print(splitSentence(sentence='ada-is*working~at@IT#company!of&USA', mode='group'))
    print(flagRe(pattern=r'(.?=*[p-y]\w+)',
                 strContent="quick fox jumps height is 8.5 m,it's so storage and pure,English queen like this q要 fox",flag=re.ASCII))
    tempStr='''temporary
string!! '''
    print(flagRe(pattern=r'^\w+',strContent=tempStr,flag=re.MULTILINE))
    print(flagRe(pattern=r'.+=*\S',strContent=tempStr,flag=re.VERBOSE))
    print(flagRe(pattern=r'(\D\S.*?\W)\d+',strContent="30 night and days ,he can bug ,20 car and computer",flag=re.UNICODE|re.DOTALL))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
