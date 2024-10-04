def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

string_informada = input("Informe uma string para inverter: ")
string_invertida = inverter_string(string_informada)
print("String invertida: ", string_invertida)