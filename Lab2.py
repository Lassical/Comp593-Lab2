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
            'title' : 'the equalizer',
            'genre' : 'action'
            },
        ],
    }

    # TODO: Step 3 - Add another movie to the data structure
    
    about_me['movies'].insert(1, {'title' : 'star wars', 'genre' : 'sci-fi'}),
    name_and_id(about_me)
    pizza_toppings2(about_me)
    add_pizza_toppings(about_me)
    pizza_toppings1(about_me)
    movie_genres(about_me)
    movie_titles(about_me)
    

# TODO: Step 4 - Function that prints student name and ID	
def name_and_id(about_me):
    print(f'My name is {about_me["name"].title()} but my friends call me {about_me["name"].split()[0].title()} The Great. \n My Student Number is: {about_me["student id"]} ')

    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure


def pizza_toppings2(about_me):
    print('\nMy favourite pizza toppings are:')
    for t in about_me["toppings"]:
        print(f'- {t.upper()}')

    return

def add_pizza_toppings(about_me):
    #toppings after about me
    
    about_me['toppings'].extend(['tomatos']),
    about_me['toppings'].extend(['peppers']),
    
    for i,t in enumerate(about_me['toppings']):
        about_me['toppings'][i] = t.title()

    about_me['toppings'].sort()

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def pizza_toppings1(about_me):
    print('\nPizza toppings i like are:')
    for t in about_me["toppings"]:
        print(f'- {t.lower()}')

    
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def movie_genres(about_me):
#    print('\nThe movie list is')
#    for i,g in enumerate(about_me.item(["genre"]):
#        if i < len(about_me['genres']) - 1:    
#         print(f'-{g["genre"]}, ', end='')

    genre_name = [g['genre'] for g in about_me['movies']]
    genre_comp = ', '.join(map(str,genre_name))
    r = genre_comp.rfind(", ")
    genre_list = genre_comp[:r] + ' and' + genre_comp [r+1:]
    print(f'\nMovie genres I like include {genre_list}')

#    genre_name = [g['genre'] for g in about_me['genre']]
#    genre_list = ', '.join(genre_name)
#    print(genre_list)

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def movie_titles(about_me):
    movie_name = [m['title'] for m in about_me['movies']]
    movie_comp = ', '.join(map(str,movie_name))
    r = movie_comp.rfind(", ")
    movie_list = movie_comp[:r] + ' and' + movie_comp [r+1:]
    print(f'\nMovies I like include {movie_list.title()}')

    return
    
if __name__ == '__main__':
    main()

# str.capitalize
# title()