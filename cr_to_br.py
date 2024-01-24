def replace_line_breaks_with_br(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    content_with_br = content.replace('\n', '<br />')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(content_with_br)

replace_line_breaks_with_br('input.txt', 'output.txt')
