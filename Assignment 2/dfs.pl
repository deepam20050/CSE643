start_dfs(Src, Dest, Solution) :-
  dfs([], Src, Solution, Dest).
dfs(Path, Src, [Src | Path], Dest) :- Src == Dest.
dfs(Path, Src, Sol, Dest) :-
  dist(Src, To),
  not(member(To, Path)),
  dfs([Src | Path], To, Sol, Dest).