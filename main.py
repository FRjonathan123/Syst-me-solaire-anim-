import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

# vitesse d'orbite en km/h / mise à l'echelle vitesse

mise_a_echelle_vitesse = 2500000
vitesse_reel_mercure = 172800 / mise_a_echelle_vitesse
vitesse_reel_venus = 126000 / mise_a_echelle_vitesse
vitesse_reel_terre = 104000 / mise_a_echelle_vitesse
vitesse_reel_mars = 86400 / mise_a_echelle_vitesse
vitesse_reel_jupiter = 46800 / mise_a_echelle_vitesse
vitesse_reel_saturne = 36000 / mise_a_echelle_vitesse
vitesse_reel_uranus = 25200 / mise_a_echelle_vitesse
vitesse_reel_neptune = 18000 / mise_a_echelle_vitesse
vitesse_reel_pluton = None

#distance du soleil en ua x mise à l'échelle distance
mise_a_echelle_distance = 30
distance_reel_mercure = 0.387098 * mise_a_echelle_distance
distance_reel_venus = 0.723331 * mise_a_echelle_distance
distance_reel_terre = 1 * mise_a_echelle_distance
distance_reel_mars = 1.523662 * mise_a_echelle_distance
distance_reel_lune =  0.0026 * 1500 # 150 sinon, la mise a l'echelle rendra la lune invisible car trop proche de la terre comparer au autres planetes
distance_reel_jupiter = 5.203363 * mise_a_echelle_distance
distance_reel_saturne = 9.537070 * mise_a_echelle_distance
distance_reel_uranus = 19.191263 * mise_a_echelle_distance
distance_reel_neptune = 30.068963 * mise_a_echelle_distance
distance_reel_pluton = None 




# On créer des listes vide pour stocker l'historique
trace_mercure_x, trace_mercure_y = [], []
trace_venus_x, trace_venus_y = [], []
trace_terre_x, trace_terre_y = [], []
trace_mars_x, trace_mars_y = [], []
trace_lune_x, trace_lune_y = [], []
#manque jupiter, saturne, uranus et neptune

# Configuration de la scene
fig, ax = plt.subplots()
ax.set_xlim(-60, 60)
ax.set_ylim(-60, 60)
ax.set_aspect('equal') # pour que les cercles soient ronds

# On dessine le soleil
plt.scatter(0, 0, color="yellow", s=700, label="Soleil")

# On créer les objets "point" qui vont bouger
mercure, = ax.plot([], [], 'co', markersize=4.9, label="Mercure")
venus, = ax.plot([], [], 'go', markersize=12.7, label="Venus")
terre, = ax.plot([], [], 'bo', markersize=12, label="Terre")
mars, = ax.plot([], [], 'ro', markersize=6.7, label="Mars")
lune, = ax.plot([], [], 'wo', markersize= 3.5, label="Lune")

# On créer l'objet graphique pour la ligne de trainée
ligne_mercure, = ax.plot([], [], 'c', alpha=0.5)
ligne_venus, = ax.plot([], [], 'g', alpha=0.5)
ligne_terre, = ax.plot([], [],'b', alpha=0.5)
ligne_mars, = ax.plot([], [],'r', alpha=0.5)
ligne_lune, = ax.plot([], [], 'w', alpha=0.5)

# Paramètre des orbites
d_mercure, v_mercure = distance_reel_mercure, vitesse_reel_mercure
d_venus, v_venus = distance_reel_venus, vitesse_reel_venus
d_terre, v_terre = distance_reel_terre, vitesse_reel_terre
d_mars, v_mars = distance_reel_mars, vitesse_reel_mars
d_lune, v_lune = distance_reel_lune, 0.5

