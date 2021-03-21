def caesar(displacement, file, encoding):
    file_text = ""
    with open(file, 'r', encoding=encoding) as f:
        for line in f.readlines():
            line_text = ""
            for element in line.strip():
                line_text += str(chr(ord(element) + int(displacement)))
            file_text += line_text + '\n'
    with open(file, 'w') as f:
        f.write(file_text)


if __name__ == "__main__":
    caesar(-2, 'test_file2.txt', 'cp1251')
