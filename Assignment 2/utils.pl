% sort in ascending order without deleting duplicates
mysort(List, Result) :- sort(0, @=<, List, Result).

% join two lists
join(List, X, Result) :- append(List, X, Result).

% to check whether element belongs to list
member(X, [X | _]).
member(X, [_ | T]) :- member(X, T).

% to concatenate lists
conc([], L, L).
conc([X | L1], L2, [X | L3]) :-
  write(X),
  write(' '),
  write(L1),
  write(' '),
  write(L2),
  conc(L1, L2, L3).