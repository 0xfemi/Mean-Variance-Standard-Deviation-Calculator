import numpy as np

def calculate(*args):
    if len(args) != 9:
        raise ValueError("Must provide exactly 9 numbers.")

    # Reshape into 3x3 numpy array
    matrix = np.array(args).reshape(3, 3)

    # Helper function to compute stats
    def stats(func):
        return [
            func(matrix, axis=0).tolist(),  # axis1 → columns
            func(matrix, axis=1).tolist(),  # axis2 → rows
            func(matrix).tolist()           # flattened
        ]

    # Build dictionary
    calculations = {
        'mean': stats(np.mean),
        'variance': stats(np.var),
        'standard deviation': stats(np.std),
        'max': stats(np.max),
        'min': stats(np.min),
        'sum': stats(np.sum)
    }

    return calculations
print(calculate(0,1,2,3,4,5,6,7,8))