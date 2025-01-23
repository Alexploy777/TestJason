def encode_decoder(input_string):
    output_string = ''
    if isinstance(input_string, str):
        for symbol in input_string:
            # Проверяем, является ли latin1
            try:
                decoded_symbol = symbol.encode('latin1').decode('cp1251')
            except UnicodeEncodeError:
                decoded_symbol = '' + symbol
            output_string += decoded_symbol
        return output_string
    else:
        return input_string