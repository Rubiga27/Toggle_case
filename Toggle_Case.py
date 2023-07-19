def toggle_case(A):
    toggled_string = ""
    for char in A:
        if 97 <= ord(char) <= 122:
            toggled_string += chr(ord(char) - 32)
        elif 65 <= ord(char) <= 90:
            toggled_string += chr(ord(char) + 32)
        else:
            toggled_string += char

    return toggled_string
A = input("")
print(toggle_case(A))

"""
Input 1:
A = "Hello"

Input 2:
A = "tHiSiSaStRiNg"

Output 1:
hELLO

Output 2:
ThIsIsAsTrInG 
"""
