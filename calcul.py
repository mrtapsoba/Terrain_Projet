import streamlit as st
import matplotlib.pyplot as plt
import math


st.title("Calcul de surface des cellules")

st.sidebar.header("Parametrage")
superficie = st.sidebar.number_input("La superficie du terrain en m2", value=7000)
longueur = st.sidebar.number_input("La longueur du terrain en m", value=100)
nbrCellule = st.sidebar.slider('Nombre total de cellules', min_value=1, max_value=20, value=11)
alle = st.sidebar.slider('Nombre d\'allés ou colonnes', min_value=1, max_value=10, value=4)
intervalle = st.sidebar.slider("Taille de chaque intervalle en decimetre", min_value=2, max_value=15, value=10, step=1)

st.subheader("************ Recapitulatif *******************")
st.text("Superficie du terrain : " +str(superficie) + " m2")
largeur = superficie / longueur
st.text("Longueur = " + str(longueur)+" m donc largeur= " + str(largeur) +" m")
st.text("Nombre de cellule : " + str(nbrCellule)+" avec " + str(alle)+" allé(s) ou colonnes")
i = intervalle / 10
st.text("Taille de chaque intervalle = "+ str(i)+" m entre les cellules")

st.text("...")
st.subheader("*********** Calcul de la superficie **************")

# calcul de surface donnée pour les intervalles
long_rest = longueur - (i * (alle-1))
#print(long_rest)

ligne = nbrCellule / alle
ligne = math.ceil(ligne)
larg_rest = largeur - (i * (ligne-1))
#print(larg_rest)

perte_surf = ((alle - 1) *longueur) + ((ligne - 1) * largeur) - ((alle - 1) * (ligne - 1)) * i

surf_rest = superficie - perte_surf

st.text("Pour atteindre l'objectif de " + str(nbrCellule) + "cellules avec "+str(alle)+" allé(s) ou colonnes il nous faut ")
st.text("Nombre de ligne : "+str(ligne))
# st.text("Longueur restant : "+str(long_rest) + ", largeur restante : "+ str(larg_rest))
st.text("Surface a prévoir pour creer les intervalles : "+str(perte_surf) + " m2")
st.text("La surface restante pour les cellules est de "+ str(surf_rest) +" m2")
tempCellule = alle * ligne
st.text("Avec "+str(alle)+" allés et "+str(ligne)+"  lignes, nous aurons environ : "+str(tempCellule) + " cellules")

tempCellSup = surf_rest / tempCellule
st.text("La superficie par cellule sera de "+ str(tempCellSup)+" m2")
tempCellSupReel = surf_rest / nbrCellule
st.text("En gardant les "+str(nbrCellule)+" cellules, chaque cellule aura une superficie de "+str(tempCellSupReel) + " m2")

st.subheader("************ Representation graphique ******************")

def plot_terrain(a, b, c):
    total_cells = a * b
    positions_x = []
    positions_y = []
    marker_size = c * 5000  # Taille du marqueur en fonction de la distance entre les cellules
    
    for i in range(a):
        for j in range(b):
            positions_x.append(j * c)
            positions_y.append(i * c)
    
    plt.figure(figsize=(5, 3.5))
    plt.scatter(positions_x, positions_y, s=marker_size, marker='s')  # Utilisation de marker_size
    plt.title(f"Représentation graphique de {total_cells} cellules")
    plt.xlabel('Position sur la longueur')
    plt.ylabel('Position sur la largeur')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    st.pyplot(plt)

plot_terrain(ligne, alle, i)