import numpy as np

def main():
    training_data = np.genfromtxt("data.csv", delimiter = ',')
    # taking initial value of gradient and y-intercept of our line to be 0
    initial_m = 0
    initial_b = 0

    learning_rate = 0.0004
    training_iterations = 10000
    print("Before training the error was {0}" .format(mean_squared_error(training_data, initial_m, initial_b)))
    [m, b] = gradient_descent(training_data, training_iterations, learning_rate, initial_m, initial_b)
    print("After tarining the error is {0}" .format(mean_squared_error(training_data, m, b)))

def mean_squared_error(data, m, b):
    N = len(data)
    error = 0
    for i in range (N):
        #extracting the x value of each data point
        x = data[i, 0]
        #extracting the y value of each data point
        y = data[i, 1]

        error += (y - (m*x + b)) ** 2

    return np.float(error/N)

def gradient_descent(data, training_iterations, learning_rate, initial_m, initial_b):
    b = initial_b
    m = initial_m

    for i in range (training_iterations):
        m, b = step_gradient(m, b, data, learning_rate)

    return [m, b]

def step_gradient(m, b, data, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = len(data)
    for i in range (N):
        x = data[i, 0]
        y = data[i, 1]

        b_gradient += -(2/N) * (y - (m*x + b))
        m_gradient += -(2/N) * x * (y - (m*x + b))

    new_m = m - learning_rate * m_gradient
    new_b = b - learning_rate * b_gradient

    return [new_m, new_b]

if __name__ == "__main__":
    main()
