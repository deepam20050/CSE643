% Ref: https://ksvi.mff.cuni.cz/~dingle/2019-20/npp/notes_5.html
attach_front(L, X, [X | L]).

bfs([[Dest | Oth] | _], _, Dest, [Dest | Oth]).

bfs([[Curr | Path] | Queue], Used, Dest, Solution) :-
    findall(X, dist(Curr, X, _), Next), subtract(Next, Used, To),           
    maplist(attach_front([Curr | Path]), To, Child),
    append(Queue, Child, NewQueue), append(To, Used, Used1),         
    bfs(NewQueue, Used1, Dest, Solution). 

start_bfs(Src, Dest, Solution) :-
    bfs([[Src]], [Src], Dest, Solution1),
    reverse(Solution1, Solution).