import numpy as np

class FrenselEquation():

    def __init__(self, theta_i, theta_t, n1, n2):
        self.theta_i = theta_i
        self.theta_t = theta_t
        self.n1 = n1
        self.n2 = n2

    def r_s(self):

        self.rs = self.n1 * np.cos(self.theta_i) - self.n2 * np.cos(self.theta_t) / self.n1 * np.cos(self.theta_i) + self.n2 * np.cos(self.theta_t)

        return self.rs

    def t_s(self):

        self.ts = 2 * n1 * np.cos(self.theta_t) / self.n1 * np.cos(self.theta_i) + self.n2 * np.cos(self.theta_t)

        return self.ts

    def r_p(self):

        self.rp = self.n1 * np.cos(self.theta_t) - self.n2 * np.cos(self.theta_i) / self.n1 * np.cos(self.theta_i) + self.n2 * np.cos(self.theta_t)

        return self.rp

    def t_p(self):

        self.ts = 2 * n1 * np.cos(theta_i) / self.n2 * np.cos(self.theta_i) + self.n1 * np.cos(self.theta_t)

        return self.tp


