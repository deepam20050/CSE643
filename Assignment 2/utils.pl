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