def booth_algorithm(multiplicand, multiplier):
    n = len(multiplier)
    m = len(multiplicand)
    
    # Initialize variables
    A = '0' * (m + 1)
    Q = multiplicand + '0'
    Q_ = '0' * (m + 1)
    M = multiplier + '0' * m

    for i in range(n):
        if Q[-1] == '0' and Q[-2] == '1':
            A = bin_addition(A, M)
        elif Q[-1] == '1' and Q[-2] == '0':
            A = bin_addition(A, bin_negation(M))

        # Right shift A and Q
        A = A[:-1]
        Q = Q[:-1]
        Q = Q_[-1] + Q

    return Q + A

def bin_addition(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    carry = 0
    result = ''

    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        sum_ = bit1 + bit2 + carry
        result = str(sum_ % 2) + result
        carry = sum_ // 2

    return result

def bin_negation(binary):
    negated = ''
    for bit in binary:
        negated += '0' if bit == '1' else '1'
    return negated

if __name__ == "__main__":
    multiplicand = '1011'  # Replace with your multiplicand in binary
    multiplier = '1101'    # Replace with your multiplier in binary

    result = booth_algorithm(multiplicand, multiplier)
    print("Binary result: " + result)
