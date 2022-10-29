start_bfs(Start, Solution) :-
  bfs([[Start]], Solution).

bfs([[Node | Path] | _], [Node | Path]) :-
  goal(Node).

bfs([[Path | Paths]], Solution) :-
  extend(Path, NewPaths),
  write(NewPaths), nl,
  conc(Paths, NewPaths, Paths1),
  bfs(Paths1, Solution).

extend(_, []).
extend([Node | Path], NewPaths) :-
  bagof([NewNode, Node | Path], (s(Node, NewNode), not(member(NewNode, [Node | Path]))), NewPaths), !.