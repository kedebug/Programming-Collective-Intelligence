# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                       'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
                       'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
                            'You, Me and Dupree': 3.5}, 
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                              'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0, 
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0}, 
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

def sim_distance(prefs, person1, person2):
    similarity = {}   
    
    for it in prefs[person1]:
        if it in prefs[person2]:
            similarity[it] = 1   
            
    if len(similarity) == 0: return 0  
    
    sum_of_sequares = sum([pow(prefs[person1][it] - prefs[person2][it], 2)
                           for it in similarity]) 
     
    return 1 / (1 + sum_of_sequares)

# http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
def sim_pearson(prefs, person1, person2):
    similarity = {}
    
    for it in prefs[person1]:
        if it in prefs[person2]:
            similarity[it] = 1
    
    n = len(similarity)
    if n == 0: return 0

    sum1 = sum([prefs[person1][it] for it in similarity])
    sum2 = sum([prefs[person2][it] for it in similarity])
    
    sum1_square = sum([pow(prefs[person1][it], 2) for it in similarity])
    sum2_square = sum([pow(prefs[person2][it], 2) for it in similarity])
    
    person_sum = sum([prefs[person1][it] * prefs[person2][it] for it in similarity])
    
    num = person_sum - (sum1 * sum2) / n
    den = sqrt((sum1_square - pow(sum1, 2)/n) * (sum2_square - pow(sum2, 2) / n))
     
    if den == 0: return 0
    
    return num / den

def main():
    person1 = 'Lisa Rose'
    person2 = 'Gene Seymour'
    print sim_pearson(critics, person1, person2)
    
if __name__ == '__main__':
    main()    
    