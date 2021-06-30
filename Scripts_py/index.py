def phone_number_code():
        Read_data = open('input.txt', 'r')
        Write_data = open('output.txt', 'a')
        for text_line in Read_data.readlines():
            format_text_line = '+7' + text_line
            Write_data.write(format_text_line)
        Write_data.close()

phone_number_code()