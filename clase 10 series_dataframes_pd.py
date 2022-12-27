import pandas as pd

# puedes especificar un index o puedes quitar uno por defecto de 0 a n
psg_players = pd.Series(['Neymar','Mbappe','Navas','Hakimi','Kimbempe'], index=[10,12,23,34,15])
psg_players2 = pd.Series(['Neymar','Mbappe','Navas','Hakimi','Kimbempe'])
dict = {1:'Navas', 7:'Mbappe', 10:'Neymar', 30:'Messi'}
psg_player3 = pd.Series(dict)

print(psg_players[0:3])

dict = {
    'Jugador': ['Neymar','Mbappe','Navas','Hakimi','Kimbempe'],
    'Altura': [183.0, 170.0, 170.0, 183.2, 190.3],
    'Goles': [10, 23, 0, 4, 5]
}
players_df = pd.DataFrame(dict)
players_df2 = pd.DataFrame(dict, index=[10,33,34,12,5])
print(players_df.columns)
print(players_df.index)
players_df