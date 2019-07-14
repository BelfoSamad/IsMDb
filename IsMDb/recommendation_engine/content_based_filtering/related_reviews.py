from IsMDb.utils import convert_to_dataframe, non_duplicated_words
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_related(qs, title):
    df = convert_to_dataframe(qs, fields=['title', 'genre', 'tags'])

    # prepare genres
    df['words'] = ''
    for index, row in df.iterrows():
        row['tags'] = row['tags'].lower().replace(',', '')
        row['words'] = [row['genre'].choices.get(int(x)).lower().replace(' ', '') for x in row['genre']]

    df = df[['title', 'words', 'tags']]

    # get words
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            if col == 'words':
                for word in row[col]:
                    words = words + word + ' '
            elif col == 'tags':
                words = words + row[col]
        words = ' '.join(non_duplicated_words(words.split()))
        row['words'] = words[:-1]

    # transfer words to numbers
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['words'])

    # get indices
    indices = pd.Series(df['title'])

    # create similarity matrix
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # init related movies
    related_movies = []

    idx = indices[indices == title].index[0]

    # get related
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)

    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        related_movies.append(list(df['title'])[i])

    return related_movies
