def main():
    fileName= raw_input('Please enter the file name: ')

    validate_file(fileName)
    new_lines = convert_file(fileName)
    for line in new_lines:
        print line

def validate_file(fileName):
    try:
        inputFile= open(fileName, 'r')
        inputFile.close()
    except IOError:
        print('File not found.')

def strip_punctuation(line):
    punctuation = ''
    line = line.strip()
    if len(line)>0:
        if line[-1] in ('.','!','?'):
            punctuation = line[-1]
            line = line[:-1]
    return line, punctuation

def convert_file(fileName):
    inputFile= open(fileName, 'r')
    converted_lines = []
    for line in inputFile:
        line, punctuation = strip_punctuation(line)
        line = line.split()
        new_words = []
        for word in line:
            endString= str(word[1:])
            them=endString, str(word[0:1]), 'ay'
            new_word="".join(them)
            new_words.append(new_word)
        new_sentence = ' '.join(new_words)
        new_sentence = new_sentence.lower()
        if len(new_sentence):
            new_sentence = new_sentence[0].upper() + new_sentence[1:]
        converted_lines.append(new_sentence + punctuation)
    return converted_lines
