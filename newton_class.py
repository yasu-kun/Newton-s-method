import sympy as sym
from sympy import sympify
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Newton(object):
    def __init__(self, function):
        self.x = sym.Symbol('x')
        self.function = sympify(function)
        self.y_plot = sym.lambdify(self.x, sympify(function), "numpy")



    def solve(self,seed,iteration=10,verbose=0):
        function = self.function
        x = self.x
        y_plot = self.y_plot

        def cal_diff(diff_function):
            diff_function = sym.diff(diff_function)
            return diff_function
        ims = []
        for n_iter in range(1,iteration):
            if n_iter == 1:
                Xn_1 = float(seed - function.subs(x,seed) / cal_diff(function).subs(x,seed))
                #---------PLOT----------
                x_r = np.arange(-10, 10, 0.001)
                y_plot = y_plot(x_r)

                y_a = cal_diff(function).subs(x, seed)
                y_y = (-y_a*seed) + function.subs(x, seed)

                y_2 = y_a*x_r + y_y
                y_3 = 0

                idx = np.argwhere(np.diff(np.sign(y_2 - y_3)))
                fig = plt.figure()
                # スケールを指定
                plt.xlim(-10,10)
                plt.ylim(-10,10)
                #X,Yが0の線
                plt.axhline(0, color='black')
                plt.axvline(0, color='black')
                plt.xlabel("x")
                plt.ylabel("y")
                plt.plot(x_r,y_plot,'b')
                line1 = plt.plot(x_r,y_2,color="red")
                line2 = plt.plot(x_r[idx], y_2[idx], 'ko')
                ims.append(line1+line2)
                #plt.show()

                if verbose==1:
                    print("-----ITERATION #{}-----".format(n_iter))
                    print("X = {}".format(Xn_1))

                    print("ERROR = {}".format(abs(seed - Xn_1)))
                else:
                    pass
            else:
                Xn = Xn_1
                Xn_1 = float(Xn - function.subs(x,Xn) / cal_diff(function).subs(x,Xn))
                #---------PLOT----------
                #x_r = np.arange(-10, 10, 0.1)
                #y_plot = y_plot(x_r)

                y_a = cal_diff(function).subs(x, Xn_1)
                y_y = (-y_a*Xn_1) + function.subs(x, Xn_1)

                y_2 = y_a*x_r + y_y
                y_3 = 0

                idx = np.argwhere(np.diff(np.sign(y_2 - y_3))).flatten()

                # スケールを指定
                plt.xlim(-10,10)
                plt.ylim(-10,10)
                #X,Yが0の線
                plt.axhline(0, color='black')
                plt.axvline(0, color='black')
                plt.xlabel("x")
                plt.ylabel("y")
                plt.plot(x_r,y_plot,'b')
                line1 = plt.plot(x_r,y_2,color="red")
                #print(x_r[idx], y_2[idx])
                line2 = plt.plot(x_r[idx], y_2[idx], 'ko')
                ims.append(line1+line2)
                #plt.show()
                if verbose==1:
                    print("-----ITERATION #{}-----".format(n_iter))
                    print("X = {}".format(Xn_1))

                    print("ERROR = {}".format(abs(Xn - Xn_1)))
                else:
                    pass



        ani = animation.ArtistAnimation(fig, ims, interval=500, repeat=True)
        ani.save('anim.gif', writer="pillow")
        plt.show()
        return Xn_1, abs(Xn - Xn_1)

def run():
    y = input('input: ')
    newton = Newton(function=y)
    x,e = newton.solve(iteration=7,seed=10,verbose=1)
    print(x,e)

if __name__ == "__main__":
    run()
