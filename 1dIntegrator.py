import math

def product_integrator_one_minus(x1, x2, f, steps):
    stepSize = (x2-x1)/steps
    result = 0
    for i in range(steps-1):
        cassi_1 = x1+i*stepSize
        cassi_2 = x1+(i+1)*stepSize
        result += (((1-cassi_1)*f(cassi_1)+(1-cassi_2)*f(cassi_2))/2)*stepSize
    return result


def product_integrator(x1, x2, f, steps):
    stepSize = (x2-x1)/steps
    result = 0
    for i in range(steps-1):
        cassi_1 = x1+i*stepSize
        cassi_2 = x1+(i+1)*stepSize
        result += ((cassi_1*f(cassi_1)+cassi_2*f(cassi_2))/2)*stepSize
    return result

# u(0) = alpha, u(1) = beta, f(x) = function, steps
def u_of_x(x, f, alpha, beta, steps):
    steps1 = int(round(x*steps))
    steps2 = int(round((1-x)*steps))
    result = (1-x)*product_integrator(0, x, f, steps1) + x*product_integrator_one_minus(x, 1, f, steps2) + (1-x)*alpha + x*beta
    return result

def f1(x):
    return x

print(u_of_x(.5, f1, 0, 0, 50))
#print(product_integrator(0, 1, f1, 10))
