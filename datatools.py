import numpy as np

def gradient_descent(gradient_fn, init_val, learning_rate = .01,
    precision = .000001, max_steps = 100000, 
    rate_change = 1, rate_change_every = None, ascent = False):
    #store parameters as array
    x = init_val
    if type(x) == int:
        x = [x]
    x = np.array(x)
    step_size = 1
    steps = 0
    while step_size > precision and steps < max_steps:
        prev_x = x
        x = x + (1 if ascent else -1) * learning_rate * gradient_fn(prev_x)
        step_size = max(abs(x - prev_x))
        steps += 1
        if rate_change_every is not None and steps % rate_change_every == 0:
            learning_rate *= rate_change
    print('Steps:', steps)
    print('Minimum at:', x)
    return(x)