
def lcs(X,Y): 
    ## Finding LCS Function starts here 
    m = len(X)                                        ## find the length of both paragraphs
    n = len(Y) 
    L = [[None]*(n+1) for i in range(m+1)]            ## using list compreshension for finding 'L'
    for i in range(m+1): 
        for j in range(n+1):                          ## loop over the paragraphs length
            if i == 0 or j == 0 : 
                L[i][j] = 0                           ## as nothing is common b/w them
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1               ## as we have common elements
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])  ## as we want longest so max()
    return L[m][n] 
    ## returns the result

  
  



