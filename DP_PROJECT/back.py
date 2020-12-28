
def lcs(X,Y): 
    ## Finding LCS Function starts here 
    lenght_X = len(X)                                                              ## find the length of both paragraphs as len(X),len(Y)
    lenght_Y= len(Y) 
    List_res= [[None]*(lenght_Y+1) for i in range(lenght_X+1)]                     ## using list compreshension for finding 'List_res'
    
    for i in range(length_X+1): 
        for j in range(lenght_Y+1):                                                ## loop over the paragraphs length
            if i == 0 or j == 0 : 
                List_res[i][j] = 0                                                 ## as nothing is common b/w them
            elif X[i-1] == Y[j-1]: 
                List_res[i][j] = List_res[i-1][j-1]+1                              ## as we have common elements
            else: 
                List_res[i][j] = max(List_res[i-1][j] , List_res[i][j-1])          ## as we want longest so max() is being used 
    return List_res[length_X][length_N] 
    ## returns the result

  
  



