import matplotlib.pyplot as plt
import math


def start_temperature_input():
    return 100
    # return int(input("Enter starting temperature: "))


def simple_euler(T0, Tenv, k, tend, h): # Numerical integration method

    def f(t, T):
        return -k*(T-Tenv)

    T = T0  # T_0
    t = 0
    i = 0
    result = []

    st = int(1/h)

    while (t <= tend):
        if i % st == 0:
            result.append(T)    # T(t_i)

        dT = f(t, T)*h  # f(t_i, T(t_i))
        T = T + dT    # T(t_{i+1})
        i = i + 1
        t = t + h     # t=t_0+h*i

    return result  # Values of the function T(t)

def kettle_solution(T0,Tenv,k,tend):
    l=[]
    for t in range(tend+1):
        T=(T0-Tenv) * math.exp(-k*t)+Tenv
        l.append(T)
    return l

def output_as_table(series):
    print("Time series is following:")
    t = 0
    for x in series:
        print("{:2} {}".format(t, x))
        t = t + 1


def plot_function(series1,series2):
    plt.plot(series1)
    plt.plot(series2)
    plt.show()

def plot_difference(s1,s2):
    
    # assert len(s1)==len(s2)
    l1 = len(s1)
    l2 = len(s2)
    
    d=[]
    for i in range(min(l1,l2)):
        d.append(s1[i]-s2[i])

    plt.plot(d)
    plt.show()

def main():
    print("Calculating temperature of a kettle in time")
    T0 = start_temperature_input()
    
    # T(t), t\in[0,tend]
    Tenv = 24
    h = 1
    tend = 60
    k = 0.1
    Tnum  = simple_euler(T0, Tenv=Tenv, h=h, tend=tend, k=k)
    Tprec = kettle_solution(T0, Tenv=Tenv, tend=tend, k=k)
    # plot_function(Tnum,Tprec)
    plot_difference(Tnum,Tprec)

main()
quit()
