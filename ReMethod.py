import re
from typing import List, Pattern, Union, Tuple
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


def FitterNumericaString(strContent: str) -> List[int]:

    centerString = []
    if simpleTypingCheck(strContent):
        stringNumberList = re.findall(r'\d+', string=strContent)
        centerString.append(stringNumberList)
    numberList = (int(i) for i in flatten_res(nested_list=centerString))
    return list(numberList)


def parseDigit(pattern: Pattern = r'\d+', strContext: str = '', locationList: list = None) -> List[str]:
    """
       'd' meaning is alone digit\n
       '^d{number}' meaning match before {number} string\n
       'd${number}' meaning match after {number} string\n

     """
    if simpleTypingCheck(pattern, strContext):
        matchString = re.finditer(pattern=pattern, string=strContext)
        locationList = (loc.group() for loc in matchString)
    return list(locationList)


def parseWord(pattern: Pattern = r"\w+", strSet: str = '', wordList: List = None) -> List[str]:
    """
    'w' meaning is alone letter,not include special symbol\n
    '/d+search+/d' is finding is work of the string
    """

    if simpleTypingCheck(pattern, strSet):
        words = re.finditer(pattern=pattern, string=strSet)
        wordList = (letter.group() for letter in words)
    return list(wordList)


def parseSpace(pattern: Pattern = r"\s+", spaces: str = '', spaceList=None) -> List[str]:
    """
    's' meaning is the alone space
    """

    if simpleTypingCheck(pattern, spaces):
        space = re.finditer(pattern=pattern, string=spaces)
        spaceList = (i.group() for i in space)
    return list(spaceList)


def parseSymbol(pattern: Pattern = r"\D+", sentence: str = '',specieList: List = None) -> List[str]:
    """
    'D' meaning is alone special symbol or letter
    """

    if simpleTypingCheck(pattern, sentence):
        symbol = re.finditer(pattern=pattern, string=sentence)
        specieList = (i.group() for i in symbol)
    return list(specieList)


def phoneNumberToSInteger(phoneNumbers: str) -> int:
    integerNumber = re.sub(r'\D+', '', string=phoneNumbers)
    return int(integerNumber)


def parseLine(escapeString: str, lineList: List = None):

    if simpleTypingCheck(escapeString):
        noEscape = re.finditer('.', escapeString)
        lineList = (i.group() for i in noEscape)
    return list(lineList)
