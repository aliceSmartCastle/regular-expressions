import re
from typing import List, Pattern, Union, Tuple, Literal, Dict
from FuncTip import flatten_res


def is_String(pram: str) -> bool:
    if not isinstance(pram, str):
        return False
    else:
        return True


def is_Pattern(pram: Pattern) -> bool:
    if is_String(pram):
        if not isinstance(re.compile(pram), Pattern):
            return False
        else:
            return True
    return False


def simpleTypingCheck(*pram: Tuple[Union[Pattern, str]]) -> bool:
    if len(pram) == 1:
        if is_String(pram[0]):
            return True
        else:
            raise TypeError("argument must be a string")
    elif len(pram) == 2:
        if is_String(pram[1]) and is_Pattern(pram[0]):
            return True
        else:
            raise TypeError('first argument must be a pattern,second argument must be a string')
    return False


def FitterNumericString(strContent: str) -> List[int]:
    centerString = []
    simpleTypingCheck(strContent)
    stringNumberList = re.findall(r'\d+', string=strContent)
    centerString.append(stringNumberList)
    numberList = (int(i) for i in flatten_res(nested_list=centerString))
    return list(numberList)


def parseDigit(pattern: Pattern = r'\d+', strContext: str = '') -> List[str]:
    """
       'd' meaning is alone digit
       '^d{number}' meaning match before {number} string\n
       'd${number}' meaning match after {number} string\n
       'd{number} symbol d{number}' meaning match {number} string and symbol\n
       'd{2}:d{2}' meaning has two number addition symbol ':' after still is two number\n
       'd{number} symbol d{number}' ...concise after many times d{number} and symbol combination\n
       'd{number,number} symbol {number,number}'' ... concise the min({number*number})
       value and  after many times d{number} and symbol combination

     """

    simpleTypingCheck(pattern, strContext)
    matchString = re.finditer(pattern=pattern, string=strContext)
    locationList = (loc.group() for loc in matchString)
    return list(locationList)


def parseWord(pattern: Pattern = r"\w+", strSet: str = '', mode: Literal['capGroup', ''] = '') \
        -> Union[List[str], Dict[str, str]]:
    """
    'w' meaning is alone letter,not include special symbol\n
    '/d+search+/d' is finding is work of the string\n
    'w*' addition (keyword) match zero or more time of string\n
     w*-juice match the apple-juice,banana-juice,coconut-juice,damson-juice\n
     keyword is (-juice)
    'w+' addition (keyword) match the no close the space element of the string\n
     hell?o match the hello or helo\n
     hello is the hell?o remove the '?'\n
     helo is remove the 'l' match of the hello \n
     complex match the rule is 'w*+-ju?ice' such as
     ben like apple-juice,"\n
    "Juan like banana-juice, Liam like coconut-juice,Olivia like "\n
    "john like damson-juice, Michael like dates-jice"\n
    match result is same of 'w*-juice' expect 'dates-jice\n
    ".+?"  is greedy match of include the "keyword" of string
    '*?+keyword' is more powerful than '*+keyword'\n
    'we??lcome' is match the 'welcome' or 'wlcome' or 'welcome'\n
    'keyword+?' is stranger than +\n
    '[start-end]' match in is range of any letter\n
    '[^keyword] remove the range or letter of string\n
    '(w+) symbol (d+)' match the parse word symbol digits of string\n
    '(?P<name> re escape)+symbol '... can capturing many group of string\n
     'd+(?=s*keyword)' match the digits before the keyword\n
     'd+(?!s*keyword)' match the digits after the keyword\n




    """

    words = re.finditer(pattern=pattern, string=strSet)
    wordList = (letter.group() for letter in words)
    simpleTypingCheck(pattern, strSet)
    if mode == "capGroup":
        fixDict = (letter.groupdict() for letter in words)
        return list(fixDict)[0]
    else:
        return list(wordList)


def parseSpace(pattern: Pattern = r"\s+", spaces: str = '') -> List[str]:
    """
    's' meaning is the alone space
    """

    simpleTypingCheck(pattern, spaces)
    space = re.finditer(pattern=pattern, string=spaces)
    spaceList = (i.group() for i in space)
    return list(spaceList)


def parseSymbol(pattern: Pattern = r"\D+", sentence: str = '') -> List[str]:
    """
    'D' meaning is alone special symbol or letter
    """

    simpleTypingCheck(pattern, sentence)
    symbol = re.finditer(pattern=pattern, string=sentence)
    specieList = (i.group() for i in symbol)
    return list(specieList)


def phoneNumberToSInteger(phoneNumbers: str) -> int:
    integerNumber = re.sub(r'\D+', '', string=phoneNumbers)
    return int(integerNumber)


def parseLine(escapeString: str) -> List[str]:
    simpleTypingCheck(escapeString)
    noEscape = re.finditer('.', escapeString)
    lineList = (i.group() for i in noEscape)
    return list(lineList)


