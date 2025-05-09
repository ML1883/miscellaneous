"""
Some simple string manipulation for Stata
"""

path_gvkeys_without_industry_code = ""

def multiplicationString(length):
    """Specifically returns a string we need. In this case geometric
    mean calculation with decreasing weight for later observations. This is 
    dependend on the length given. Length must be an integer."""
    
    assert type(length) == int, "Length is not an integer"
    multiplicationString = "excessReturn[_n-1]"
    
    for i in range(1,length):
        multiplicationString = multiplicationString + " + 0.7937^" + str(i)\
        + " * excessReturn[_n-" + str(i+1) + "]"
    
    print(multiplicationString)

    
def rollingRegressionString(lagVal):
    """Specifically returns a string we need. Depending on the
    amount of lags needed. Lags must be an integer."""
    
    assert type(lagVal) == int, "Length is not an integer"
    
    rollingRegStr = "quietly logit generalDEF l" + str(lagVal) + ".LTMTA_w l"\
    + str(lagVal) + ".LCTAT_w l" + str(lagVal) +\
    ".NIMTA_w l" + str(lagVal) + ".priceLogTrunc l" + str(lagVal) + ".stockSigma_w l"\
    + str(lagVal) + ".MB_w l" + str(lagVal) + ".excessRetMean_w l"\
    + str(lagVal) + ".DD_w l" + str(lagVal) +\
    ".ASVI if monthDate >=`i' & monthDate <= `i' + 36, vce(cluster gind)"

    print(rollingRegStr)

    
def dropStringIndustryCodesMiss():
    """Gives a drop list for stata so that all of the firms without an industry
    code can be deleted"""
    with open(path_gvkeys_without_industry_code) as gvkeyFile:
        gvKeylist = gvkeyFile.readlines()

    gvKeylist = list(map(lambda s: s.strip(),gvKeylist))
    dropList = "drop if gvkey == "
    
    for i in range(0, len(gvKeylist)):
        dropList += gvKeylist[i] + " | gvkey == "
    print(dropList)

    
def outregString(lagVal):
    """Specifically returns a string we need. Depending on the
    amount of lags needed. Lags must be an integer."""
    
    assert type(lagVal) == int, "Length is not an integer"
    
    outregString = "logit generalDEF l" + str(lagVal) + ".LTMTA_w l"\
    + str(lagVal) + ".LCTAT_w l" + str(lagVal) +\
    ".NIMTA_w l" + str(lagVal) + ".priceLogTrunc l" + str(lagVal) + ".stockSigma_w l"\
    + str(lagVal) + ".MB_w l" + str(lagVal) + ".excessRetMean_w l"\
    + str(lagVal) + ".DD_w l" + str(lagVal) +\
    ".CSC16min10, vce(cluster gind)"
    
    print(outregString)
