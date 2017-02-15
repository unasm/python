import pandas as pd
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
path = "/Users/tianyi/project/pydata-book/ch02/movielens/users.dat"
users = pd.read_table(path, sep = '::', header = None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
rpath = "/Users/tianyi/project/pydata-book/ch02/movielens/ratings.dat"
ratings = pd.read_table(rpath, sep = '::', header = None, names = rnames)

mnames = ['movie_id', 'title', 'genres']
mpath = "/Users/tianyi/project/pydata-book/ch02/movielens/movies.dat"
movies = pd.read_table(mpath, sep = '::', header = None, names = mnames)

#print users[: 5]
#print movies[: 5]

data = pd.merge(pd.merge(users, ratings), movies)

ratings_by_title = data.groupby('title').size()
#print ratings_by_title
active_title = ratings_by_title.index[ratings_by_title >= 250]

#print active_title[0]
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc = 'mean')
mean_ratings = mean_ratings.ix[active_title]
#top_female_ratings = mean_ratings.sort_index(by = 'F', ascending = False)
#print top_female_ratings[: 10]
#print mean_ratings[: 5]
#print data

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sort_by_diff = mean_ratings.sort_index(by = 'diff')
print sort_by_diff[: 15]
