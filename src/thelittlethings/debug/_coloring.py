from colorama import Fore, Style, Back
from .. import to_string


def translate_color_codes(string: str, console=True):
    # Parse for [<Attribute>: <Value>, ...] patterns. Replaces colorama as logging colorama characters
    # to a file results in the escape characters being shown in unwanted ways.

    i = 0

    legal_attributes = {
        "fore": Fore,
        "foreground": Fore,
        "text": Fore,
        "color": Fore,
        "style": Style,
        "back": Back,
        "background": Back,
        "fill": Back,
    }

    while i < len(string):
        if string[i] == "[":
            i += 1
            if string[i] == "\\":
                string = string[:i] + string[i+1:]
            else:
                expression_start = i
                attribute_value_pairs = {}
                while True:
                    attribute = ""
                    try:
                        while string[i] != ":":
                            if string[i] == "]":
                                raise SyntaxError(f"In string \"{string}\": String colorization requires attribute and value. Syntax: [<Attribute>: <value>, ...]")
                            attribute += string[i]
                            i += 1

                        i += 1

                        while string[i] == " ":
                            i += 1
                        
                        value = ""
                        while string[i] != "]" and string[i] != " " and string[i] != ",":
                            value += string[i]
                            i += 1
                        
                        if value == "":
                            raise SyntaxError(f"In string \"{string}\": No value given.")
                        
                        attribute_value_pairs[attribute.lower()] = value

                        while string[i] == " ":
                            i += 1
                        
                        if string[i] != ",":
                            break
                        i += 1
                        while string[i] == " ":
                            i += 1
                    except IndexError as e:
                        raise SyntaxError(f"In string \"{string}\": \"[\" was not closed.") from e

                colorization_string = ""

                if console:
                    for key in attribute_value_pairs:
                        if key not in legal_attributes:
                            valid_attributes = to_string.list([f'"{attr.title()}"' for attr in list(legal_attributes)])
                            raise AttributeError(f"Attribute \"{key}\" not found. Valid attributes are {valid_attributes}")
                        try:
                            colorization_string += getattr(legal_attributes[key], attribute_value_pairs[key].upper())
                        except AttributeError as e:
                            valid_values = to_string.list([f'"{value.lower()}"' for value in dir(legal_attributes[key]) if not value.startswith("_")])
                            raise ValueError(f"Invalid value for {key.title()}: {attribute_value_pairs[key]}. Valid values are {valid_values}") from e

                string = string[:expression_start-1] + colorization_string + string[i+1:]
                i = expression_start + len(colorization_string) - 2
                
        i += 1
        
    return string