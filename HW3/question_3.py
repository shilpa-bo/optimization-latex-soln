import numpy as np

def h(x):
    x_1, x_2 = x
    return np.array([4+3*x_1+2*x_2, 1+2*x_1+3*x_2])

def zero_alg(x_0, step_size, iterations=10):
    x = x_0
    for k in range(iterations):
        print(f"Iteration {k}: x_{k} = {x}, h(x_{k}) = {h(x)}")
        x = x - step_size*h(x)
    return x
exp_x1 = -2
exp_x2 = 1
def zero_alg(x_0, step_size, iterations=10):
    x = x_0
    k = 0
    while True:
        prev_f_x = h(x)
        print(f"Iteration {k}: x_{k} = {x}, h(x_{k}) = {h(x)}")
        x = x - step_size*h(x)
        new_f_x = h(x)
        x_1, x_2 = x
        if np.linalg.norm(new_f_x) > np.linalg.norm(prev_f_x):
            print(f"Function increased at iteration {k}. Exiting.")
            print(f"{prev_f_x}, {new_f_x}")
            break
        if abs(exp_x1-x_1) < 0.01 and abs(exp_x2-x_2) < 0.01:
            break
        k += 1
    return x, k
iterations = 20
x_0 = np.array([0,0])
step_size = 1
x_final = zero_alg(x_0, step_size, iterations)
print(step_size)
print(f"Final x after {x_final[1]} iterations: {x_final[0]}")