# la fonction qui anime (appelée à chaque frame)
def update(frame):
    #Calcul des nouvelle positions
    x_mer = d_mercure * np.cos(frame * v_mercure)
    y_mer = d_mercure * np.sin(frame * v_mercure)

    x_v = d_venus * np.cos(frame * v_venus)
    y_v = d_venus * np.sin(frame * v_venus)

    x_t = d_terre * np.cos(frame * v_terre)
    y_t = d_terre * np.sin(frame * v_terre)

    x_m = d_mars * np.cos(frame * v_mars)
    y_m = d_mars * np.sin(frame * v_mars)


    x_lune = x_t + d_lune * np.cos(frame * v_lune)
    y_lune = y_t + d_lune * np.sin(frame * v_lune)

    # Gestion de la trainée, ajout des positions aux listes de trainées
    trace_mercure_x.append(x_mer)
    trace_mercure_y.append(y_mer)
    trace_venus_x.append(x_v)
    trace_venus_y.append(y_v)
    trace_terre_x.append(x_t)
    trace_terre_y.append(y_t)
    trace_mars_x.append(x_m)
    trace_mars_y.append(y_m)
    trace_lune_x.append(x_lune)
    trace_lune_y.append(y_lune)

    # on garde seulement les 50 derniers points pour l'effet "queue de comète"
    if len(trace_terre_x) > 50:
        trace_mercure_x.pop(0)
        trace_mercure_y.pop(0)
        trace_venus_x.pop(0)
        trace_venus_y.pop(0)
        trace_terre_x.pop(0)
        trace_terre_y.pop(0)
        trace_mars_x.pop(0)
        trace_mars_y.pop(0)
        trace_lune_x.pop(0)
        trace_lune_y.pop(0)

    #mise à jour des points sur le grapyhique
    mercure.set_data([x_mer], [y_mer])
    venus.set_data([x_v], [y_v])
    terre.set_data([x_t], [y_t])
    mars.set_data([x_m], [y_m])
    lune.set_data([x_lune], [y_lune])

    # On met a jour les lignes
    ligne_mercure.set_data(trace_mercure_x, trace_mercure_y)
    ligne_venus.set_data(trace_venus_x, trace_venus_y)
    ligne_terre.set_data(trace_terre_x, trace_terre_y)
    ligne_mars.set_data(trace_mars_x, trace_mars_y)
    ligne_lune.set_data(trace_lune_x, trace_lune_y)

    return mercure, venus, terre, mars, lune, ligne_terre, ligne_mars, ligne_venus, ligne_lune, ligne_mercure

# lancement de l'animation
ani = FuncAnimation(fig, update, frames=np.arange(0,5000), interval=20, blit=True)


plt.legend()
plt.show()











# graphique normal 
#| 👇 | 👇 | 👇 |
"""
distance_terre = 10
vitesse_terre = 0.05

distance_mars = 15.2
vitesse_mars = 0.03

distance_venus = 19
vitesse_venus = 0.02

distance_jupiter = 25
vitesse_jupiter = 0.01


terre_x, terre_y = [], []
mars_x, mars_y = [], []
venus_x, venus_y = [], []
jupiter_x, jupiter_y = [], []

angle = 0

for i in range(200):
    terre_x.append(distance_terre * np.cos(angle * vitesse_terre))
    terre_y.append(distance_terre * np.sin(angle * vitesse_terre))

    mars_x.append(distance_mars * np.cos(angle * vitesse_mars))
    mars_y.append(distance_mars * np.sin(angle * vitesse_mars))

    venus_x.append(distance_venus * np.cos(angle * vitesse_venus))
    venus_y.append(distance_venus * np.sin(angle * vitesse_venus))

    jupiter_x.append(distance_jupiter * np.cos(angle * vitesse_jupiter))
    jupiter_y.append(distance_jupiter * np.sin(angle * vitesse_jupiter))

    angle += 1


plt.plot(terre_x, terre_y, label="Terre", color="blue")
plt.plot(mars_x, mars_y, label="Mars", color="red")
plt.plot(venus_x, venus_y, label="Venus", color="brown")
plt.plot(jupiter_x, jupiter_y, label="jupiter", color="green")


plt.scatter(0,0, color='yellow', s=500, label="Soleil")
plt.scatter(terre_x[-1], terre_y[-1], color="blue", s=80, edgecolors="black")
plt.scatter(mars_x[-1], mars_y[-1], color="red", s=100, edgecolors="black")
plt.scatter(venus_x[-1], venus_y[-1], color="brown", s=150, edgecolors="black")
plt.scatter(jupiter_x[-1], jupiter_y[-1], color="green", s=200, edgecolors="black")
plt.axis('equal')
plt.legend()
plt.show()
"""
