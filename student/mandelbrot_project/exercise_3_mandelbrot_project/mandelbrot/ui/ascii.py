def mandelbrot_ascii(escape_times,multiplier=3):
    translation_table = [' ', '.', ':', 'o', 'O', '0', 'H', 'X', '#']
    mandel_ascii = ''
    for row in escape_times:
        for el in row:
            idx = min(el+1, len(translation_table)-1)
            mandel_ascii += translation_table[idx] * 3
        mandel_ascii += '\n'
    print mandel_ascii