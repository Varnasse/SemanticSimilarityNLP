import spacy

nlp = spacy.load("en_core_web_md")

def similar_movie(description):
    # Read in the "movies.txt" file and store the descriptions and titles in a list
    with open('movies.txt', 'r') as f:
        movies = [line.strip().split(":") for line in f]

    # Create a spaCy doc object
    doc = nlp(description)

    # Initialise variables to store the highest similarity score
    highest_similarity = 0
    most_similar_movie = ""

    # Iterate through movies and compare the similarity to the doc object
    for title, movie_description in movies:

        # Create a spaCy doc object for movie description
        movie_doc = nlp(movie_description)
        
        # Calculate the similarity between the doc and movie description
        similarity = doc.similarity(movie_doc)

        # Update the highest similarity score and most similar title
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_movie = title
    
    # Return the movie title with the most similar
    return most_similar_movie

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
movie = similar_movie(description)
print(f"You might like {movie}as it has a similar description")