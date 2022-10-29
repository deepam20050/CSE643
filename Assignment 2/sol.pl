start :-
  write('Enter which search to use: '), nl, nl,
  write('[1]. Show Depth First Search and Best-first search on this data.'), nl, nl,
  write('[2]. Show Breadth First Search and A* search on this data.'), nl, nl,
  read(Option), nl, nl,
  (Option = 1 -> choiceA ; choiceB).

choiceA :-
  write('Enter Source : '), nl, nl,
  read(Src), nl, nl,
  write('Enter Destination : '), nl, nl,
  read(Dest), nl, nl,
  format('Starting Depth First Search...'), nl, nl,
  start_dfs(Src, Dest, Path_DFS_R),
  reverse(Path_DFS_R, Path_DFS),
  format('Printing Depth First Search Path...'), nl, nl,
  print_list(Path_DFS).

choiceB :-
  write('Enter Source : '), nl, nl,
  read(Src), nl, nl,
  write('Enter Destination : '), nl, nl,
  read(Dest), nl, nl,
  format('Starting Breadth First Search...'), nl, nl,
  start_bfs(Src, Dest, Path_BFS),
  format('Printing Breadth First Search Path...'), nl, nl,
  print_list(Path_BFS).

start_dfs(Src, Dest, Solution) :-
  dfs([], Src, Solution, Dest).
dfs(Path, Src, [Src | Path], Dest) :- Src == Dest.
dfs(Path, Src, Sol, Dest) :-
  dist(Src, To, _),
  not(member(To, Path)),
  dfs([Src | Path], To, Sol, Dest).

% Ref: https://ksvi.mff.cuni.cz/~dingle/2019-20/npp/notes_5.html
bfs([[Dest | Oth] | _], _, Dest, [Dest | Oth]).
bfs([[Curr | Path] | Queue], Used, Dest, Solution) :-
  findall(X, dist(Curr, X, _), Next), subtract(Next, Used, To),           
  maplist(attach_front([Curr | Path]), To, Child),
  append(Queue, Child, NewQueue), append(To, Used, Used1),         
  bfs(NewQueue, Used1, Dest, Solution). 
start_bfs(Src, Dest, Solution) :-
  bfs([[Src]], [Src], Dest, Solution),
  reverse(Solution1, Solution).

%------- PROLOG HELPER FUNCTIONS -------
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