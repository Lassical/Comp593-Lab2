def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'name' : 'alexander vass',
        'student id' : '10071934',
        'toppings' : [
            'peperoni',
            'onions',
            'bacon'
        ],
        'movies' : [
            {
            'title' : 'knives out',
            'genre' : 'mystery'
            },
            {
            'title' : 'test',
            'genre' : 'test'
            },
        ],
    }

    # TODO: Step 3 - Add another movie to the data structure
    
    about_me['movies'].insert(1, {'title' : 'test2', 'genre' : 'test2'}),
    name_and_id(about_me)
    add_pizza_toppings(about_me)
    pizza_toppings(about_me)
    movie_genres(about_me)
    movie_titles(about_me)
    

# TODO: Step 4 - Function that prints student name and ID	
def name_and_id(about_me):
    print(f'Name {about_me["name"]} Number {about_me["student id"]} ')

    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me):
    #toppings after about me
    about_me['toppings'].extend(['tomatos']),
    
    for i,t in enumerate(about_me['toppings']):
        about_me['toppings'][i] = t.title()

    about_me['toppings'].sort()

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def pizza_toppings(about_me):
    print('\nThe toppings list is')
    for t in about_me["toppings"]:
        print(f'- {t}')

    
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def movie_genres(about_me):
#    print('\nThe movie list is')
#    for i,g in enumerate(about_me.item(["genre"]):
#        if i < len(about_me['genres']) - 1:    
#         print(f'-{g["genre"]}, ', end='')

    genre_name = [{g['movie']['genre']} for g in about_me]
    genre_list = ', '.join(genre_name)
    print(genre_name)


#    genre_name = [g['genre'] for g in about_me['genre']]
#    genre_list = ', '.join(genre_name)
#    print(genre_list)

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()

# str.capitalize
# title()