dist(a, 1).
dist(a, 2).
dist(a, 3).
dist(b, 2).
dist(d, 5).
mylist([1, 2, 3, 4, 5]).

print_list([]).
print_list([H | T]) :-
  format('~s ', [H]),
  print_list(T).



%solve([]).
% solve(List) :-
    %dist(a, X), join(List, [X], List), !.
    % mysort(List, List).

solve([Node | Path], NewPaths) :-
  findall([NewNode, Node | Path],
  (dist(NewNode, _), \+ member(NewNode, Path)), NewPaths).