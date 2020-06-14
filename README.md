# Miscellinious Work
## Pathfinder Algorithm
### Improvements needed
```
1. To find shortest distance between any two points in GRID.
2. start < destination i.e. only goes forward
3. Path is down and up no diagonal path
```

```
MAZE is 

0       0       65535   65535   0       65535   65535   65535   65535   65535

0       0       65535   0       65535   65535   65535   65535   65535   0

0       65535   65535   65535   65535   0       65535   65535   0       65535

0       0       0       0       0       0       65535   65535   65535   0

65535   0       65535   0       0       0       65535   0       65535   0

65535   65535   65535   0       0       0       0       0       0       65535

0       65535   0       0       65535   65535   65535   0       0       0

65535   65535   0       0       65535   65535   65535   65535   65535   0

65535   0       0       65535   65535   0       65535   65535   65535   0

0       0       65535   65535   0       0       65535   65535   65535   0

```

```
Calculated Path is follow 1

STEPS 18
1       0       0       0       0       0       0       0       0       0

1       0       0       0       0       0       0       0       0       0

1       0       0       0       0       0       0       0       0       0

1       1       1       1       1       1       0       0       0       0

0       0       0       0       0       1       0       0       0       0

0       0       0       0       0       1       1       1       1       0

0       0       0       0       0       0       0       0       1       1

0       0       0       0       0       0       0       0       0       1

0       0       0       0       0       0       0       0       0       1

0       0       0       0       0       0       0       0       0       1

```
