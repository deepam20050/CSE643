start :-
  write('Enter which search to use: '), nl, nl,
  write('[1]. Show Depth First Search'), nl, nl,
  write('[2]. Show Best-first search'), nl, nl,
  write('[3]. Show Breadth First Search'), nl, nl,
  read(Option), nl, nl,
  (Option = 1 -> choice_depth ; (Option = 2 -> choice_best ; choice_breadth)).

choice_depth :-
  write('Enter Source : '), nl, nl,
  read(Src), nl, nl,
  write('Enter Destination : '), nl, nl,
  read(Dest), nl, nl,
  format('Starting Depth First Search...'), nl, nl,
  start_dfs(Src, Dest, Path_DFS_R),
  reverse(Path_DFS_R, Path_DFS),
  format('Printing Depth First Search Path...'), nl, nl,
  print_list(Path_DFS), nl, nl.

choice_best :-
  write('Enter Source : '), nl, nl,
  read(Src), nl, nl,
  write('Enter Destination : '), nl, nl,
  read(Dest), nl, nl,
  format('Starting Best First Search...'), nl, nl,
  start_best(Src, Dest, Path_Best_R),
  format('Printing Best First Search Path...'), nl, nl,
  reverse(Path_Best_R, Path_Best),
  print_list(Path_Best), nl, nl.

choice_breadth :-
  write('Enter Source : '), nl, nl,
  read(Src), nl, nl,
  write('Enter Destination : '), nl, nl,
  read(Dest), nl, nl,
  format('Starting Breadth First Search...'), nl, nl,
  start_bfs(Src, Dest, Path_BFS),
  format('Printing Breadth First Search Path...'), nl, nl,
  print_list(Path_BFS), nl, nl.

start_dfs(Src, Dest, Solution) :-
  dfs([], Src, Solution, Dest).
dfs(Path, Src, [Src | Path], Dest) :- Src == Dest.
dfs(Path, Src, Sol, Dest) :-
  dist(Src, To, _),
  not(member(To, Path)),
  dfs([Src | Path], To, Sol, Dest).

% https://github.com/DrAlbertCruz/CMPS-4560-Informed-Search
start_best(Src, Dest, Path) :-
  best_first([[Src]], Dest, Path).
best_first([[Dest | Path] | _], Dest, [Dest | Path]).
best_first([Path | PriorityQueue], Dest, Sol) :-
  genpaths(Path, MorePaths), append(PriorityQueue, MorePaths, PriorityQueue2),
  sort_list(PriorityQueue2, UpdPriorityQueue, Dest),
  best_first(UpdPriorityQueue, Dest, Sol).

genpaths([Curr | Path], MorePaths) :-
  findall([To, Curr | Path], (dist(Curr, To, _), \+ member(To, Path)), MorePaths).

% Ref: https://ksvi.mff.cuni.cz/~dingle/2019-20/npp/notes_5.html
start_bfs(Src, Dest, Solution) :-
  bfs([[Src]], [Src], Dest, Solution1),
  reverse(Solution1, Solution).
bfs([[Dest | Oth] | _], _, Dest, [Dest | Oth]).
bfs([[Curr | Path] | Queue], Used, Dest, Solution) :-
  findall(X, dist(Curr, X, _), Next), subtract(Next, Used, To),           
  maplist(attach_front([Curr | Path]), To, Child),
  append(Queue, Child, NewQueue), append(To, Used, Used1),         
  bfs(NewQueue, Used1, Dest, Solution). 

% ------- PROLOG HELPER FUNCTIONS -------
% sort in ascending order without deleting duplicates
mysort(List, Result) :- sort(0, @=<, List, Result).

% join two lists
join(List, X, Result) :- append(List, X, Result).

% to check whether element belongs to list
member(X, [X | _]).
member(X, [_ | T]) :- member(X, T).

% to concatenate lists
conc([], L, L).
conc([E | L1], L2, [E | L3]) :- conc(L1, L2, L3).

% print list
print_list([]).
print_list([H | T]) :-
  format('~s ', [H]),
  print_list(T).

% attach at the front
attach_front(L, X, [X | L]).

% sort list for best first and A*
sort_list(L, L, _).
sort_list(L, L2, Dest) :- predicate(L, L1, Dest), !, sort_list(L1, L2, Dest).

% predicate to sort based on heuristic
predicate([[H1 | H2], [HH1 | HH2] | T], [[HH1 | HH2], [H1 | H2] | T], Dest) :- h(H1, Dest, Dist1), h(HH1, Dest, Dist2), Dist1 > Dist2.
predicate([H | T], [H | T2], Dest) :- predicate(T, T2, Dest).

% --------- PROLOG KNOWLEDGE BASE ---------