def usefulMethod(strContent: str, method: Literal['duplicate', 'backer', 'repeat'] = '') -> Union[List[str], str]:
    match method:
        case 'duplicate':
            return re.sub(pattern=r"(\w+)\s+\1", repl=r'\1', string=strContent)
        case 'backer':
            matchQuote = re.search(pattern=r'([\'"])(.*?)\1', string=strContent)
            return matchQuote.group()
        case 'repeat':
            return [i for i in strContent if re.search(pattern=r'\b\w*(\w)\1\w*\b', string=i)]
        case "" | _:
            return "you can not chosen any method"


def pipiString(pattern: Pattern, strContent: str) -> List[str]:
    return re.findall(pattern=pattern, string=strContent)


def captureTime(strContent: str) -> List[str]:
    timeMatch = re.finditer(pattern=r'([0,9]\d|[0-9]):[0-5]\d', string=strContent)
    timeString = (i.group() for i in timeMatch)
    return list(timeString)


def findPrefix(prefix: str, strContent: str, mode: Literal['remove', 'package', 'tittle', ''] = '') \
        -> Union[List[str], str, List[Tuple[str, str]]]:
    """
    find the word prefix of the string\n
    if you find the prefix is im\n
    you also enter the  im\n
    default mode : result your find the all strContent\n
    start with the 'im' word\n
    remove mode : remove the prefix of the strContent\n
    package mode : package the tuple include the match word, and it's remove the prefix\n
    tittle mode : it same to the package mode but ignore the word tittle(tittle mean str of python method str.tittle())
    and not tittle\n
    """
    defaultPattern = rf"({re.escape(prefix)}(\w+))"
    if prefix not in strContent:
        return "you entered the string is not include the prefix"
    else:
        match mode:
            case 'remove':
                patten = rf"{re.escape(prefix)}(\w+)"
                return re.findall(pattern=patten, string=strContent)
            case 'package':
                return re.findall(pattern=defaultPattern, string=strContent)
            case 'tittle':
                return re.findall(pattern=defaultPattern, string=strContent, flags=re.IGNORECASE)
            case _:
                pattern = rf"{re.escape(prefix)}\w+"
                return re.findall(pattern=pattern, string=strContent)


def matchEmail(email: str) -> str:
    pattern = r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}'
    if re.fullmatch(pattern=pattern, string=email) is not None:
        return f"{email} is valid email"
    else:
        return f"{email} is not valid email"


def matchBegin(pattern: Pattern, strContent: str) -> str:
    beginValid = re.match(pattern=pattern, string=strContent)
    if beginValid is not None:
        return beginValid.group()
    else:
        return "you entered the string is not valid"


def anyMatch(pattern: Pattern = None, searchWord='', strContent: str = '', mode: Literal['first', ''] = '') \
        -> Union[str, Tuple[str, str]]:
    if pattern is not None:
        matchString = re.search(pattern=pattern, string=strContent)
        if matchString is not None:
            return matchString.group()
        else:
            return f"not any keyword match found"
    else:
        match mode:
            case "first":
                pattern = rf"\b((\w+){re.escape(searchWord)})\b"
                searchResult = re.search(pattern, strContent)
                return searchResult.groups()
            case _:
                pattern = rf"\b{re.escape(searchWord)}\b"
                firstMatch = re.search(pattern=pattern, string=strContent, flags=re.IGNORECASE)
                return firstMatch.group()


def usefulSub(strContent: str = '', pattern: str = '',
              mode: Literal['overlap', 'back', 'function'] = 'overlap', nativeSymbol: str = '', replaceSymbol: str = '',
              stringList: List[str] = None, func=None) \
        -> Union[str, List[str]]:
    if stringList is None:
        stringList = []
    match mode:
        case 'overlap':
            return re.sub(pattern=pattern, repl='', string=strContent)
        case 'back':
            pattern = rf"{re.escape(nativeSymbol)}(.*?){re.escape(nativeSymbol)}"
            wordRepl = rf"{re.escape(replaceSymbol)}\1{re.escape(replaceSymbol)}"
            return re.sub(pattern=pattern, repl=wordRepl, string=strContent)
        case 'function':
            pattern = r'\d+'
            secretList = (re.sub(pattern=pattern, repl=func, string=liters) for liters in stringList)
            return list(secretList)
        case '':
            return "you can not chosen any method"


def splitSentence(pattern: str = r'\W+', sentence: str = '', maxSplit: int = 0, mode: Literal['group'] = ''):
    match mode:
        case 'group':
            pattern = r'(\W+)'
            return re.split(pattern=pattern, string=sentence, maxsplit=abs(int(maxSplit)))
        case '':
            return re.split(pattern=pattern, string=sentence, maxsplit=abs(int(maxSplit)))


def flagRe(pattern: str, strContent: str, flag=re.IGNORECASE) -> str:
    return re.findall(pattern=pattern, string=strContent, flags=flag)
