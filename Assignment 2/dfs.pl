solve(Node, End, Solution) :-
  dfs([], Node, Solution, End).

dfs(Path, Node, [Node | Path], End) :-
  Node == End.

dfs(Path, Node, Sol, End) :-
  s(Node, Node1),
  not(member(Node1, Path)),
  dfs([Node | Path], Node1, Sol, End).