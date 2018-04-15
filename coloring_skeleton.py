#!/usr/bin/env python3

import pycosat

NUM_COLORS = 3

# Given a vertex index and a color, return the variable number
# variables N*i, N*i+1, N*i+2, ... represent vertex i being colored
#   red, green, blue, ... respectively
def var( vertexIdx, color ):
    # assert: 0 <= color < NUM_COLORS
    return ( NUM_COLORS * ( vertexIdx + 1 ) ) + color

# Make all the clauses for a single vertex.
def vertexClauses( i ):
    clauses = []
    clauses.append( [ TODO: Put the "at least one color" clause in here ] )
    for color1 in range( NUM_COLORS ):
        color2 = ( color1 + 1 ) % NUM_COLORS
        clauses.append( [ TODO: Put the "not multiple colors" clause in here ] )
    return clauses

# Make all the clauses for a single edge
def edgeClauses( n1, n2 ):
    clauses = []
    for j in range( NUM_COLORS ):
        clauses.append( [ TODO: Put the "vertices are not the same color" clause in here ] )
    return clauses

def extractColors( vars ):
    colors = []
    for v in vars:
        if v < 0:
            continue
        vertexIdx = ( v // NUM_COLORS ) - 1
        color = v % NUM_COLORS
        colors.append( ( vertexIdx, color ) )
    return colors

def canBeGraphColored( edges ):
    n = len( edges )
    clauses = []
    for i in range( n ):
        clauses += vertexClauses( i )
    for i in range( len( edges ) ):
        for j in range( len( edges[ i ] ) ):
            clauses += edgeClauses( i, edges[ i ][ j ] )
    # print( clauses )
    result = pycosat.solve( clauses )
    if result == 'UNSAT':
        return False
    else:
        return extractColors( result )

# The edges for a graph are encoded as a list of lists.
# At position i of the big list is a list of all the lower-index vertices
# that vertex i is connected to.

# 3-vertex complete graph
k3 = [ [], [ 0 ], [ 0, 1 ] ]
# 4-vertex complete graph
k4 = [ [], [ 0 ], [ 0, 1 ], [ 0, 1, 2 ] ]
# 6-vertex simple cycle
c6 = [ [], [ 0 ], [ 1 ], [ 2 ], [ 3 ], [ 0, 4 ] ]

TODO: Make an interesting graph that is 3-colorable
TODO: Make an interesting graph that is not 3-colorable

print( canBe3Colored( k3 ) )
print( canBe3Colored( k4 ) )
print( canBe3Colored( c6 ) )
