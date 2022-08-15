#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import numpy as np
# import pyre library
from pyre import *


import time
import datetime
start_time = time.time()

p_fac=np.array([0.5,0.6,0.7,0.8])

def limitstatefunction_1(X1, X2):
    """
    example limit state function
    """
    x=X2*p_fac[0]
    return  (0.693*(np.sqrt(X1))) - ((x*1000*976)/(150*150**2))

def limitstatefunction_2(X1, X2):
    """
    example limit state function
    """
    x=X2*p_fac[1]
    return  (0.693*(np.sqrt(X1))) - ((x*1000*976)/(150*150**2))

def limitstatefunction_3(X1, X2):
    """
    example limit state function
    """
    x=X2*p_fac[2]
    return  (0.693*(np.sqrt(X1))) - ((x*1000*976)/(150*150**2))

def limitstatefunction_4(X1, X2):
    """
    example limit state function
    """
    x=X2*p_fac[3]
    return  (0.693*(np.sqrt(X1))) - ((x*1000*976)/(150*150**2))
    
# Define a main() function.
def main():

    # Define limit state function
    # - case 1: define directly as lambda function
    #limit_state = LimitState(lambda X1,X2,X3: 1 - X2*(1000*X3)**(-1) - (X1*(200*X3)**(-1))**2)
    # - case 2: use predefined function
    limit_state1 = LimitState(limitstatefunction_1)
    limit_state2 = LimitState(limitstatefunction_2)
    limit_state3 = LimitState(limitstatefunction_3)
    limit_state4 = LimitState(limitstatefunction_4)

    # Set some options (optional)
    options = AnalysisOptions()
    # options.printResults(False)

    stochastic_model = StochasticModel()
    # Define random variables
    stochastic_model.addVariable(Normal('X1', 56.51, 3))
    stochastic_model.addVariable(Normal('X2', 21.32, 0.41))

    # If the random variables are correlatet, then define a correlation matrix,
    # else no correlatin matrix is needed
    #stochastic_model.setCorrelation(CorrelationMatrix([[1.0, 0.3, 0.2],
                                                      # [0.3, 1.0, 0.2],
                                                       #[0.2, 0.2, 1.0]]))

    # Perform FORM analysis
    Analysis1 = Form(analysis_options=options,
                    stochastic_model=stochastic_model, limit_state=limit_state1)
    Analysis2 = Form(analysis_options=options,
                    stochastic_model=stochastic_model, limit_state=limit_state2)
    Analysis3 = Form(analysis_options=options,
                    stochastic_model=stochastic_model, limit_state=limit_state3)
    Analysis4 = Form(analysis_options=options,
                    stochastic_model=stochastic_model, limit_state=limit_state4)
    # More detailed output
    Analysis1.showDetailedOutput()
    Analysis2.showDetailedOutput()
    Analysis3.showDetailedOutput()
    Analysis4.showDetailedOutput()
    
    # Perform SORM analysis, passing FORM result if it exists
    sorm1 = Sorm(analysis_options=options,stochastic_model=stochastic_model, 
                limit_state=limit_state1, form=Analysis1)
    sorm2 = Sorm(analysis_options=options,stochastic_model=stochastic_model, 
                limit_state=limit_state2, form=Analysis2)
    sorm3 = Sorm(analysis_options=options,stochastic_model=stochastic_model, 
                limit_state=limit_state3, form=Analysis3)
    sorm4 = Sorm(analysis_options=options,stochastic_model=stochastic_model, 
                limit_state=limit_state4, form=Analysis4)
    sorm1.run()
    sorm2.run()
    sorm3.run()
    sorm4.run()

    # Perform Distribution analysis
    Analysis1 = DistributionAnalysis(
        analysis_options=options, stochastic_model=stochastic_model, limit_state=limit_state1)
    Analysis2 = DistributionAnalysis(
        analysis_options=options, stochastic_model=stochastic_model, limit_state=limit_state2)
    Analysis3 = DistributionAnalysis(
        analysis_options=options, stochastic_model=stochastic_model, limit_state=limit_state3)
    Analysis4 = DistributionAnalysis(
        analysis_options=options, stochastic_model=stochastic_model, limit_state=limit_state4)

    # Detailed output
    sorm1.showDetailedOutput()
    sorm2.showDetailedOutput()
    sorm3.showDetailedOutput()
    sorm4.showDetailedOutput()

    # This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
