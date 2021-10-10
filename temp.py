seasons_korean=['봄','여름','가을','겨울']
seasons_english=['spring','summer','autumn','winter']
season_hot_place=['walking','ocean','mountain','ski']
original_list=[]

for pair in zip(seasons_korean,seasons_english):
    print(pair)
    count=0
    original_dict={
        'season_korean' : pair[0],
        'season_english' : pair[1],
        'hot_place' : season_hot_place[count]
    }
    original_list.append(original_dict)
    
