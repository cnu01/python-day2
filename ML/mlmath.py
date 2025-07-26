

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length.")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must match number of rows in B.")
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result


def conditional_probability(events):
    p_a_and_b = events.get("P(A and B)")
    p_b = events.get("P(B)")
    
    if p_b == 0:
        raise ZeroDivisionError("P(B) cannot be zero.")
    if p_a_and_b is None or p_b is None:
        raise KeyError("Missing required keys: 'P(A and B)' and 'P(B)'")
    
    return p_a_and_b / p_b
