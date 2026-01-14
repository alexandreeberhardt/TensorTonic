# Usefull numpy functions

## `np.asarray(x, dtype=float)`

Convertis un tableau en array numpy de float

[0, 2.3] -> [0.0, 2.3]

## `np.maximum(x,0)`

equivalent à 
for i in range(len(x)) :
    if x[i] < 0:
	x[i] = 0;

## `x.reshape(1)`

Si c'est un int ça devient un np.array

## `np.where(cond, a, b)`

application conditionnelle
Sur un tenseur x, ça applique l'effet a si la condition est vraie et b sinon

très puissant

## `np.exp(x)`

exponentielle de x

## `np.sum(x)`

fais la somme de x

## `np.sum(x, axis=1, keepdims=True)`

Fais la somme de x par ligne de la matrice (axis 1) et garde la dimension (keepdims=True)
Sinon ça met un int à la place du tableau de la ligne par ex
