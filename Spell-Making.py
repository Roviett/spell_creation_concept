def component_count():
    communicating = True
    text = "INVALID COMPONENT COUNT"
    
    while communicating:
        try:
            component_input = int(input("Enter a Number of Components: "))
            if component_input <= 0:
                raise ValueError
        except ValueError:
            print(f"\n\n{text}\n{"-" * len(text)}\n")
        else:
            communicating = False

    return component_input

def communication_gather(count):
    limit_list = "ABCDEF"
    factor_list = []

    for i in range(count):
        seeking = True
        while seeking:
            try:
                caster_input = input(f"Please Enter Spell Factor {i+1}: ")
                if caster_input.isalnum():
                    if caster_input.isalpha():
                        caster_input = caster_input.upper()
                        if caster_input in limit_list:
                            factor_list.append(caster_input)
                            seeking = False
                        else:
                            raise ValueError
                    else:
                        caster_input = int(caster_input)
                        if caster_input > 9:
                            raise ValueError
                        else:
                            factor_list.append(caster_input)
                            seeking = False
                else:
                    raise ValueError
            except ValueError:
                print("\nFailed\n")
                pass
            

    return factor_list

def gather_interpret(value_list):
    spell = {}

    for index in range(len(value_list)):
        item = value_list[index]
        position = index
        if position == len(value_list ) - 1 and len(value_list) != 1:
            position = "Last"
        if len(value_list) == 1:
            position = "Middle"

        encoding = spell_encode(item, position)

        if index == 0:
            prefix = encoding
        elif index == len(value_list) -1:
            form = encoding
        else:
            if encoding in spell.keys():
                spell[encoding] += 1
            else:
                spell[encoding] = 1

    print("\n" + prefix)
    for key, item in spell.items():
        print(f"{key} x{item}")
    try:
        print(form)
    except UnboundLocalError:
        pass

def spell_encode(value, index):
    if index == 0:
        target_key = "First"
    elif index == "Last":
        target_key = "Last"
    else:
        target_key = "Middle"
    
    if value == 1:
        spell_dict = {"First": "Big",
                       "Middle": "Fire",
                       "Last": "Ball"}
        return spell_dict[target_key]

    if value == 2:
        spell_dict = {"First": "Long",
                       "Middle": "Frost",
                       "Last": "Storm"}
        return spell_dict[target_key]

def main():
    length = component_count()
    data = communication_gather(length)
    gather_interpret(data)

main()
exit_text = "Press Enter to end Program"
exit_prompt = input(f"\n{exit_text}\n{'-' * len(exit_text)}")


