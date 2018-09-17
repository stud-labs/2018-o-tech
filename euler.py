import matplotlib.pyplot as plt

def input_data():
    return 100

def process_data(T0, Tenv, k, tend, h):
    
    def f(t,T):
        return -k*(T-Tenv)
    
    T = T0 # T_0
    t = 0
    i = 0
    result = []
    
    st = int(1/h)
    
    while (t<=tend):
        if i % st == 0:
            result.append(T)    # T(t_i)
            
        dT= f(t, T)*h # f(t_i, T(t_i))
        T = T + dT    # T(t_{i+1})
        i = i + 1
        t = t + h     # t=t_0+h*i
        
        
    return result # Values of the function T(t)

def output_as_table(series):
    print("Time series is following:")
    t = 0
    for x in series:
        print("{:2} {}".format(t,x))
        t = t + 1

def output_as_graphicx(series):
    plt.plot(series)
    plt.show()

def main():
    print("Calculating temperature of a kettle in time")
    T0=input_data()
    r=process_data(T0, Tenv=24, h=0.01, tend=60, k=0.1)
    output_as_graphicx(r)

main()
quit()
