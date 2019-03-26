from urllib2 import urlopen
import re
 
def wordify(num):
    url = 'https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?number={}&format=words&letter_case=lowercase&action=solve'.format(num)
    return re.search(r'<div id="answer">(.*?)</div>', urlopen(url).read()).group(1)
 
n = 7364
print(wordify(n))