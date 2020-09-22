#!/usr/bin/env python
import copy
from .pyOpt_optimization import Optimization


class Solution(Optimization):
    def __init__(self, optProb, optTime, optInform):
        """
        This class is used to describe the solution of an optimization
        problem. This class inherits from Optimization which enables a
        solution to be used as an input to a subsequent optimization problem.

        Parameters
        ----------
        optProb : Optimization problem class
            Optimization problem used to create solution

        optTime : float
            Time required for the optimization

        optInform : int
            The inform code from the optimization.
        """

        Optimization.__init__(self, optProb.name, None)

        # Copy over the variables, constraints, and objectives
        self.variables = copy.deepcopy(optProb.variables)
        self.constraints = copy.deepcopy(optProb.constraints)
        self.objectives = copy.deepcopy(optProb.objectives)
        self.optTime = optTime
        self.optInform = optInform

    def __str__(self):
        """
        Print Structured Solution
        """
        text0 = Optimization.__str__(self)
        text1 = ""
        lines = text0.split("\n")
        lines[1] = lines[1][len("Optimization Problem -- ") :]
        for i in range(5):
            text1 += f"{lines[i]}\n"

        text1 += "\n    Solution: \n"
        text1 += f"{'-' * 80}\n"
        text1 += f"    Total Time: {self.optTime:25.4f}\n"
        text1 += f"       User Objective Time :   {self.userObjTime:10.4f}\n"
        text1 += f"       User Sensitivity Time : {self.userSensTime:10.4f}\n"
        if hasattr(self, "userJProdTime"):
            text1 += f"       User J-Product Time :   {self.userJProdTime:10.4f}\n"
            text1 += f"       User J^T-Product Time : {self.userJTProdTime:10.4f}\n"
        text1 += f"       Interface Time :        {self.interfaceTime:10.4f}\n"
        text1 += f"       Opt Solver Time:        {self.optCodeTime:10.4f}\n"
        text1 += f"    Calls to Objective Function : {int(self.userObjCalls):7}\n"
        text1 += f"    Calls to Sens Function :      {int(self.userSensCalls):7}\n"
        if hasattr(self, "userJProdCalls"):
            text1 += f"    Calls to JProd Function :     {int(self.userJProdCalls):7}\n"
            text1 += f"    Calls to JTProd Function :    {int(self.userJTProdCalls):7}\n"

        for i in range(5, len(lines)):
            text1 += f"{lines[i]}\n"

        text1 += f"{'-' * 80}\n"

        return text1
