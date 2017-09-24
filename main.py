import sys

def isNumber(value):
    """Return True if input is an integer or decimal number."""
    value = str(value)
    decimal = False
    for i in value:
        if i == '.' and not decimal:
            decimal = True
        else:
            try:
                int(i)
            except ValueError:
                return False
    return True

def str_to_int(sentence):
    """Returns spelled-out numbers as integers.
return_int: Return an integer rather than a string."""

    number_conversion_table = {

        'negative': '0',
        '': '0',
        'and': '0',
        'dollars': '0',
        'dollar': '0',
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10',
        'eleven': '11',
        'twelve': '12',
        'thirteen': '13',
        'fourteen': '14',
        'fifteen': '15',
        'sixteen': '16',
        'seventeen': '17',
        'eighteen': '18',
        'nineteen': '19',
        'twenty': '20',
        'thirty': '30',
        'forty': '40',
        'fifty': '50',
        'sixty': '60',
        'seventy': '70',
        'eighty': '80',
        'ninety': '90',
        'hundred': '00',
        'thousand': '000',
        'k': '000',
        'grand': '000',
        'million': '000000',
        'billion': '000000000',
        'trillion': '000000000000',
        'quadrillion': '000000000000000',
        'quintillion': '000000000000000000',
        'sextillion': '000000000000000000000',
        'septillion': '000000000000000000000000',
        'octillion': '000000000000000000000000000',
        'nonillion': '000000000000000000000000000000',
        'decillion': '000000000000000000000000000000000',
        'undecillion': '000000000000000000000000000000000000',
        'duodecillion': '000000000000000000000000000000000000000',
        'tredecillion': '000000000000000000000000000000000000000000',
        'quattuordecillion': '000000000000000000000000000000000000000000000',
    }

    flags = ['hundred', 'thousand', 'grand', 'million', 'billion', 'trillion',
             'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion',
             'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion',
             'quattuordecillion', 'k']
    sub_flags = ['hundred']

    section = 0
    sections = []
    hundred_flag = False  # detected value 'hundred'
    negative_flag = False  # detected value 'negative'
    currency_flag = False  # detected value 'dollar'

    sentence = sentence.replace('-', ' ').split(' ')  # allow spaces and hyphens
    lowered_sentence = []

    for i in sentence:
        lowered_sentence.append(i.lower())

    sentence = lowered_sentence  # create list of words in lowercase

    for word in sentence:

        if word in ['point', 'dot']:
            raise FloatingPointError('Sentence must represent an integer.')

        while True:
            try:
                number = number_conversion_table[word]
                if word == 'negative':  # detect negative
                    negative_flag = True
                if word in ['dollar', 'dollars', 'k']:
                    currency_flag = True
                break
            except KeyError:
                print("{} is not a numerical word.".format(word))
                exit()

        if word in flags:
            section = str(section)
            section += number
            if word in sub_flags:
                hundred_flag = True

        else:
            section = int(section) + int(number)

        if word in flags and hundred_flag == False:
            sections.append(int(section))
            section = 0

        hundred_flag = False

    sections.append(int(section))

    output = sum(sections)

    if negative_flag:
        output = 0 - output

    if currency_flag:
        output = format(output, ',d')
        return '$' + output

    else:
        return output


def int_to_str(number):
    """Return integer as a spelled-out string."""

    if not str(number).isnumeric() and '-' not in str(number):
        raise ValueError('Input must be an integer')

    number = str(number)

    dollar_flag = False
    negative_flag = False

    while True:
        if number[0] == '$':
            dollar_flag = True
            number = number[1:]
        elif number[0] == '-':
            negative_flag = True
            number = number[1:]
        else:
            break

    number_conv_table = {

        '-': 'negative',
        '$': 'dollar',
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    number_conv_table_spec = {
        '0': 'zero',
        '1': 'zero',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety',
    }

    number_conv_table_ones = {
        '0': 'ten',
        '1': 'eleven',
        '2': 'twelve',
        '3': 'thirteen',
        '4': 'fourteen',
        '5': 'fifteen',
        '6': 'sixteen',
        '7': 'seventeen',
        '8': 'eighteen',
        '9': 'nineteen',
    }

    flags = ['hundred', 'thousand', 'million', 'billion', 'trillion',
             'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion',
             'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion',
             'quattuordecillion']

    output = []
    word = ''
    tens_flag = False

    if str(number) in number_conv_table:
        if negative_flag:
            return 'negative ' + number_conv_table[str(number)]
        else:
            return number_conv_table[str(number)]

    number = number[::-1]
    sectors = []

    for i in range(0, len(number), 3):
        sectors.append(number[i:i + 3][::-1])

    sectors.reverse()
    sector_place = len(sectors)

    if negative_flag:
        output.append('negative')

    for sector in sectors:

        hundred_flag = False

        if len(sector) == 3 and int(sector[0]) > 0:
            hundred_flag = True

        nums_place = len(sector)

        for num in sector:

            if nums_place == 1 and tens_flag:
                word = number_conv_table_ones[num]
                tens_flag = False

            elif nums_place == 2:

                if num == '1':
                    tens_flag = True
                else:
                    word = number_conv_table_spec[num]

            else:
                word = number_conv_table[num]

            if word != 'zero' and len(number) > 1 and not tens_flag:
                output.append(word)

            if hundred_flag:
                output.append('hundred')
                hundred_flag = False

            if sector_place > 1 and nums_place == 1 and sector is not '000':
                if (sector_place - 1) < 16:
                    output.append(flags[sector_place - 1])
                else:
                    raise ValueError('Input number too large.')

            nums_place -= 1

        sector_place -= 1

    if dollar_flag:
        output.append('dollars')

    return ' '.join(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            raw_num = sys.argv[1].replace(',', '')
            num = int(raw_num)
            print(int_to_str(num))
        except ValueError:
            sentence = str(sys.argv[1])
            print(str_to_int(sentence))
    else:
        print('USAGE: main.py "<string/integer>"')