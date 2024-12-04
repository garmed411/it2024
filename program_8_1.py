def generate_password(g):


    try:
        g_str = str(g)
        if len(g_str) != 7:
            return "WRONG"


        modified_g = g_str + g_str[0]


        reversed_number = modified_g[::-1]


        mapping = {
            '0': 'O',
            '1': 'I',
            '2': 'Z',
            '3': 'E',
            '4': '!',
            '5': 'S',
            '6': 'b',
            '7': 'J',
            '8': '#',
            '9': 'P'
        }
        password = "".join([mapping[digit] for digit in reversed_number])

        return password
    except (ValueError, KeyError):
        return "WRONG"



try:
    input_number = int(input())
    print(generate_password(input_number))
except ValueError:
    print("WRONG")


