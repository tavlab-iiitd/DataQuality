from smith_waterman import smith_waterman as sw
import textdistance
class String_matching:
    def lcs(X,Y): 
        m = len(X) 
        n = len(Y) 

        L = [[None]*(n+1) for i in range(m+1)] 

        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0 : 
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]: 
                    L[i][j] = L[i-1][j-1]+1
                else: 
                    L[i][j] = max(L[i-1][j] , L[i][j-1]) 
        return L[m][n]/(max(len(X),len(Y)))
    
    def iterative_levenshtein(s, t):
        rows = len(s)+1
        cols = len(t)+1
        dist = [[0 for x in range(cols)] for x in range(rows)]

        for i in range(1, rows):
            dist[i][0] = i

        for i in range(1, cols):
            dist[0][i] = i
            
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0
                else:
                    cost = 1
                dist[row][col] = min(dist[row-1][col] + 1,dist[row][col-1] + 1,dist[row-1][col-1] + cost) 
        
        return dist[row][col]/(max(len(s),len(t)))

    def hamming_distance(string1, string2):
        try:
            distance = 0
            L = len(string1)
            for i in range(L):
                if string1[i] != string2[i]:
                    distance += 1
            return distance/(max(len(string1),len(string2)))
        except:
            return textdistance.hamming.normalized_similarity(string1,string2)
    
    def smith_waterman(string1,string2):
        return textdistance.smith_waterman.normalized_similarity(string1,string2)
    
    def jaro_winkler(string1,string2):
        return textdistance.jaro_winkler.normalized_similarity(string1,string2)
    
    def Strcmp95(string1,string2):
        return textdistance.strcmp95.normalized_similarity(string1,string2)
    
    def Needleman_wunsch(string1,string2):
        return textdistance.needleman_wunsch.normalized_similarity(string1,string2)

    def gotoh(string1,string2):
        return textdistance.gotoh.normalized_similarity(string1,string2)
    
    def jaccard(string1,string2):
        return textdistance.jaccard.normalized_similarity(string1,string2)
    
    def sorensen_dice(string1,string2):
        return textdistance.sorensen_dice.normalized_similarity(string1,string2)
    
    def tversky(string1,string2):
        return textdistance.tversky.normalized_similarity(string1,string2)
    
    def overlap(string1,string2):
        return textdistance.overlap.normalized_similarity(string1,string2)
    
    def tanimoto(string1,string2):
        return textdistance.tanimoto.normalized_similarity(string1,string2)
    
    def cosine(string1,string2):
            return textdistance.cosine.normalized_similarity(string1,string2)
    
    def mra(string1,string2):
            return textdistance.mra.normalized_similarity(string1,string2)
    
    def editex(string1,string2):
            return textdistance.editex.normalized_similarity(string1,string2)