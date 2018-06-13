def generator_backwards(num: int):

    sequence = []
    control_sequence = []

    current = num;
    top = num;
    bottom = num - 1

    sequence.append([bottom])


    if num % 2 == 0:

        current = current + 1

        control_sequence.append(current)

        print(sequence)
        print(control_sequence)

        

    else:

        control_sequence.append(current)

        print(sequence)
        print(control_sequence)



