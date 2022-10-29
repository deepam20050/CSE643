start_best(Src, Dest, Path) :-
  best_first([[Src]], Dest, Path).

best_first([[Dest | Path] | _], Dest, [Dest | Path]).
best_first([Path | PriorityQueue], Dest, Sol) :-
  genpaths(Path, MorePaths), append(PriorityQueue, MorePaths, PriorityQueue2),
  sort_list(PriorityQueue2, UpdPriorityQueue, Dest),
  best_first(UpdPriorityQueue, Dest, Sol),

genpaths([Curr | Path], MorePaths) :-
  findall([To, Curr | Path], (dist(Curr, To, _), \+ member(To, Path)), MorePaths).

sort_list(L, L, Dest).
sort_list(L, L2, Dest) :- predicate(L, L1, Dest), !, sort_list(L1, L2, Dest).

predicate([[H1 | H2], [HH1 | HH2] | T], [[HH1 | HH2], [H1 | H2] | T], Dest) :- h(H1, Dest, Dist1), h(HH1, Dest, Dist2), Dist1 > Dist2.
predicate([H | T], [H | T2], Dest) :- predicate(T, T2, Dest).