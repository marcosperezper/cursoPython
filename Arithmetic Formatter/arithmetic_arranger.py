def arithmetic_arranger(problems, do_maths=False):
    numerator = ''
    denominator = ''
    results = ''
    dashes = ''
    # if problems is greater than 5 throw an error
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # split problems into parts
    for x in problems:
        y = (x.split(' '))
        first_num = y[0]
        operator = y[1]
        second_num = y[2]
        # Check the numers are four digits or less
        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # Check the operands are numbers
        if not first_num.isnumeric() or not second_num.isnumeric():
            return 'Error: Numbers must only contain digits.'
        # Check if operator is + or -
        if (operator == '+' or operator == '-'):
            if operator == "+":
                sums = str(int(first_num) + int(second_num))
            else:
                sums = str(int(first_num) - int(second_num))

             # Set the lenght of rows
            length = max(len(first_num), len(second_num)) + 2
            top = str(first_num).rjust(length)
            bottom = operator + str(second_num).rjust(length - 1)
            dash = ''
            res = str(sums).rjust(length)
            for d in range(length):
                dashes += '-'
           # Creating the string
            if x != problems [-1]:
                numerator += top + '    '
                denominator += bottom + '    '
                dashes += dash + '    '
                results += res + '    '
            else:
                numerator += top
                denominator += bottom
                dash += dash
                results += res
        else:
            return "Error: Operator must be '+' or '-'."

    # strip out spaces to the right of the string
    numerator.rstrip()
    denominator.rstrip()
    dashes.rstrip()
    if do_maths:
        results.rstrip()
        arranged_problems = numerator + '\n' + denominator + '\n' + dashes + '\n' + results
    else:
        arranged_problems = numerator + '\n' + denominator + '\n' + dashes
    return arranged_problems