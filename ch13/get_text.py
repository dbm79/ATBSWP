# get_text.px

import docx


def get_text(filename):
    ''' This function will get all of the text from a .docx file and print it. '''

    doc = docx.Document(filename)
    full_text = []

    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)

    return '\n'.join(full_text)


def main():
    ''' This is the main function of the program. '''

    print(get_text('demo.docx'))


if __name__ == '__main__':
    main()
